---
title: "Implementation Summary: Deal Templates upgrades for Prompt Improver"
description: "Prompt Improver now routes on the user's own words, delivers the improved prompt before any question with every default as a numbered open item, and opens a claude.ai reply with a bare fence that copies exactly the prompt."
trigger_phrases:
  - "deal templates upgrades implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "006-deal-templates-upgrades"
    last_updated_at: "2026-10-18T19:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Implemented R1 to R3 and ran the static gates"
    next_safe_action: "Coordinator applies the residency resync pairs, then the operator reviews and commits"
    blockers:
      - "residency_check.py stays red until the reported resync pairs are applied to systems.py"
    key_files:
      - "AI Systems/Prompt Improver/sk-prompt-improver/SKILL.md"
      - "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
      - "AI Systems/Prompt Improver/benchmark/router/route_contract.py"
      - "AI Systems/Prompt Improver/benchmark/grader/deliverable_lint.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "006-deal-templates-upgrades"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary: Deal Templates upgrades for Prompt Improver

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 006-deal-templates-upgrades |
| **Completed** | 2026-10-18 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A prompt you paste no longer picks the mode, you get the improved prompt in the first reply, and on claude.ai the copy button copies the prompt and nothing else. Skill v1.0.1.0 and kernel v1.0.1 carry all three.

### Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit

The router sets your pasted prompt aside before it reads commands and keywords, so a text prompt about photo editing stays text work. When you send a prompt or a task, it ships right away, and each default it took follows as a numbered open item: a bold topic, a `Situation:` bullet and an `Open:` bullet. Only a message with no prompt and no task, or two conflicting mode commands, gets a question first. The A/B/C framework question is gone by the operator's approval. On claude.ai the reply opens with one bare code fence holding the prompt alone, so a JSON or YAML prompt you copy still parses.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-prompt-improver/SKILL.md` | Modified | Router, interaction rules, open items, Project override, rules; v1.0.1.0 |
| `sk-prompt-improver/references/` (4) and `assets/format-guide-*.md` (3) | Modified | Deliver-first flow, library default, bare-fence lines; third segment raised |
| `claude project/Custom Instructions.md` | Modified | Kernel v1.0.1 |
| `claude project/knowledge/` (7) | Modified | Hand-written mirrors |
| `benchmark/router/` | Modified | `strip_source_prompt()`, 32 fixtures, README |
| `benchmark/grader/` | Modified | Fence-contract linter, README, twin docstring |
| `benchmark/gates/rule_parity.py` | Modified | Comment only |
| `AGENTS.md`, `README.md`, `sk-prompt-improver/README.md`, `claude project/README.md`, `SYNC.md` | Modified | Doc sweep and dated note |
| `sk-prompt-improver/manual-testing-playbook/` | Modified | 78 scenarios and root at patch versions |
| `sk-prompt-improver/changelog/v1.0.1.0.md` | Created | Release notes |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Skill source first, then the oracle and fixtures, then the hand-written kernel and mirrors, then the linter, playbook and docs. Every check was static. Nothing was committed, staged or pushed in either repository.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Quoted spans count as the pasted prompt from three words up | A one-word platform name such as `"midjourney"` is the user's own routing signal |
| The lead-in rule runs only when no fence or quote was found | A lead-in followed by a quote would otherwise strip the user's own words after the quote |
| The CLI export keeps its header and divider | In the CLI the file and the chat are separate, so the header never enters the copied prompt |
| `*-canvas.md` scenario files keep their names | IDs and links stay stable across reports |
| No whole-reply examples or example lint | Not needed for R1 to R3, and a new knowledge file needs a new declared pair in a shared file |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_fixtures.sh` | PASSED 32/32 fixtures |
| `kernel_parity.py` | PASSED |
| `rule_parity.py` | PASSED 6 rules, 13 of 13 pairs |
| `pair_divergence.py prompt-improver` | PASSED 13 pairs |
| Playbook validator | PASS, 78 scenarios, 0 violations, 0 warnings |
| `validate_document.py` against HEAD | No changed doc worse than HEAD; root README improved |
| Linter on sample replies | Clean replies clean, old shape and malformed open items red; `lint_replies.py` exit 0 then 1 |
| `residency_check.py prompt-improver` | FAILED 28 findings across 21 statements, all resolved in simulation by 43 resync pairs |
| Kernel size | 27,104 bytes, up from 24,233 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Residency is red until the declaration is resynced.** The pairs are reported with their statement keys; editing `systems.py` was out of scope.
2. **No live run.** Whether a model follows deliver-first and the bare fence is proven only by the next playbook run.
3. **The CLI format guides still say JSON and YAML are files, never inline.** The Project line beside it explains the fence, but the core rule sentence was left as written.
<!-- /ANCHOR:limitations -->

---
