---
title: "Implementation Plan: Prompt Improver Visual Mode Interface-Design Reconciliation"
description: "Phased plan to fold the Public anti-default discipline into Visual Mode across six files, with MiMo drafting, DeepSeek implementing at max thinking, and the orchestrator verifying each edit against canon."
trigger_phrases:
  - "visual mode reconciliation plan"
  - "deepseek visual mode implementation"
  - "evoke anti-default fold plan"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "001-prompt-improver-interface-design"
    last_updated_at: "2026-06-21T00:00:00Z"
    last_updated_by: "claude-opus-4-8"
    recent_action: "Plan executed; six mechanisms shipped and verified"
    next_safe_action: "Optional live fixture and project-side canon check"
    blockers: []
    key_files:
      - "spec.md"
      - "plan.md"
      - "tasks.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "template-session"
      parent_session_id: null
    completion_pct: 95
    open_questions: []
    answered_questions: []
---
# Implementation Plan: Prompt Improver Visual Mode Interface-Design Reconciliation

<!-- SPECKIT_LEVEL: 3 -->
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core + level2-verify + level3-arch | v2.2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Artifact type** | Prompt-engineering skill (markdown docs), not application code |
| **Target repo** | `AI_Systems/Barter/Prompt Improver` (outside Public git) |
| **Upstream canon** | `sk-prompt/references/design_generation_patterns.md`; `sk-interface-design/references/design-process/{design_principles,real_ui_loop,variation_diversity,ux_quality_reference}.md` |
| **Drafting** | MiMo v2.5 Pro via cli-opencode (read-only) |
| **Implementation** | DeepSeek v4 pro at max thinking via cli-opencode |
| **Verification** | Orchestrator (file-by-file against canon) + spec `validate.sh --strict` |

### Overview
Six mechanisms (M1-M6) graft the Public anti-default discipline into Visual Mode while keeping its evocative prose and platform optimization. The work edits six Prompt Improver files. Because those files sit outside the Public git tree, the durable Public deliverable is this spec folder; the edits are verified against canon by the orchestrator, not by Public CI.

<!-- /ANCHOR:summary -->
---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Conflict verified verbatim against both canon files and the current `visual_mode.md`
- [x] Six mechanisms mapped to requirements with checkable acceptance criteria
- [x] Decision (reconcile deep + fold-into-EVOKE) recorded in `decision-record.md`
- [x] Target-file map complete, including the EVOKE-in-two-files detail

### Definition of Done
- [ ] All P0 requirements (REQ-001..005) met and verified against the edited files
- [ ] SC-001 fixture: a median brief scores below threshold / is blocked under revised EVOKE
- [ ] No pick-a-vibe menu / auto-detect direction logic remains (SC-002)
- [ ] `validate.sh --strict` passes on the spec folder
- [ ] `checklist.md` items marked with evidence; completion metadata reconciled

<!-- /ANCHOR:quality-gates -->
---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Reconciliation overlay: keep the VIBE→EVOKE skeleton, insert grounding + anti-default discipline at the seams the canon specifies (before VIBE; inside the brief; inside EVOKE; before emission).

### Key Components
- **Step 0 — Ground the subject** (`visual_mode.md`): subject / audience / single job, before VIBE.
- **Brief slots** (`visual_mode.md`): avoid-list + one justified aesthetic risk + UX floor.
- **Directions as default-naming** (`visual_mode.md`, `visual_mode_library.md`): name the category default, then deviate — no chooser.
- **Anti-default EVOKE** (`visual_mode.md` §5 + `patterns_evaluation.md` §7): grounding/anti-default dimension and/or blocking gate so a median can't pass.
- **Pre-output critique gate** (`visual_mode.md`): "would I produce this for any similar brief?".
- **Seed-of-thought** (`visual_mode.md`): grounded distinct angles for N variations.
- **Provenance** (`visual_mode.md`): cite `design_generation_patterns.md` as upstream canon.

### Data Flow
```
Brief → [Step 0: subject/audience/job] → VIBE extraction
      → compose brief (+ avoid-list + one risk + UX floor)
      → [N>1? seed-of-thought → distinct grounded angles]
      → [critique gate: similar-brief test] → EVOKE (anti-default enforced) → emit or revise
```

<!-- /ANCHOR:architecture -->
---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

### Phase 1: Spec scaffold (this packet)
- [x] Author spec.md / plan.md / tasks.md / checklist.md / decision-record.md
- [ ] Backfill description.json + graph-metadata.json
- [ ] `validate.sh --strict` green

### Phase 2: Implement M1-M3 (structure + directions) — DeepSeek
- [ ] `visual_mode.md`: Step 0 grounding; avoid-list + single-risk slots
- [ ] `visual_mode.md`: directions reframed to default-naming (remove pick-one)
- [ ] `visual_mode_library.md`: vocabulary banks recast as default-naming + deviation

### Phase 3: Implement M4-M6 (scoring + discipline) — DeepSeek
- [ ] `patterns_evaluation.md` §7 + `visual_mode.md` §5: anti-default EVOKE fold
- [ ] `visual_mode.md`: pre-output critique gate; seed-of-thought; UX floor; provenance citation
- [ ] `SKILL.md`: routing/loading for the new flow

### Phase 4: Documentation sync — DeepSeek
- [ ] `README.md` and `claude project/` mirror updated to the reconciled mode

### Phase 5: Verification — orchestrator
- [ ] File-by-file check against canon; SC-001 median-brief fixture; grep for residual chooser logic
- [ ] Author implementation-summary.md; reconcile completion metadata

<!-- /ANCHOR:phases -->
---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Method | Pass Criteria |
|-----------|-------|--------|---------------|
| Spec validation | spec folder | `validate.sh --strict` | Exit 0/1 |
| Anti-default fixture | revised EVOKE | Score a known median brief | Below threshold or blocked (SC-001) |
| Structural inspection | edited Prompt Improver files | Read + grep | Step 0, avoid-list, risk, critique, UX floor present; no chooser logic (SC-002..006) |
| Tone preservation | sample emitted brief | Manual read | Still evocative prose; platform length target met (SC-007) |

<!-- /ANCHOR:testing -->
---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| cli-opencode + `xiaomi`/`deepseek` providers | External | Green (verified) | No model dispatch; orchestrator authors directly |
| Public canon files | Internal | Green | Cannot ground requirements |
| Prompt Improver repo write access | External | Assumed | Implementation cannot land |

<!-- /ANCHOR:dependencies -->
---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: Reconciled Visual Mode flattens output or breaks platform expectations.
- **Procedure**: The edits are confined to six files; revert them in the Prompt Improver repo (git or backup copy taken before edit). The Public spec folder is documentation only and need not be reverted.

<!-- /ANCHOR:rollback -->
---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Phase 1 (Scaffold) ──> Phase 2 (M1-M3) ──> Phase 3 (M4-M6) ──> Phase 4 (Docs) ──> Phase 5 (Verify)
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| 1 Scaffold | None | All |
| 2 M1-M3 | 1 | 3, 4 |
| 3 M4-M6 | 2 (directions reframed before EVOKE references them) | 4 |
| 4 Docs | 2, 3 | 5 |
| 5 Verify | All | None |

<!-- /ANCHOR:phase-deps -->
---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| 1 Scaffold | Low | Done in-session |
| 2 M1-M3 | Medium | 1 DeepSeek dispatch + verify |
| 3 M4-M6 | High (EVOKE calibration) | 1-2 DeepSeek dispatches + verify |
| 4 Docs | Low | 1 dispatch |
| 5 Verify | Medium | Orchestrator |

<!-- /ANCHOR:effort -->
---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Back up the six Prompt Improver files (copy to `/tmp` or git stash in the Prompt Improver repo) before DeepSeek edits
- [ ] Record the pre-edit state so each file can be restored independently

### Rollback Procedure
1. Identify the offending mechanism (which file/section).
2. Restore that file from the pre-edit backup (edits are file-scoped and additive).
3. Re-verify the remaining mechanisms still cohere.

### Data Reversal
- No data migrations; documentation-only changes.

<!-- /ANCHOR:enhanced-rollback -->
---

<!-- ANCHOR:dependency-graph -->
## L3: DEPENDENCY GRAPH

```
        ┌────────────────────┐
        │ Public canon (RO)  │  design_generation_patterns.md
        │ design_principles  │  real_ui_loop / variation_diversity / ux_quality_reference
        └─────────┬──────────┘
                  │ grounds
                  ▼
        ┌────────────────────┐
        │ spec 009 (Public)  │ ── requirements ──┐
        └─────────┬──────────┘                   │
                  │ drives                        │ verified against canon
                  ▼                               ▼
   ┌───────────────────────────────────────────────────┐
   │ Visual Mode (outside Public git)            │
   │  visual_mode.md ─┬─ patterns_evaluation.md (EVOKE) │
   │  visual_mode_library.md ─ SKILL.md ─ README/mirror │
   └───────────────────────────────────────────────────┘
```

<!-- /ANCHOR:dependency-graph -->
---

<!-- ANCHOR:critical-path -->
## L3: CRITICAL PATH

1. Scaffold + validate spec — CRITICAL
2. M3 directions reframed (EVOKE and library both reference directions) — CRITICAL
3. M4 anti-default EVOKE fold (both files) — CRITICAL, needs calibration
4. Verify SC-001 fixture — CRITICAL

**Parallel opportunities**: README/mirror sync (Phase 4) can draft alongside Phase 3; the library recast (M3 in `visual_mode_library.md`) can run with the `visual_mode.md` direction reframe.

<!-- /ANCHOR:critical-path -->
---

<!-- ANCHOR:milestones -->
## L3: MILESTONES

| Milestone | Description | Success Criteria | Target |
|-----------|-------------|------------------|--------|
| M-A | Spec scaffolded + validated | `validate.sh --strict` green | This session |
| M-B | Structure + directions reconciled | Step 0 + avoid-list present; no chooser (SC-002/003) | Phase 2 |
| M-C | Anti-default EVOKE live | Median fixture below threshold (SC-001) | Phase 3 |
| M-D | Docs synced + verified | All SC met; summary written | Phase 5 |

<!-- /ANCHOR:milestones -->
---

<!-- ANCHOR:l3-adr-summary -->
## L3: ARCHITECTURE DECISION SUMMARY

See `decision-record.md`:

| ADR | Decision | Rationale |
|-----|----------|-----------|
| ADR-001 | Reconcile deep + fold anti-default into EVOKE | Fixes the pick-a-vibe menu and EVOKE blind spot while preserving evocative prose; layering is cosmetic, full rebuild is destructive |

<!-- /ANCHOR:l3-adr-summary -->
