---
title: "Feature Specification: Prompt Improver complexity rubric and export layout"
description: "Prompt Improver rates complexity with a scored rubric and delivers each prompt as a file with a header and a body. These phases set how the rating is made and how the delivered file is laid out, on the skill and in the Claude Project."
trigger_phrases:
  - "prompt improver complexity rubric"
  - "prompt improver export layout"
  - "prompt improver header separator"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "005-pi-complexity-rubric"
    last_updated_at: "2026-09-27T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed phase 002 on edecbed and 07ca0122"
    next_safe_action: "None; a live run under skill 0.6.2 is the next evidence"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "005-pi-complexity-rubric-parent"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---

<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->
<!-- SPECKIT_LEVEL: 2 -->

# Feature Specification: Prompt Improver complexity rubric and export layout

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-27 |
| **Branch** | `main` |
| **Parent Spec** | None |
| **Parent Packet** | 005-pi-complexity-rubric |
| **Predecessor** | `046-benchmark-code-alignment` |
| **Successor** | None |
| **Handoff Criteria** | Each phase validates on its own, and the skill and the Claude Project pass the parity gate after it |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Prompt Improver's deliverables carry two things a reader has to tell apart: a header line that reports the mode, the complexity and the framework, and the prompt the user will paste. The rating in that header had no rule for a 9 or a 10, and the header sits directly on top of the prompt, so a reader copying the prompt can take the header with it.

### Purpose
The complexity rating follows a rubric anyone can recount, and every delivered file keeps its header visibly apart from the prompt, on both runtimes and in the benchmark pack.

> **Phase-parent note:** This spec.md is the only authored document at the parent level. Planning, tasks, checks and decisions live in the child phase folders listed in the Phase Documentation Map below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The Complexity Rubric, its label scale, the rerun of the 48 framework-coverage scenarios, their grading and the removal of the company name from both packages (phase 001)
- A divider between the header line and the prompt in every export and every Deliverable Block, in the skill, the Claude Project, the playbook, the checking tools and the benchmark pack (phase 002)

### Out of Scope
- Framework selection, question routes and scoring gates
- The fields the header carries

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| `sk-prompt-improver/references/depth-framework.md` and its Project twin | Modify | 001 | The Complexity Rubric |
| `sk-prompt-improver/SKILL.md`, `assets/format-guide-*.md`, `claude project/Custom Instructions.md` and the Project format guides | Modify | 001, 002 | The label scale, then the header divider |
| `sk-prompt-improver/manual-testing-playbook/` | Modify | 001, 002 | Scenario tiers, then the file layout the scenarios check |
| `export/benchmark/skill/`, `export/benchmark/claude project/` | Replace, Modify | 001, 002 | The rerun's deliverables, then the divider added by hand |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> This spec uses phased decomposition. Each phase is an independently executable child spec folder. All implementation details live inside the phase children.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | `001-complexity-rubric/` | The Complexity Rubric, the 48-scenario rerun, its grading and the company name removal | Complete |
| 2 | `002-header-separator/` | A divider between the header and the prompt in every export and Deliverable Block | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently before the next phase begins
- Parent spec tracks aggregate progress via this map
- Use `/speckit:resume [parent-folder]/[NNN-phase]/` to resume a specific phase
- Run `validate.sh --recursive` on parent to validate all phases as integrated unit

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 001 | 002 | The rubric work is committed and pushed, and the parity gate passes | `validate_parity.py prompt-improver` PASSED 13/13 on Prompt Improver 4f55b66 |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- Whether a text scenario's target model must be named in the prompt, recorded in the 2026-09-27 run README
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: See sub-folders `[0-9][0-9][0-9]-*/` for per-phase spec.md, plan.md, tasks.md
- **Graph Metadata**: See `graph-metadata.json` for `derived.last_active_child_id` pointer
