#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: KERNEL ROUTER PARITY GATE
# ───────────────────────────────────────────────────────────────

"""Kernel router parity gate for the Prompt Improver Claude Project.

A Claude Project reads its kernel on every turn and retrieves Knowledge only
by relevance, so a router kept in a Knowledge document routes a turn only
when retrieval happens to pull it. The kernel therefore ends with
`## 8. ROUTER CODE`, one python fence holding the Smart Router Pseudocode
from `sk-prompt-improver/SKILL.md` with every comment removed. The comments
explain the design to a maintainer and change nothing a model routes, so the
kernel copy carries the code without them.

The two copies can drift silently. A fixture run proves the executable route
contract routes as intended and says nothing about the kernel's copy, so a
hand edit to either side stays invisible until the Project's routing
contradicts the skill. This gate proves the kernel's one python fence equals
the skill's pseudocode block minus its comments, byte for byte after the
strip and as a syntax tree, so drift fails here with the first differing
line named. A missing file, heading, fence or source block reports a
labelled failure line, never a traceback.

Python 3.9 compatible.
"""
from __future__ import annotations

import ast
import io
import re
import sys
import tokenize
from pathlib import Path
from typing import List, Optional

# ───────────────────────────────────────────────────────────────
# 1. CONFIGURATION
# ───────────────────────────────────────────────────────────────

HERE = Path(__file__).resolve().parent
SYSTEM_ROOT = HERE.parent.parent
SKILL_MD = SYSTEM_ROOT / "sk-prompt-improver" / "SKILL.md"
KERNEL_MD = SYSTEM_ROOT / "claude project" / "Custom Instructions.md"

PSEUDOCODE_HEADING = "### Smart Router Pseudocode"
KERNEL_ROUTER_HEADING = "## 8. ROUTER CODE"

# Any fence a markdown renderer will highlight as python. A check written as
# the single literal "```python" anchored to a whole line is a check every
# other spelling of the same fence walks past: the "py" alias, a capital in
# the language name, a trailing space, four backticks or tildes, the
# indentation markdown still reads as a fence, and the braced "```{python}"
# and "``` {.python}" forms several toolchains read as executable cells.
PYTHON_FENCE_RE = re.compile(
    r"^[ ]{0,3}(?:`{3,}|~{3,})[ \t]*\{?[ \t]*\.?(?:python|python3|py|py3|ipython|sage)\b",
    re.M | re.I,
)

# Every spelling the matcher must catch, pinned as data so a weakened matcher
# fails here instead of waving a repasted fence through the count below.
PYTHON_FENCE_SPELLINGS = (
    "```python", "```py", "```python3", "```py3", "```ipython", "```sage",
    "```Python", "```python ", "````python", "~~~python", "   ```python",
    "```{python}", "``` {.python}",
)


# ───────────────────────────────────────────────────────────────
# 2. BLOCK EXTRACTION AND COMMENT STRIPPING
# ───────────────────────────────────────────────────────────────

def fenced_block(text: str, heading: str, name: str) -> str:
    """Return the ```python block under `heading` in a markdown document.

    The section ends at the next heading of the same or a higher level, and
    the walk tracks fenced code, so a `#` comment inside a fence never reads
    as a heading and a python fence in a later section is never picked up.
    """
    found = re.search(rf"^[ ]{{0,3}}{re.escape(heading)}[ \t]*$", text, re.M)
    if not found:
        raise LookupError(f"{name} has no {heading!r} section")
    level = len(heading) - len(heading.lstrip("#"))
    section: List[str] = []
    in_fence = False
    for line in text[found.end():].splitlines():
        if re.match(r"^[ ]{0,3}(?:`{3,}|~{3,})", line):
            in_fence = not in_fence
        elif not in_fence and re.match(rf"[ ]{{0,3}}#{{1,{level}}}[ \t]", line):
            break
        section.append(line)
    match = re.search(r"```python\n(.*?)\n```", "\n".join(section), re.S)
    if not match:
        raise LookupError(f"{name} has no python block under {heading!r}")
    return match.group(1)


def strip_comments(block: str) -> str:
    """Return a python block with every comment removed and blank runs collapsed.

    The tokenizer finds the comments, so a `#` inside a string or a regex is
    kept. A line left empty by the cut is dropped, and a run of blank lines
    collapses to one, so the result is the code alone in its original order
    and indentation.
    """
    cuts = {tok.start[0]: tok.start[1]
            for tok in tokenize.generate_tokens(io.StringIO(block).readline)
            if tok.type == tokenize.COMMENT}
    kept: List[str] = []
    for number, line in enumerate(block.split("\n"), 1):
        if number in cuts:
            line = line[:cuts[number]]
            if not line.strip():
                continue
        kept.append(line.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip("\n")


# ───────────────────────────────────────────────────────────────
# 3. THE PARITY CHECK
# ───────────────────────────────────────────────────────────────

def check_kernel_parity() -> List[str]:
    """Prove the kernel's Router Code is the skill's router minus its comments.

    Every failure is a labelled line, never a traceback: an unreadable file,
    a missing heading, a missing fence and a block that cannot be tokenized
    or parsed each report what went wrong.
    """
    failures: List[str] = []

    for spelling in PYTHON_FENCE_SPELLINGS:
        if not PYTHON_FENCE_RE.search(f"{spelling}\nx = 1\n"):
            failures.append(
                "kernel parity: the python fence matcher no longer catches "
                f"{spelling!r}, so a router pasted in under that spelling "
                "would clear the fence count below")

    try:
        skill_text: Optional[str] = SKILL_MD.read_text(encoding="utf-8")
    except OSError as exc:
        failures.append(
            f"kernel parity: the skill router source is unreadable: {exc}")
        skill_text = None

    skill_block: Optional[str] = None
    if skill_text is not None:
        try:
            skill_block = fenced_block(
                skill_text, PSEUDOCODE_HEADING, SKILL_MD.name)
        except LookupError as exc:
            failures.append(f"kernel parity: {exc}")

    try:
        kernel_text: Optional[str] = KERNEL_MD.read_text(encoding="utf-8")
    except OSError as exc:
        failures.append(f"kernel parity: the kernel is unreadable: {exc}")
        kernel_text = None

    kernel_block: Optional[str] = None
    if kernel_text is not None:
        kernel_fences = len(PYTHON_FENCE_RE.findall(kernel_text))
        if kernel_fences != 1:
            failures.append(
                f"kernel parity: the kernel carries {kernel_fences} python "
                "fences where it carries exactly one, the router under "
                f"{KERNEL_ROUTER_HEADING!r}")
        try:
            kernel_block = fenced_block(
                kernel_text, KERNEL_ROUTER_HEADING, KERNEL_MD.name)
        except LookupError as exc:
            failures.append(f"kernel parity: {exc}")

    if skill_block is None or kernel_block is None:
        return failures

    try:
        expected = strip_comments(skill_block)
    except (SyntaxError, ValueError, tokenize.TokenError) as exc:
        failures.append(
            "kernel parity: the skill's router block cannot be tokenized: "
            f"{exc}")
        return failures

    if kernel_block != expected:
        kernel_lines = kernel_block.splitlines()
        expected_lines = expected.splitlines()
        drift = next(
            (number for number, (have, want) in enumerate(
                zip(kernel_lines, expected_lines), 1) if have != want),
            min(len(kernel_lines), len(expected_lines)) + 1)
        kernel_line = kernel_lines[drift - 1] if drift <= len(kernel_lines) else "<absent>"
        expected_line = expected_lines[drift - 1] if drift <= len(expected_lines) else "<absent>"
        failures.append(
            f"kernel parity: the kernel's router is not {SKILL_MD.name}'s "
            "Smart Router Pseudocode minus its comments, first difference at "
            f"code line {drift}: kernel has {kernel_line!r} where the strip "
            f"expects {expected_line!r}")
        return failures

    try:
        same_tree = (ast.dump(ast.parse(kernel_block))
                     == ast.dump(ast.parse(skill_block)))
    except (SyntaxError, ValueError) as exc:
        failures.append(
            "kernel parity: a router block does not parse, so its syntax "
            f"tree cannot be compared: {exc}")
    else:
        if not same_tree:
            failures.append(
                "kernel parity: removing the comments changed the router's "
                "syntax tree, so the kernel's copy no longer means what the "
                "skill's router means")
    return failures


# ───────────────────────────────────────────────────────────────
# 4. ENTRY POINT
# ───────────────────────────────────────────────────────────────

def main() -> int:
    """Run the parity gate, printing each failure or the one PASSED line."""
    failures = check_kernel_parity()
    if failures:
        for failure in failures:
            print(f"FAILED {failure}")
        return 1
    print(
        f"PASSED kernel router parity: {KERNEL_MD.name}'s one python fence "
        f"under {KERNEL_ROUTER_HEADING!r} equals {SKILL_MD.name}'s Smart "
        "Router Pseudocode with its comments removed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
