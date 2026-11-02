---
title: "Acceptance Criteria: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "deal templates upgrades acceptance criteria"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "006-deal-templates-upgrades"
    last_updated_at: "2026-10-18T19:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Marked every criterion with observed evidence"
    next_safe_action: "Coordinator applies the resync pairs"
    blockers: []
    key_files:
      - "AI Systems/Prompt Improver/benchmark/router/fixtures.json"
      - "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "006-deal-templates-upgrades"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Deal Templates upgrades: user-word routing, deliver-first open items, prompt-only copy unit

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 006-deal-templates-upgrades
**Level:** 2
**Status:** Complete
**Date:** 2026-10-18
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given a pasted prompt about photo editing or a video clip transcript, When the router runs, Then the intent is TEXT, while a one-word quoted platform and `$image` stay IMAGE | `run_fixtures.sh` printed `PASSED 32/32 fixtures`; the oracle moved the photo probe from IMAGE and the clip probe from VIDEO to TEXT | Met | - |
| AC-002 | REQ-001 | Given the skill pseudocode and the kernel Router Code, When parity runs, Then they are equal minus comments | `kernel_parity.py` printed `PASSED kernel router parity` | Met | - |
| AC-003 | REQ-002 | Given a request with a prompt, When the contract is read, Then it delivers first and lists defaults as numbered open items with `Situation:` and `Open:` bullets and no blank lines | `SKILL.md` Open Items section and kernel Section 6; the linter flags a blank line inside an item | Met | - |
| AC-004 | REQ-003 | Given a claude.ai reply, When it is linted, Then it must open with an untagged fence holding only the prompt | `deliverable_lint.py` clean on the good samples, red on the old shape; `lint_replies.py` exit 0 then 1 | Met | - |
| AC-005 | REQ-004 | Given the changed docs and playbook, When the validators run, Then nothing is worse than HEAD | Playbook validator PASS with 0 violations; `validate_document.py` no doc worse than HEAD; grep sweep left only historical reports, spec history and deliberate negatives | Met | - |
| AC-006 | REQ-005 | Given the changed kernel and mirror text, When residency runs, Then every failing statement has a resync pair that makes it present again | 43 pairs over 21 statement keys, each unique across `systems.py`, simulated as present in the current files | Met | - |
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

The router fixtures, parity gates, linter samples and the resync simulation carried the packet. Whole-reply examples, an example lint and the success statistics were left out by scope.
<!-- /ANCHOR:closure -->
