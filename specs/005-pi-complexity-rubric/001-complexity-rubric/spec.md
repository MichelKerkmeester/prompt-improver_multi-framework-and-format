---
title: "Feature Specification: Prompt Improver complexity rubric and prose-friendly VIBE scenarios"
description: "Prompt Improver rates complexity 1 to 10 with no rule for what a 9 or 10 is, so its runtime never rated a prompt above 8 and 27 of 48 framework-coverage deliverables missed their tier. This packet adds a scored complexity rubric to the skill and its Claude Project mirror, lets the four VIBE scenarios accept pillars written as prose, and reruns the 48 to measure it."
trigger_phrases:
  - "prompt improver complexity rubric"
  - "complexity rating 9 or 10"
  - "vibe scenarios accept prose"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Prompt Improver complexity rubric and prose-friendly VIBE scenarios

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-27 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 1 of 2 |
| **Predecessor** | None |
| **Successor** | 002-header-separator |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The skill rates a prompt's complexity 1 to 10 under the constraint "Do not add unrequested complexity" (`references/depth-framework.md` lines 125 to 127) and labels it Low, Medium or High, but no rule says what earns a 9 or a 10. In the 2026-09-26 framework-coverage run on `claude-sonnet-5` at effort `xhigh`, no deliverable rated itself above 8/10, 27 of 48 missed the tier their scenario asks for, and the Project side rated lower than the skill. Separately, the four VIBE and VIBE-MP scenarios require labelled pillars while `references/visual-mode.md` line 62 asks for flowing prose, so a grading fails all four whatever the runtime writes.

### Purpose
A request whose stated load is heavy rates as Complex (9 to 10) on both runtimes, by a rubric anyone can recount from the request, and the VIBE scenarios grade the pillars the skill actually asks for.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A scored complexity rubric in the DEPTH Complexity Assessment: five dimensions scored 0 to 2 from what the user stated, rating = 1 + sum capped at 10, bands Low 1 to 4, Medium 5 to 6, High 7 to 8 and Complex 9 to 10
- The header label scale gains Complex, in `SKILL.md`, the three format guides and the kernel's header template, each pointing to the rubric
- The same rules in the Claude Project mirror: the DEPTH knowledge file, the three format-guide knowledge files and the kernel, with the version bumps and the `SYNC.md` record the parity method asks for
- The four VIBE and VIBE-MP scenarios accept the four pillars as prose, labelled or not
- A rerun of the 48 framework-coverage scenarios on `claude-sonnet-5` at effort `xhigh` in a new run folder, a header check, an independent structure review and a README, with the new deliverables replacing the SFW and PFW files in `export/benchmark/`
- Added on the operator's decision after the rerun: the six creative scenario pairs re-tiered to the blind recount's band, a Low tier in the playbook, and their files and titles renamed to match
- Added from the run README's next steps on 2026-09-27: the grading of the 48 against their Pass/fail lines, the removal of the company name that reached two Project deliverables as skill 0.6.1, and a trial of tighter rubric wording that two blind raters recounted and the operator did not keep

### Out of Scope
- The framework-selection thresholds that read complexity, such as RCAF's bonus at 6 or below - the operator asked for a rating rule, not a selection change
- The interactive question routes at 5 to 6 and 7 or more - a Complex rating still falls under 7 or more, so no route changes
- The 30 core scenarios and their exports

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-prompt-improver/references/depth-framework.md` | Modify | The rubric in the Complexity Assessment |
| `sk-prompt-improver/SKILL.md`, `sk-prompt-improver/changelog/v0.6.0.0.md` | Modify, Create | Header label scale and version 0.6.0 |
| `sk-prompt-improver/assets/format-guide-{markdown,json,yaml}.md` | Modify | The label scale and a pointer to the rubric, and in the JSON and YAML guides structure tiers named by range alone, so no tier but 9 to 10 is called Complex |
| `claude project/Custom Instructions.md`, `claude project/knowledge/*` (4), `claude project/README.md` | Modify | The Project mirror, kernel v0.7.0 |
| `SYNC.md`, `README.md` | Modify | Review note, version claims and Local Output |
| `sk-prompt-improver/manual-testing-playbook/*-framework-coverage/vibe-*` (4) | Modify | Pillars accepted as prose |
| `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/` | Create | The rerun, its harness, checks, review and README |
| `export/benchmark/skill/SFW-*`, `export/benchmark/claude project/PFW-*` | Replace | The 48 deliverables from the rerun |
| `sk-prompt-improver/manual-testing-playbook/*-framework-coverage/{frame,motion,vibe}-*` (12), root | Modify, Rename | The creative pairs at the recount's tier, a Low tier in the root |
| `sk-prompt-improver/references/{depth-framework,interactive-mode}.md`, `claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md` | Modify | The company name removed from two titles and the closing line on both sides |
| `sk-prompt-improver/SKILL.md`, `description.json`, `README.md`, `changelog/v0.6.1.0.md`, `claude project/README.md`, `SYNC.md`, `README.md` | Modify, Create | Skill 0.6.1 and its records, kernel unchanged |
| `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/{results.csv,results.md,grading-notes.md,deliverable-lint.csv,rubric-recount-b.md,rubric-wording-trial.md}`, its `README.md` | Create, Modify | The grading, the second recount and the wording trial |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The rubric sits in the skill's DEPTH Complexity Assessment and, with the same dimensions, anchors and bands, in the Project's DEPTH knowledge file |
| REQ-002 | Every header label scale in the skill and the Project names Low, Medium, High and Complex with their ranges and points to the rubric |
| REQ-003 | The parity gate passes and the kernel H1, `SKILL.md` version and README claims agree |
| REQ-004 | The four VIBE and VIBE-MP scenarios pass a deliverable whose four pillars are present as prose, and the playbook validator passes with 78 scenarios |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | All 48 framework-coverage scenarios rerun on `claude-sonnet-5` at effort `xhigh`, with `check_run.py` at exit 0 |
| REQ-006 | The run README gives one row per ID with the new rating, the old rating, tier check, structure verdict and reported score, and counts the tier hits against the 2026-09-26 run under the same checker |
| REQ-007 | `export/benchmark/` holds the rerun's 48 deliverables and the 18 core exports, in `skill/` and `claude project/` only |
| REQ-008 | The six creative scenario pairs target the tier the blind recount gives their input, and the playbook still validates with 78 scenarios |
| REQ-009 | No file either runtime reads names the company, and `SKILL.md`, `description.json`, the READMEs, the changelog and `SYNC.md` agree on skill 0.6.1 with the kernel unchanged |
| REQ-010 | The 48 are graded against their Pass/fail lines as they stood at the run, with one row per ID in `results.csv`, the evidence in `grading-notes.md` and `check_report.sh` run on the folder |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Complex-tier requests rate 9 or 10 on both runtimes in most cases, where the 2026-09-26 run rated none of 18 above 8
- **SC-002**: Anyone can recount a rating from the request and the rubric table and reach the same number within one point
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The rubric over-rates simple requests | Med | Every point must point to something the user stated, and the rerun reports Medium-tier ratings too |
| Risk | Higher ratings shift framework selection through the `complexity <= 6` thresholds | Low | Every framework-coverage input names its framework; the core scenarios' ratings are left to the next core run |
| Risk | A kernel line the parity gate declares changes its residency key | Med | Run the residency check and resync any declared statement |
| Dependency | The `claude` engine and the `claude-sonnet-5` model | High | The run records the engine version, and `check_run.py` proves the model per event stream |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The rubric fits in one table and a short scoring rule, so the runtime can apply it without a separate load

### Security
- **NFR-S01**: No secret, credential or private data enters a rule, a scenario or a run record

### Reliability
- **NFR-R01**: The deliverables are verbatim run output, and the collector warns on any edit
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A one-line request with no stated load rates 1, the floor
- A request at full load on all five dimensions rates 10, the cap

### Error Scenarios
- A runtime that ignores the rubric: the rerun shows it as a tier miss with the same checker, and the README says so

### State Transitions
- The old deliverables leave `export/benchmark/` but stay in git history and in the 2026-09-26 run folder's records
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | About 20 authored files in two repositories, plus a run folder and 48 run outputs |
| Risk | 12/25 | A skill and kernel rule change that reaches every future rating |
| Research | 8/20 | Calibration against the 24 inputs |
| **Total** | **36/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Settled: the operator chose the rubric, its scored shape, prose-friendly VIBE scenarios and a full rerun with a pack refresh on 2026-09-27, and later that day kept the rubric wording as it was after the recount trial
- Open for the operator, recorded as next steps in the run README: whether a text scenario's target model must be named in the prompt, and how to stop skill replies opening with a check instead of the saved path
<!-- /ANCHOR:questions -->

---
