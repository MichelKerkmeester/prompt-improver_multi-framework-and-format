# gates: rule parity between the skill and its Project mirrors

One check: does a rule this system states hold the same number of times on
both sides of every declared skill-to-Project pair.

---

## 1. OVERVIEW

| File | What it holds |
| --- | --- |
| `rule_parity.py` | Reads this system's 13 declared pairs from the shared fleet declaration, counts named rule phrases on both sides of each, and reports any pair where the count disagrees or a rule's teaching-pair count falls below its declared floor |

Current state:

- Before this phase this system had no `benchmark/gates/` directory and no rule-level check of any kind, only the file-inventory and byte-parity gates the shared fleet tooling already runs
- `rule_parity.py` names 6 rules and the verbatim phrases that carry them, read out of `sk-prompt-improver/references/` and `sk-prompt-improver/assets/` and their Project Knowledge mirrors
- It reads pairs from `AI Systems/z — Claude Project Sync Loop/systems.py`, never from a local map, because that file already declares this system's 13 pairs and is the file every fleet gate reads

---

## 2. WHERE THE PAIRS COME FROM

`systems.py` declares, for system id `prompt-improver`, a `pairs` dict mapping
each Project Knowledge filename to the skill-relative source it renders. This
gate reads that dict as source text with `sys.dont_write_bytecode` set, the
same way the shared gate reads its own declaration, and flips each entry to
`(source, mirror)` before comparing. It never writes `systems.py`, and it
never keeps a second copy of the pair list anywhere in this system's own
files, because a second map is a second place the same fact can go stale.

## 3. WHY THIS GATE EXISTS

Nothing else reads what a document says. The file-inventory gate confirms a
mirror exists, the fleet declaration confirms its filename, and neither reads
a sentence. Diffing all 13 pairs while building this gate found that a fleet-
wide house-style pass strips most em dashes and semicolons out of the Project
copy while leaving the skill source as written, with no content lost, which
is exactly the kind of change that looks like drift to a naive comparison. So
every phrase in `RULES` was checked against the live pairs before being kept,
and none depends on that punctuation.

Counting rather than testing presence is deliberate. A rule stated five times
in `interactive-mode.md` and five times in its mirror is not the same
evidence as a rule stated five times on one side and once on the other, and a
presence test cannot tell them apart.

`min_pairs` exists because counting alone cannot see a rule change owners. A
rule deleted from the one pair that taught it and never added anywhere else
leaves that pair's count at 0 against 0, which a straight comparison calls
agreement. The floor is what notices a rule reaching zero pairs when one or
more is declared.

## 4. ADDING A RULE

Add an entry to `RULES` with the verbatim phrase or phrases that carry it and
the number of declared pairs that teach it today, checked against the live
files, not guessed. Prefer a short phrase where presence is the evidence, and
the whole sentence including its full stop where the exact wording is the
rule, since a mirror can extend a short phrase with a qualifier and reverse
the rule while the count holds. Avoid an em dash or a semicolon inside a
phrase unless both sides are confirmed to still carry it identically.

## 5. VALIDATION

Run from the system root (`AI Systems/Prompt Improver/`):

```bash
python3 benchmark/gates/rule_parity.py
```

Expected result: a `pairs:` line, one line per rule naming how many declared
pairs teach it, then `PASSED 6 rules hold on both sides of every pair that
teaches them` and exit 0. A finding prints as `FAILED <n> rule parity
finding(s)` with each one on its own line and exit 1. No declared pairs, or a
declared source outside the skill root, exits 2.

### How this was proven, not just written

Two defect shapes were injected against the live files (backed up outside
this tree first, restored after, `git status` confirmed clean):

- Reworded the one sentence carrying "creative-mode deliverables close with
  an invitation to share the result back" in the Image Mode Library's Project
  mirror only. The gate reported the exact phrase, the exact count on each
  side (1 vs 0) and the exact two files
- Reworded the one sentence carrying "framework fit beats framework
  complexity" identically on both the skill source and its mirror, so the
  per-pair count stayed equal (0 vs 0) and no phrase-mismatch fired. The
  floor check still caught it, reporting the rule as taught by 0 pair(s)
  against 1 declared

Both cases confirmed green again once reverted.

---

## 6. RELATED

- [`SYNC.md`](../../SYNC.md), this system's own change notes
- [`benchmark/grader/`](../grader/README.md), the checks that run over a finished benchmark report
- [`z — Claude Project Sync Loop/README.md`](<../../../z — Claude Project Sync Loop/README.md>), the shared gate whose declaration this reads
