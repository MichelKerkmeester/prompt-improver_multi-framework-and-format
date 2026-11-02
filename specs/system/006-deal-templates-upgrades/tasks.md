---
title: "Tasks: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "deal templates upgrades tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit

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

- [x] T001 Scaffold the Level 2 packet and confirm the templates were written (`specs/006-deal-templates-upgrades/`)
- [x] T002 Capture the route oracle before the change on the probes (HEAD copy in the session scratchpad)
- [x] T003 [P] Record the HEAD baselines: residency passing, kernel 24,233 bytes, 25 fixtures
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Add `strip_source_prompt()` to the router prose and pseudocode (`sk-prompt-improver/SKILL.md`)
- [x] T005 Mirror it in the oracle and add seven fixtures (`benchmark/router/route_contract.py`, `fixtures.json`)
- [x] T006 Rewrite the interaction rules for deliver-first and open items (`SKILL.md`, `references/interactive-mode.md`, `references/depth-framework.md`, `references/patterns-evaluation.md`, `references/visual-mode.md`)
- [x] T007 Move the Project delivery to a bare fence (`SKILL.md`, `assets/format-guide-*.md`)
- [x] T008 Hand-write kernel v1.0.1 and the seven knowledge mirrors (`claude project/`)
- [x] T009 Rewrite the reply linter for the fence contract (`benchmark/grader/deliverable_lint.py`)
- [x] T010 Update the playbook scenarios, root and versions (`sk-prompt-improver/manual-testing-playbook/`)
- [x] T011 Update AGENTS.md, the READMEs, the grader and router READMEs, SYNC.md and the changelog
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 Run the router fixtures, kernel parity and rule parity
- [x] T013 Run the linter on sample replies, the playbook validator, pair divergence and `validate_document.py` against HEAD
- [x] T014 Run residency, derive the resync pairs and simulate them against the current files
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed: static checks only, no model runs by instruction
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

- [x] CHK-001 [P0] Requirements documented in spec.md
- [x] CHK-002 [P0] Technical approach defined in plan.md
- [x] CHK-003 [P1] Dependencies identified and available
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Code passes lint/format checks: `run_fixtures.sh` PASSED 32/32
- [x] CHK-011 [P0] No console errors or warnings: every gate run printed PASSED
- [x] CHK-012 [P1] Error handling implemented: the linter keeps its exit codes, 0 clean and 1 dirty
- [x] CHK-013 [P1] Code follows project patterns: oracle and pseudocode share one function body
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met
- [x] CHK-021 [P0] Manual testing complete: static only, live runs are the operator's
- [x] CHK-022 [P1] Edge cases tested: one-word quote, `$image` control, fenced block only
- [x] CHK-023 [P1] Error scenarios validated: the old-shape reply turns the linter red
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class: all three are `class-of-bug` across source, mirror, oracle, linter and playbook
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed by grep for Canvas, attestation and `[Assumes`
- [x] CHK-FIX-003 [P0] Consumer inventory completed for the router function, the linter and the playbook
- [x] CHK-FIX-004 [P0] Parser fix includes adversarial fixtures: one-word quote, lead-in without quotes, fenced block alone, command with a quote
- [x] CHK-FIX-005 [P1] Matrix axes listed in plan.md: quote length, fence, lead-in, command
- [x] CHK-FIX-006 [P1] Hostile global state: residency and pair checks ran with a fresh `PYTHONPYCACHEPREFIX`
- [x] CHK-FIX-007 [P1] Evidence is pinned to the uncommitted working tree against Prompt Improver HEAD `f0cf00d`
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets
- [x] CHK-031 [P0] Input validation implemented: the stripper never removes command tokens outside quotes or fences
- [x] CHK-032 [P1] Auth/authz working correctly: not applicable
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized
- [x] CHK-041 [P1] Code comments adequate, with no ephemeral IDs
- [x] CHK-042 [P2] README updated (if applicable)
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only: working files sat in the session scratchpad
- [x] CHK-051 [P1] scratch/ cleaned before completion: only `.gitkeep` remains
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 13 | 13/13 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-18
<!-- /ANCHOR:summary -->

---
