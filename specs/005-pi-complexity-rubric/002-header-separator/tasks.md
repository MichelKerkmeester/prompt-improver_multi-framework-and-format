---
title: "Tasks: Prompt Improver header divider"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "header divider tasks"
  - "prompt improver export layout tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Prompt Improver header divider

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

- [x] T001 Convert 079 to a phase parent, move the finished work to `001-complexity-rubric/` and scaffold this phase
- [x] T002 Inventory every file that states or parses the layout (rule files, kernel, playbook, `deliverable_lint.py`, the format gate, residency)
- [x] T003 Baseline: residency, router fixtures, playbook validator, export line scan [EVIDENCE: residency PASSED, router 25/25, playbook PASS 78 scenarios, 0 of 66 exports with the divider]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Skill layout rules edited in place (`sk-prompt-improver/SKILL.md` lines 412, 499, 558, 561) [EVIDENCE: 653 lines before and after]
- [x] T005 Header section, allowed table, examples and checklists (`sk-prompt-improver/assets/format-guide-{markdown,json,yaml}.md`) [EVIDENCE: 5, 2 and 3 example headers divided]
- [x] T006 Same edits in the Project guides (`claude project/knowledge/Prompt Improver - Format Guide *.md`) [EVIDENCE: the changed lines of each twin pair are identical]
- [x] T007 Rule 7, DELIVERY PROTOCOL template and H1 v0.7.1 (`claude project/Custom Instructions.md`) [EVIDENCE: three declared statements resynced in `systems.py`, residency PASSED on 07ca0122]
- [x] T008 Divider check and docstring (`benchmark/grader/deliverable_lint.py`, `benchmark/grader/README.md`, `README.md`) [EVIDENCE: four samples behave, 33 Project exports clean]
- [x] T009 Layout wording and remapped citations (`sk-prompt-improver/manual-testing-playbook/`) [EVIDENCE: 344 named and 13 bare citations moved, validator PASS]
- [x] T010 Divider inserted in the 66 exports (`export/benchmark/skill/`, `export/benchmark/claude project/`) [EVIDENCE: 66 of 66 scan clean, diff +136 -0]
- [x] T011 Hand edit recorded in both run READMEs (`benchmark/reports/2026-09-25--*/README.md`, `benchmark/reports/2026-09-27--*/README.md`) [EVIDENCE: section 9 and section 6]
- [x] T012 Skill 0.6.2, changelog, `SYNC.md` note and README claims [EVIDENCE: parity reports README claims 0.7.1 and 0.6.2 live]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Residency, router fixtures, playbook validator and doc checks pass [EVIDENCE: residency PASSED, router 25/25, playbook PASS, doc issue counts equal to HEAD]
- [x] T014 Export scan and JSON/YAML parse pass [EVIDENCE: 66 with the divider; parse results equal to the baseline, PFW-005 and PFW-007 failing as before]
- [x] T015 Commit Prompt Improver and Barter with the same paths, then parity on the commit and push [EVIDENCE: edecbed and 07ca0122 pushed, parity PASSED 13/13; the Barter push used a one-push route-gate override the operator approved, since the gate flagged another session's stale sk-doc manifest]
- [x] T016 README Output Formats line names the Complex tier, a phase 001 leftover the operator asked to fix (`README.md` line 380) [EVIDENCE: Prompt Improver e8a1f25 and Barter 3c4c599d pushed, the Barter push with an approved one-push route-gate override]
- [x] T017 Live check on DeepSeek V4.1 Flash, 22 scenarios on both runtimes (`benchmark/reports/2026-09-28--header-divider--deepseek-v4.1-flash-high/`) [EVIDENCE: 21 of 21 skill files and 18 of 18 Project blocks with a header carry the divider; `check_run.py` 0 findings]
- [x] T018 A request for valid JSON or YAML only binds the payload and keeps the framing, skill 0.6.3 (`assets/format-guide-{json,yaml}.md` and their Project twins, Divider paragraph) [EVIDENCE: Prompt Improver f4cdfcb and Barter 55be753f pushed; residency PASSED, parity 13/13 with Skill v0.6.3]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every acceptance criterion Met
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

- [x] CHK-001 [P0] Operator decisions recorded before any edit [EVIDENCE: layout, phase under 079 and both export folders, spec.md section 10]
- [x] CHK-002 [P0] Baseline gates run before the edit [EVIDENCE: T003]
- [x] CHK-003 [P1] Every consumer of the layout named [EVIDENCE: plan.md affected surfaces]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The skill and Project guides carry the same header section [EVIDENCE: twin diff of changed lines, no difference]
- [x] CHK-011 [P0] Declared kernel statements stay verbatim [EVIDENCE: resynced with the gate's tool, `run_residency.sh prompt-improver` PASSED on 07ca0122]
- [x] CHK-012 [P1] `SKILL.md` line count unchanged [EVIDENCE: 653]
- [x] CHK-013 [P1] No citation into a changed guide points at a shifted line [EVIDENCE: HEAD-to-working map; 12 bare kernel citations already stale since 001 moved to the lines they name]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-007 Met]
- [x] CHK-021 [P0] The linter flags a block without the divider and passes one with it [EVIDENCE: good exit 0, missing and no-blank exit 1]
- [x] CHK-022 [P1] Every JSON and YAML payload parses below the divider as it did before [EVIDENCE: 16 of 18 parse before and after]
- [x] CHK-023 [P1] Each export's text outside the inserted lines is unchanged [EVIDENCE: script assert per file, diff has 0 deletions]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The layout rule is classed `class-of-bug` and every file stating it was searched [EVIDENCE: phrase sweep over both packages, READMEs and the three README examples]
- [x] CHK-FIX-002 [P0] Twins changed together [EVIDENCE: CHK-010, parity 13/13]
- [x] CHK-FIX-003 [P1] Consumers of the changed rule files checked [EVIDENCE: linter, 2026-09-27 header checker identical before and after, format gate does not cover this system]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commits that land this phase [EVIDENCE: Prompt Improver edecbed, Barter 07ca0122]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secret, credential or private data in a rule, scenario or export [EVIDENCE: layout-only change]
- [x] CHK-031 [P1] The public repo commit carries no attribution line [EVIDENCE: edecbed message]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized
- [x] CHK-041 [P1] The changelog and `SYNC.md` record the change [EVIDENCE: `changelog/v0.6.2.0.md`, the last `SYNC.md` note]
- [x] CHK-042 [P2] README Format Lock line names the divider
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in the session scratchpad only
- [x] CHK-051 [P0] `export/benchmark/` holds the same 66 file names as before [EVIDENCE: 66 modified, none added or removed]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 9 | 9/9 |
| P1 Items | 11 | 11/11 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-27
<!-- /ANCHOR:summary -->

---
