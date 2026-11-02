---
title: "Decision Record: Prompt Improver Visual Mode Interface-Design Reconciliation"
description: "ADR for reconciling Visual Mode with the Public anti-default canon: reconcile-deep and fold the anti-default discipline into EVOKE, over layering checks alongside or a full rebuild."
trigger_phrases:
  - "visual mode reconciliation decision"
  - "evoke anti-default adr"
  - "reconcile vs layer vs rebuild"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "001-prompt-improver-interface-design"
    last_updated_at: "2026-06-21T00:00:00Z"
    last_updated_by: "claude-opus-4-8"
    recent_action: "Recorded ADR-001 reconcile-deep with alternatives"
    next_safe_action: "Optional live fixture and project-side canon check"
    blockers: []
    key_files:
      - "decision-record.md"
      - "spec.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "template-session"
      parent_session_id: null
    completion_pct: 10
    open_questions: []
    answered_questions: []
---
# Decision Record: Prompt Improver Visual Mode Interface-Design Reconciliation

<!-- SPECKIT_LEVEL: 3 -->
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Reconcile Visual Mode with the anti-default discipline

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-06-21 |
| **Deciders** | Operator, orchestrator (analysis) |

---

<!-- ANCHOR:adr-001-context -->
### Context

Visual Mode is a deployed prompt-engineering system that turns technical briefs into evocative prompts for AI design tools (MagicPath, Lovable, Aura, Bolt, v0.dev). It is built on the VIBE framework and EVOKE scoring, which share lineage with the Public canon (DEPTH/CLEAR/COSTAR) but predate the anti-default refinements now codified in `design_generation_patterns.md` and `design_principles.md`. The two contradict at the load-bearing level: Visual Mode's eight named Design Directions function as exactly the pick-a-vibe menu the canon forbids (`design_generation_patterns.md` §3/§6, `real_ui_loop.md` §8); it has no subject grounding, no avoid-list, no single justified aesthetic risk, and no critique-against-defaults gate; and EVOKE has no dimension or gate for grounding, so a templated default can score 45/50 and ship.

### Constraints

- Visual Mode is deployed; an abrupt behavior change risks existing user workflows.
- Its evocative Creative-Director prose and platform-specific optimization are the product's differentiation and must survive.
- Target files live outside the Public git tree, so no Public CI catches a regression.
- The operator fixed three decisions up front: scope is analyze plus implement; approach is reconcile deep; EVOKE folds the discipline into the score.
<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**We chose**: Reconcile deep. Fold the anti-default discipline into Visual Mode's existing structure rather than layering checks beside it or rebuilding from scratch.

**How it works**: Add Step 0 subject grounding before VIBE; add an avoid-list plus one justified aesthetic risk to the emitted brief; reframe the eight directions from a chooser into default-naming vocabulary; fold a grounding/anti-default enforcement into EVOKE (a scored dimension and/or a blocking gate, in both `visual_mode.md` §5 and `patterns_evaluation.md` §7) so a median cannot pass; add a non-skippable pre-output critique; add seed-of-thought debias for multi-direction asks; carry the UX quality floor into every brief; and cite `design_generation_patterns.md` as upstream canon.
<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **(a) Reconcile deep [chosen]** | Fixes root causes (chooser, EVOKE blind spot, missing grounding); preserves evocative prose + platform optimization; EVOKE stays 50 pts; directions become richer vocabulary | Higher effort; needs care to avoid flattening tone; Prompt Improver files outside Public git | 8/10 |
| (b) Layer checks alongside | Lower risk to existing output; quick; no structural change | Leaves the forbidden menu and EVOKE blind spot in place; checks are skippable; two competing quality systems confuse | 4/10 |
| (c) Full rebuild around `design_generation_patterns.md` | Cleanest canon alignment; eliminates legacy structure | Destroys the evocative-prose differentiation; high regression risk; loses platform optimization; user-facing breaking change | 3/10 |

**Why this one**: Option (a) is the only approach that fixes the structural problems while preserving what makes Visual Mode valuable. Option (b) is cosmetic; option (c) discards the assets the operator asked to keep.
<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**What improves**:
- Visual Mode output is grounded and anti-default by construction.
- EVOKE can no longer pass a well-written templated default.
- The eight directions become default-naming vocabulary instead of a chooser.
- Public canon is honored without forking; drift is checked by an explicit upstream citation.

**What it costs**:
- Edits span six Prompt Improver files; the EVOKE fold needs calibration to avoid over-penalizing a default a pinned brief explicitly asked for. Mitigation: the pinned-direction edge case overrides the gate; calibrate against the SC-001 fixture.
- Deployed users see an additive structure change (Step 0 first, avoid-list present). Mitigation: VIBE and platform behavior preserved; structure is additive.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| Reconciliation flattens evocative tone | H | Acceptance tests target median-rejection, not tone; prose preserved by design |
| Prompt Improver files drift from canon again | M | Provenance citation in `visual_mode.md`; recommended project keyword check |
| Edit silently wrong (no Public CI) | M | Orchestrator file-by-file verification against canon |
<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-five-checks -->
### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | Visual Mode currently ships templated defaults the Public canon forbids; the conflict is verbatim and live |
| 2 | **Beyond Local Maxima?** | PASS | Three options weighed (reconcile / layer / rebuild) with scored trade-offs |
| 3 | **Sufficient?** | PASS | Six mechanisms map 1:1 to the canon's load-bearing rules; nothing added beyond closing the gap |
| 4 | **Fits Goal?** | PASS | Directly answers the operator's "improve the visual mode" with grounding + anti-default discipline |
| 5 | **Open Horizons?** | PASS | Citation keeps Visual Mode aligned to evolving Public canon instead of forking it |

**Checks Summary**: 5/5 PASS
<!-- /ANCHOR:adr-001-five-checks -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**:
- `visual_mode.md`: Step 0, brief slots, directions, critique gate, seed-of-thought, EVOKE §5, provenance.
- `patterns_evaluation.md`: EVOKE §7 fold.
- `visual_mode_library.md`: vocabulary recast.
- `SKILL.md`: routing; `README.md` + `claude project/` mirror: docs.

**How to roll back**: Edits are file-scoped and additive. Restore any single file from its pre-edit backup taken in the Prompt Improver repo; the Public spec folder is documentation only and need not be reverted.
<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->
