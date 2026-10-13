---
title: "Tasks: Prompt Improver example pack, playbook extension and scenario upgrade"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "task breakdown"
  - "pi example pack tasks"
  - "verification checklist"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Prompt Improver example pack, playbook extension and scenario upgrade

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Scaffold the packet and write the goal with the operator's decisions (`goal.md`) [EVIDENCE: D1 to D6 recorded; the packet name follows the redirect to quality]
- [x] T002 Snapshot the 18 exports and the 15 playbook files (`scratch/before/`, `scratch/before-playbook/`) [EVIDENCE: 18 and 15 files copied before any edit]
- [x] T003 Write the shared brief with the new inputs and the canonical wordings (`scratch/shared-brief.md`) [EVIDENCE: eight pairs with exact Turn 1 and Turn 2 inputs, five rule wordings]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 [P] Tighten the 14 existing scenarios with their inputs frozen (`manual-testing-playbook/*/`) [EVIDENCE: 14 files at 1.1.0.0; 14 of 14 turns identical to HEAD]
- [x] T005 [P] Write the 16 new scenarios and update the root (`manual-testing-playbook/`) [EVIDENCE: root 1.1.0.0, 30 scenarios; 16 of 16 turns identical to the brief]
- [x] T006 [P] Improve the 18 exports in three groups by scenario pair (`export/benchmark/skill/`, `export/benchmark/claude project/`) [EVIDENCE: STX-001 meta description and SFM-001 002 risks_and_blockers removed; every header, attestation and file name kept]
- [x] T007 [P] Write the eight examples through the skill (`export/benchmark/examples/`) [EVIDENCE: 4 text-mode and 4 format and creative examples, each with its header]
- [x] T008 Add the collector edit guard and its selftest (`run/collect_exports.py`, `run/selftest.py`) [EVIDENCE: 7 of 7 PASS; committed as Prompt Improver ba5f796 and Barter 4cd5d2ba]
- [x] T009 Write the examples index and the README pointer (`export/benchmark/examples/README.md`, `README.md`) [EVIDENCE: validate_document.py VALID, 0 issues]
- [x] T010 Record the edit, the pack, the playbook and the next steps in the run README (`benchmark/reports/2026-09-25--.../README.md`) [EVIDENCE: sections 9 to 12, eight rule gaps with lines]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T011 [P] Independent review of the 18 exports before and after [EVIDENCE: 18 of 18 at or above the original and past the gate; PIR-001, SIR-002 and PIR-002 repaired]
- [x] T012 [P] Independent review of the new scenarios, the root and the examples [EVIDENCE: 11 findings fixed, 4 notes; SFM-003, SCR-002 and STX-005 turned from FAIL to PASS]
- [x] T013 Add the scope test to the 22 delivering scenarios that lacked it, and scope expansion to six Fail conditions [EVIDENCE: 28 of 30 files state it; the two refusal scenarios deliver no prompt]
- [x] T014 Run the full verification on the final state [EVIDENCE: validator PASS 30, runner 30 in one wave each, formats parse, lint 9 clean, dry run 18 warnings]
- [x] T015 Commit in both repos, then parity on the commit [EVIDENCE: Prompt Improver 9257494 and Barter 3ae67ce0, 60 files each; run_parity.sh PASSED 13/13, exit 0]
- [x] T016 Push on the operator's go-ahead [EVIDENCE: Prompt Improver d473b93..9257494; Barter 8923ad82..3ae67ce0, the route gate overridden once on the operator's approval, since a peer session's uncommitted cli-cursor edits left the shared cli-external-orchestration manifest stale and these commits carry no routing file]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:phase-4 -->
## Phase 4: Framework coverage

- [x] T017 Drop the eight agent-written examples and record why (`export/benchmark/examples/`, `decision-record.md`) [EVIDENCE: 9 files deleted, git keeps them at 9257494; ADR-001]
- [x] T018 Fix the 24 inputs, frameworks, tiers and formats in one brief (`scratch/framework-brief.md`, `scratch/framework-brief.json`) [EVIDENCE: 24 pairs; every input names its framework]
- [x] T019 Write the 48 scenarios and move the root to 1.2.0.0 (`manual-testing-playbook/skill-framework-coverage/`, `manual-testing-playbook/project-framework-coverage/`) [EVIDENCE: validator PASS scenarios=78 categories=14 violations=0; 48 IDs in wave 6 with 1 turn each; 0 mismatches against the brief]
- [x] T020 Pilot four IDs, then run the other 44 on `claude-sonnet-5` at effort `xhigh` (`benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/`) [EVIDENCE: 48 of 48 ok; `check_run.py` read 48 event streams, 0 findings, exit 0]
- [x] T021 Collect into `export/benchmark/`, fixing two extraction misses in the run's collector (`run/collect_exports.py`) [EVIDENCE: 24 SFW and 24 PFW files; the header-above-fence step changes only PFW-007 and the bracketed number only PFW-001; the 2026-09-25 run collects byte-identically under the committed collector and this one]
- [x] T022 Check every header and rerun each tier miss once (`run/check_framework_headers.py`, `first-attempt/`) [EVIDENCE: 48 of 48 name their target framework; 16 in tier on the first attempt, 5 more after the rerun, 27 recorded misses]
- [x] T023 Independent structure review of all 48 (`scratch/review-framework-structure.md`, copied to the run folder as `structure-review.md`) [EVIDENCE: two batches by two reviewers; 39 PASS, 9 FAIL; 20 fact changes; three fact findings spot-checked and confirmed; payloads parse]
- [x] T024 Write the run README with one row per ID (`benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/README.md`) [EVIDENCE: 48 table rows built from the checker output and the review; `validate_document.py` VALID, 0 issues; 0 em or en dashes]
- [x] T025 Point the Local Output paragraph and the older run README at the new run (`README.md`, `benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/README.md`) [EVIDENCE: Local Output names both runs; sections 10 and 11 of the older README point to the new run and the 78 scenarios]
- [x] T026 Final-state verification, `validate.sh --strict`, commits in both repos and the parity gate [EVIDENCE: RESULT: PASSED, 0 warnings; Prompt Improver 02dbfe3 and Barter 5f711610, the same 390 paths; parity PASSED 13/13, exit 0; 078's 14 modified files left unstaged]
- [x] T027 Push on the operator's go-ahead [EVIDENCE: go-ahead 2026-09-27; Prompt Improver 9257494..02dbfe3; Barter 3ae67ce0..5f711610, routing gate fresh with no override]
<!-- /ANCHOR:phase-4 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every export, scenario and example reviewed by an agent that did not write it
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Operator decisions recorded before any edit [EVIDENCE: new packet, quality over conciseness, no rule changes, improve 18 plus new examples, extend the playbook and tighten the existing scenarios; plan approved 2026-09-26]
- [x] CHK-002 [P0] Exports and playbook snapshotted before any edit [EVIDENCE: scratch/before/ 18 files, scratch/before-playbook/ 15 files]
- [x] CHK-003 [P1] Inputs and wordings fixed in one brief before parallel writing [EVIDENCE: scratch/shared-brief.md]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] No change to `SKILL.md`, `AGENTS.md`, the references, the assets, the kernel or the knowledge files [EVIDENCE: git status in the Prompt Improver repo lists no path under those files]
- [x] CHK-011 [P0] Every scenario Prompt, table Exact Prompt and root Prompt match [EVIDENCE: validator PASS with 0 violations]
- [x] CHK-012 [P1] The collector guard keeps edited exports and `--force` restores them [EVIDENCE: selftest 7 of 7 with a negative control against d473b93]
- [x] CHK-013 [P1] The runner parses the new root without a code change [EVIDENCE: load_playbook and load_waves list 30 IDs, each in one wave]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Each of the 18 exports at or above its original and past its gate, with facts and limits kept and no added scope [EVIDENCE: review table, 18 of 18]
- [x] CHK-021 [P0] The 14 existing inputs unchanged [EVIDENCE: 14 of 14 turns identical to a HEAD archive]
- [x] CHK-022 [P1] Each example passes its own scenario's Turn 1 lines [EVIDENCE: 8 of 8 after the review repairs]
- [x] CHK-023 [P1] JSON and YAML payloads parse and no dash appears [EVIDENCE: 4 JSON and 2 YAML parse; 0 files with U+2014 or U+2013]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The missing scope test is classed `class-of-bug` and fixed in every delivering scenario, not only the four the reviewer named [EVIDENCE: 22 files gained it, 28 of 30 carry it]
- [x] CHK-FIX-002 [P0] Twins changed together [EVIDENCE: each export and scenario repair landed on both sides of its pair, or the pair already differed in the original]
- [x] CHK-FIX-003 [P1] Consumers of the exports checked: run README, collector, grading citations [EVIDENCE: README section 9 says the verdicts cite the graded originals at 59a50ac and ab96eebb; the collector keeps the edits]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commits that land this packet [EVIDENCE: guard ba5f796 and 4cd5d2ba, pack 9257494 and 3ae67ce0]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secret, credential or private data in any example or scenario [EVIDENCE: every input is a made-up business case; the only personal name is the fictional hire in STX-003]
- [x] CHK-031 [P1] The public repo commit carries no attribution line [EVIDENCE: ba5f796 message has none]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P0] The run README says the exports were edited after grading and that the verdicts cite the originals [EVIDENCE: README section 9, first paragraph]
- [x] CHK-041 [P0] The examples are marked ungraded wherever they are listed [EVIDENCE: examples/README.md section 1, run README section 10, README.md Local Output. Superseded by ADR-001: the examples are deleted, and section 10 and Local Output now say so]
- [x] CHK-042 [P1] Spec, plan and tasks synchronized [EVIDENCE: all three describe 30 scenarios, the eight pairs and the guard]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Snapshots and the brief kept in scratch/ only [EVIDENCE: scratch/before/, scratch/before-playbook/, scratch/shared-brief.md]
- [x] CHK-051 [P1] scratch/ holds nothing temporary [EVIDENCE: every file there is evidence the reviews compared against]
- [x] CHK-052 [P0] `export/benchmark/` holds only `skill/` and `claude project/` [EVIDENCE: `ls -A` lists the two; no other directory under it]
- [x] CHK-053 [P0] The 48 deliverables are verbatim run output [EVIDENCE: collector dry run over the run prints 48 lines and 0 keep warnings, exit 0]
- [x] CHK-054 [P1] The header check can be rerun from the repository [EVIDENCE: `run/check_framework_headers.py` with `run/framework-targets.json` gives the same 48 verdicts as the scratch checker]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 13 | 13/13 |
| P1 Items | 12 | 12/12 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-09-26
<!-- /ANCHOR:summary -->

---
