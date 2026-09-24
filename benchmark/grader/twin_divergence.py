#!/usr/bin/env python3
"""Report scenario twins whose two runtimes disagreed in a run.

`sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md` (section 1,
Coverage map) declares fourteen scenarios in two runtime sets over six categories:
identity (ID), interactive routing (IR), text modes (TX), format modes (FM), creative
modes (CR) and safety boundaries (SB). Every id is `S` or `P` for the runtime, the
two-letter category, a dash, then a zero-padded number, for example `SID-001` on the
skill runtime and `PID-001` on the Project runtime for the same identity-handover
brief. `SIR-001`/`PIR-001` and `SIR-002`/`PIR-002` cover the two interactive-routing
scenarios, and `STX`, `SFM`, `SCR` and `SSB` each pair with their `P` counterpart the
same way. Fourteen scenarios, seven twins, no category runs on only one side.

Both runtimes read the same rules, one from a file tree and one from a Project's
retrieval step, and this pairing is the only instrument here for a behavioral
difference no static check can see: the packagings could hold identical rule text,
pass every rule-parity and inventory check, and still answer a scenario differently
because one consults a file directly and the other depends on what a retrieval pass
surfaced. `SID-001`/`PID-001` exists specifically to prove the two runtimes cannot be
swapped for each other: the skill anchors on a real export path, the Project anchors on
the verbatim `Canvas Artifact` string and the no-save contract, and the playbook's own
two-runtime proof rule calls a reply that could have come from either runtime a `FAIL`
on its own.

A twin pair is the unit. A scenario run on only one runtime is unpaired, not counted as
agreeing, because a comparison that quietly drops half its input reports agreement it
never measured. An id carrying a suffix after the number is a variant, a re-run or a
diagnostic rather than a runtime's answer to the scenario, and is listed rather than
paired. A `PARTIAL` result is never compared: most of these scenarios chain up to two
user turns, and a run that only completed the first turn is evidence about that turn
alone, not a verdict a comparison can use.

Exit codes:
  0  every paired twin agreed
  1  at least one pair disagreed
  2  no results file, or nothing in it that could be paired

Usage:
  twin_divergence.py <run report dir, or a results.csv>
"""
import csv
import re
import sys
from pathlib import Path

# Matches the playbook's own id shape: runtime letter, two-letter category, dash,
# digits. A trailing suffix (`SID-001b`, `PID-001-retry`) does not match and falls
# through to the variants list instead of being forced into a pair.
SCENARIO_ID = re.compile(r"^([SP])([A-Z]{2})-(\d+)$")

PARTIAL = "PARTIAL"


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main(argv) -> int:
    if len(argv) < 2:
        print("usage: twin_divergence.py <run report dir, or a results.csv>", file=sys.stderr)
        return 64
    target = Path(argv[1]).resolve()
    results = target / "results.csv" if target.is_dir() else target
    if not results.is_file():
        print(f"no results file at {results}, so no twin was compared", file=sys.stderr)
        return 2

    paired, variants = {}, []
    for row in rows(results):
        scenario_id = (row.get("id") or "").strip()
        match = SCENARIO_ID.match(scenario_id)
        if not match:
            variants.append(scenario_id or "?")
            continue
        runtime, category, number = match.groups()
        paired.setdefault(f"{category}-{number}", {})[runtime] = row

    if not paired:
        print(f"no rows in {results.name} carry a twin id, so nothing was compared", file=sys.stderr)
        return 2

    disagreed, agreed, unpaired, partial = [], [], [], []
    for key, sides in sorted(paired.items()):
        if len(sides) < 2:
            unpaired.append((key, next(iter(sides))))
            continue
        skill, project = sides["S"]["result"].strip(), sides["P"]["result"].strip()
        if PARTIAL in (skill, project):
            partial.append((key, skill, project))
            continue
        (agreed if skill == project else disagreed).append((key, skill, project))

    for key, skill, project in disagreed:
        print(f"  {key}: skill {skill}, Project {project}")
    print(f"  {len(agreed)} twin(s) agreed, {len(disagreed)} disagreed, "
          f"{len(partial)} not settled, {len(unpaired)} run on one runtime only")
    if partial:
        print("  not settled: " + ", ".join(f"{k} (skill {s}, Project {p})" for k, s, p in partial))
    if unpaired:
        print("  unpaired: " + ", ".join(f"{k} ({s})" for k, s in unpaired))
    if variants:
        print("  variants not paired: " + ", ".join(variants))

    if disagreed:
        print(f"FAILED {len(disagreed)} twin(s) disagreed across runtimes")
        return 1
    print("PASSED every paired twin agreed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
