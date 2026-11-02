---
title: "Implementation Plan: Prompt Improver example pack, playbook extension and scenario upgrade"
description: "Parallel Opus agents tighten the 14 existing scenarios, write 16 new ones, raise the quality of the 18 exports and write 8 examples through the skill. Independent reviewers check every export and example, and a selftest proves the collector keeps hand edits."
trigger_phrases:
  - "pi example pack plan"
  - "prompt improver playbook extension plan"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Prompt Improver example pack, playbook extension and scenario upgrade

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown and JSON or YAML prompts, Markdown playbook, Python (collector, selftest) |
| **Framework** | Prompt Improver skill, its manual testing playbook and its run tooling |
| **Storage** | None |
| **Testing** | Playbook validator, runner parse, rubric reviews, format parsing, collector selftest |

### Overview
Seven Opus agents work in parallel from one shared brief that fixes the new inputs and the rule wordings. Two independent reviewers then score and check the exports and the new material against snapshots and rule sources, and the collector gains an edit guard with a selftest. No scenario runs.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [ ] All acceptance criteria met
- [ ] Tests passing (if applicable)
- [ ] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Shared brief first, parallel writers second, independent review third

### Key Components
- **Shared brief** (`scratch/shared-brief.md`): the new scenarios' exact inputs and the canonical rule wordings every writer uses
- **Snapshots** (`scratch/before/`, `scratch/before-playbook/`): the originals each review compares against
- **Collector guard** (`run/collect_exports.py`, `run/selftest.py`): keeps a hand-edited export unless `--force` is given

### Data Flow
Brief to writers to reviewers to repair. Snapshot to diff to rubric score.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Playbook root | Scenario index the runner parses | 16 new blocks, waves, counts, version 1.1.0.0 | Validator, `load_playbook`, `load_waves` |
| 14 existing scenarios | Graded contracts | Wording tightened, inputs frozen | Byte check of every input against the snapshot |
| 18 exports | Run deliverables | Quality raised in place | Rubric review against the snapshot |
| `run/collect_exports.py` | Rebuilds `export/benchmark` | Edit guard | `run/selftest.py` with a negative control |

Required inventories:
- Same-class producers: every scenario file that states the Canvas stand-in, the summary band or the question rule.
- Consumers of changed symbols: `run/playbook_runner.py` reads the root blocks and waves.
- Matrix axes: mode (8 new), format (Markdown, JSON, YAML), runtime (skill, Project).
- Algorithm invariant: a scenario's Prompt, table Exact Prompt and root Prompt match character for character.
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
| Unit | Collector guard | `run/selftest.py`, with the unguarded collector as control |
| Integration | Playbook and runner | Validator, `load_playbook` and `load_waves` |
| Manual | Exports and examples | Independent rubric reviews against snapshots |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Prompt Improver `d473b93` rules | Internal | Green | None, they are committed |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: a review finds an export or scenario worse than its original, or the validator fails in a way that cannot be repaired in scope
- **Procedure**: restore the file from `scratch/before/` or `scratch/before-playbook/`, or `git revert` the commits in both repos
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
| Setup | Low | 20 minutes |
| Core Implementation | High | 2 to 3 hours, seven agents in parallel |
| Verification | Med | 1 hour |
| **Total** | | **About 5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Snapshot of the 18 exports and the 15 playbook files in `scratch/`

### Rollback Procedure
1. `git revert` the phase commits in both repos
2. Rerun the playbook validator and the collector selftest

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
