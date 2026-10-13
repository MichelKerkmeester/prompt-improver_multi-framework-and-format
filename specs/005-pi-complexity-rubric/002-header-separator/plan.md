---
title: "Implementation Plan: Prompt Improver header divider"
description: "Edit the layout rule at its source in the skill, mirror it by hand into the kernel and the Project format guides, then bring the playbook, the linter and the 66 benchmark exports in line, and record the release as skill 0.6.2 and kernel v0.7.1."
trigger_phrases:
  - "header divider plan"
  - "prompt improver export layout plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Prompt Improver header divider

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown rule files, Python 3 linter, Markdown/JSON/YAML exports |
| **Framework** | Prompt Improver skill and its hand-written Claude Project mirror |
| **Storage** | None |
| **Testing** | `run_residency.sh`, `validate_parity.py`, router fixtures, playbook validator, `deliverable_lint.py` |

### Overview
The rule that a file holds "a single-line header plus enhanced prompt content only" changes to name the divider: header line, blank line, `---`, blank line, prompt. It is edited in place in `SKILL.md`, so no line moves there, and in the format guides, where each example gains two lines. The kernel and the Project guides get the same change by hand, the playbook and the linter follow, and the exports are edited by a script that inserts the divider after line 1 and checks nothing else moved.
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
- [ ] Residency, parity, router fixtures and playbook validator pass
- [ ] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source first, mirror by hand, per the manual parity method in `SYNC.md`.

### Key Components
- **Skill rules**: `SKILL.md` lines 412, 499, 558 and 561, and the Mandatory Header Format section of each format guide
- **Project mirror**: kernel rule 7 and the DELIVERY PROTOCOL template, and the three knowledge format guides
- **Checks**: `deliverable_lint.py`, which already strips the attestation at the last `---` and now also reads the divider under the header

### Data Flow
A deliverable is written as header, divider, prompt. On the Project it is followed by the attestation divider and line. The linter reads the first non-blank line after the `Mode:` line and expects `---`.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `SKILL.md` layout rules | States the file structure | Edited in place to name the divider | Line count unchanged |
| Skill and Project format guides | Header section and examples | Divider added to the rule and every example with a header | `rg` for a header line followed by a non-divider line |
| Kernel | Rule 7 and the block template | Divider named and shown | `run_residency.sh` |
| `deliverable_lint.py` | Only tool that splits header from body | New check, leading divider stripped | Run on a sample with and without the divider |
| Playbook | Describes the layout, cites guide lines | Wording and citations updated | Validator, citation spot check |
| Benchmark exports | The example pack | Divider inserted by script | Line 1 to 4 scan, text diff equal apart from the insert |

Required inventories:
- Same-class producers: every file stating "single-line header", "header plus", "only header" or "header and the prompt" in both packages.
- Consumers of changed symbols: playbook citations into the changed guides, `deliverable_lint.py`, the 2026-09-27 run's `check_framework_headers.py`.
- Matrix axes: runtime (skill, Project) by format (Markdown, JSON, YAML).
- Algorithm invariant: the divider is the first `---` after the header, so a `---` inside a prompt never splits it.
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
| Gate | Kernel residency, skill-to-Project parity | `run_residency.sh prompt-improver`, `validate_parity.py prompt-improver` |
| Unit | The linter's divider check | `deliverable_lint.py` on two sample files |
| Structural | 66 exports, JSON and YAML payloads | A line scan and `json.loads` or a YAML loader on the payload below the divider |
| Package | Playbook | `validate-playbook-package.cjs`, router fixtures |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 001 committed | Internal | Green | Edits would mix with unrecorded work |
| Sync Loop gates | Internal | Green | No parity or residency evidence |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: a gate fails after commit, or the operator rejects the layout
- **Procedure**: `git revert` the Prompt Improver and Barter commits, then rerun residency, parity and the playbook validator
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
| Core Implementation | Med | 1 to 2 hours |
| Verification | Low | 30 minutes |
| **Total** | | **About 2 to 3 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] The exports before the edit stay in git history

### Rollback Procedure
1. `git revert` the commits in both repos
2. Rerun residency, parity, the playbook validator and the router fixtures

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
