---
title: "Tasks: Prompt Improver complexity rubric and prose-friendly VIBE scenarios"
description: "Rule edits on both sides, playbook edits, a 48-scenario rerun, its checks and records, then the commits and the parity gate."
trigger_phrases:
  - "pi complexity rubric tasks"
  - "complexity rubric rerun tasks"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Prompt Improver complexity rubric and prose-friendly VIBE scenarios

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

- [x] T001 Scaffold the packet and write the spec with the operator's four decisions (`spec.md`) [EVIDENCE: rubric, scored dimensions, prose VIBE scenarios, all 48 rerun with a pack refresh; REQ-001 to REQ-007]
- [x] T002 Measure the baseline under one strict header checker (`run/check_framework_headers.py` on the 2026-09-26 pack) [EVIDENCE: 17 of 48 in tier with a bare `High` failing the Complex tier, 21 under the old lenient rule]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Add the Complexity Rubric to the skill's DEPTH Complexity Assessment (`references/depth-framework.md`) [EVIDENCE: five dimensions 0 to 2, the rating rule and the bands; the Focus bullet points to it]
- [x] T004 Carry the rubric to the Project DEPTH knowledge file (`Prompt Improver - DEPTH Thinking Framework - v0.200.md`) [EVIDENCE: the 19-line block from the heading to the Bands line is byte-identical on both sides]
- [x] T005 Name Complex in every header label scale and point it to the rubric (`SKILL.md`, three format guides, three Project format guides, the kernel) [EVIDENCE: eight files state Low (1 to 4), Medium (5 to 6), High (7 to 8) or Complex (9 to 10)]
- [x] T006 Drop the Simple, Medium and Complex names from the JSON and YAML structure tiers, thresholds kept (`assets/format-guide-json.md`, `assets/format-guide-yaml.md` and their mirrors) [EVIDENCE: found after the first run start; the tiers read 1 to 3, 4 to 6 and 7 to 10 on both sides, line counts unchanged]
- [x] T007 Versions, changelog and records (`SKILL.md` 0.6.0, kernel v0.7.0, `description.json`, both READMEs, `changelog/v0.6.0.0.md`, `SYNC.md`) [EVIDENCE: residency PASSED, exit 0, after the kernel line moved out of a declared statement]
- [x] T008 Remap the playbook citations the inserts shifted (65 playbook files) [EVIDENCE: 222 citations; `SKILL.md` lines 558-561 now 558-562 in 17 places, kernel lines 367-390 now 367-392 in 30 and line 398 now 400 in 33]
- [x] T009 Let the four VIBE and VIBE-MP scenarios pass pillars written as prose, and the root with them (`*-framework-coverage/vibe-*.md`, `manual-testing-playbook.md`) [EVIDENCE: Objective, Body, outcome, Pass/fail, steps, Evidence and table row changed together; root per-ID blocks and the framework-coverage rule follow]
- [x] T010 Name `Complex` in the 18 Complex-tier scenarios and the root tier table, and cite the rubric under the table (`manual-testing-playbook.md`) [EVIDENCE: 18 of 18 replaced once each; 20 scenario files at a minor version bump, root 1.3.0.0]
- [x] T011 Build the run folder from the 2026-09-26 harness with the strict Complex tier (`benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/run/`) [EVIDENCE: the checker's Complex labels are `complex` and `very high`; its docstring says why]
- [x] T020 [P] Blind recount of the 24 inputs with the rubric alone, by an agent that saw no tier, target or deliverable (`scratch/rubric-recount.md`) [EVIDENCE: 24 rows, every rating recomputed from its five scores; 11 of 24 land in their scenario tier, 11 of 18 text and 0 of 6 creative]
- [x] T012 Run all 48 on `claude-sonnet-5` at effort `xhigh` and check the run (`run/check_run.py`) [EVIDENCE: 48 of 48 `ok`, 22.38 USD, 118.6 min of session time; `check_run.py` 48 event streams, 0 findings, exit 0; a first start stopped after 2 sessions for T006]
- [x] T013 Refresh the pack: remove the old SFW and PFW files and collect the new ones (`run/collect_exports.py`) [EVIDENCE: 48 tracked files removed, 48 collected, exit 0; `--dry-run` 48 lines, 0 keep warnings]
- [x] T014 Check every header and compare the tier hits with the 2026-09-26 pack under the same checker [EVIDENCE: 48 of 48 name their framework and match their format; 25 of 48 in tier, against 13 first attempts and 17 after rerun in the old run; 12 rate 9 or 10, against 0]
- [x] T015 Independent structure review of the 48 (`structure-review.md`) [EVIDENCE: two reviewers by twin pair; 45 PASS, 3 FAIL, 29 fact changes; dash totals match a byte scan, 141; four fact findings spot-checked and confirmed; one JSON miscount corrected with a note]
- [x] T016 Write the run README, point the older run README and the system README at it [EVIDENCE: 48 table rows; `validate_document.py` VALID, 0 issues; output gate passed; 0 em or en dashes; four old-run cells recounted and corrected before commit]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T017 Playbook, runner and router checks on the edited playbook [EVIDENCE: validator PASS scenarios=78 categories=14 violations=0, exit 0; `load_waves` 78 IDs with the 48 in wave 6; router fixtures PASSED 25/25]
- [x] T018 Final-state verification, `validate.sh --strict`, commits in both repos and the parity gate on the commit [EVIDENCE: RESULT: PASSED, 0 errors, 0 warnings; Prompt Improver 4da1a1a and Barter ccd0425c, the same 318 paths; `validate_parity.py prompt-improver` PASSED 13/13, exit 0; residency exit 0; router 25/25; validator 78, 0 violations]
- [x] T019 Push on the operator's go-ahead [EVIDENCE: go-ahead 2026-09-27; Prompt Improver 44e5982..4da1a1a; Barter a51666b2..ccd0425c through the barter account, then switched back]
- [x] T021 Re-tier the six creative pairs to the blind recount and add a Low tier (`*-framework-coverage/{frame,motion,vibe}-*`, root) [EVIDENCE: operator decision 2026-09-27; 019, 021 and 022 to Low, 020 and 023 to Medium, 024 to High; 12 files renamed with `git mv`; root 1.4.0.0 with a Low row; no old slug outside the two run records]
- [x] T022 Recheck the playbook and the pack under the new tiers [EVIDENCE: validator PASS scenarios=78 violations=0; runner loads 78 per side with no missing file; a scratch copy of the checker with a Low band reads 30 of 48 in tier, 7 of 12 creative]
- [x] T023 Record the re-tier in the run README and Local Output [EVIDENCE: run README section 7 note; Local Output says the creative frameworks sit at the tier the rubric gives their input; committed as Prompt Improver 13bdf85 and Barter 5b5c51d6, the same 15 paths; parity PASSED 13/13, exit 0]
- [x] T024 Push the re-tier on the operator's go-ahead [EVIDENCE: go-ahead 2026-09-27; Prompt Improver 4da1a1a..13bdf85; Barter ccd0425c..5b5c51d6 through the barter account, then switched back]
- [x] T025 Grade the 48 against their Pass/fail lines at the run's playbook (`results.csv`, `results.md`, `grading-notes.md`) [EVIDENCE: four graders, six twin pairs each, none of whom wrote a scenario or deliverable; 6 PASS, 42 FAIL; the key claims rerun; the failing-item map matches `facts_intact` and the header checker on every ID]
- [x] T026 Run `check_report.sh` on the run folder [EVIDENCE: exit 2; `twin_divergence` 20 agreed, 4 disagreed, the same four the grading adjudicates; `lint_replies` 22 clean of 48, skill replies dirty by design, PFW-012 a false positive]
- [x] T027 Trace the company name through the event streams [EVIDENCE: line 676 of the Interactive Mode knowledge file is the only Barter string in any Project tool result, read by all 24 Project sessions]
- [x] T028 Remove the company name from both packages as skill 0.6.1 (`references/depth-framework.md`, `references/interactive-mode.md`, `Prompt Improver - Interactive Mode - v0.700.md`, versions, `changelog/v0.6.1.0.md`, `SYNC.md`) [EVIDENCE: `grep -i barter` over `AGENTS.md`, `SKILL.md`, references, assets, kernel and knowledge finds nothing; changelog VALID]
- [x] T029 Trial a tighter rubric wording with two blind raters, then restore the rubric on the operator's decision (`rubric-wording-trial.md`) [EVIDENCE: readers within a point on 24 of 24 under both wordings; ratings about half a point lower; recount in tier 17 and 16 of 24 against 13 and 12; both rubric blocks back to the committed text and byte-identical]
- [x] T030 Record the grading, the second recount and the trial in the run folder (`README.md`, `rubric-recount-b.md`) [EVIDENCE: finding 11, next steps 6 and 7, notes on items 2, 4 and 5; the five run documents VALID with 0 issues]
- [x] T031 Commit both repos with the same paths and run the gates on the commit, no push on the operator's decision [EVIDENCE: Prompt Improver 4f55b66 and Barter ff3e5526, the same 17 paths; `validate_parity.py prompt-improver` PASSED 13/13, exit 0, kernel v0.7.0 and Skill v0.6.1 live; residency exit 0; router 25/25; validator 78, 0 violations; operator chose commit only on 2026-09-27]
- [x] T032 Push both commits on the operator's go-ahead [EVIDENCE: "commit push all" on 2026-09-27; Prompt Improver 13bdf85..4f55b66; Barter 5b5c51d6..ff3e5526 through the barter account, then switched back; the uncommitted Product Context files left alone]
- [x] T033 Operator follow-up: set the What's inside lists of the Prompt Improver and Product Owner READMEs as bold subheadings with the description below (`README.md` in both systems) [EVIDENCE: 7 pairs each, a backslash line break after each subheading; sk-doc issue counts unchanged at 13 and 14; 0 dashes added; pushed as Product Owner 13a3754, Prompt Improver bc0c5b2 and Barter a39b814d]
- [x] T034 Operator follow-up: put each What's inside description on a bullet under its subheading, backslash breaks removed (`README.md` in both systems) [EVIDENCE: 7 bullets each; sk-doc issue counts unchanged at 13 and 14; pushed as Product Owner f9cad05, Prompt Improver d6575bb and Barter db0be5b0]
- [x] T035 Operator follow-up: shorten every What's inside bullet so none wraps (`README.md` in both systems) [EVIDENCE: 14 bullets, 40 to 68 characters; sk-doc issue counts unchanged at 13 and 14; pushed as Product Owner df791f6, Prompt Improver 118ce57 and Barter 2dded08a]
- [x] T036 Operator follow-up: restore the original What's inside list in both READMEs, undoing T033 to T035 (`README.md` in both systems) [EVIDENCE: each README identical to its state before T033, Product Owner 1cdacec and Prompt Improver 4f55b66; pushed as Product Owner f6ef45e, Prompt Improver 2e720be and Barter f89a463e]
- [x] T037 Operator follow-up: remove the Why it earns a place list from the Prompt Improver README (`README.md`) [EVIDENCE: heading and 3 bullets removed, 6 lines; pushed as Prompt Improver 49d0ffc and Barter 5cac6677]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] The 48 deliverables reviewed by an agent that wrote none of them
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

- [x] CHK-001 [P0] Operator decisions recorded before any edit [EVIDENCE: four answers on 2026-09-27, recorded in spec.md section 10]
- [x] CHK-002 [P0] Baseline measured before the rerun [EVIDENCE: 17 of 48 in tier under the strict checker]
- [x] CHK-003 [P1] The engine and the model available [EVIDENCE: the first two sessions of the stopped start returned `ok`]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The rubric block is identical on both sides [EVIDENCE: `cmp` of the extracted 19-line blocks, no difference]
- [x] CHK-011 [P0] Declared kernel statements stay verbatim [EVIDENCE: `run_residency.sh` PASSED, exit 0, after the guide fix]
- [x] CHK-012 [P1] No selection threshold changed [EVIDENCE: the structure tiers keep 1 to 3, 4 to 6 and 7 to 10; `framework-pattern-library.md` untouched]
- [x] CHK-013 [P1] No citation into a changed rule file points at a shifted line [EVIDENCE: HEAD-to-working line map applied; a scan for bare citations past each insert point found 0]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-011 Met]
- [x] CHK-021 [P0] `check_run.py` exits 0 across the 48 [EVIDENCE: 48 scenarios, 48 declared turns, 48 event streams read, 0 finding(s), exit 0]
- [x] CHK-022 [P1] Tier hits compared like for like with the 2026-09-26 pack [EVIDENCE: one checker on both packs and on the old first attempts: 25 against 13]
- [x] CHK-023 [P1] JSON and YAML payloads checked [EVIDENCE: 12 of 14 parse; PFW-005 and PFW-007 fail on an unquoted colon, recorded as findings, the deliverables left verbatim]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The label collision is classed `class-of-bug` and every file naming a complexity band was searched [EVIDENCE: a search for Simple, Medium and Complex with a range found only the JSON and YAML structure tiers, fixed on both sides]
- [x] CHK-FIX-002 [P0] Twins changed together [EVIDENCE: every rule edit has its Project counterpart; the four VIBE files changed as two pairs]
- [x] CHK-FIX-003 [P1] Consumers of the changed rule files checked [EVIDENCE: 222 playbook citations remapped; nothing quotes the old tier names]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commits that land this packet [EVIDENCE: Prompt Improver 4da1a1a, 13bdf85 and 4f55b66, Barter ccd0425c, 5b5c51d6 and ff3e5526]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secret, credential or private data in a rule, scenario or run record [EVIDENCE: every input is a made-up business case]
- [x] CHK-031 [P1] The public repo commit carries no attribution line [EVIDENCE: 4da1a1a message has none]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: all three name the rubric, the guide fix, the 48-scenario rerun and the pack refresh]
- [x] CHK-041 [P1] The changelog and `SYNC.md` record every rule change, the guide fix included [EVIDENCE: `changelog/v0.6.0.0.md` scope line and label section and `changelog/v0.6.1.0.md` for the name; the two 2026-09-27 `SYNC.md` notes]
- [x] CHK-042 [P2] README Local Output names the new run [EVIDENCE: Local Output links the 2026-09-27 run and says it replaced the 2026-09-26 deliverables]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] The stopped start's partial output kept out of the run folder [EVIDENCE: moved to the session scratchpad, not deleted]
- [x] CHK-051 [P0] `export/benchmark/` holds only `skill/` and `claude project/` [EVIDENCE: `ls -A` lists the two]
- [x] CHK-052 [P0] The 48 deliverables are verbatim run output [EVIDENCE: collector dry run, 48 lines and 0 keep warnings]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 11 | 11/11 |
| P1 Items | 11 | 11/11 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-27
<!-- /ANCHOR:summary -->

---
