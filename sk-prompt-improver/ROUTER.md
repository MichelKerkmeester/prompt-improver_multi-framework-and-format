---
title: "sk-prompt-improver Router"
description: "Sibling router for sk-prompt-improver: the command table, the phase detection, the resource map, the Smart Router Pseudocode and the confidence and mode rules a reader parses first."
trigger_phrases:
  - "sk-prompt-improver router"
  - "sk-prompt-improver routing"
importance_tier: normal
contextType: general
version: 1.0.0.0
router_state: active
skill_pointer: SKILL.md
---

# sk-prompt-improver Router

The machine router for [`SKILL.md`](./SKILL.md). `SKILL.md` keeps the short routing prose and the
link that points here; this file holds the routing detail and the machine-readable declaration a
reader parses to decide what loads.

---

## 1. OVERVIEW

A request to write, improve, refine, shorten, deepen or score a prompt, or to draft a visual, image or video generation prompt, reaches sk-prompt-improver, and this router binds it to one primary intent and one output format. Each intent loads its lane from `references/` and `assets/` on top of the always-loaded DEPTH framework and interactive mode, and the matching format guide joins it when a format is locked.

The router answers one question: given a request, which skill-local resources load, in what order, and what happens when nothing matches. The Claude Project kernel ends with the Smart Router Pseudocode below minus its comments, and `benchmark/router/kernel_parity.py` holds the two equal.

---

## 2. INTENT MODEL

### Phase Detection

Resolve the route in a fixed order, reading mode, source prompt, desired format, target model, target platform, complexity, creative medium, reference assets and missing context as you go, then load only what the bound intent needs.

0. **Set the pasted prompt aside.** The prompt the user wants improved is the thing to work on, never a routing signal, because its words describe the target AI's task. A fenced block and a quoted span of three or more words are the pasted prompt. With neither present, the text after a `prompt:` lead-in, up to the next blank line, is the pasted prompt. A quoted span of one or two words, such as `"midjourney"`, is the user naming something and stays. Every later step reads only what is left, so `Improve this prompt: "Write a blog post about photo editing"` routes as text work, never Image, and a pasted prompt with no other signal routes to Improve.
1. **Tokenize and match exactly.** Extract every complete `$token` and check it against the command table by set membership, never a substring `in` test, so `$img` never fires inside a longer word and a bare alias is never a partial hit.
2. **One primary intent, command wins.** A single explicit mode command selects the intent outright and overrides every natural-language signal, so `$short but this is a deep, complex, multi-step system` binds Short, not Deep. Two conflicting mode commands in the same request (for example `$short` and `$deep` together) are not silently resolved; they route to Interactive Mode so the user names the one they meant. With no command, score keywords on word boundaries (`\bprompt\b` matches "write me a prompt" but never "promptly", and `\bask\b` matches "ask a question" but never "basket") and take the single highest-scoring intent. No second intent loads a second resource lane.
3. **Lock the format independently.** `$json`, `$yaml` and `$markdown` (`$j`, `$y`, `$md`, `$m`) select the output format on their own axis and never compete with the mode intent for the primary route; a bare format command with no mode signal still routes the mode to Interactive while the format stays locked.
4. **Disambiguate once when unsure.** A request with no command, no keyword hit and no pasted prompt, or one with conflicting mode commands, routes to Interactive Mode: ask one comprehensive question, then wait. Never invent the mode. After 3 unresolved clarification attempts, use smart defaults and list them as open items instead of asking a fourth time.
5. **Load the lane.** Load the ALWAYS set, the bound intent's resources, and the matching format guide, discovered and guarded at call time.

### Confidence Thresholds

The deterministic oracle characterizes the lane decision only: `command`, `semantic` or `fallback`. The percentage bands below are advisory phrasing for how confidently the assistant speaks about a `semantic`-sourced route; they are not a fourth lane and never change which resources load.

High document-routing confidence is `0.85` or higher.
Medium document-routing confidence is `0.60` or higher.
Low document-routing confidence is `0.40` or higher.
Fallback confidence is below `0.40`.
Signal-based mode auto-detection uses separate user-facing boundaries.
At `80%+` mode confidence, auto-select the mode and explain briefly if useful.
At `50-79%` mode confidence, proceed with the likeliest mode and name it as an open item the user can change.
Below `50%` mode confidence with no pasted prompt, ask one clarifying question, up to 3 clarification attempts total.
If confidence still fails after 3 attempts, use smart defaults and list each one as an open item.

### Natural-Language Topic Signals

Every term below is scored on a word boundary, never as a substring, and folds into the intent it names.

Framework terms route to patterns and evaluation: RCAF, COSTAR, TIDD-EC, CRAFT, RACE, CIDI, CRISPE, RISEN, structure and template.
Scoring terms route to patterns and evaluation: CLEAR, EVOKE, VISUAL, evaluate, quality, assessment, rating, score and points.
Visual UI terms route to visual mode and library: visual concepting, design vibe, UI design, Lovable, Aura, Bolt, v0 and v0.dev.
MagicPath terms route to visual mode and library with VIBE-MP: MagicPath, MagicPath.ai, magic path, multi-page flow, user journey and pathfinding.
Interactive terms route to interactive mode: question, clarify, conversation, dialog, gather and ask.
Thinking terms route to DEPTH: depth, phases, energy, cognitive, rigour, rigor and analysis.
Image-generation terms route to image mode and library: image prompt, picture, photo, Midjourney, DALL-E, Dalle, Stable Diffusion, SDXL, Flux, Flux 2, Imagen, Nano Banana, Seedream, Ideogram, Leonardo, Firefly and Runway image.
Video-generation terms route to video mode and library: video prompt, clip, animation, Runway, Gen-4, Sora, Kling, Veo, Pika, Luma, Ray3, Minimax, Hailuo, Seedance, OmniHuman, Wan and motion.

### Routing Workflow

1. Tokenize and scan explicit `$` commands first, by exact set membership.
2. If two mode commands conflict, stop and ask which one; otherwise the single command wins outright.
3. With no command, scan natural-language mode signals on word boundaries.
4. Detect the format command independently from mode; it never competes for the primary route.
5. Detect target platform for visual, image or video intents.
6. Detect framework mention when the user names one.
7. Load the ALWAYS references.
8. Load the bound intent's mode reference before its mode library.
9. Load the format guide when format is `json`, `yaml`, or an explicit `$markdown`/`$md`/`$m` token.
10. Load patterns and evaluation for framework selection, scoring, repair or alternatives.
11. If a command resolved alone, process immediately.
12. If natural-language scoring produced the top intent, proceed and disclose the route briefly if useful.
13. If no command, no keyword hit and no pasted prompt, or commands conflicted, enter Interactive Mode and ask one comprehensive question.
14. If still ambiguous after 3 clarification attempts, use smart defaults and list each one as an open item.

The pseudocode in Section 3 names the canon's two resilience markers in its own words. `guard_in_skill` is the `_guard_in_skill` path guard: it refuses a path outside the skill and any file that is not markdown. The `INTERACTIVE` lane with source `fallback` is the `UNKNOWN_FALLBACK` route, taken when two mode commands conflict or when nothing else binds.

### Mode Mapping

Raw uses no framework, no scoring and Raw energy.
Text uses RCAF/COSTAR, CLEAR and Standard energy.
Improve uses automatic framework selection, CLEAR and Standard energy.
Refine uses automatic framework selection, CLEAR and Standard energy.
Short uses automatic framework selection, CLEAR and Quick energy.
Deep uses complexity-matched framework selection, CLEAR and Deep energy.
Visual uses VIBE or VIBE-MP, EVOKE and Creative energy; it grounds the subject first (Step 0) and an anti-default grounding gate rejects briefs that read as templated defaults.
MagicPath uses VIBE-MP, EVOKE 42+ and Creative energy.
Image uses FRAME, VISUAL image scoring and Creative energy.
Video uses MOTION, VISUAL video scoring and Creative energy.

### Platform Detection

MagicPath has priority over generic visual routing.
Image platform detection includes Flux, Imagen, Nano Banana, Midjourney, DALL-E, Stable Diffusion, Seedream, Leonardo, Ideogram, Firefly and Runway image.
Video platform detection includes Runway, Sora, Kling, Veo, Pika, Luma, Minimax, Hailuo, Seedance, OmniHuman and Wan.
Full platform syntax stays in the corresponding mode reference and library.

---

## 3. MACHINE ROUTER

The machine-readable projection of the intent model above, moved verbatim from `SKILL.md`: the command table, the resource domains, the loading levels and the Smart Router Pseudocode. This section is the last in the file.

### Primary Detection Signal

Detect the routed intent and lock the output format before loading references. Mode and format are independent axes: a mode command always wins the intent axis, a format command always wins the format axis, and neither steals the other's decision.

```text
$raw                          -> Raw Mode      -> Raw energy, no scoring
$text | $t                    -> Text Mode     -> Standard energy, CLEAR
$improve | $i                 -> Improve Mode  -> Standard energy, CLEAR
$refine | $r                  -> Refine Mode   -> Standard energy, CLEAR
$short | $s                   -> Short Mode    -> Quick energy, CLEAR
$deep | $d                    -> Deep Mode     -> Deep energy, CLEAR
$vibe | $v                    -> Visual Mode   -> Creative energy, EVOKE
$image | $img                 -> Image Mode    -> Creative energy, VISUAL
$video | $vid                 -> Video Mode    -> Creative energy, VISUAL
$json | $j                    -> locks format=json (independent of mode)
$yaml | $y                    -> locks format=yaml (independent of mode)
$markdown | $md | $m          -> locks format=markdown (independent of mode)
no command, keyword hit       -> semantic detection by intent
no command, pasted prompt     -> Improve Mode (the prompt is the request)
two conflicting mode commands -> Interactive Mode (ask which one)
no command, no keyword hit    -> Interactive Mode (one comprehensive question)
```

MagicPath, Framework, Scoring, Interactive and Thinking have no `$` command: word-boundary keyword score is their only way into the primary route.

### Resource Domains

The router discovers markdown resources recursively from `references/` and `assets/` and then applies intent scoring.

```text
references/...   operating docs: DEPTH framework, interactive intelligence, mode workflows, patterns and evaluation
assets/...       copy/apply material: framework pattern library, mode libraries, format guides
```

- `SKILL.md` contains identity, rules, command dispatch and the routing contract; it is never itself a loadable resource.
- `references/depth-framework.md` contains DEPTH phases, energy levels, cognitive rigor and detailed CLEAR gates.
- `references/interactive-mode.md` contains the one-question state machine, conversation templates and recovery patterns.
- `references/patterns-evaluation.md` contains the enhancement patterns and the CLEAR, EVOKE, VISUAL and REPAIR rubrics; `assets/framework-pattern-library.md` holds the framework matrix and selection algorithms.
- `references/visual-mode.md` and `assets/visual-mode-library.md` cover the grounding-first Visual Mode, VIBE/VIBE-MP workflow, MagicPath routing and reusable UI vocabulary.
- `references/image-mode.md` and `assets/image-mode-library.md` cover FRAME workflow, VISUAL image scoring, image platform routing and FRAME banks.
- `references/video-mode.md` and `assets/video-mode-library.md` cover MOTION workflow, VISUAL video scoring, video platform routing and temporal banks.
- `assets/format-guide-markdown.md`, `assets/format-guide-json.md` and `assets/format-guide-yaml.md` carry the syntax and delivery rules for their locked format.

### Resource Loading Levels

| Level       | When to Load                | Resources                                                        |
| ----------- | ---------------------------- | ------------------------------------------------------------------ |
| ALWAYS      | Every skill invocation       | `references/depth-framework.md`, `references/interactive-mode.md` |
| CONDITIONAL | If intent or format matches  | `references/patterns-evaluation.md`, `assets/framework-pattern-library.md`, `references/visual-mode.md`, `assets/visual-mode-library.md`, `references/image-mode.md`, `assets/image-mode-library.md`, `references/video-mode.md`, `assets/video-mode-library.md`, `assets/format-guide-markdown.md`, `assets/format-guide-json.md`, `assets/format-guide-yaml.md` |
| ON_DEMAND   | Only on explicit request     | None beyond the CONDITIONAL set today; archived `z_legacy/` material (when present) is out of routing scope entirely and is never loaded by the router |

### Smart Router Pseudocode

```python
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent
RESOURCE_BASES = (SKILL_ROOT / "references", SKILL_ROOT / "assets")

ALWAYS = ["references/depth-framework.md", "references/interactive-mode.md"]

# Explicit mode commands win outright. Flat token -> intent map, exact whole-
# token match only.
MODE_COMMANDS = {
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

# Output format is a separate axis; it never competes for the primary route.
FORMAT_COMMANDS = {
    "$json": "json", "$j": "json",
    "$yaml": "yaml", "$y": "yaml",
    "$markdown": "markdown", "$md": "markdown", "$m": "markdown",
}

# Natural-language signals, word-boundary scored, never substring. MAGICPATH,
# FRAMEWORK, SCORING, INTERACTIVE and THINKING have no $ command.
INTENT_WEIGHT = {
    "RAW": 6, "TEXT": 5, "IMPROVE": 5, "REFINE": 5, "SHORT": 5, "DEEP": 5,
    "VISUAL": 6, "MAGICPATH": 7, "IMAGE": 6, "VIDEO": 6,
    "FRAMEWORK": 4, "SCORING": 4, "INTERACTIVE": 3, "THINKING": 3,
}
INTENT_KEYWORDS = {
    "RAW": ["raw mode", "passthrough", "no validation"],
    "TEXT": ["text mode", "prompt mode", "prompt", "rcaf", "costar"],
    "IMPROVE": ["improve prompt", "make better", "enhance prompt"],
    "REFINE": ["refine this", "optimise", "optimize", "feedback"],
    "SHORT": ["shorten", "concise", "quick", "fast", "minor"],
    "DEEP": ["complex", "strategic", "multi-step", "comprehensive", "system"],
    "VISUAL": ["visual concepting", "design vibe", "ui design", "lovable", "aura", "bolt", "v0", "v0.dev"],
    "MAGICPATH": ["magicpath", "magic path", "magicpath.ai", "multi-page flow", "user journey", "pathfinding"],
    "IMAGE": ["image prompt", "picture", "photo", "midjourney", "dall-e", "dalle", "stable diffusion", "sdxl", "flux", "flux 2", "imagen", "nano banana", "seedream", "ideogram", "leonardo", "firefly", "runway image"],
    "VIDEO": ["video prompt", "clip", "animation", "runway", "gen-4", "sora", "kling", "veo", "pika", "luma", "ray3", "minimax", "hailuo", "seedance", "omnihuman", "wan", "motion"],
    "FRAMEWORK": ["framework", "rcaf", "costar", "tidd-ec", "craft", "race", "cidi", "crispe", "risen", "template", "structure"],
    "SCORING": ["clear", "evoke", "visual", "score", "quality", "rating", "evaluate", "assessment", "points"],
    "INTERACTIVE": ["question", "clarify", "conversation", "dialog", "gather", "ask", "interactive"],
    "THINKING": ["depth", "phases", "energy", "cognitive", "rigour", "rigor", "analysis"],
}

ENERGY = {"RAW": "raw", "TEXT": "standard", "IMPROVE": "standard", "REFINE": "standard",
          "SHORT": "quick", "DEEP": "deep", "VISUAL": "creative", "MAGICPATH": "creative",
          "IMAGE": "creative", "VIDEO": "creative", "FRAMEWORK": "standard",
          "SCORING": "standard", "INTERACTIVE": "standard", "THINKING": "standard"}
SCORER = {"RAW": None, "TEXT": "CLEAR", "IMPROVE": "CLEAR", "REFINE": "CLEAR", "SHORT": "CLEAR",
          "DEEP": "CLEAR", "VISUAL": "EVOKE", "MAGICPATH": "EVOKE", "IMAGE": "VISUAL",
          "VIDEO": "VISUAL", "FRAMEWORK": None, "SCORING": None, "INTERACTIVE": None, "THINKING": None}

RESOURCE_MAP = {
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
FORMAT_GUIDE = {"json": "assets/format-guide-json.md", "yaml": "assets/format-guide-yaml.md", "markdown": "assets/format-guide-markdown.md"}

MAX_CLARIFYING_QUESTIONS = 3

def discover_markdown_resources():
    docs = []
    for base in RESOURCE_BASES:
        if base.exists():
            docs.extend(p for p in base.rglob("*.md") if p.is_file())
    return {d.relative_to(SKILL_ROOT).as_posix() for d in docs}

def guard_in_skill(relative_path):
    resolved = (SKILL_ROOT / relative_path).resolve()
    resolved.relative_to(SKILL_ROOT)
    if resolved.suffix.lower() != ".md":
        raise ValueError(f"Only markdown resources are routable: {relative_path}")
    return resolved.relative_to(SKILL_ROOT).as_posix()

_TOKEN_RE = re.compile(r"\$[a-z]+")  # whole $tokens only, never substrings

# The prompt the user pasted is the thing to improve, never a routing signal:
# its words describe the target AI's task, so "photo" or "clip" inside it must
# not bind Image or Video. Fenced blocks and quoted spans of three or more
# words are removed, and when neither is present, the text after a
# "prompt:" lead-in up to the next blank line is removed instead. A quoted
# span of one or two words is the user naming something, such as a platform,
# so it stays.
_FENCE_RE = re.compile(r"(`{3}|~{3}).*?(?:\1|\Z)", re.S)
_QUOTE_RE = re.compile(r"\"([^\"]*)\"|\u201c([^\u201d]*)\u201d")
_LEAD_IN_RE = re.compile(r"(\bprompt\b(?:\s+is)?\s*:)[^\n]*(?:\n(?![ \t]*\n)[^\n]*)*", re.I)
SOURCE_QUOTE_MIN_WORDS = 3

def strip_source_prompt(text):
    original = text or ""
    own = _FENCE_RE.sub(" ", original)

    def drop_quote(match):
        quoted = match.group(1) if match.group(1) is not None else match.group(2)
        return " " if len(quoted.split()) >= SOURCE_QUOTE_MIN_WORDS else match.group(0)

    own = _QUOTE_RE.sub(drop_quote, own)
    if own == original:
        own = _LEAD_IN_RE.sub(lambda match: match.group(1), own)
    return own, own != original

def tokenize(text):
    return _TOKEN_RE.findall((text or "").lower())

def detect_command(text):
    # Exact whole-token set membership. Two distinct mode commands in one
    # request are a conflict, not silently resolved.
    modes = {MODE_COMMANDS[tok] for tok in tokenize(text) if tok in MODE_COMMANDS}
    if len(modes) == 1:
        return next(iter(modes)), False
    return None, len(modes) > 1

def detect_format(text):
    for tok in tokenize(text):
        if tok in FORMAT_COMMANDS:
            return FORMAT_COMMANDS[tok], True
    return "markdown", False

def score_intents(text):
    lowered = (text or "").lower()
    scores = {intent: 0 for intent in INTENT_KEYWORDS}
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", lowered):  # word boundary, not substring
                scores[intent] += INTENT_WEIGHT[intent]
    return scores

def detect_intent(text):
    # Only the user's own words route: commands and keywords are read with
    # the pasted prompt removed.
    own, has_source = strip_source_prompt(text)
    command, conflict = detect_command(own)
    if conflict:
        return "INTERACTIVE", "fallback"
    if command:
        return command, "command"  # exact command wins outright over keywords
    scores = score_intents(own)
    best = max(scores, key=scores.get)
    if scores[best] > 0:
        return best, "semantic"
    # A pasted prompt with no other signal is itself the request to improve.
    return ("IMPROVE", "semantic") if has_source else ("INTERACTIVE", "fallback")

def route_prompt_improver_resources(user_request):
    inventory = discover_markdown_resources()
    loaded, seen = [], set()

    def load_if_available(relative_path):
        guarded = guard_in_skill(relative_path)
        if guarded in inventory and guarded not in seen:
            load(guarded)
            loaded.append(guarded)
            seen.add(guarded)

    for reference in ALWAYS:
        load_if_available(reference)

    intent, source = detect_intent(user_request)
    fmt, explicit = detect_format(strip_source_prompt(user_request)[0])

    for reference in RESOURCE_MAP.get(intent, []):
        load_if_available(reference)
    if fmt in ("json", "yaml") or explicit:
        load_if_available(FORMAT_GUIDE[fmt])

    return {
        "intent": intent,
        "energy": ENERGY[intent],
        "scorer": SCORER[intent],
        "format": fmt,
        "source": source,
        "needs_disambiguation": intent == "INTERACTIVE",
        "resources": loaded,
    }
```
