---
title: "Feature Specification: Prompt Improver Visual Mode Interface-Design Reconciliation"
description: "Visual Mode emits design prompts via a pick-a-vibe direction menu and a grounding-blind EVOKE score, contradicting the Public anti-default canon. This spec reconciles it: subject grounding, avoid-list plus one risk, directions-as-default-naming, anti-default EVOKE, seed-of-thought, and a UX floor."
trigger_phrases:
  - "visual mode interface design reconciliation"
  - "prompt improver anti-default"
  - "vibe evoke grounding"
  - "design generation patterns alignment"
  - "pick-a-vibe menu removal"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "001-prompt-improver-interface-design"
    last_updated_at: "2026-06-21T00:00:00Z"
    last_updated_by: "claude-opus-4-8"
    recent_action: "Shipped six mechanisms to live Visual Mode; verified"
    next_safe_action: "Optional live fixture and project-side canon check"
    blockers: []
    key_files:
      - "spec.md"
      - "plan.md"
      - "tasks.md"
      - "checklist.md"
      - "decision-record.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "template-session"
      parent_session_id: null
    completion_pct: 95
    open_questions: []
    answered_questions:
      - "Scope: analyze plus implement the Prompt Improver rewrite"
      - "Approach: reconcile deep, not layer-on or full rebuild"
      - "EVOKE: fold the anti-default discipline into the score"
---
# Feature Specification: Prompt Improver Visual Mode Interface-Design Reconciliation

<!-- SPECKIT_LEVEL: 3 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core + level2-verify + level3-arch | v2.2 -->

---

<!-- ANCHOR:executive-summary -->
## EXECUTIVE SUMMARY

The Prompt Improver is a general-purpose, brand-agnostic prompt-engineering system; its Visual Mode (`$vibe`/`$v`) turns technical briefs into evocative prompts for AI design tools. Its eight named "Design Directions" and its grounding-blind EVOKE score produce exactly the templated-default output that the Public repo's own canon — `sk-prompt/references/design_generation_patterns.md` and `sk-interface-design/.../design_principles.md` — exists to prevent. This spec reconciles Visual Mode with that canon through six mechanisms while preserving its evocative Creative-Director prose, platform optimization, and screenshot analysis.

**Key Decisions**: Reconcile deep (not a light layer-on or a full rebuild); fold the anti-default discipline into EVOKE so a well-written median cannot pass; reframe the eight directions from a chooser into default-naming vocabulary.

**Critical Dependencies**: The target files live outside the Public git tree (no Public CI/review); `design_generation_patterns.md` §2-§3 and `design_principles.md` §2/§4 are the upstream canon and must not drift.

<!-- /ANCHOR:executive-summary -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 3 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-06-21 |
| **Branch** | `001-prompt-improver-interface-design` |
| **System** | Prompt Improver (Visual Mode) |
| **Target repo** | `AI_Systems/Barter/Prompt Improver` (outside Public git) |

<!-- /ANCHOR:metadata -->
---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Visual Mode offers eight named Design Directions (Precision & Density, Warmth & Approachability, …) that the model auto-selects from — structurally identical to the "pick-a-vibe menu" that `design_generation_patterns.md` §3 and `real_ui_loop.md` §8 forbid ("If the option set could be reused across briefs unchanged, it has become a preset and must not ship"). It has no Step-0 subject grounding (`design_principles.md` §2), no avoid-list naming the median, no single justified aesthetic risk (`design_generation_patterns.md` §2: "the load-bearing additions"), and no critique-against-defaults gate (`design_principles.md` §4). EVOKE scoring (Evocative/Visual/Open/Kinetic/Emotional, 50 pts) has no dimension or gate for subject-grounding or anti-default deviation, so a templated default can score 45/50 and ship.

### Purpose
Visual Mode emits design-generation prompts grounded in the concrete subject, explicitly steering off the AI median, that score below threshold if they read as templated defaults — while preserving evocative Creative-Director prose, platform-specific optimization, and screenshot analysis.

<!-- /ANCHOR:problem -->
---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `skill/references/visual_mode.md` — Step 0 grounding; avoid-list + single-risk slots; directions reframed to default-naming; pre-output critique gate; seed-of-thought; UX floor; EVOKE §5 anti-default fold; provenance citation.
- `skill/references/patterns_evaluation.md` — fold the grounding/anti-default enforcement into the §7 EVOKE definition.
- `skill/assets/visual_mode_library.md` — recast direction vocabulary banks from chooser to default-naming + deviation material.
- `skill/SKILL.md` — routing/loading updated for the new Step 0 → VIBE → critique → EVOKE flow.
- `README.md` + `claude project/` mirror — documentation synced to the reconciled mode.

### Out of Scope
- Non-Visual modes (Raw/Text/Improve/Refine/Short/Deep/Image/Video/Interactive) — untouched.
- Full rebuild from scratch — reconciliation only; VIBE acronym and platform list preserved.
- The platform set (MagicPath, Lovable, Aura, Bolt, v0.dev) — unchanged.
- The Public upstream lenses (`design_generation_patterns.md`, `design_principles.md`, `real_ui_loop.md`) — read-only canon, cited not edited.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `…/skill/references/visual_mode.md` | Modify | Step 0; avoid-list + risk; directions→default-naming; critique gate; seed-of-thought; UX floor; EVOKE §5 fold; cite canon |
| `…/skill/references/patterns_evaluation.md` | Modify | Fold grounding/anti-default enforcement into the §7 EVOKE definition (keep 50-pt total coherent) |
| `…/skill/assets/visual_mode_library.md` | Modify | Recast direction vocabulary banks as default-naming + deviation, not a chooser |
| `…/skill/SKILL.md` | Modify | Routing/loading for the new Visual Mode flow |
| `…/README.md` | Modify | Document the reconciled Visual Mode |
| `…/claude project/` (Visual Mode mirror) | Modify | Sync the web-interface mirror to README/skill changes |

<!-- /ANCHOR:scope -->
---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | (M1) Ground-the-Subject Step 0 runs before any aesthetic processing: name the concrete subject, its audience, and the screen's single job. | `visual_mode.md` has an explicit Step 0 that executes before VIBE; the emitted-prompt template carries Subject / Audience / Single-Job fields; no aesthetic vocabulary precedes grounding. Mirrors `design_principles.md` §2. |
| REQ-002 | (M2) The emitted brief carries an avoid-list naming the median plus one justified aesthetic risk. | `visual_mode.md` template has an Avoid-List slot (defaulting to the three median clusters in `design_principles.md` §4 — cream+serif+terracotta / near-black+one-acid-accent / broadsheet-hairlines — plus generic SaaS gradient and centered-hero+three-cards) and a Single-Aesthetic-Risk slot requiring a one-sentence justification. Mirrors `design_generation_patterns.md` §2. |
| REQ-003 | (M3) The eight directions are reframed from a pick-one chooser into vocabulary for naming the category's expected default, which the brief then deviates from. | No auto-detect/pick-one direction logic remains in `visual_mode.md` or `visual_mode_library.md`; directions appear only as default-naming references ("this category usually looks like X; this brief deviates by Y"). Satisfies the no-preset rule of `design_generation_patterns.md` §6 / `real_ui_loop.md` §8. |
| REQ-004 | (M4) EVOKE incorporates anti-default enforcement so a prompt that fails subject-grounding or reads as a templated default cannot clear the threshold (40; MagicPath 42). | Applied in BOTH `visual_mode.md` §5 and `patterns_evaluation.md` §7. A grounding/anti-default element is added as a scored dimension and/or a blocking gate inside the EVOKE evaluation; the 50-pt total and the five existing EVOKE dimensions stay coherent. A median brief that scored ~45 under current EVOKE now scores below threshold or is blocked. |
| REQ-005 | (M4) A mandatory, non-skippable pre-output self-critique runs between composition and emission: "Would I produce this for any similar brief? If yes, revise." | `visual_mode.md` contains an explicit critique gate before emission; it is not skippable; the question is equivalent to the `design_principles.md` §4 review step. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-006 | (M5) Multi-direction asks (2+ variations) use string seed-of-thought to force distinct grounded angles, not N cosmetic copies of the median. | `visual_mode.md` documents the seed algorithm (12-char alphanumeric → ASCII-sum mod N → index into brief-grounded directions, re-seed per variation); indexed options are grounded in the current subject, never a reusable style menu. Mirrors `design_generation_patterns.md` §3 + `variation_diversity.md`. |
| REQ-007 | (M6) The emitted brief carries the UX quality floor: responsive, visible keyboard focus, reduced motion respected. | `visual_mode.md` template includes a non-negotiable UX-Floor section referencing all three, per `ux_quality_reference.md` / `design_principles.md` §5. |
| REQ-008 | (M6) `visual_mode.md` cites `design_generation_patterns.md` as upstream canon to prevent future drift. | A provenance/dependencies note in `visual_mode.md` references `design_generation_patterns.md` §2-§3 (and `design_principles.md` §2/§4) as authoritative; reconciliation context recorded as durable WHY, not an artifact id. |
| REQ-009 | README + Claude-project mirror reflect the reconciled Visual Mode. | Both describe grounded, anti-default Visual Mode; no pick-a-vibe direction references remain; the EVOKE description reflects the anti-default enforcement. |

<!-- /ANCHOR:requirements -->
---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A well-written median brief (generic SaaS dashboard, no subject grounding, untouched component-library surface) scores below threshold or is blocked under revised EVOKE — down from ~45/50 under current EVOKE.
- **SC-002**: No reusable pick-a-vibe menu, named aesthetic dial, or auto-detect direction logic remains in `visual_mode.md` or `visual_mode_library.md` (Given a grep for selection logic, When inspected, Then none remains).
- **SC-003**: Every emitted-brief template contains Subject, Audience, Single Job, Avoid-List, Single Aesthetic Risk, and UX Floor — verified by inspecting the template.
- **SC-004**: The eight former directions appear only as default-naming vocabulary in `visual_mode_library.md`.
- **SC-005**: The pre-output critique gate is present and non-skippable in `visual_mode.md`.
- **SC-006**: `design_generation_patterns.md` is cited as upstream canon in `visual_mode.md`.
- **SC-007**: Evocative Creative-Director prose, platform-specific length targets, and screenshot analysis are preserved (Given a graded brief, When emitted, Then it still reads as prose and meets the platform length target).

<!-- /ANCHOR:success-criteria -->
---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Over-correction flattens the evocative prose into clinical checklists | High — the prose is the product differentiation | Mechanisms are additive; M3 reframes (not removes) directions; M4 adds to EVOKE, not replaces it; acceptance tests for median-rejection, not tone |
| Risk | Prompt Improver files drift from Public canon again (separate repos) | Medium — same conflict resurfaces later | REQ-008 provenance citation; visual_mode.md references the canon as upstream; recommend a project-side keyword check |
| Risk | Deployed-behavior regression (Step 0 first, avoid-list present) | Medium — user-facing structure change | Additive structure; VIBE preserved; platform length targets unchanged (NFR) |
| Dependency | Target files outside Public git — no Public CI/review/validation | Medium — edits could be silently wrong | Orchestrator verifies each edit against the canon after DeepSeek; manual review before any merge in the Prompt Improver repo |
| Dependency | `design_generation_patterns.md`, `design_principles.md`, `real_ui_loop.md` | Low — read-only | Cite, never edit |

<!-- /ANCHOR:risks -->
---

<!-- ANCHOR:nfr -->
## 7. NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: Emitted prompts still hit platform length targets (MagicPath 150-400 words; Lovable 100-250; Aura/Bolt 50-150; v0 100-300). Added Step 0/avoid-list/UX-floor content fits the budget or the platform-optimization step compresses other sections.
- **NFR-P02**: No latency change — Visual Mode is a document-generation flow (prompt in, text out); no new API/render steps.

### Reliability
- **NFR-R01**: EVOKE remains a 50-pt total after the fold; scoring stays deterministic and explainable.

<!-- /ANCHOR:nfr -->
---

<!-- ANCHOR:edge-cases -->
## 8. EDGE CASES

### Data Boundaries
- **Brief already pins a direction** ("I want Linear-style precision"): follow verbatim, skip the deviation gate for that axis — mirrors `design_principles.md` §4 ("Where the brief pins down a visual direction, follow it exactly").
- **Pure-logic / no-UI request** (API, CLI): Step 0 still captures subject + single job; VIBE aesthetic slots marked N/A; grounding enforcement still checks subject-awareness.

### Error Scenarios
- **Multi-platform request** (same brief for MagicPath + v0.dev): avoid-list and grounding carry across; platform-optimization compresses per platform; seed-of-thought re-seeds per platform.
- **Single-variation request**: seed-of-thought is skipped; the one prompt still runs Step 0 → VIBE → critique → EVOKE.

<!-- /ANCHOR:edge-cases -->
---

<!-- ANCHOR:complexity -->
## 9. COMPLEXITY ASSESSMENT

| Dimension | Score | Triggers |
|-----------|-------|----------|
| Scope | 18/25 | Six files in the Prompt Improver repo, substantial mode-doc rewrite, one system |
| Risk | 16/25 | Deployed-system behavior change; no Public CI on the targets; no auth/API surface |
| Research | 14/20 | Cross-referencing two Public canons against a 1,014-line mode doc |
| Multi-Agent | 9/15 | MiMo drafts, DeepSeek implements, orchestrator verifies |
| Coordination | 9/15 | Cross-repo (Public spec drives the edits); six-file dependency order |
| **Total** | **66/100** | **Level 3** |

<!-- /ANCHOR:complexity -->
---

<!-- ANCHOR:risk-matrix -->
## 10. RISK MATRIX

| Risk ID | Description | Impact | Likelihood | Mitigation |
|---------|-------------|--------|------------|------------|
| R-001 | Reconciliation flattens evocative tone | H | M | Acceptance tests target median-rejection, not tone; prose preserved by design |
| R-002 | EVOKE reweight over-penalizes legitimate defaults a pinned brief asked for | M | M | Pinned-direction edge case overrides the gate; calibrate against SC-001 fixture |
| R-003 | an edit silently wrong (no Public CI) | M | M | Orchestrator file-by-file verification against canon |
| R-004 | Canon drift recurs across the repo boundary | M | M | Provenance citation + recommended project keyword check |

<!-- /ANCHOR:risk-matrix -->
---

<!-- ANCHOR:user-stories -->
## 11. USER STORIES

### US-001: Grounded, non-generic output (Priority: P0)

**As a** designer briefing Visual Mode for a fintech app, **I want** the emitted prompt grounded in my actual product, **so that** the design tool produces output specific to my product, not a generic SaaS dashboard.

**Acceptance Criteria**:
1. Given a brief for a Gen-Z budgeting app, When Visual Mode processes it, Then the prompt names subject/audience/single-job before any aesthetic language.
2. Given that brief, When emitted, Then the avoid-list includes "generic SaaS gradient" and "centered hero with three cards" and the prompt spends one justified aesthetic risk.

### US-002: Canon-aligned, verifiable mode (Priority: P0)

**As a** maintainer of the Prompt Improver skill, **I want** Visual Mode aligned to the Public anti-default canon, **so that** I can verify it against `design_generation_patterns.md` and `design_principles.md` without manual diffing.

**Acceptance Criteria**:
1. Given the reconciled `visual_mode.md`, When compared to canon, Then every load-bearing element (grounding, avoid-list, single risk, critique gate, no pick-a-vibe menu) has a corresponding section and the file cites the canon as upstream.

### US-003: Genuinely distinct variations (Priority: P1)

**As a** user asking for three variations of a recipe-app landing page, **I want** distinct grounded angles, **so that** I have real options rather than three cosmetic copies of one default.

**Acceptance Criteria**:
1. Given a 3-variation request, When generated, Then each variation starts from a different seed index and names a different grounded angle from the subject; no two share the same palette or layout skeleton.

<!-- /ANCHOR:user-stories -->
---

<!-- ANCHOR:questions -->
## 12. OPEN QUESTIONS

- EVOKE fold mechanism: scored sixth dimension vs. blocking gate inside the EVOKE evaluation — **RESOLVED: implementation's choice; REQ-004 requires only that a median cannot pass and the 50-pt total stays coherent.**
- Should a project-side CI keyword check enforce the canon long-term? Deferred (recommended, out of this packet's scope).

<!-- /ANCHOR:questions -->
---

<!-- ANCHOR:related-docs -->
## RELATED DOCUMENTS

- **Implementation Plan**: See `plan.md`
- **Task Breakdown**: See `tasks.md`
- **Verification Checklist**: See `checklist.md`
- **Decision Records**: See `decision-record.md`

<!-- /ANCHOR:related-docs -->
