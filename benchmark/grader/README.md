# grader: checks over a finished benchmark report

Two after-the-fact checks over a run's captured replies and results, and one
command that runs both. Before this phase this system had no grader of any
kind, so there was nothing to point at a run and nothing that read a reply
for compliance with the rules this system actually states.

---

## 1. OVERVIEW

| File | What it holds |
| --- | --- |
| `deliverable_lint.py` | Single-file linter. Reads one reply, checks it against Prompt Improver's own stated output rules, prints JSON |
| `lint_replies.py` | Walks a run's `replies/` directory (or lints one file with `--brief`), writes `deliverable-lint.csv`, exits 0 only when every reply is clean |
| `twin_divergence.py` | Reads a run's `results.csv`, pairs scenarios by this system's `S`/`P` id scheme, reports any pair whose verdicts disagree |
| `check_report.sh` | Runs both of the above over a report directory, continuing past findings, exit code is the count of checks that reported findings |

---

## 2. WHAT THE LINTER CHECKS, AND WHERE EACH RULE IS STATED

`deliverable_lint.py` was built only after reading `claude project/Custom
Instructions.md`, because this system states no banned-vocabulary or
punctuation rule for the prompts it writes the way Deal Templates and
Copywriter do for their deal copy. What it states instead is a structural
contract for the Deliverable Block and an absolute ban on claiming a save or
an export a claude.ai Project cannot perform:

| Check | Rule | Source |
| --- | --- | --- |
| `claimed_execution` | Never claim this Project saved, exported, verified on disk or executed anything | Custom Instructions.md, RULES > NEVER #12, line 347 |
| `attestation_missing` / `attestation_incomplete` | The Deliverable Block's footer states `execution = did not occur` and `save = did not occur` | DELIVERY PROTOCOL template, lines 376-377 |
| `header_missing` / `header_malformed` | The block opens with one line carrying Mode, Complexity, Framework and Score | RULES > ALWAYS #7, line 320, and DELIVERY PROTOCOL, line 372 |
| `deliverable_not_first` | The block renders before any commentary | RULES > ALWAYS #6, line 319, and NEVER #8, line 342 |
| `scoring_inside_block` | No scoring breakdown, processing note or format option inside the block | RULES > NEVER #6, line 340 |
| `emoji_bullets` | No emoji bullets in question or validation text | `references/interactive-mode.md`, NEVER #14, line 536 |

`deliverable_not_first` and `scoring_inside_block` need to know where the
block ends, so they only run when the reply carries an explicit
`<DELIVERABLE>...</DELIVERABLE>` tag (this system's own convention for a
benchmark capture, absent a live harness today). The rest read the whole
reply and run regardless, at whatever confidence the extraction found, so a
plain chat capture with no tags is still checked for a claimed save, an
attestation footer, a header and emoji bullets. `confidence` is reported on
every result rather than folded into the pass/fail so a reader can see why a
structural check did or did not run.

## 3. WHY REPLIES GET LINTED AT ALL

A linter that only exists is not a check. `deliverable_lint.py` reads one
file and prints JSON, and nothing calls it after a benchmark run unless
something is built to do that on purpose. `lint_replies.py` is that
something: it walks every reply a run captured, not just the ones a step
remembered to point the linter at.

Its exit code is the part worth stating plainly, because the fleet has
already gotten this wrong once for a different system's linter: a single-file
tool that always exits 0 has had that 0 read as a pass. `lint_replies.py`
exits 0 only when every reply is clean, 1 when any reply carries a hard
violation, 2 when there was nothing under `replies/` to read, 64 with no
argument. `deliverable_lint.py`'s own exit code was changed to match (0
clean, 1 dirty) too, even though nothing here depends on it (`lint_replies.py`
imports `lint_reply()` directly rather than shelling out), because there is
no reason to leave the same trap sitting in a file that looks like a gate.

A dirty reply is a finding about the runtime that produced it, not about this
repository. This tool never edits a reply, only reports.

## 4. WHY TWINS GET COMPARED

`sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md`
declares fourteen scenarios in two runtime sets, skill and Project, over six
categories, each id shaped `S`/`P` + two-letter category + `-NNN`: `SID-001`/
`PID-001`, `SIR-001`/`PIR-001`, `SIR-002`/`PIR-002`, `STX-001`/`PTX-001`,
`SFM-001`/`PFM-001`, `SCR-001`/`PCR-001`, `SSB-001`/`PSB-001`. Both runtimes
read the same rules, one from a file tree and one from a Project's retrieval
step, and a twin pair is the only instrument here for a behavioral difference
that no rule-parity or inventory check can see, because both packagings can
hold identical rule text and still answer a live request differently.

`twin_divergence.py` pairs rows by category and number, never by a guess, and
treats three shapes as not-agreement rather than silently as agreement:

- A scenario present on only one runtime is **unpaired**, not counted as
  agreeing, because a comparison that drops half its input has not measured
  agreement on that scenario at all
- An id carrying a suffix after the number (`SCR-001-retry`) is a **variant**,
  a re-run or a diagnostic rather than a runtime's answer, and is listed
  rather than paired
- A `PARTIAL` result on either side is **not settled** and never compared,
  since most scenarios here chain two user turns and a run that stopped after
  the first is evidence about that turn alone

Only an actual disagreement between two completed verdicts fails the check.

## 5. WHY THE RUNNER EXISTS

Neither check runs itself. A check that depends on someone remembering to
call it after a playbook pass is the same as no check. `check_report.sh` runs
both over one report directory, continues past a finding so the first does
not hide the second, and exits with the count of checks that reported
findings, not the first one's own code and not the count of checks that
failed to run. `${1:?...}` would exit 1, and 1 already means one check
reported findings here, so the usage path exits 64 and a missing directory
exits 2, both clear of the count.

---

## 6. VALIDATION

Run from the system root (`AI Systems/Prompt Improver/`):

```bash
python3 benchmark/grader/deliverable_lint.py <reply file>
python3 benchmark/grader/lint_replies.py <run report dir>
python3 benchmark/grader/lint_replies.py <one file> --brief
python3 benchmark/grader/twin_divergence.py <run report dir, or a results.csv>
bash benchmark/grader/check_report.sh <run report dir>
```

`results.csv` needs at minimum an `id` column carrying the scenario id and a
`result` column carrying `PASS`, `FAIL` or `PARTIAL`. `replies/` holds one
`.txt` or `.md` file per captured reply.

### How this was proven, not just written

All four proofs ran against fixtures outside this tree (this system has no
finished benchmark report yet to run against), then were removed:

- A reply claiming `"I've saved this to your files already"`, opening before
  its `<DELIVERABLE>` tag, restating `CLEAR score` / `Perspectives:` /
  `Assumptions:` inside the block, dropping `save = did not occur` from its
  attestation line and closing with an emoji bullet turned `deliverable_lint.py`
  red on all five checks at once, each with its own sample text. A clean
  reply alongside it turned `lint_replies.py` red for exactly the one dirty
  file (`1 clean of 2`) and green once that file was removed (`1 clean of 1`)
- A `results.csv` naming `SIR-001,PASS` and `PIR-001,FAIL` turned
  `twin_divergence.py` red, naming `IR-001: skill PASS, Project FAIL`,
  alongside a `PARTIAL` pair and an unpaired row that were reported but did
  not fail the check, and a `-retry` id that was listed as a variant rather
  than paired. Fixing the one disagreement turned it green while the
  not-settled and unpaired rows stayed reported
- A report directory carrying both the dirty reply and the disagreeing pair
  turned `check_report.sh` red on both checks in one run (`2 of 2 report
  checks reported findings`, exit 2), proving neither finding hid the other.
  Removing both turned it green (`all 2 report checks clean`, exit 0)

---

## 7. RELATED

- [`benchmark/gates/`](../gates/README.md), the rule-parity check this pairs with
- [`benchmark/parity/`](../parity/README.md), the shared fleet gate wrappers
- [`sk-prompt-improver/manual-testing-playbook/`](<../../sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md>), the scenario inventory `twin_divergence.py` pairs
