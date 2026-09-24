#!/usr/bin/env python3
"""Hold each named rule on both sides of its declared pair.

Prompt Improver ships its routing and delivery rules in two packagings: a skill
tree consulted by file path, and a set of Project Knowledge documents consulted
by retrieval. `AI Systems/z — Claude Project Sync Loop/systems.py` already declares which
skill file mirrors into which Project document for this system (13 pairs, id
`prompt-improver`). Nothing in that declaration or in the file-inventory gates
built on it reads what a document says, only that it exists and what it is
named. A rule tightened in one packaging and left stale in the other would
still show a clean inventory and a clean fleet declaration.

Diffing all 13 pairs to build this gate surfaced a fleet-wide house-style pass
that strips most em dashes and semicolons out of the Project Knowledge copy
while leaving the skill source as originally written (`references/depth-
framework.md` alone drops from 15 em dashes and 8 semicolons in the skill
source to 5 and 0 in its mirror, with no content lost). That means a rule
phrase built around an em dash or a semicolon would read as drift on almost
every pair even with no rule change at all. Every phrase below was checked
against the live pair before being kept, and none needs one.

This gate names the phrases that carry each rule and requires the same count
on both sides of every declared pair that teaches it. Asymmetry is the
finding: a pair where neither side carries a phrase simply does not teach
that rule and is not a gap.

Counting rather than testing presence is the point. A rule stated three times
in a source and twice in its mirror is exactly the drift a presence test
would call agreement.

What this gate does not catch, so its green is not read as more than it is:
prose that quotes a rule's phrase while discussing it counts as an instance,
so a mirror could reach the same count with a sentence that mentions the rule
rather than states it. Three rules below (scorer exclusivity, the file-
delivery ban on inline output, and framework fit) use the whole sentence as
the phrase where the exact wording is the contract, which closes that gap
for them. The rest rely on a reader.

Usage:
  rule_parity.py            -> check every declared pair, exit 1 on any finding
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CW = os.environ.get("CW_ROOT") or os.path.dirname(os.path.dirname(HERE))
SKILL_ROOT = os.path.join(CW, "sk-prompt-improver")
KNOWLEDGE = os.path.join(CW, "claude project", "knowledge")
SYSTEM_ID = "prompt-improver"

# The shared fleet declaration this system's pairs come from. Never a local
# SYNC.md map: only Deal Templates has one of those in a table this gate could
# parse, and the fleet gates already read every system's pairs from here, so a
# second per-system map would just be a second place the same fact goes stale.
GATE_ROOT = os.environ.get("PARITY_GATE_ROOT") or os.path.join(os.path.dirname(CW), "z — Claude Project Sync Loop")
DECLARATION = os.path.join(GATE_ROOT, "systems.py")


def declared_pairs():
    """The (skill source, Project mirror) pairs `systems.py` declares for this system.

    Read as source text with bytecode disabled, never imported, the same way the
    shared gate reads its own declaration: an import can be answered from
    bytecode cached by path and a modification time truncated to the second,
    which would make an edit written in that same second invisible. `pairs` in
    the declaration maps a mirror filename to a skill-relative source path, the
    opposite order this gate wants, so the pair is flipped on the way out.
    """
    if not os.path.isfile(DECLARATION):
        return None
    sys.dont_write_bytecode = True
    source_text = open(DECLARATION, encoding="utf-8").read()
    namespace = {"__file__": DECLARATION, "__name__": "systems"}
    exec(compile(source_text, DECLARATION, "exec"), namespace)  # noqa: S102  read-only declaration, no writes follow
    decl = namespace["SYSTEMS"].get(SYSTEM_ID)
    if not decl:
        return None
    return [(source, mirror) for mirror, source in decl.get("pairs", {}).items()]


# Each rule names what carries it and how many declared pairs teach it today.
#
# `phrases` are verbatim spans, never patterns, so a reader can grep for one and
# land on the same lines this gate reads. Where the exact statement is the
# contract rather than its presence, the phrase is the whole sentence. The
# clearest case here is the scorer-exclusivity rule: with `CLEAR for visual UI`
# as the span, a mirror could add "is fine in early drafts" after it and keep
# the count at one while reversing the rule. The sentence ends where the rule
# ends, so an edit like that drops the count to zero instead.
#
# `min_pairs` is how many declared pairs teach the rule today, measured against
# the live pairs, not a target. A rule moved from one declared pair to another
# leaves every per-pair count equal, 0 against 0 here and 1 against 1 there, so
# counting alone would report a rule that changed owners as unchanged. The
# floor is what notices the departure. A rise is not a failure, it means the
# number was updated deliberately after adding a pair or a phrase.
RULES = {
    # Interactive Mode states this five times and DEPTH's own Single-Point
    # Interaction principle restates it once more, both holding the same
    # count on both sides today. The single-question contract is what keeps a
    # request for missing context from turning into a multi-message
    # interrogation, so the phrase is the fixed span rather than a synonym
    # like "one question" that would also match incidental prose.
    "every clarifying turn asks exactly one comprehensive question": {
        "phrases": ("one comprehensive question",),
        "min_pairs": 2,
    },
    # Standard and Deep energy both gate on this floor before Harmonize, and
    # DEPTH's own Overview restates it for Interactive Mode's internal
    # processing description. Below this floor the deliverable has not been
    # analysed from enough angles to call the DEPTH pass real.
    "standard and deep energy analyse from a minimum of three perspectives, target five": {
        "phrases": ("Multi-perspective analysis (min 3, target 5)",),
        "min_pairs": 2,
    },
    # CLEAR, EVOKE and VISUAL score three disjoint prompt families. Stated as
    # four sentences, three NEVER and one ALWAYS, because a scorer swap is
    # exactly the kind of edit that survives a presence check: the word
    # "CLEAR" would still be there, just applied to the wrong lane.
    "CLEAR, EVOKE and VISUAL never substitute for each other's prompt family": {
        "phrases": (
            "NEVER use CLEAR for visual UI, image or video prompts.",
            "NEVER use EVOKE for text, image or video prompts.",
            "NEVER use VISUAL for text or visual UI prompts.",
            "ALWAYS validate with the correct scoring system: CLEAR for text, "
            "EVOKE for visual UI, VISUAL for image or video.",
        ),
        "min_pairs": 1,
    },
    # The three creative-mode library assets carry the actual instruction
    # sentence, and the two slim workflow references for Image and Video defer
    # to their library asset under the same MANDATORY heading rather than
    # restating the sentence, so the heading is counted alongside it. Visual
    # Mode's own reference does not carry either span today, which the floor
    # of 5 reflects rather than hides.
    "creative-mode deliverables close with an invitation to share the result back": {
        "phrases": (
            "always ask the user to share their result",
            "### Post-Delivery Question (MANDATORY)",
        ),
        "min_pairs": 5,
    },
    # JSON and YAML each state their own Core Rule with the matching
    # extension. Markdown carries no equivalent sentence because Markdown is
    # the default format and was never given one, which is a real asymmetry
    # in the source material rather than a gap this gate should paper over.
    "JSON and YAML deliverables are downloadable files, never inline": {
        "phrases": (
            "Every enhancement MUST be delivered as a downloadable file (.json), "
            "NEVER inline or in chat.",
            "Every enhancement MUST be delivered as a downloadable file (.yaml/.yml), "
            "NEVER inline or in chat.",
        ),
        "min_pairs": 2,
    },
    # The Framework Pattern Library's own default rule: RCAF is the ordinary
    # choice and complexity must earn a switch away from it, not the reverse.
    "framework fit beats framework complexity, RCAF is the ordinary default": {
        "phrases": (
            "ALWAYS choose framework fit over framework complexity, and use "
            "RCAF as the ordinary default when no better fit is indicated.",
        ),
        "min_pairs": 1,
    },
}


def body(path, drop_frontmatter=False):
    """The document's text, or None when it cannot be read.

    Skill sources carry YAML frontmatter (`title`, `version`, `trigger_phrases`
    and the like) and every Project Knowledge mirror drops it by design, so a
    rule phrase that happened to sit in frontmatter would count on one side and
    not the other and report drift where the packaging is behaving exactly as
    designed. No rule phrase here lives in frontmatter today, which is exactly
    when to close the gap rather than after a phrase moves into one.
    """
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError:
        return None
    if drop_frontmatter and text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    return text


def inside(root, path):
    """Whether a resolved path stays under root, checked lexically.

    `systems.py` names the source side of a pair as a path relative to
    `sk-prompt-improver/`, so a row that climbed out with `..` or supplied an
    absolute path would have `os.path.join` hand back whatever it pointed at
    instead. Nothing in this system's 13 pairs is a symlink today, but the
    check stays lexical rather than resolving, because a symlink into a shared
    knowledge tree elsewhere in the fleet resolves outside every skill root by
    construction and a gate that would reject a legitimate pair the day one is
    added is a gate nobody keeps. `abspath` normalises `..` and relative
    segments without following a link, which is the property this needs.
    """
    root = os.path.abspath(root)
    target = os.path.abspath(path)
    return target == root or target.startswith(root + os.sep)


def main() -> int:
    pairs = declared_pairs()
    if not pairs:
        print("no declared pairs, so no rule could be compared", file=sys.stderr)
        return 2

    findings, taught, compared = [], {name: 0 for name in RULES}, 0
    for source, document in pairs:
        source_path = os.path.join(SKILL_ROOT, source)
        if not inside(SKILL_ROOT, source_path):
            findings.append(
                f"{source}: the declared source sits outside the skill root, so "
                f"this pair was not compared"
            )
            continue
        left = body(source_path, drop_frontmatter=True)
        right = body(os.path.join(KNOWLEDGE, document))
        if left is None or right is None:
            missing = source if left is None else document
            findings.append(f"{missing}: cannot be read, so this pair was not compared")
            continue
        compared += 1
        for name, rule in RULES.items():
            pair_teaches = False
            for phrase in rule["phrases"]:
                here, there = left.count(phrase), right.count(phrase)
                if here or there:
                    pair_teaches = True
                if here != there:
                    findings.append(
                        f"{name}: `{phrase}` appears {here}x in {source} and "
                        f"{there}x in its mirror {document}"
                    )
            if pair_teaches:
                taught[name] += 1

    for name, rule in RULES.items():
        if taught[name] < rule["min_pairs"]:
            findings.append(
                f"{name}: taught by {taught[name]} pair(s) and {rule['min_pairs']} "
                f"are declared, so the rule left a pair that carried it"
            )

    print(f"  pairs: {compared} of {len(pairs)} declared pairs compared")
    for name, rule in RULES.items():
        print(f"  {name}: taught by {taught[name]} pair(s), {rule['min_pairs']} declared")

    if findings:
        print(f"FAILED {len(findings)} rule parity finding(s)")
        for finding in findings:
            print(f" - {finding}")
        return 1
    print(f"PASSED {len(RULES)} rules hold on both sides of every pair that teaches them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
