---
title: "Tasks: Prompt Improver Visual Mode Interface-Design Reconciliation"
description: "Task breakdown for the six-mechanism Visual Mode reconciliation: setup the spec, implement M1-M6 across six Prompt Improver files via DeepSeek, verify against canon."
trigger_phrases:
  - "visual mode reconciliation tasks"
  - "vibe evoke reconciliation task list"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "001-prompt-improver-interface-design"
    last_updated_at: "2026-06-21T00:00:00Z"
    last_updated_by: "claude-opus-4-8"
    recent_action: "All implementation + verification tasks complete"
    next_safe_action: "Optional live fixture and project-side canon check"
    blockers: []
    key_files:
      - "tasks.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "template-session"
      parent_session_id: null
    completion_pct: 95
    open_questions: []
    answered_questions: []
---
# Tasks: Prompt Improver Visual Mode Interface-Design Reconciliation

<!-- SPECKIT_LEVEL: 3 -->
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->

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

- [x] T001 Author spec.md / plan.md / decision-record.md / tasks.md / checklist.md (spec folder)
- [x] T002 Backfill description.json + graph-metadata.json (spec folder) {deps: T001}
- [x] T003 Run `validate.sh --strict` and clear HIGH issues (spec folder) {deps: T002}
- [x] T004 [P] Back up the six target files before any edit (Prompt Improver repo) {deps: T001}

<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

Dispatch: DeepSeek v4 pro at max thinking via cli-opencode; orchestrator verifies each edit.

### M1-M3 — structure and directions
- [x] T005 Add Step 0 subject-grounding (Subject / Audience / Single Job) before VIBE (`skill/references/visual_mode.md`) {deps: T004}
- [x] T006 Add Avoid-List + Single-Aesthetic-Risk slots to the emitted-brief template (`skill/references/visual_mode.md`) {deps: T005}
- [x] T007 Reframe the eight directions from pick-one chooser to default-naming + deviation (`skill/references/visual_mode.md`) {deps: T005}
- [x] T008 [P] Recast direction vocabulary banks as default-naming + deviation; remove selection logic (`skill/assets/visual_mode_library.md`) {deps: T007}

### M4-M6 — scoring and discipline
- [x] T009 Fold grounding/anti-default enforcement into EVOKE in `patterns_evaluation.md` §7 (keep 50-pt total) {deps: T007}
- [x] T010 Mirror the EVOKE fold in `visual_mode.md` §5 consistent with §7 (`skill/references/visual_mode.md`) {deps: T009}
- [x] T011 Add non-skippable pre-output critique gate ("would I produce this for any similar brief?") (`skill/references/visual_mode.md`) {deps: T006}
- [x] T012 Add seed-of-thought debias for N>1 variations; UX-floor section; provenance citation to `design_generation_patterns.md` (`skill/references/visual_mode.md`) {deps: T006}

### Routing and docs
- [x] T013 Update routing/loading for the Step 0 → VIBE → critique → EVOKE flow (`skill/SKILL.md`) {deps: T010, T011}
- [x] T014 [P] Update README to describe the reconciled Visual Mode (`README.md`) {deps: T013}
- [x] T015 [P] Sync the `claude project/` Visual Mode mirror (`claude project/`) {deps: T014}

<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T016 SC-001 fixture: score a known median brief under revised EVOKE; confirm below threshold / blocked (`patterns_evaluation.md`) {deps: T010}
- [x] T017 Grep both files for residual auto-detect/pick-one/dial logic; confirm none remains (`visual_mode.md`, `visual_mode_library.md`) {deps: T007, T008}
- [x] T018 Verify every emitted-brief template carries Subject, Audience, Single Job, Avoid-List, Single Risk, UX Floor, provenance (`visual_mode.md`) {deps: T012}
- [x] T019 Author implementation-summary.md; reconcile completion metadata; final `validate.sh --strict` (spec folder) {deps: T016, T017, T018}

<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] All P0 tasks complete; P1 complete or user-approved deferral
- [ ] No residual pick-a-vibe menu / dial / auto-detect logic
- [ ] SC-001 median-brief fixture passes (below threshold / blocked)
- [ ] `validate.sh --strict` green; checklist.md verified with evidence
- [ ] ADR-001 status: Accepted

<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
- **Checklist**: See `checklist.md`
- **Decisions**: See `decision-record.md`

<!-- /ANCHOR:cross-refs -->
