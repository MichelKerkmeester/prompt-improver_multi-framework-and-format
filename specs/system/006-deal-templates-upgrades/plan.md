---
title: "Implementation Plan: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit"
description: "Change the skill source first, then the router oracle and fixtures, then the hand-written kernel and knowledge mirrors, then the linter, playbook and docs, and prove each step with the system's own static gates."
trigger_phrases:
  - "deal templates upgrades plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill and kernel, Python 3 router oracle and linter |
| **Framework** | None |
| **Storage** | None |
| **Testing** | `run_fixtures.sh`, `kernel_parity.py`, `rule_parity.py`, `pair_divergence.py`, the playbook validator, `validate_document.py` |

### Overview
The skill source changes first: the router gains `strip_source_prompt()`, the interaction rules move to deliver-first with open items and the Project override moves to a bare fence. The oracle and fixtures pin the routing, the kernel and seven knowledge files are hand-written from the skill, and the linter, playbook and docs follow.
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
Source and hand-written mirror: `sk-prompt-improver/` is the source, `claude project/` mirrors it by hand.

### Key Components
- **Router**: the skill pseudocode, `route_contract.py` and the kernel Router Code, held equal by `kernel_parity.py`
- **Delivery contract**: CLI export-first in `AGENTS.md` and `SKILL.md`, Project bare fence in the kernel Section 6
- **Reply linter**: `deliverable_lint.py`, which checks a captured Project reply against the fence contract

### Data Flow
User message, then `strip_source_prompt()`, then command and keyword detection on what is left, then the bound mode, then delivery with open items.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Skill and kernel router | Choose the mode | Update | `run_fixtures.sh`, `kernel_parity.py` |
| Interactive Mode source and mirror | Question flow | Update | Residency simulation, pair divergence |
| Format guides and mirrors | Project delivery lines | Update | Pair divergence, rule parity |
| Reply linter | Grades captured replies | Update | Sample replies in scratch |
| Playbook | Grades live runs | Update | Playbook validator |

Required inventories:
- Same-class producers: `grep -rn "Canvas\|attestation\|\[Assumes" --include='*.md' --include='*.py'` across the system, reports and spec history excluded.
- Consumers of changed symbols: `strip_source_prompt` appears in the skill, the kernel and `route_contract.py` only.
- Matrix axes: quote length (one, two, three or more words), fence present, lead-in present, command present.
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
| Unit | Route oracle on 32 fixtures, linter on four sample replies | `run_fixtures.sh`, `deliverable_lint.py`, `lint_replies.py` |
| Integration | Skill and kernel parity, rule parity, pair divergence, residency simulation | `kernel_parity.py`, `rule_parity.py`, `pair_divergence.py`, `residency_check.py` |
| Manual | Live claude.ai and CLI runs | Not run: no model runs in this packet |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| `systems.py` residency declarations | Internal, shared | Yellow | Residency stays red until the reported pairs are applied |
| Live claude.ai Project upload | External, manual | Yellow | Live users keep the old kernel until it is pasted again |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: The operator rejects the behavior change, or a live run shows the fence contract breaking a workflow
- **Procedure**: Nothing is committed; `git -C "AI Systems/Prompt Improver" checkout -- .` after review restores HEAD, and the new changelog and spec folder are removed by hand
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Phase 1 (Setup) ──► Phase 2 (Source, oracle, mirrors, docs) ──► Phase 3 (Verify)
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core |
| Core | Setup | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | Under 1 hour |
| Core Implementation | High | Most of a session |
| Verification | Med | 1 to 2 hours |
| **Total** | | **One long session** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created (if data changes): HEAD holds the prior state, nothing committed
- [x] Feature flag configured: not applicable
- [x] Monitoring alerts set: not applicable

### Rollback Procedure
1. Leave the live claude.ai Project on the old kernel
2. Restore the changed files from HEAD after the operator's review
3. Rerun `run_fixtures.sh` and `kernel_parity.py`
4. Tell the coordinator not to apply the resync pairs

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
