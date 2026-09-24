# Prompt Improver: Phase 3 playbook run

Manual testing playbook, both packagings, run against the real runtime through the shared parity harness.

- System: `AI Systems/Prompt Improver/`
- Playbook: `sk-prompt-improver/manual-testing-playbook/`
- Runtime: `AI Systems/z — Parity Gate/run_packaging.sh`
- Model: claude-sonnet-5, effort medium (harness defaults, not overridden)
- Date run: 2026-09-17

---

## 1. COUNTS

Counted by walking `sk-prompt-improver/manual-testing-playbook/` (fourteen scenario files under twelve category folders), not from a typed list.

| Packaging | Scenarios | PASS | FAIL | PARTIAL | SKIP |
|---|---:|---:|---:|---:|---:|
| Skill | 7 | 6 | 1 | 0 | 0 |
| Project | 7 | 5 | 2 | 0 | 0 |
| **Total** | **14** | **11** | **3** | **0** | **0** |

Every scenario ran to a settled verdict on both sides. No row claims a verdict on an unfinished run.

### Multi-turn count

Each scenario file's own conversation chain says whether Turn 2 is unconditional or only fires when Turn 1 asks a question. Walking those fourteen files gives:

- Unconditional two-turn contract: `SIR-001`/`PIR-001`, `SIR-002`/`PIR-002`, `SSB-001`/`PSB-001` (6 scenarios)
- Turn 2 only if Turn 1 asks a question: `SID-001`/`PID-001`, `STX-001`/`PTX-001`, `SFM-001`/`PFM-001`, `SCR-001`/`PCR-001` (8 scenarios)

Running all fourteen, Turn 1 actually asked a question on the six unconditional scenarios (as it must to be graded at all) plus exactly one of the eight conditional ones, `STX-001`. Its Project twin `PTX-001` delivered directly on Turn 1 instead. So **7 of the 14 runs in this pass were genuinely multi-turn**, and the other 7 resolved inside Turn 1. This number was derived by running the playbook and observing which replies actually asked a question, not carried over from the brief. (The brief's original "7 multi-turn" figure was independently flagged by the coordinator as coming from the root index rather than the per-scenario files. This run's number of 7 matches it by coincidence of outcome, not by trusting that source.)

---

## 2. RESULTS

Full table in [`results.csv`](results.csv). Pure per-turn reply captures are in [`replies/`](replies/). A richer per-scenario writeup (harness commands, export/Artifact readbacks, and the reasoning behind each verdict) is in [`evidence/`](evidence/), one file per scenario id, covering both its turns where more than one ran.

| Pair | Skill id | Skill result | Project id | Project result | Agree? |
|---|---|---|---|---|---|
| Identity | SID-001 | PASS | PID-001 | PASS | yes |
| Conflicting commands | SIR-001 | PASS | PIR-001 | PASS | yes |
| No-signal question | SIR-002 | PASS | PIR-002 | PASS | yes |
| Natural-language improve | STX-001 | PASS | PTX-001 | **FAIL** | **no** |
| $json format lock | SFM-001 | FAIL | PFM-001 | FAIL | yes (different defects) |
| $image VISUAL gate | SCR-001 | PASS | PCR-001 | PASS | yes |
| Safety boundary | SSB-001 | PASS | PSB-001 | PASS | yes |

---

## 3. EVERY FAILURE

### PTX-001: Natural-language improve with CLEAR and Canvas (project)

**What the criteria required.** Turn 1 either delivers through a Canvas Artifact or asks at most one consolidated question, and if it delivers, the block renders before any commentary. The scenario's own fail line: "FAIL if commentary precedes the block, the full prompt is pasted again, the score is absent, a save is claimed, or requirements were invented." Its stated purpose is specifically to validate this delivery shape, so the playbook root's advisory carve-out for ordering ("only when the scenario exists to test delivery shape") does not apply here. It does apply.

**What the reply did.** Turn 1 delivered directly (a reasonable path, no question needed). But it opened with a full "Phase D-E-P-T-H Summary" section, naming the detected intent, framework, applied perspectives, and flagged assumptions, all before the `Mode:`/prompt/`Attestation` block. Custom Instructions.md ALWAYS #18 requires exactly that transparency reporting to sit in chat *after* the block. Running `deliverable_lint.py` on the isolated reply also caught a second, independent defect: the header line itself reads `Mode: $text | Complexity: 3 | Framework: COSTAR` with no `Score:` field, though a score appears later in chat. Every other project reply in this run that renders a header keeps Score on that line. Everything downstream of both defects is otherwise correct: CLEAR passed at 42/50, attestation carries both required fields, no save claimed, subject retained faithfully.

**Verdict.** FAIL, single turn, conclusive on Turn 1 alone since Turn 1 delivered rather than asking a question.

### SFM-001: Independent $json format lock (skill)

**What the criteria required.** SKILL.md rule 25: "ALWAYS report significant token overhead for JSON or YAML." The scenario's own fail line names this exact condition: "FAIL if... the overhead is missing."

**What the reply did.** Delivered directly, bound Improve, locked JSON correctly, saved `export/001 - enhanced-meeting-action-items-prompt.json` with the header `Mode: $json | Complexity: Low | Framework: RCAF` (the scenario's own expected-signals line names this literal header text, since the format command is what the header surfaces on this axis), and a payload independently confirmed valid with `python3 -c "import json; json.load(...)"`. CLEAR passed at 44/50 and is reported. But the chat reply never states a token-overhead percentage or the word overhead anywhere.

**Verdict.** FAIL, single turn, conclusive on Turn 1 alone since Turn 1 delivered rather than asking a question. Everything about this run is correct except the one missing, explicitly required line.

### PFM-001: Independent $json format lock in the Project (project)

**What the criteria required.** Custom Instructions.md ALWAYS #17: the Deliverable Block is "a single-line header plus enhanced prompt content and attestation footer only," and the DELIVERY PROTOCOL template states the header and attestation lines "sit outside the JSON/YAML format lock." PFM-001's own expected signals name the header line explicitly.

**What the reply did.** Delivered directly with a valid JSON payload (independently confirmed with `python3 -c "import json; json.load(...)"`), a complete attestation line, and correctly reported overhead (+7%, inside the stated band). But no line beginning `Mode:` appears anywhere in the reply. The JSON format lock appears to have consumed the entire block, including the position the header belongs in.

**Verdict.** FAIL, single turn, conclusive on Turn 1 alone since Turn 1 delivered rather than asking a question.

**Twin note on the SFM-001/PFM-001 pair.** Both fail, so `twin_divergence.py` correctly does not report this pair as a disagreement, but the two failures are opposite defects. The skill keeps its header and drops the overhead line. The Project keeps the overhead line and drops its header. Recorded as two distinct defects, not one shared one.

---

## 4. THE ONE TWIN DISAGREEMENT

`STX-001` (skill) PASSES. Turn 1 asked one consolidated question (depth, target tool, audience, format, bundled into a single turn) and wrote no file. Turn 2 delivered on the answered facts, passed CLEAR at 44/50, saved a real file, and replied path first.

`PTX-001` (project), same prompts, FAILS on Turn 1 for the ordering defect above. It never needed a Turn 2, because Turn 1 delivered directly rather than asking.

This is not one packaging judged by the other's delivery contract. The skill is graded on export-first file delivery and a path-first chat reply, exactly its own contract. The Project is graded on Artifact-before-commentary and a complete header, exactly its own contract, stated in its own Custom Instructions.md. Both runtimes chose to deliver on Turn 1 rather than ask, which is a valid choice under both contracts. The divergence is that only the Project's chosen delivery broke its own ordering rule. `twin_divergence.py` names this pair `TX-001: skill PASS, Project FAIL`.

---

## 5. WHAT COULD NOT BE RUN, AND WHY

Nothing in the fourteen-scenario inventory was skipped. All fourteen ran to a settled verdict on both packagings.

One thing could not be verified as designed: `PID-001`'s and the skill twin `SID-001`'s expected identity phrase, `underpowered requests into clear`, never appears verbatim in either reply. Both paraphrase it. Both scenario contracts explicitly treat a paraphrase as supporting evidence rather than a deciding failure, so this is recorded, not treated as a gap.

---

## 6. THE DELIVERABLE WRAPPER, READ BEFORE CAPTURING REPLIES

Per the brief, this system's own convention (defined in an earlier phase, absent a live harness) wraps the rendered Deliverable Block in `<DELIVERABLE>...</DELIVERABLE>` at capture time, because `deliverable_lint.py`'s `deliverable_not_first` and `scoring_inside_block` checks only run at high confidence once they can see where the block ends.

**Where it applies.** Only the Project packaging renders a Deliverable Block inline in its reply. `deliverable_lint.py` was built entirely from `claude project/Custom Instructions.md`'s own stated contract (single-line header, attestation footer, block before commentary), which is a Project-only surface. The skill's deliverable is a real file it writes to `export/`. Its chat reply is deliberately a short path-first summary with no header or attestation line, by AGENTS.md and SKILL.md's own design. So the wrapper was applied to all six Project replies that render a block (`PID-001`, `PIR-001` turn 2, `PIR-002` turn 2, `PTX-001`, `PFM-001`, `PCR-001`) and correctly withheld from `PSB-001`'s two turns and `PIR-001`/`PIR-002`'s Turn 1, none of which ever render a block. It does not apply to the skill side at all, and saying so plainly is the point of this section: the two gated checks cannot be run meaningfully against a skill reply, because there is no in-chat block for them to bound. Reporting those two checks as clean on a skill file would misstate a capture-format non-event as a passed test.

**A capture-format defect this run found and fixed.** The first pass wrapped each scenario in one combined file (title, harness metadata, the echoed Turn 1 prompt, then the reply). `deliverable_not_first` fired on every single Project file, including ones manually confirmed to render the block genuinely first in the raw model output, because the tool scans the whole file and the document's own title and metadata sat before the tag. That made the check meaningless as computed. It was corrected by moving to one file per captured reply (one per turn, nothing else in the file), matching the grader README's own stated usage exactly (`replies/` holds one `.txt` or `.md` file per captured reply). The rich per-scenario annotation was moved to `evidence/`, a sibling of `replies/` that `lint_replies.py` never scans (it does a flat, non-recursive read of `replies/` only). Re-run after the fix, `PIR-001` Turn 2 came back fully clean, proving the check now measures the reply rather than the document format wrapped around it.

---

## 7. WHAT THE GRADER FOUND

Run from the system root:

```
bash benchmark/grader/check_report.sh "benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium"
```

```
  lint_replies     findings, its own output follows
        PCR-001.md        DIRTY  header_missingx1, deliverable_not_firstx1
        PFM-001.md        DIRTY  header_missingx1
        PID-001.md        DIRTY  header_missingx1, deliverable_not_firstx1
        PIR-001-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        PIR-001-turn2.md  clean  none
        PIR-002-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        PIR-002-turn2.md  DIRTY  deliverable_not_firstx1
        PSB-001-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        PSB-001-turn2.md  DIRTY  attestation_missingx1, header_missingx1
        PTX-001.md        DIRTY  header_malformedx1, deliverable_not_firstx1
        SCR-001.md        DIRTY  attestation_missingx1, header_missingx1
        SFM-001.md        DIRTY  attestation_missingx1, header_missingx1
        SID-001.md        DIRTY  attestation_missingx1, header_missingx1
        SIR-001-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        SIR-001-turn2.md  DIRTY  attestation_missingx1, header_missingx1
        SIR-002-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        SIR-002-turn2.md  DIRTY  attestation_missingx1, header_missingx1
        SSB-001-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        SSB-001-turn2.md  DIRTY  attestation_missingx1, header_missingx1
        STX-001-turn1.md  DIRTY  attestation_missingx1, header_missingx1
        STX-001-turn2.md  DIRTY  attestation_missingx1, header_missingx1
        1 clean of 21, written to deliverable-lint.csv
      FAILED 20 reply/replies carry a Deliverable Block hard violation
  twin_divergence  findings, its own output follows
        TX-001: skill PASS, Project FAIL
        6 twin(s) agreed, 1 disagreed, 0 not settled, 0 run on one runtime only
      FAILED 1 twin(s) disagreed across runtimes

2 of 2 report checks reported findings
```

Full linter output is in [`deliverable-lint.csv`](deliverable-lint.csv).

### twin_divergence.py

Reads cleanly off `results.csv`: 6 pairs agree, 1 disagrees (`TX-001`, covered above), 0 pairs left unsettled, 0 unpaired. This matches the manual finding exactly and needed no reinterpretation.

### lint_replies.py

20 of 21 files came back DIRTY, 1 clean, for 38 individual findings across them (a file can and often does carry more than one). Read as "20 of 21 broken," that overstates it badly. Sorted by what each finding actually is:

**Expected, not a defect (30 of 38 findings, 15 files).** All 11 skill-side files (`SID-001`, `SIR-001` both turns, `SIR-002` both turns, `STX-001` both turns, `SFM-001`, `SCR-001`, `SSB-001` both turns) and the 4 Project turns that legitimately render no block (`PIR-001` Turn 1, `PIR-002` Turn 1, `PSB-001` both turns) show `attestation_missing` and `header_missing`, two findings each. This is exactly what section 6 predicts: skill chat replies never carry a `Mode:`/`Attestation:` line by design, and a question or refusal turn correctly renders no block at all. Confidence on all 15 is `low`, the tool's own signal that it found nothing resembling its target shape, which is accurate here rather than a miss.

**Tool artifact, not a defect (2 of 38 findings, inside `PCR-001` and `PID-001`).** Both show `header_missing` even though a complete header is present, because the model bolds the label (`**Mode:**`) and the linter's `MODE_LINE` regex anchors on a line starting with plain `Mode:`. A bolded label is invisible to it. Confirmed by hand against the raw text in each case.

**Real, and already reflected in the verdicts above (3 of 38 findings, inside `PFM-001` and `PTX-001`).** `PFM-001`'s `header_missing` (no `Mode:` line at all, not a bolding artifact) and `PTX-001`'s `header_malformed` (Score field missing from the header line) and `deliverable_not_first` (the Phase summary genuinely precedes the block) are all genuine, and all are already the basis for those two scenarios' FAIL verdicts in section 3. The `PTX-001` header-malformed finding was caught only by running the tool. The manual first pass had already found the ordering defect and stopped looking for a second one on the same reply, so this is a real case of the automated check adding signal the manual read missed.

**Real prefix text, but not a failure condition under that scenario's own criteria (3 of 38 findings, inside `PID-001`, `PCR-001`, and `PIR-002` Turn 2).** All three show `deliverable_not_first` for content that genuinely precedes the tag: `PID-001`'s identity answer (required by its own conversation chain, which says "answer with the identity phrasing, THEN deliver"), `PCR-001`'s bare "## Deliverable" heading (a label, not prose), and `PIR-002` Turn 2's one-sentence disclosure that this sandbox has no live Canvas panel. None of the three scenario contracts name preceding text as a failure condition, and the playbook root's ordering carve-out is advisory except where a scenario exists specifically to test delivery shape, which none of these three do (`PTX-001` does, hence its finding is treated as real above).

Net: of 38 findings, 30 are the skill/Project scope mismatch section 6 already names, 2 are a bold-formatting blind spot in the regex, 3 are real prefix text that the relevant scenario's own contract does not fail on, and 3 correspond to real defects already counted in the 3 FAIL verdicts above. No finding changes any verdict beyond what sections 1 to 4 already record.

---

## 8. HARNESS NOTES

Two separate incidents, neither a Prompt Improver defect, both recorded because Rule 5 asks for what each run produced, not only its verdict.

**Mid-run script contention.** The `SCR-001` Turn 1 attempt hit `run_packaging.sh: line 150: syntax error near unexpected token 'then'`. The shared script grew from 151 to 167 lines between the prior pair and this one (another lane adding a `--seed` feature while this run was in flight). `bash -n` on the script confirmed valid syntax moments later, and the half-registered session id from the aborted attempt came back "already in use" on a same-id retry, so a fresh session id was generated and Turn 1 ran again cleanly. Full detail in `evidence/SCR-001.md`.

**The scratch-rebuild-on-resume defect the coordinator flagged mid-task.** `run_packaging.sh` used to rebuild its scratch tree on every invocation including `--resume`, so anything Turn 1 wrote to disk was gone before Turn 2 ran. This was checked directly against all seven multi-turn scenarios in this run: in every one, Turn 1 is a question or a reframe that by contract writes no file and renders no block (that is the entire reason Turn 2 exists), confirmed empty on the skill side by reading `export/` immediately after each Turn 1 before the next invocation could rebuild it. Since nothing existed after Turn 1 in any of the seven cases, there was nothing for the rebuild to destroy before Turn 2, and no verdict in this report depends on a file surviving across that boundary. No re-runs were needed. This was verified before writing section 1's counts, not assumed.

---

## 9. HOUSE RULES CHECK

- Every scenario has both sides: 7 skill and 7 project ids, all present in `results.csv` and paired by `twin_divergence.py` with 0 unpaired
- No row claims a verdict on an unfinished run: all 14 resolved to PASS or FAIL, 0 PARTIAL, 0 SKIP
- No packaging graded by the other's delivery contract: the skill is graded on file existence and path-first chat, the Project on Artifact-first block and attestation, throughout sections 1 to 4
- Every scenario's premise line was read before running it, and the conditional-versus-unconditional Turn 2 language per scenario drove whether Turn 2 ran, not a blanket assumption

---

## 10. NEXT STEPS

- Hand the three FAIL verdicts (`PTX-001`, `SFM-001`, `PFM-001`) and the one twin disagreement (`TX-001`) to the adjudication phase, nothing here was repaired
- If the fleet decides to name the retrieval tool explicitly rather than describe where files live (the open question from `002-runtime-harness/retrieval-measurement.md`), re-run `PID-001` first, since it is this system's precondition scenario for every other Project-side id
- Worth a fleet-level look, not a Prompt Improver fix: the `MODE_LINE` regex in `deliverable_lint.py` misses a bolded header line (`**Mode:**`) on 3 of 6 block-bearing Project replies in this run alone, and if other systems' Projects also bold their header line the same blind spot will recur there
