---
title: "Feature Specification: Prompt Improver example pack, playbook extension and scenario upgrade"
description: "Prompt Improver's benchmark exports cover only Markdown and JSON from seven scenario pairs, and the playbook behind them carries wording defects its last run found. This packet raises the quality of the 18 exports, extends the playbook to 78 scenarios, tightens the existing 14 and fills the pack with a real framework-coverage run."
trigger_phrases:
  - "prompt improver example pack"
  - "pi benchmark exports quality"
  - "prompt improver playbook extension"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Prompt Improver example pack, playbook extension and scenario upgrade

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-26 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
`export/benchmark/` in the Prompt Improver repo is the page a reader opens to see what the system writes, yet it holds only 14 Markdown and 4 JSON prompts from seven scenario pairs, covering `$text`, one `$image` and `$json`. Nothing shows `$deep`, `$short`, `$refine`, `$raw`, `$yaml`, `$video` or `$vibe`. Two of the exports carry extras the operator has since ruled scope expansion. The playbook that produced them has wording defects its 2026-09-25 run recorded, and a re-collection would overwrite any hand improvement, since the collector has no edit guard.

### Purpose
A reader of `export/benchmark/` sees strong prompts in every format the system writes, and the playbook can grade all of them.

### Reopened on 2026-09-26
The operator then ruled that `export/benchmark/` holds only the `skill/` and `claude project/` output of real runs, and that the pack had too many simple prompts with no visible framework. The eight agent-written examples were dropped (ADR-001). In their place, 24 framework-coverage scenario pairs run on the real harness give medium, high and complex prompts organised by each framework in the skill's library.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Raise the quality of the 18 run exports in place, keeping header, attestation, file name, supplied facts and scenario limits
- Eight examples written through the skill for the new modes and formats, in `export/benchmark/examples/`, marked ungraded. Superseded by ADR-001 and deleted
- 24 framework-coverage scenario pairs, SFW-001 to SFW-024 and PFW-001 to PFW-024, taking the playbook to 78 at root 1.2.0.0
- A run of those 48 on `claude-sonnet-5` at effort `xhigh`, collected into `export/benchmark/`, with a header check, one rerun per tier miss and an independent structure review
- A run folder README with one row per SFW and PFW ID
- Eight new scenario pairs, taking the playbook from 14 to 30, and a root that lists them
- Tighter wording in the 14 existing scenarios, with their inputs frozen
- The collector's edit guard and a selftest for it

### Out of Scope
- A rerun or grading of the 30 core scenarios
- Grading the 48 framework-coverage scenarios against their Pass/fail lines. This run checks header, tier and structure only
- Any change to `SKILL.md`, `AGENTS.md`, the references, the kernel or the knowledge files
- Project-side example outputs, since only a real claude.ai Project produces those

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `export/benchmark/skill/*`, `export/benchmark/claude project/*` | Modify | 18 exports improved |
| `export/benchmark/examples/*` | Create, then Delete | 8 examples and an index, deleted under ADR-001 |
| `export/benchmark/skill/SFW-*`, `export/benchmark/claude project/PFW-*` | Create | 48 framework-coverage deliverables, verbatim run output |
| `sk-prompt-improver/manual-testing-playbook/*-framework-coverage/` | Create | 48 scenarios, root at 1.2.0.0 |
| `benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/` | Create | The run, its harness, the header checker and its README |
| `sk-prompt-improver/manual-testing-playbook/**` | Modify, Create | 14 scenarios tightened, 16 added, root at 1.1.0.0 |
| `benchmark/reports/2026-09-25--.../run/collect_exports.py`, `run/selftest.py` | Modify, Create | Edit guard and its selftest |
| `benchmark/reports/2026-09-25--.../README.md`, `README.md` | Modify | The edit, the pack and the playbook recorded |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Each of the 18 exports scores at or above its original on its routed rubric, passes its gate, keeps every supplied fact and scenario limit and adds no scope |
| REQ-002 | The playbook holds 30 scenarios that the validator passes and the runner parses, each in one wave |
| REQ-003 | The 14 existing scenarios keep every user input byte for byte |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | Eight examples, one per new skill scenario, parse in their format and pass their gate. Superseded by ADR-001 |
| REQ-005 | The collector keeps an edited export unless `--force` is given, proven by a selftest with a negative control |
| REQ-006 | The run README records the edit, the pack and the playbook change, and names a rerun as the next step |
| REQ-007 | The playbook holds 78 scenarios that the validator passes and the runner puts in one wave each, and `export/benchmark/` holds only `skill/` and `claude project/` |
| REQ-008 | Every one of the 48 framework-coverage scenarios runs on `claude-sonnet-5` at effort `xhigh`, proven by `check_run.py` |
| REQ-009 | Each of the 48 has a collected deliverable whose header names its target framework, and a tier miss gets one rerun and is then recorded, never hand-edited |
| REQ-010 | The run README has one row per SFW and PFW ID with framework, tier, header check, structure verdict and reported score |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A reader finds a strong example for every mode and format the system supports
- **SC-002**: The next playbook run can grade all 30 scenarios without a structural fix
- **SC-003**: Each library framework has a runtime-produced prompt in the pack at every tier the brief set for it
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A quality pass adds scope the user never asked for | High | An independent reviewer checks every export against its scenario and snapshot |
| Risk | Examples written by agents differ from what the real runtime writes | Med | They are marked ungraded, and the next step is a run of the new scenarios |
| Risk | New scenario rules cite lines that do not say what they claim | Med | Writers verify each citation, and a reviewer checks them |
| Risk | The runtime rates complexity below the brief's tier | Med | One rerun per miss, and a second miss is recorded in the run README |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: A grader decides each Pass/fail line from the reply and the export alone

### Security
- **NFR-S01**: No secret, credential or private data enters any example or scenario

### Reliability
- **NFR-R01**: A re-collection never undoes a hand edit without `--force`
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A Turn 2 revision export (`002` or `-pm`) keeps what distinguishes it from the Turn 1 file
- Raw mode writes no score, so its example carries no score line

### Error Scenarios
- A route the skill would still question: the writer records the question and delivers on the defaults the rules allow

### State Transitions
- The graded originals stay in git history, and the run's verdicts keep citing them
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 20/25 | About 55 files in two repositories, then about 160 more for the framework-coverage run, most of them scenario files and run output |
| Risk | 10/25 | Scope expansion inside prompts, unverified agent examples |
| Research | 8/20 | Mode rules read per new scenario |
| **Total** | **38/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose the packet, the aim, no rule changes and the variety approach on 2026-09-26, and approved the plan
<!-- /ANCHOR:questions -->

---
