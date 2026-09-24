#!/usr/bin/env python3
"""Deterministic route contract for the Barter Prompt Improver skill.

Characterizes a request into one stable route object so intent routing,
format locking and disambiguation behavior are testable without invoking a
model. This is the executable oracle the skill and project kernels are
written against; it is not a claim about what claude.ai executes
internally.

The contract fixes the observed failure class: substring alias matching (a
command like `$short` matched by an `in` check, or a keyword like `ask`
matched inside `basket`) must never select a route. Only a complete
`$token` and a word-boundary keyword can. A single explicit mode command
wins over natural-language scoring, so `$short but this is a deep, complex,
multi-step system` binds Short, not Deep. Two conflicting mode commands in
one request are not silently resolved; they route to Interactive Mode.
Mode and output format are independent axes and never steal each other's
decision. Every decision here is deterministic and fixture-checkable.

Python 3.9 compatible.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Token tables (exact, delimiter-aware matches only)
# ---------------------------------------------------------------------------

# Explicit mode commands. A single one wins over any natural-language signal.
# Flat token -> intent map, exact whole-token match only.
MODE_COMMANDS: Dict[str, str] = {
    "$raw": "RAW",
    "$text": "TEXT", "$t": "TEXT",
    "$improve": "IMPROVE", "$i": "IMPROVE",
    "$refine": "REFINE", "$r": "REFINE",
    "$short": "SHORT", "$s": "SHORT",
    "$deep": "DEEP", "$d": "DEEP",
    "$vibe": "VISUAL", "$v": "VISUAL",
    "$image": "IMAGE", "$img": "IMAGE",
    "$video": "VIDEO", "$vid": "VIDEO",
}

# Output format is a separate axis. It never competes for the primary route.
FORMAT_COMMANDS: Dict[str, str] = {
    "$json": "json", "$j": "json",
    "$yaml": "yaml", "$y": "yaml",
    "$markdown": "markdown", "$md": "markdown", "$m": "markdown",
}

# Natural-language mode signals (word-boundary, not substring). MAGICPATH,
# FRAMEWORK, SCORING, INTERACTIVE and THINKING have no $ command: keyword
# score is their only way into the primary route. Weights follow the
# skill's INTENT_WEIGHT: one flat weight per intent, applied per match.
INTENT_WEIGHT: Dict[str, int] = {
    "RAW": 6, "TEXT": 5, "IMPROVE": 5, "REFINE": 5, "SHORT": 5, "DEEP": 5,
    "VISUAL": 6, "MAGICPATH": 7, "IMAGE": 6, "VIDEO": 6,
    "FRAMEWORK": 4, "SCORING": 4, "INTERACTIVE": 3, "THINKING": 3,
}
INTENT_KEYWORDS: Dict[str, List[str]] = {
    "RAW": ["raw mode", "passthrough", "no validation"],
    "TEXT": ["text mode", "prompt mode", "prompt", "rcaf", "costar"],
    "IMPROVE": ["improve prompt", "make better", "enhance prompt"],
    "REFINE": ["refine this", "optimise", "optimize", "feedback"],
    "SHORT": ["shorten", "concise", "quick", "fast", "minor"],
    "DEEP": ["complex", "strategic", "multi-step", "comprehensive", "system"],
    "VISUAL": ["visual concepting", "design vibe", "ui design", "lovable",
               "aura", "bolt", "v0", "v0.dev"],
    "MAGICPATH": ["magicpath", "magic path", "magicpath.ai", "multi-page flow",
                  "user journey", "pathfinding"],
    "IMAGE": ["image prompt", "picture", "photo", "midjourney", "dall-e",
              "dalle", "stable diffusion", "sdxl", "flux", "flux 2", "imagen",
              "nano banana", "seedream", "ideogram", "leonardo", "firefly",
              "runway image"],
    "VIDEO": ["video prompt", "clip", "animation", "runway", "gen-4", "sora",
              "kling", "veo", "pika", "luma", "ray3", "minimax", "hailuo",
              "seedance", "omnihuman", "wan", "motion"],
    "FRAMEWORK": ["framework", "rcaf", "costar", "tidd-ec", "craft", "race",
                  "cidi", "crispe", "risen", "template", "structure"],
    "SCORING": ["clear", "evoke", "visual", "score", "quality", "rating",
                "evaluate", "assessment", "points"],
    "INTERACTIVE": ["question", "clarify", "conversation", "dialog", "gather",
                     "ask", "interactive"],
    "THINKING": ["depth", "phases", "energy", "cognitive", "rigour", "rigor",
                 "analysis"],
}

# Energy and scorer per intent. Meta/topic intents (FRAMEWORK, SCORING,
# INTERACTIVE, THINKING) carry no scorer: they are informational routes, not
# a gated prompt deliverable. RAW carries no scorer by design (no framework,
# no scoring).
ENERGY_MAP: Dict[str, str] = {
    "RAW": "raw", "TEXT": "standard", "IMPROVE": "standard", "REFINE": "standard",
    "SHORT": "quick", "DEEP": "deep", "VISUAL": "creative", "MAGICPATH": "creative",
    "IMAGE": "creative", "VIDEO": "creative", "FRAMEWORK": "standard",
    "SCORING": "standard", "INTERACTIVE": "standard", "THINKING": "standard",
}
SCORER_MAP: Dict[str, Optional[str]] = {
    "RAW": None, "TEXT": "CLEAR", "IMPROVE": "CLEAR", "REFINE": "CLEAR",
    "SHORT": "CLEAR", "DEEP": "CLEAR", "VISUAL": "EVOKE", "MAGICPATH": "EVOKE",
    "IMAGE": "VISUAL", "VIDEO": "VISUAL", "FRAMEWORK": None, "SCORING": None,
    "INTERACTIVE": None, "THINKING": None,
}

# ---------------------------------------------------------------------------
# Route object schema (fixed field set; unknown or duplicate fields reject)
# ---------------------------------------------------------------------------

ROUTE_FIELDS = [
    "intent", "energy", "scorer", "format", "source", "needs_disambiguation",
    "resources",
]

INTENT_VALUES = [
    "RAW", "TEXT", "IMPROVE", "REFINE", "SHORT", "DEEP", "VISUAL", "MAGICPATH",
    "IMAGE", "VIDEO", "FRAMEWORK", "SCORING", "INTERACTIVE", "THINKING",
]
ENERGY_VALUES = ["raw", "quick", "standard", "deep", "creative"]
SCORER_VALUES = ["CLEAR", "EVOKE", "VISUAL"]  # None is also legal (see below)
FORMAT_VALUES = ["markdown", "json", "yaml"]
SOURCE_VALUES = ["command", "semantic", "fallback"]

# --- Runtime discovery + guarded loading (resilient router mechanics) ---
# Resource names below are resolved against the actual skill inventory at
# every call, so a renamed or deleted reference degrades to a smaller
# resource set instead of a dead path or a crash. This mirrors the canonical
# smart-router resilience pattern: discover, guard, dedupe, fall back.
SKILL_ROOT = Path(__file__).resolve().parent.parent.parent / "sk-prompt-improver"
RESOURCE_BASES = ("references", "assets")

ALWAYS = ["references/depth-framework.md", "references/interactive-mode.md"]
RESOURCE_MAP: Dict[str, List[str]] = {
    "RAW": [],
    "TEXT": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md", "assets/format-guide-markdown.md"],
    "IMPROVE": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md", "assets/format-guide-markdown.md"],
    "REFINE": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md", "assets/format-guide-markdown.md"],
    "SHORT": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md", "assets/format-guide-markdown.md"],
    "DEEP": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md", "assets/format-guide-markdown.md"],
    "VISUAL": ["references/visual-mode.md", "assets/visual-mode-library.md", "references/patterns-evaluation.md"],
    "MAGICPATH": ["references/visual-mode.md", "assets/visual-mode-library.md", "references/patterns-evaluation.md"],
    "IMAGE": ["references/image-mode.md", "assets/image-mode-library.md", "references/patterns-evaluation.md"],
    "VIDEO": ["references/video-mode.md", "assets/video-mode-library.md", "references/patterns-evaluation.md"],
    "FRAMEWORK": ["references/patterns-evaluation.md", "assets/framework-pattern-library.md"],
    "SCORING": ["references/patterns-evaluation.md"],
    "INTERACTIVE": [],
    "THINKING": ["references/patterns-evaluation.md"],
}
FORMAT_GUIDE: Dict[str, str] = {
    "json": "assets/format-guide-json.md",
    "yaml": "assets/format-guide-yaml.md",
    "markdown": "assets/format-guide-markdown.md",
}


def discover_resource_inventory() -> Set[str]:
    """Return routable markdown paths under references/ and assets/.

    Returns package-relative posix paths (for example
    ``references/depth-framework.md``) so the maps above resolve directly.
    A missing base contributes nothing instead of raising.
    """
    inventory: Set[str] = set()
    for base_name in RESOURCE_BASES:
        base = SKILL_ROOT / base_name
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.is_file():
                inventory.add(path.relative_to(SKILL_ROOT).as_posix())
    return inventory


def guard_resources(names: List[str], inventory: Set[str]) -> List[str]:
    """Keep only resources that exist in the current inventory, dedupe, keep order."""
    seen: Set[str] = set()
    kept: List[str] = []
    for name in names:
        if name in inventory and name not in seen:
            seen.add(name)
            kept.append(name)
    return kept


# ---------------------------------------------------------------------------
# Tokenization + detection
# ---------------------------------------------------------------------------

_TOKEN_RE = re.compile(r"\$[a-z]+")


def tokenize(text: str) -> List[str]:
    """Return every exact `$token` in the request, case-normalized."""
    return _TOKEN_RE.findall((text or "").lower())


def detect_command(text: str) -> Tuple[Optional[str], bool]:
    """Explicit mode command, if any. Only exact full-token matches count.

    Returns (intent, conflict). Two distinct mode commands in the same
    request are a conflict (ask which one), never silently resolved to
    either one.
    """
    modes = {MODE_COMMANDS[tok] for tok in tokenize(text) if tok in MODE_COMMANDS}
    if len(modes) == 1:
        return next(iter(modes)), False
    return None, len(modes) > 1


def detect_format(text: str) -> Tuple[str, bool]:
    """Output-format command, independent of mode. Exact token match only."""
    for tok in tokenize(text):
        if tok in FORMAT_COMMANDS:
            return FORMAT_COMMANDS[tok], True
    return "markdown", False


def score_intents(text: str) -> Dict[str, int]:
    """Word-boundary keyword scores per intent. Never substring."""
    lowered = (text or "").lower()
    scores: Dict[str, int] = {intent: 0 for intent in INTENT_KEYWORDS}
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", lowered):
                scores[intent] += INTENT_WEIGHT[intent]
    return scores


def detect_intent(text: str) -> Tuple[str, str]:
    """Resolve one primary intent and how it was found.

    A single explicit command wins outright; a conflict between two
    commands routes to INTERACTIVE for disambiguation; otherwise the
    highest word-boundary keyword score wins; a request with neither falls
    back to INTERACTIVE so the router asks one comprehensive question
    instead of guessing.
    """
    command, conflict = detect_command(text)
    if conflict:
        return "INTERACTIVE", "fallback"
    if command:
        return command, "command"
    scores = score_intents(text)
    best = max(scores, key=lambda intent: scores[intent])
    if scores[best] > 0:
        return best, "semantic"
    return "INTERACTIVE", "fallback"


def resources_for(intent: str, fmt: str, explicit_format: bool) -> List[str]:
    inventory = discover_resource_inventory()
    names = list(ALWAYS) + RESOURCE_MAP.get(intent, [])
    if fmt in ("json", "yaml") or explicit_format:
        names.append(FORMAT_GUIDE[fmt])
    return guard_resources(names, inventory)


# ---------------------------------------------------------------------------
# Route resolution + schema validation
# ---------------------------------------------------------------------------

def route_request(text: str) -> Dict[str, Any]:
    intent, source = detect_intent(text)
    fmt, explicit_format = detect_format(text)
    return {
        "intent": intent,
        "energy": ENERGY_MAP[intent],
        "scorer": SCORER_MAP[intent],
        "format": fmt,
        "source": source,
        "needs_disambiguation": intent == "INTERACTIVE",
        "resources": resources_for(intent, fmt, explicit_format),
    }


def validate_route_object(obj: Dict[str, Any]) -> List[str]:
    """Reject unknown or duplicate fields and invalid enum values.

    Returns a list of violations (empty when the object is schema-valid).
    """
    errors: List[str] = []
    if not isinstance(obj, dict):
        return ["route object is not a dict"]
    if list(obj.keys()) != ROUTE_FIELDS:
        missing = [f for f in ROUTE_FIELDS if f not in obj]
        extra = [k for k in obj if k not in ROUTE_FIELDS]
        if missing:
            errors.append(f"missing fields: {missing}")
        if extra:
            errors.append(f"unknown fields: {extra}")
    if obj.get("intent") not in INTENT_VALUES:
        errors.append(f"bad intent: {obj.get('intent')}")
    if obj.get("energy") not in ENERGY_VALUES:
        errors.append(f"bad energy: {obj.get('energy')}")
    if obj.get("scorer") not in (None,) + tuple(SCORER_VALUES):
        errors.append(f"bad scorer: {obj.get('scorer')}")
    if obj.get("format") not in FORMAT_VALUES:
        errors.append(f"bad format: {obj.get('format')}")
    if obj.get("source") not in SOURCE_VALUES:
        errors.append(f"bad source: {obj.get('source')}")
    if not isinstance(obj.get("needs_disambiguation"), bool):
        errors.append("needs_disambiguation must be a bool")
    if not isinstance(obj.get("resources"), list):
        errors.append("resources must be a list")
    return errors


# ---------------------------------------------------------------------------
# Fixture runner
# ---------------------------------------------------------------------------

def load_fixtures(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _check_duplicate_json_keys(path: str) -> List[str]:
    """Reject duplicate keys inside any single JSON object in the fixture file.

    json.load silently keeps the last duplicate, which would let a typo'd
    override pass; scan per object so the manifest cannot drift silently.
    """
    def _pairs(pairs):
        seen = {}
        for k, v in pairs:
            if k in seen:
                raise ValueError(f"duplicate key {k!r} in object")
            seen[k] = v
        return seen

    errors = []
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    try:
        json.loads(raw, object_pairs_hook=_pairs)
    except ValueError as exc:
        errors.append(str(exc))
    return errors


def run_fixtures(fixtures: List[Dict[str, Any]], source_path: Optional[str] = None) -> Tuple[int, List[str]]:
    failures: List[str] = []
    if source_path:
        failures.extend(_check_duplicate_json_keys(source_path))
    for idx, fx in enumerate(fixtures, start=1):
        inp = fx["input"]
        expect = fx["expect"]
        unknown = [k for k in expect if k not in ROUTE_FIELDS]
        if unknown:
            failures.append(f"fixture {idx} unknown expect fields: {unknown}")
        actual = route_request(inp)
        schema_errors = validate_route_object(actual)
        if schema_errors:
            failures.append(f"fixture {idx} schema: {schema_errors}")
            continue
        for field in ROUTE_FIELDS:
            if field not in expect:
                continue
            if actual.get(field) != expect[field]:
                failures.append(
                    f"fixture {idx} field {field}: expected {expect[field]!r}, got {actual.get(field)!r}"
                )
    return len(failures), failures


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("usage: route_contract.py <request-or-fixtures.json | --self-check>")
        return 2
    arg = argv[1]
    if arg == "--self-check":
        sample = route_request("improve this prompt")
        errs = validate_route_object(sample)
        print(json.dumps(sample, indent=2, ensure_ascii=False))
        return 0 if not errs else 1
    # A path to a fixtures file runs the gate; anything else is a single
    # request to inspect. Branch on the filesystem so a request string never
    # falls into the fixture loader (open() would raise instead of routing).
    if not Path(arg).is_file():
        obj = route_request(arg)
        errs = validate_route_object(obj)
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        if errs:
            print("SCHEMA ERRORS:", errs, file=sys.stderr)
            return 1
        return 0
    try:
        fixtures = load_fixtures(arg)
    except json.JSONDecodeError as exc:
        print(f"invalid fixtures JSON: {exc}", file=sys.stderr)
        return 2
    count, failures = run_fixtures(fixtures, arg)
    if failures:
        print(f"FAILED {count}/{len(fixtures)}")
        for f in failures:
            print(" -", f)
        return 1
    print(f"PASSED {len(fixtures)}/{len(fixtures)} fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
