#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: DELIVERABLE BLOCK LINTER
# ───────────────────────────────────────────────────────────────

"""Deterministic linter for Prompt Improver's own stated output rules.

Usage: deliverable_lint.py <file>   ->  prints JSON {file, clean, confidence, violations:[...]}

This system states no banned-vocabulary or punctuation rule for the prompts it writes,
the way Deal Templates and Copywriter do for prose copy. What it states, repeatedly and
without qualification, is a structural contract for a Project reply and a hard ban on
claiming a save or an export that a claude.ai Project cannot perform:

  - ALWAYS open the reply with one bare code fence holding only the improved prompt,
    so its copy button copies exactly the prompt (Custom Instructions.md's delivery
    rule and DELIVERY PROTOCOL). A tagged fence scrolls sideways on claude.ai, so the
    fence carries no language tag
  - NEVER put a header line, a divider footer, scoring, processing notes or assumptions
    inside the fence; the header facts, score, summary and open items follow it in chat
  - Open items are numbered, each topic in bold over a `- **Situation:**` bullet and a
    `- **Open:**` bullet, no blank line inside or between items, or `None identified`
  - NEVER claim this Project saved, exported, verified on disk or executed anything
  - Interactive Mode bans emoji bullets in question or validation text

Every check below cites the rule above it. This is a CODE gate: each check is a fixed
string or a narrow structural pattern, never a model asked to judge tone.

The opening fence is the block boundary, so confidence is high when the reply opens
with a fence and low when it does not. At low confidence the fence checks cannot run
and `fence_not_first` is reported instead; the claimed-save, header, open items and
emoji checks read the whole reply either way.
"""
import json
import re
import sys

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

ANSI = re.compile(r"\x1b\[[0-9;]*m")

# Custom Instructions.md's ban on claiming a save or an export, and the advisory-only
# header: this Project "cannot write files to a filesystem, run the CLI export sequence
# or verify a saved path". Any of these phrases in a reply is that claim being made
# anyway.
CLAIMED_EXECUTION_PHRASES = [
    "i've saved", "i have saved", "has been saved", "successfully saved",
    "saved to disk", "saved to your", "saved the file", "wrote the file",
    "exported to", "successfully exported", "i've exported", "i have exported",
    "the file has been created", "written to disk", "verified on disk",
    "the file is now available at", "download the saved file",
]

# DELIVERY PROTOCOL: the reply opens with one fence. The opener is three or more
# backticks or tildes; anything after them is a language tag, which makes claude.ai
# scroll long lines sideways instead of wrapping them.
FENCE_OPEN = re.compile(r"^[ ]{0,3}(`{3,}|~{3,})(.*)$")

# The header facts move to chat after the fence: "Mode: $[mode] | Complexity: [level] |
# Framework: [Framework]" on one line. Score is deliberately absent from it, because
# the score has its own line.
MODE_LINE = re.compile(r"^\s*Mode:.*$", re.M)
REQUIRED_HEADER_FIELDS = ("Complexity:", "Framework:")

# The retired footer. Its facts are either chat lines or the standing no-save ban, and
# inside the fence it would be copied with the prompt.
ATTESTATION_LINE = re.compile(r"^\s*Attestation:", re.M)

# Scoring breakdowns, processing notes, format options and assumptions belong in chat
# after the fence, never inside it.
FORBIDDEN_INSIDE_FENCE = (
    "CLEAR score", "EVOKE score", "VISUAL score", "Perspectives:", "Assumptions:",
    "[Assumes:",
)

# Open items shape, the same one Deal Templates uses, because claude.ai joins a label
# on a line of its own to the line above it while a bullet keeps its line.
OPEN_HEADING = re.compile(r"^#{2,4}\s+Open items\s*$", re.M)
OPEN_ITEM = re.compile(r"^(\d+)\. \*\*[^*]+\*\*$")
OPEN_SITUATION = re.compile(r"^   - \*\*Situation:\*\* \S")
OPEN_QUESTION = re.compile(r"^   - \*\*Open:\*\* \S")
OPEN_NONE = "None identified"

# Interactive Mode bans emoji bullets in question or validation text. Markdown dashes
# stay allowed, since Interactive Mode's own MUST list asks for them. This matches
# only decorative emoji used as a bullet glyph at the start of a line.
EMOJI_BULLET = re.compile(
    "^[ \t]*(?:✅|❌|\U0001f539|\U0001f538|▪|\U0001f53a|"
    "➡|\U0001f449|\U0001f4cc|⭐|✨|\U0001f3af|\U0001f4a1|\U0001f680)\\s+",
    re.M,
)


# ───────────────────────────────────────────────────────────────
# 2. HELPERS
# ───────────────────────────────────────────────────────────────


def samples(pattern_or_literal, text, n=2, literal=False):
    """Up to n short excerpts of text around each match.

    Args:
        pattern_or_literal: A compiled pattern, or the literal text to find when
            `literal` is True.
        text: The reply text to search.
        n: Maximum number of excerpts to return.
        literal: Match `pattern_or_literal` as plain text rather than a pattern.

    Returns:
        A list of single-line context excerpts.
    """
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


def extract_fence(clean: str):
    """Return (opener_line, body, after, confidence) for the reply's opening fence.

    The fence counts only when it is the first non-blank line. It closes at the first
    later line made of the same character, at least as long as the opener, so a
    shorter fence inside the prompt stays part of the body. An unclosed fence runs to
    the end of the reply.
    """
    lines = clean.split("\n")
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first is None:
        return None, None, clean, "low"
    match = FENCE_OPEN.match(lines[first])
    if not match:
        return None, None, clean, "low"
    marker = match.group(1)
    closer = re.compile(r"^[ ]{0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*$")
    for end in range(first + 1, len(lines)):
        if closer.match(lines[end]):
            return lines[first], "\n".join(lines[first + 1:end]), "\n".join(lines[end + 1:]), "high"
    return lines[first], "\n".join(lines[first + 1:]), "", "high"


def open_items_errors(text: str):
    """Problems in a reply's Open items, or an empty list when the shape holds."""
    lines = text.split("\n")
    start = next((i for i, line in enumerate(lines) if OPEN_HEADING.match(line)), None)
    if start is None:
        return None
    rest = lines[start + 1:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    if rest and rest[0].strip() == OPEN_NONE:
        return []
    body = []
    while rest and rest[0].strip() and (OPEN_ITEM.match(rest[0]) or rest[0].startswith("   ")):
        body.append(rest.pop(0))
    if not body:
        return ["Open items holds no numbered item and no `None identified` line"]
    after = next((line for line in rest if line.strip()), "")
    if OPEN_ITEM.match(after) or after.startswith("   - **"):
        return ["a blank line sits inside or between open items, which claude.ai renders as a label joined to the line above"]
    if len(body) % 3:
        return [f"Open items holds {len(body)} line(s), where each item takes a topic, a Situation bullet and an Open bullet"]
    problems = []
    for number, at in enumerate(range(0, len(body), 3), start=1):
        topic, situation, question = body[at:at + 3]
        found = OPEN_ITEM.match(topic)
        if not found or int(found.group(1)) != number:
            problems.append(f"open item {number} does not open on `{number}. **Topic**`")
        if not OPEN_SITUATION.match(situation):
            problems.append(f"open item {number} has no indented `- **Situation:**` bullet with its text on the same line")
        if not OPEN_QUESTION.match(question):
            problems.append(f"open item {number} has no indented `- **Open:**` bullet with its text on the same line")
    return problems


# ───────────────────────────────────────────────────────────────
# 3. CORE LOGIC
# ───────────────────────────────────────────────────────────────


def lint_reply(raw: str):
    """Return (violations, confidence) for one reply's full text.

    The fence checks run only when the reply opens with a fence, because that fence is
    the only trustworthy block boundary. The claimed-save, header, open items and
    emoji checks are stated for the reply as a whole and always run.
    """
    clean = ANSI.sub("", raw)
    opener, body, after, confidence = extract_fence(clean)
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

    if confidence != "high":
        first = next((line for line in clean.splitlines() if line.strip()), "")
        add("fence_not_first", 1, [f"the reply opens with: {first.strip()[:80]!r}"])
        chat = clean
    else:
        chat = after
        tag = FENCE_OPEN.match(opener).group(2).strip()
        add("fence_tagged", 1 if tag else 0, [f"the opening fence carries the tag {tag!r}"])
        add("header_inside_fence", len(MODE_LINE.findall(body)), samples(MODE_LINE, body))
        add("attestation_inside_fence", len(ATTESTATION_LINE.findall(body)), samples(ATTESTATION_LINE, body))
        for token in FORBIDDEN_INSIDE_FENCE:
            if token in body:
                add("scoring_inside_fence", body.count(token), samples(token, body, n=1, literal=True))
        stripped = body.strip()
        if stripped[:1] in ("{", "["):
            try:
                json.loads(stripped)
            except ValueError as error:
                add("payload_unparseable", 1, [f"the fence opens like JSON but does not parse: {error}"])

    mode_lines = MODE_LINE.findall(chat)
    if not mode_lines:
        add("header_missing", 1, ["no `Mode:` line follows the fence in chat"])
    else:
        bad = [line for line in mode_lines
               if any(field not in line for field in REQUIRED_HEADER_FIELDS)]
        add("header_malformed", len(bad), [b.strip()[:120] for b in bad[:2]])

    raw_mode = any("$raw" in line for line in mode_lines)
    problems = open_items_errors(chat)
    if problems is None:
        if not raw_mode:
            add("open_items_missing", 1, ["no `### Open items` heading follows the fence"])
    else:
        add("open_items_malformed", len(problems), problems[:2])

    add("emoji_bullets", len(EMOJI_BULLET.findall(clean)), samples(EMOJI_BULLET, clean))

    return violations, confidence


# ───────────────────────────────────────────────────────────────
# 4. ENTRY POINT
# ───────────────────────────────────────────────────────────────


def main(argv) -> int:
    """Lint one reply file and print the result as JSON.

    Returns 0 when the reply carries no hard violation, 1 on any hard
    violation, 2 when the file cannot be read and 64 when it is not named.
    """
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
