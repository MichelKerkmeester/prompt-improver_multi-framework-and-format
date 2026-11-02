---
title: "Implementation Plan: Prompt Improver complexity rubric and prose-friendly VIBE scenarios"
description: "A scored rubric goes into the skill's DEPTH Complexity Assessment and its Project twin, the header label scale gains Complex, and the playbook accepts VIBE pillars as prose. A rerun of the 48 framework-coverage scenarios measures the rubric against the 2026-09-26 run with one strict header checker."
trigger_phrases:
  - "pi complexity rubric plan"
  - "complexity rubric rerun plan"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Prompt Improver complexity rubric and prose-friendly VIBE scenarios

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill and knowledge files, Markdown playbook, Python run tooling |
| **Framework** | Prompt Improver skill, its Claude Project package and its manual testing playbook |
| **Storage** | None |
| **Testing** | Residency and parity gates, playbook validator, router fixtures, a 48-scenario harness run, a header checker and an independent structure review |

### Overview
The rule change is hand-written on both sides, skill first and the Project mirror second, per the `SYNC.md` manual parity method. The playbook's VIBE scenarios and Complex-tier wording follow the new rules. The 48 framework-coverage scenarios then rerun on `claude-sonnet-5` at effort `xhigh`, and one strict header checker scores both the new run and the 2026-09-26 run so the tier counts compare like for like.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] Tests passing (if applicable)
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Rule source first, hand-written mirror second, scenario contract third, measured run last

### Key Components
- **Complexity Rubric** (`references/depth-framework.md`, Project DEPTH knowledge file): five dimensions scored 0 to 2, rating 1 plus the sum capped at 10, bands Low 1 to 4, Medium 5 to 6, High 7 to 8, Complex 9 to 10
- **Label scale** (`SKILL.md`, three format guides, the kernel's Delivery Protocol): names the four bands and points to the rubric
- **Playbook** (root and four VIBE scenario files, 18 Complex-tier files): prose pillars pass, and `Complex` passes the Complex tier
- **Run folder** (`benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/`): the 2026-09-26 harness with a header checker whose Complex tier no longer accepts a bare `High`

### Data Flow
Rubric to label scale to kernel. Skill file to Project file by hand. Run to collector to `export/benchmark/`, then header checker and structure review to the run README.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| DEPTH Complexity Assessment | Where the runtime rates complexity | Rubric added, Focus bullet points to it | Byte-identical block on both sides |
| Header label scale | Tells the runtime which labels exist | Complex added with ranges | `rg` for the old Low, Medium or High wording on both sides |
| Kernel | claude.ai kernel, residency-declared statements | One line after the declared delivery statement, H1 v0.7.0 | `run_residency.sh` |
| Playbook citations | Line references into the changed rule files | Remapped from HEAD to the working files | Sample counts before and after, validator |
| VIBE and Complex-tier scenarios | Graded contracts | Prose pillars pass, `Complex` named | Validator, `load_waves` |

Required inventories:
- Same-class producers: every file that states the complexity label scale, in `SKILL.md`, the format guides, the kernel and their Project twins.
- Consumers of changed symbols: playbook citations into `SKILL.md`, the kernel and the format guides.
- Matrix axes: runtime (skill, Project), tier (Medium, High, Complex), format (Markdown, JSON, YAML).
- Algorithm invariant: every rubric point comes from something the user stated, so an unstated need adds nothing.
<!-- /ANCHOR:affected-surfaces -->


---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Unit | Header checker | `run/check_framework_headers.py` on the old pack as a baseline |
| Integration | Skill, Project and playbook | `run_residency.sh`, `validate_parity.py prompt-improver`, playbook validator, `load_waves`, router fixtures |
| Manual | The 48 deliverables | Harness run, `check_run.py`, header check, independent structure review |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| `claude` CLI with `claude-sonnet-5` | External | Green | The rerun cannot measure the rubric |
| The 2026-09-26 run folder | Internal | Green | No baseline to compare the tier counts against |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: the rubric makes ratings worse on the rerun, or the parity or residency gate cannot pass in scope
- **Procedure**: `git revert` the commits in the Prompt Improver repo and in Barter, which restores the rules, the playbook and the 2026-09-26 pack together
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Phase 1 (Setup) ──────┐
                      ├──► Phase 2 (Core) ──► Phase 3 (Verify)
Phase 1.5 (Config) ───┘
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core, Config |
| Config | Setup | Core |
| Core | Setup, Config | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 15 minutes |
| Core Implementation | Med | 1 to 2 hours, plus about 40 minutes of run time |
| Verification | Med | 1 hour |
| **Total** | | **About 3 to 4 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] The 2026-09-26 deliverables stay in git history and in their run folder

### Rollback Procedure
1. `git revert` the commits in both repos
2. Rerun residency, parity, the playbook validator and the router fixtures

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
