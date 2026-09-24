# Independent verdict, Prompt Improver, 2026-09-17 run

Written by a reviewer who built none of these instruments and ran none of this
playbook. Every figure below was reproduced from the files on disk or from a
command run during this review, not copied from another document's prose.
Paths are relative to `AI Systems/Prompt Improver/` unless stated otherwise.

**A process note before the verdicts.** `benchmark/grader/check_report.sh` was
run once against the live report directory to reproduce section 7's grader
output. That script's `lint_replies.py` step writes `deliverable-lint.csv` as
a side effect, and since `deliverable_lint.py` was repaired the morning after
this report was committed, the regenerated file differed from the committed
one on one line (`PTX-001.md`, described under claim 5 below). This was
caught by `git status` immediately after and reverted with `git checkout --
deliverable-lint.csv` before anything else was read from it. `git status`
confirms the file matches HEAD. Every other command run against this system
in this review was read-only (`deliverable_lint.py` invoked directly,
`twin_divergence.py`, `validate_parity.py`, `residency_check.py`, `rule_parity.py`,
and one gate injection test performed on a backed-up-and-restored file,
confirmed clean by `git status --short` afterward). No file under
`Prompt Improver`, `z — Parity Gate` or `z — Knowledge` differs from HEAD as
this record is written, except one untracked directory,
`z — Parity Gate/episodes/state/`, which holds cache entries for systems this
review never touched (Copywriter, Blog Posts, HubSpot, Deal Templates) and is
almost certainly a concurrent peer session's artifact per this tree's own
"never reset --hard, peer sessions hold uncommitted work here" convention. It
was left alone rather than guessed at.

---

## 1. Verdict on each claim

### Claim 1: checks proved by injection. UPHELD

`benchmark/gates/README.md` and `benchmark/grader/README.md` each claim their
checks were proven by injecting a defect and watching the check turn red,
then reverting and watching it turn green. Both claims were reproduced
independently in this review, not read and trusted.

- **Gate.** Backed up
  `claude project/knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md`,
  reworded its one instance of `always ask the user to share their result`,
  and ran `python3 benchmark/gates/rule_parity.py`. It reported
  `FAILED 1 rule parity finding(s)` naming the exact phrase, the exact count
  on each side (`1x` in the skill source, `0x` in its mirror) and the exact
  file. Restoring the file from the backup and re-running returned
  `PASSED 6 rules hold on both sides of every pair that teaches them`, and
  `git status --short` on the file came back empty, confirming the tree was
  left exactly as found.
- **Grader.** Built a fixture reply combining all five defects
  `deliverable_lint.py` claims to catch (a false save claim, prose before the
  `<DELIVERABLE>` tag, `CLEAR score`/`Perspectives:`/`Assumptions:` inside the
  block, an attestation line missing `save = did not occur`, and a trailing
  emoji bullet) and ran `python3 benchmark/grader/deliverable_lint.py` on it.
  All five violation types fired in one pass, each with its own quoted
  sample. Placed that file alongside a clean fixture in a scratch
  `replies/` directory and ran `lint_replies.py`: `1 clean of 2`, exit 1.
  Removing the dirty file and re-running gave `1 clean of 1`, exit 0. A
  fixture `results.csv` naming `SIR-001,PASS` / `PIR-001,FAIL` alongside a
  `PARTIAL` pair, an unpaired row and a `-retry` variant turned
  `twin_divergence.py` red on the one true disagreement while reporting, but
  not failing on, the not-settled and unpaired rows and listing the variant
  separately. Fixing the disagreement turned it green while the other three
  rows stayed reported. `check_report.sh` against the combined dirty
  directory reported `2 of 2 report checks reported findings` and exited 2,
  the count of checks with findings, matching its documented exit contract
  exactly.

### Claim 2: full coverage, no verdict on an unfinished run. UPHELD

Counted by walking, not by reading the README's own count:

- `find sk-prompt-improver/manual-testing-playbook -mindepth 1 -maxdepth 1 -type d` returns 12 category folders
- `find ... -name "*.md"` under those folders, excluding the root playbook file, returns 14 scenario files
- `tail -n +2 results.csv | wc -l` returns 14 rows, `grep -c ",PASS," results.csv` returns 11, `grep -c ",FAIL," results.csv` returns 3, matching the 6/1 skill and 5/2 project split exactly
- No row's `result` column reads `PARTIAL` or `SKIP`, and a grep for those words across `evidence/*.md` turns up only unrelated prose ("partial support," "partial answers"), never a verdict label
- `replies/` holds 21 files, one per captured turn, confirmed by `ls | wc -l`, matching `1 clean of 21` in the grader's own count
- `evidence/` holds 14 files, one per scenario id, confirmed by `ls | wc -l`

The lint file is `deliverable-lint.csv`, and a repo-wide search
(`find . -iname "hvr-lint.csv"` and `find . -iname "deliverable-lint.csv"`
from the `AI Systems` directory) confirms every other system's benchmark
report in this tree (Product Owner, Media Editor, Copywriter, Blog Posts,
HubSpot & Automation, Deal Templates) carries `hvr-lint.csv` while Prompt
Improver alone carries `deliverable-lint.csv`. This matches the claim that it
checks deliverable structure rather than voice, and `deliverable_lint.py`'s
own source contains no vocabulary or punctuation list, confirmed by reading
it in full.

The claim that an earlier capture format combined turns into one file and
made `deliverable_not_first` fire on every Project file could not be checked
against a surviving artifact: `git log` on the report directory shows only
two commits, and the first one (`ff2f2d1`) already committed the current
one-file-per-turn format, so the broken combined format was apparently found
and corrected before the first commit and left no trace in history. What was
checked instead, directly: whether the *current* format supports the
verdicts recorded. Re-running `deliverable_lint.py` on every file in
`replies/` today reproduces the finding pattern the report's section 7 shows
line for line (see Claim 5 for the one line that changed), so the current
per-turn format does measure what the report says it measures.

### Claim 3: the one twin divergence is adjudicated and tested from a second direction. UPHELD

`python3 benchmark/grader/twin_divergence.py <report dir>` (read-only, confirmed
by `git status --short` after) returns `6 twin(s) agreed, 1 disagreed, 0 not
settled, 0 run on one runtime only`, naming `TX-001: skill PASS, Project
FAIL`. This is the only pair in the report.

`sampling.md`'s central number was independently rebuilt rather than read.
Its discriminator (deliverable-first for the Project side, path-first for the
skill side, scored on the first delivering turn) was reimplemented from the
document's own written rule in a fresh script and run against the 23 raw
files in `samples/` (12 turn-1 files, 11 turn-2 files, `ls samples | grep
turn1 | wc -l` and `... turn2 ...` confirm the split, and the skill's
`project-03` sample delivered on turn 1 so its conditional turn 2 never ran,
accounting for the missing 12th turn-2 file). The independent script reproduced every
row of `sampling.md` section 3 exactly: skill 6 PASS / 0 FAIL, project 2 PASS
/ 4 FAIL, with the same per-sample prefix lengths (13, 522, 17, 0, 0, 606
characters). The Fisher exact test on that 0-of-6 vs 4-of-6 table was also
recomputed independently (`scipy.stats.fisher_exact([[0,6],[4,2]])`), giving
p = 0.0606, matching the claimed 0.061.

The record does not overclaim. `sampling.md` states plainly that the
divergence is "a draw at the level the committed run measured it" and that
the packaging asymmetry is "short of settled" at p = 0.061, above the
conventional 0.05 line. That is the honest reading of the reproduced numbers,
not a rounding of an inconvenient result into a clean story. The second
direction the claim asks for is present twice over: `adjudication.md` tested
the ordering defect behaviorally (three fresh harness runs, one with write
tools withheld) and structurally (against the other five Project replies in
the same run that carry a block), and `sampling.md` then tested the same
divergence statistically at six samples per side. Both directions were
checked against primary files in this review, not taken on the report's
word.

### Claim 4: repairs landed on both sides, behaviour re-measured, runtime faults recorded unrepaired. UPHELD

**The header-field repair.** `git log --oneline -- benchmark/grader/deliverable_lint.py`
shows exactly two commits. `git show 076133a` was read in full. It removes
`Score:` from `claude project/Custom Instructions.md`'s DELIVERY PROTOCOL
header template, drops `"Score:"` from `deliverable_lint.py`'s
`REQUIRED_HEADER_FIELDS`, and resyncs two `statement_key` hashes in
`z — Parity Gate/systems.py` to match the edited text (both quoted in the
diff, old and new hash). `SKILL.md`'s frontmatter still reads `version: 1.3.0`,
confirming the commit's own claim that the skill side needed no edit.

The specific technical claim behind the repair, that the old check reported
one violation for a correct three-field header and one violation for a
header missing its `Framework` field, so it could not tell them apart, was
tested directly rather than taken from the commit message. A script applying
both the old field tuple `("Complexity:", "Framework:", "Score:")` and the
new tuple `("Complexity:", "Framework:")` to three synthetic header lines
showed: a correct `Mode: ... | Complexity: 3 | Framework: COSTAR` line comes
back `malformed=True` under the old tuple and `malformed=False` under the
new one, while a line missing `Framework:` but carrying `Score:` comes back
`malformed=True` under both. The claim holds exactly: the old check could not
distinguish the two cases (both surfaced as one `header_malformed` finding),
and the new check passes the correct header while still catching the
malformed one.

The claim of twelve statements of the three-field header form across both
format guides was counted, not read off the commit message. `grep -c
'Mode:.*Complexity:.*Framework:'` against
`claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md`
returns 6, and the same pattern against
`sk-prompt-improver/assets/format-guide-markdown.md` returns 6. Neither file
contains a `Mode:` line carrying `Score:`. Twelve, exactly.

**Behaviour re-measured.** `python3 z — Parity Gate/validate_parity.py
prompt-improver` returns `PASSED 13/13 declared pairs, seven checks`.
`python3 z — Parity Gate/residency_check.py prompt-improver` returns `PASSED 1
system(s), every declared statement owned and placed`. Both ran clean against
the post-repair tree, confirming the resynced residency keys actually match
the edited statements rather than merely being present.

**Runtime fault recorded unrepaired.** `z — Parity Gate/episodes/hand-run/011-fleet-capability-leak/runtime-faults-recorded.md`
exists and its "Prompt Improver TX-001, transparency before the block"
section states the rule citations, the sampling result (six per side, Fisher
p = 0.061, "not settled at that size"), and explicitly separates the ordering
fault (not repaired) from the header field (separately repaired, and named as
"not a runtime fault"). This matches what `adjudication.md` and `sampling.md`
independently support, checked above.

### Claim 5: no count in the record disagrees with the tree. UPHELD, with one artifact-staleness finding and one unrelated commit-message figure that does not check out

Every count named in the brief and in the report's own prose was recomputed
in this review by parsing a file or walking a directory, listed together
here:

| Count | Claimed | Reproduced | Method |
|---|---|---|---|
| Scenario files | 14 | 14 | `find` on `manual-testing-playbook/` |
| Category folders | 12 | 12 | `find -maxdepth 1 -type d` |
| Total scenario results | 14 | 14 | `tail -n +2 results.csv \| wc -l` |
| PASS / FAIL | 11 / 3 | 11 / 3 | `grep -c` on `results.csv` |
| `replies/` files | 21 | 21 | `ls \| wc -l` |
| `evidence/` files | 14 | 14 | `ls \| wc -l` |
| `samples/` turn-1 / turn-2 files | 12 / 11 | 12 / 11 | `ls samples \| grep turn1\|turn2 \| wc -l` |
| Twins agreed / disagreed | 6 / 1 | 6 / 1 | `twin_divergence.py` re-run |
| Fisher p (0/6 vs 4/6) | 0.061 | 0.0606 | `scipy.stats.fisher_exact` |
| Three-field header statements, Project guide | 6 | 6 | `grep -c` |
| Three-field header statements, skill guide | 6 | 6 | `grep -c` |
| Total findings in `deliverable-lint.csv` | 38 | 38 | summed `hard_violations` column, parsed with `csv.DictReader` |
| Clean / dirty reply files | 1 / 20 | 1 / 20 | same parse |

One disagreement, found only because the grader was run against the live
report directory and its write side effect was caught before this record was
written. The committed `deliverable-lint.csv` still shows `PTX-001.md` with
two violations, `header_malformedx1, deliverable_not_firstx1`. Running the
*current* `deliverable_lint.py` (post header-field repair) against
`replies/PTX-001.md` returns only `deliverable_not_firstx1`, one violation,
because the repaired `REQUIRED_HEADER_FIELDS` no longer flags a three-field
header as malformed. This is not a defect in the report: the report was
committed the evening before the header-field repair landed, so its CSV is a
correct snapshot of what the tool found at the time, and the total finding
count (38) and dirty-file count (20 of 21) are unaffected either way, since
`PTX-001.md` was and remains dirty on the ordering finding alone. But nothing
in the report, in `SYNC.md`, or in the repair commit flags that re-running
`check_report.sh` against this exact directory today will no longer
reproduce section 7's `PTX-001.md` line byte for byte. That gap is recorded
under section 2 below.

One figure outside the five claims, encountered while checking the header
repair commit, does not check out. The commit message and the matching
`SYNC.md` entry for `076133a` state the kernel's `NNN` placeholder was
changed to `[###]` "against thirteen uses of the other form on the skill
side." Every reasonable scoping of that count was tried and none produced
thirteen: `grep -rc 'export/\[###\]'` across the seven skill-side files that
state the export path template (`README.md`, `SKILL.md`, and five
`manual-testing-playbook/skill-*` scenario files) gives 12. Adding
`AGENTS.md`'s three uses of the identical phrase gives 16. A bare `[###]`
token search across every non-`claude project/` markdown file, excluding the
two files that only describe the change in prose (`SYNC.md`,
`adjudication.md`), gives 19. Thirteen was not reached under any of these
scopings. This is a minor, narrative-only figure (it does not gate anything,
`validate_parity.py` and `residency_check.py` both pass regardless of its
exact value) and it is not one of the five claims this record was asked to
judge, but the brief's own instruction to attack every count in the record
means it belongs here rather than being passed over because it is
convenient.

---

## 2. What nobody recorded

The most significant unrecorded fact from this review is the artifact
staleness under Claim 5: `benchmark/reports/.../deliverable-lint.csv` is a
point-in-time snapshot that a routine re-run of the documented validation
command (`bash benchmark/grader/check_report.sh <this report dir>`, exactly
as `README.md` section 7 tells a reader to run it) will silently overwrite
with post-repair output that disagrees with the committed file on the
`PTX-001.md` line, with nothing on disk or in `SYNC.md` warning a future
reader that the report and the live tool have diverged by one repair's worth
of history. The verdict is unaffected (both old and new lines mark
`PTX-001.md` dirty, and the FAIL verdict on that scenario was already
established to rest on the ordering defect and not the header field), but a
reader who trusts `git diff` after re-running the grader, the way this review
almost did, would see a change and not know from anything in this directory
whether it is a regression or an expected consequence of a since-landed fix
elsewhere in the tree. Worth a one-line note in this report's own section 7
or in `SYNC.md` saying the grader's checked-in CSV output was captured under
kernel v1.4.4 and will not byte-for-byte reproduce under v1.4.5 or later, so
the next person who runs the documented command does not read the diff as a
new finding.
