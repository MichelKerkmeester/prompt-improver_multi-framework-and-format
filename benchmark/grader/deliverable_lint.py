#!/usr/bin/env python3
"""Deterministic linter for Prompt Improver's own stated output rules.

Usage: deliverable_lint.py <file>   ->  prints JSON {file, clean, confidence, violations:[...]}

This system has no grader of any kind before this file. Building one meant reading
`claude project/Custom Instructions.md` first to name what it actually requires of a
reply, rather than reusing another system's word list. Deal Templates and Copywriter
gate punctuation and vocabulary in prose copy. Prompt Improver states no such rule for
the prompts it writes. What it states, repeatedly and without qualification, is a
structural contract for the Deliverable Block and a hard ban on claiming a save or an
export that a claude.ai Project cannot perform:

  - ALWAYS render the Deliverable Block before any commentary (Custom Instructions.md
    RULES > ALWAYS #6), and NEVER skip it for loose inline chat text instead (#8)
  - ALWAYS keep the Deliverable Block to a single-line header plus prompt content plus
    an attestation footer only (#7), matching the template in DELIVERY PROTOCOL
  - NEVER put scoring breakdowns, processing notes or format options inside the block
    (NEVER #6), and NEVER paste the full deliverable again in chat afterward (#7)
  - NEVER claim this Project saved, exported, verified on disk or executed anything
    (NEVER #12). The QUALITY CHECKLIST repeats it: "no execution, save or verification
    was claimed"
  - Interactive Mode's own NEVER #14 bans emoji bullets in question or validation text

Every check below cites the line above it. This is a CODE gate: each check is a fixed
string or a narrow structural pattern, never a model asked to judge tone.

Extraction confidence is carried rather than hidden. A benchmark capture that wraps the
rendered block in `<DELIVERABLE>...</DELIVERABLE>` (this system's own convention, absent
a live harness today) gives high confidence and unlocks the two checks that need to know
where the block ends: nothing must sit inside it besides the header, the prompt and the
footer, and nothing must sit before it. A capture with no tags is scored on the header,
attestation, execution-claim and emoji checks only, at medium confidence when a `Mode:`
line is still findable and low confidence when it is not, because a chat reply is prose
throughout and the block boundary cannot be trusted either way. The counts still stand
regardless of confidence.
"""
import json
import re
import sys

DELIVERABLE_TAG = re.compile(r"<DELIVERABLE>(.*?)</DELIVERABLE>", re.S | re.I)
ANSI = re.compile(r"\x1b\[[0-9;]*m")

# Custom Instructions.md NEVER #12 and the advisory-only header (line 10): this Project
# "cannot write files to a filesystem, run the CLI export sequence or verify a saved
# path". Any of these phrases in a reply is that claim being made anyway.
CLAIMED_EXECUTION_PHRASES = [
    "i've saved", "i have saved", "has been saved", "successfully saved",
    "saved to disk", "saved to your", "saved the file", "wrote the file",
    "exported to", "successfully exported", "i've exported", "i have exported",
    "the file has been created", "written to disk", "verified on disk",
    "the file is now available at", "download the saved file",
]

# DELIVERY PROTOCOL's attestation line states both fields as a fixed pair, and NEVER
# #12 forbids the reverse of either.
ATTESTATION_LINE = re.compile(r"^Attestation:.*$", re.M)
REQUIRED_ATTESTATION_FIELDS = ("execution = did not occur", "save = did not occur")

# DELIVERY PROTOCOL's header template: "Mode: $[mode] | Complexity: [level] |
# Framework: [Framework]", three fields on one line. Score is deliberately absent:
# ALWAYS #8 puts score, assumptions and docs consulted in chat after the block, and
# the protocol's own line says the Artifact carries the prompt and not the scoring
# explanation. A fourth Score field was required here and cited to ALWAYS #7, which
# says nothing about field count, so the check failed a runtime for obeying #8.
MODE_LINE = re.compile(r"^\s*Mode:.*$", re.M)
REQUIRED_HEADER_FIELDS = ("Complexity:", "Framework:")

# Interactive Mode NEVER #14. Markdown dashes stay allowed, since Interactive Mode's
# own MUST list asks for them. This matches only decorative emoji used as a bullet
# glyph at the start of a line.
EMOJI_BULLET = re.compile(
    "^[ \t]*(?:✅|❌|\U0001f539|\U0001f538|▪|\U0001f53a|"
    "➡|\U0001f449|\U0001f4cc|⭐|✨|\U0001f3af|\U0001f4a1|\U0001f680)\\s+",
    re.M,
)

# NEVER #6: scoring breakdowns, processing notes and format options belong in chat
# after the block, never inside it.
FORBIDDEN_INSIDE_BLOCK = (
    "CLEAR score", "EVOKE score", "VISUAL score", "Perspectives:", "Assumptions:",
)


def samples(pattern_or_literal, text, n=2, literal=False):
    out = []
    if literal:
        start = 0
        needle = pattern_or_literal
        while len(out) < n:
            i = text.lower().find(needle.lower(), start)
            if i == -1:
                break
            out.append(text[max(0, i - 25): i + len(needle) + 25].replace("\n", " ").strip())
            start = i + len(needle)
        return out
    for m in pattern_or_literal.finditer(text):
        out.append(text[max(0, m.start() - 25): m.end() + 25].replace("\n", " ").strip())
        if len(out) >= n:
            break
    return out


def extract_deliverable(raw: str):
    """Return (block_or_None, confidence, prefix).

    `prefix` is whatever sits before the opening tag, which is only meaningful, and
    only trustworthy, at high confidence: a capture with no explicit tag has no
    reliable block boundary to check a prefix against.
    """
    clean = ANSI.sub("", raw)
    match = DELIVERABLE_TAG.search(clean)
    if match:
        return match.group(1), "high", clean[:match.start()]
    if MODE_LINE.search(clean):
        return None, "medium", None
    return None, "low", None


def lint_reply(raw: str):
    """Return (violations, confidence) for one reply's full text.

    Most checks read the whole reply rather than an extracted block, because the
    rules they enforce (no execution claim, an attestation footer, no emoji bullets)
    are stated for the reply as a whole, not for text a harness happened to tag. Only
    the two checks that need to know where the block ends are gated on having found
    an explicit `<DELIVERABLE>` tag.
    """
    clean = ANSI.sub("", raw)
    block, confidence, prefix = extract_deliverable(raw)
    violations = []

    def add(kind, count, sample_list, severity="hard"):
        if count:
            violations.append({"type": kind, "severity": severity, "count": count, "samples": sample_list})

    exec_hits = sum(clean.lower().count(p) for p in CLAIMED_EXECUTION_PHRASES)
    exec_samples = []
    for p in CLAIMED_EXECUTION_PHRASES:
        if p in clean.lower():
            exec_samples.extend(samples(p, clean, n=1, literal=True))
    add("claimed_execution", exec_hits, exec_samples[:2])

    attestation_lines = ATTESTATION_LINE.findall(clean)
    if not attestation_lines:
        add("attestation_missing", 1, ["no line beginning `Attestation:` was found"])
    else:
        bad = [line for line in attestation_lines
               if any(field not in line for field in REQUIRED_ATTESTATION_FIELDS)]
        add("attestation_incomplete", len(bad), [b.strip()[:120] for b in bad[:2]])

    mode_lines = MODE_LINE.findall(clean)
    if not mode_lines:
        add("header_missing", 1, ["no line beginning `Mode:` was found"])
    else:
        bad = [line for line in mode_lines
               if any(field not in line for field in REQUIRED_HEADER_FIELDS)]
        add("header_malformed", len(bad), [b.strip()[:120] for b in bad[:2]])

    add("emoji_bullets", len(EMOJI_BULLET.findall(clean)), samples(EMOJI_BULLET, clean))

    if confidence == "high":
        if prefix and prefix.strip():
            add("deliverable_not_first", 1, [prefix.strip()[-80:]])
        body_lines = block.splitlines()
        body = "\n".join(body_lines[1:]) if body_lines else ""
        body = body.rsplit("\n---\n", 1)[0] if "\n---\n" in body else body
        for token in FORBIDDEN_INSIDE_BLOCK:
            if token in body:
                add("scoring_inside_block", body.count(token), samples(token, body, n=1, literal=True))

    return violations, confidence


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: deliverable_lint.py <file>", file=sys.stderr)
        return 64
    path = argv[1]
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            raw = handle.read()
    except OSError as error:
        print(f"cannot read {path}: {error}", file=sys.stderr)
        return 2
    violations, confidence = lint_reply(raw)
    hard = [v for v in violations if v["severity"] == "hard"]
    result = {
        "file": path,
        "clean": not hard,
        "confidence": confidence,
        "violations": violations,
    }
    print(json.dumps(result, indent=2))
    # Deal Templates' equivalent single-file tool always exits 0, clean or not, and
    # that zero has already been misread once in this fleet as a pass. Nothing here
    # depends on this exit code (`lint_replies.py` imports `lint_reply` directly
    # rather than shelling out), so there is no reason to carry the same trap.
    return 0 if not hard else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
