---
title: "Decision Record: Prompt Improver example pack, playbook extension and scenario upgrade"
description: "Why the eight agent-written examples were dropped and a real framework-coverage run took their place."
trigger_phrases:
  - "decision record"
  - "adr examples dropped"
  - "framework coverage run"
  - "examples dropped"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "004-pi-example-pack"
    last_updated_at: "2026-09-27T00:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Recorded why the examples gave way to the framework-coverage run"
    next_safe_action: "Point AC-004 at ADR-001"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-004-pi-example-pack"
      parent_session_id: null
    completion_pct: 80
    open_questions: []
    answered_questions: []
---
# Decision Record: Prompt Improver example pack, playbook extension and scenario upgrade

<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Replace the agent-written examples with a real framework-coverage run

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-09-26 |
| **Deciders** | The operator |

---

<!-- ANCHOR:adr-001-context -->
### Context

The first pass put eight prompts in `export/benchmark/examples/`, written by Opus agents through the skill and marked ungraded. AC-004 was met on them, and the pass was pushed at Prompt Improver `9257494`. The operator then ruled that `export/benchmark/` holds only `skill/` and `claude project/`, as Product Owner's does. They added that the pack had too many simple prompts with no clear use of a named framework, and asked for medium, high and complex prompts built with the frameworks in the skill's library.

### Constraints

- No change to `SKILL.md`, `AGENTS.md`, `references/`, `assets/`, the kernel or the knowledge files (goal D1)
- Deliverables come from real runs, never from agent-written examples (goal D2)
- The operator chose Sonnet 5 at effort xhigh as the engine
<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**We chose**: to delete the eight examples and their index, and to fill the pack with a real harness run of 24 framework-coverage scenario pairs.

**How it works**: SFW-001 to SFW-024 and their Project twins PFW-001 to PFW-024 cover RCAF, COSTAR, CIDI, TIDD-EC, CRISPE and CRAFT at medium, high and complex work, plus FRAME, MOTION, VIBE and VIBE-MP. The playbook runner ran them on `claude-sonnet-5` at effort `xhigh`, and the run's collector copied each deliverable into `skill/` or `claude project/`. Each header was checked for its framework and tier with one rerun per miss, and a reviewer who wrote none of them judged the framework structure.
<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **A real run of 24 framework pairs** | Runtime output on both runtimes, and scenarios that can grade it | About 34 USD of sessions, and the complexity rating is the runtime's own | 9/10 |
| Keep the eight and add framework examples written by agents | Cheap and fast | Not runtime output, which the operator ruled out | 3/10 |
| Move the eight into `skill/` | Matches the two-folder layout | Still agent-written, and mixes ungraded prompts with run output | 2/10 |

**Why this one**: it is the only option that meets both of the operator's rulings, real run output only and visible framework use.
<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**What improves**:
- The pack gains 48 runtime-produced prompts, each naming its framework in its header, in Markdown, JSON and YAML
- 48 new playbook scenarios can grade those prompts in a later run

**What it costs**:
- `$short`, `$refine` and `$raw` no longer have a prompt in the pack. Mitigation: STX-003 to STX-005 and their twins stay in the playbook, so a run of the 30 core scenarios gives them runtime deliverables
- AC-004 no longer describes the packet's state. Mitigation: it is superseded here, and git keeps the eight at `9257494`

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| The runtime rates complexity below the brief's tier | M | One rerun per miss under goal D5, and a second miss is recorded in the run README, never hand-edited |
| Creative briefs write the framework as prose rather than labelled parts | M | Recorded as a finding for the operator, since the prose comes from a mode rule that D1 keeps unchanged |
<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-five-checks -->
### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | The operator ruled the examples out and asked for framework coverage |
| 2 | **Beyond Local Maxima?** | PASS | Three options compared above |
| 3 | **Sufficient?** | PASS | One run folder, one checker and one review, with the existing harness |
| 4 | **Fits Goal?** | PASS | Goal D2 and D3 describe exactly this run |
| 5 | **Open Horizons?** | PASS | The scenarios stay in the playbook for every later run |

**Checks Summary**: 5/5 PASS
<!-- /ANCHOR:adr-001-five-checks -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**:
- `export/benchmark/examples/` is deleted, eight prompts and the index
- The playbook gains `skill-framework-coverage/` and `project-framework-coverage/`, 24 files each, and its root moves to 1.2.0.0 with 78 scenarios
- `benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/` holds the run, and the 48 deliverables land in `export/benchmark/skill/` and `export/benchmark/claude project/`

**How to roll back**: in the Prompt Improver repo, `git checkout 9257494 -- export/benchmark/examples` restores the eight and their index. Deleting the SFW and PFW files from `export/benchmark/`, the two framework-coverage folders and the run folder, then `git checkout 9257494 -- sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md`, removes the run and returns the root to 1.1.0.0.
<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->

---
