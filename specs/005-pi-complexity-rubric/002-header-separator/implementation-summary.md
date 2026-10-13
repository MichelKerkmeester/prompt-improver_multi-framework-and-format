---
title: "Implementation Summary: Prompt Improver header divider"
description: "Every Prompt Improver file and Deliverable Block now keeps its Mode header apart from the prompt with a blank line, a --- divider and a blank line, on the skill, in the Project, in the playbook, in the linter and in the 66 benchmark exports."
trigger_phrases:
  - "header divider summary"
  - "prompt improver 0.6.2"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "005-pi-complexity-rubric/002-header-separator"
    last_updated_at: "2026-09-27T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Committed and pushed edecbed and 07ca0122"
    next_safe_action: "None; a Claude run under skill 0.6.3 is the next evidence"
    blockers: []
    key_files:
      - "AI Systems/Prompt Improver/sk-prompt-improver/SKILL.md"
      - "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
      - "AI Systems/Prompt Improver/benchmark/grader/deliverable_lint.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "005-pi-complexity-rubric-002"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary: Prompt Improver header divider

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 002-header-separator |
| **Completed** | 2026-09-27 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A Prompt Improver deliverable now reads as two things, not one. The `Mode:` line sits on top, a `---` divider follows after a blank line, and the prompt starts after another blank line, so copying the prompt no longer drags the header along.

### Phase 2: header-separator

The rule lives in `SKILL.md` and the three format guides, and the Project states it in kernel rule 7 and the DELIVERY PROTOCOL template. A Project block therefore carries two `---` lines: one under the header and one above the attestation, with the format lock covering the prompt between them. The linter reports a missing divider, the playbook treats it as advisory except in the six format-lock scenarios that exist to test delivery shape, and all 66 benchmark exports carry it.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-prompt-improver/SKILL.md` | Modified | Format lock, rule 23 and Output File Rules name the divider, in place; version 0.6.2 |
| `sk-prompt-improver/assets/format-guide-{markdown,json,yaml}.md` | Modified | Header block, allowed table, examples and checklists |
| `claude project/knowledge/Prompt Improver - Format Guide *.md` | Modified | Same edits as the skill twins |
| `claude project/Custom Instructions.md` | Modified | Rule 7, template, framing sentence, H1 v0.7.1 |
| `z — Claude Project Sync Loop/systems.py` | Modified | Three declared statements resynced |
| `benchmark/grader/deliverable_lint.py` and `README.md` | Modified | `header_divider_missing`, leading divider stripped before the attestation split |
| `sk-prompt-improver/manual-testing-playbook/` | Modified | Advisory rule, six format-lock contracts, layout wording, citations |
| `export/benchmark/skill/`, `export/benchmark/claude project/` | Modified | 66 files with the divider |
| Run READMEs, changelog, `SYNC.md`, READMEs, `description.json` | Created, Modified | Records and version claims |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The skill rules changed first, then the Project mirror by hand, then the checks and the exports, each step with its own check. Prompt Improver commit `edecbed` is pushed. Barter commit `07ca0122` carries the same 158 paths plus `systems.py` and is pushed. The pre-push route gate reads the shared Code_Environment tree and found the sk-doc manifest stale from another session's uncommitted edits, so the operator approved a one-push override.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The divider is advisory in the playbook, blocking only in the six format-lock scenarios | The root's Defect severity section lets a delivery-shape preference fail only scenarios that exist to test delivery shape |
| The blank line above `---` is part of the rule | Without it Markdown reads the header as a heading and the divider disappears |
| Framework scenarios parse "the payload below the header and its divider" | A JSON parse of everything below the header would include `---` and fail a correct export |
| Declared statements resynced with `resync_statement.py` | It is the gate's own tool for an intended change to declared text; the 56 stale keys already in the moved lists show those lists are historical |
| Twelve bare kernel citations moved four lines, not two | They still pointed where the chat bullets sat before phase 001 inserted its line |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_residency.sh prompt-improver` on 07ca0122 | PASSED, every declared statement owned and placed |
| `validate_parity.py prompt-improver` | PASSED 13/13, kernel v0.7.1 and Skill v0.6.2 live |
| Router fixtures | PASSED 25/25 |
| Playbook validator | PASS, 78 scenarios, 0 violations |
| Export scan | 66 of 66 with the divider, diff +136 -0, parse results equal to baseline |
| `deliverable_lint.py` | Samples behave, 33 Project exports clean |
| 2026-09-27 header checker | Same output before and after the edit |
| Collector dry runs | 48 and 18 keep warnings, exit 0, nothing written |
| Doc checks | Issue counts equal to HEAD on every changed README |
| README line 380 follow-up | Names Complex 9 to 10; e8a1f25 and 3c4c599d pushed |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **One model checked live.** DeepSeek V4.1 Flash wrote the divider in every deliverable with a header, 21 skill files and 18 Project blocks (`benchmark/reports/2026-09-28--header-divider--deepseek-v4.1-flash-high/`). It dropped the whole framing once, when a user asked for "valid JSON only", which skill 0.6.3 now covers in the JSON and YAML guides. Claude has not run under the rule yet.
<!-- /ANCHOR:limitations -->

---
