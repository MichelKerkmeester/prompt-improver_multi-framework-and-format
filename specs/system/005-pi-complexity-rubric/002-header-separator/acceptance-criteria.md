---
title: "Acceptance Criteria: Prompt Improver header divider"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "acceptance criteria"
  - "closure gate"
  - "ac traceability"
  - "waiver adr"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "005-pi-complexity-rubric/002-header-separator"
    last_updated_at: "2026-09-27T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met all seven criteria on edecbed and 07ca0122"
    next_safe_action: "None; a live run under skill 0.6.2 is the next evidence"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "005-pi-complexity-rubric-002"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Prompt Improver header divider

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 005-pi-complexity-rubric/002-header-separator
**Level:** 2
**Status:** Complete
**Date:** 2026-09-27
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the skill, When a reader looks up the file layout, Then it names the header, a blank line, `---`, a blank line and the prompt | `sk-prompt-improver/SKILL.md` lines 412, 499, 558 and 561; each skill format guide's Mandatory Header Format block | Met | - |
| AC-002 | REQ-002 | Given the Project, When the kernel and the Project guides are read, Then they state the same layout and the DELIVERY PROTOCOL template shows it | `Custom Instructions.md` line 320 and lines 372-379; twin diff of changed lines identical; `validate_parity.py prompt-improver` PASSED 13/13 on edecbed | Met | - |
| AC-003 | REQ-003 | Given a JSON or YAML export, When the payload below the divider is parsed, Then it parses exactly as the payload did before the edit | Export scan: 16 of 18 parse before and after, PFW-005 and PFW-007 failing in both, a 001 finding | Met | - |
| AC-004 | REQ-004 | Given the 66 exports, When lines 1 to 4 are read, Then each is a `Mode:` header, a blank line, `---` and a blank line, and nothing else changed | Scan: 66 with the divider, 0 without; `git diff --numstat`: +136 -0 | Met | - |
| AC-005 | REQ-005 | Given the playbook, When its scenarios and citations are read, Then they describe the divider and point at the lines they name | Validator PASS, 78 scenarios, 0 violations; 344 named and 13 bare citations moved; root Advisory lists the divider and the six format-lock scenarios fail on it | Met | - |
| AC-006 | REQ-006 | Given a block without the divider, When `deliverable_lint.py` reads it, Then it reports `header_divider_missing` and a block with the divider stays clean | Samples: good exit 0, missing and no-blank exit 1; 33 Project exports clean | Met | - |
| AC-007 | REQ-007 | Given the release, When the version records are read, Then skill 0.6.2 and kernel v0.7.1 agree everywhere and both run READMEs record the edit | Parity: README claims 0.7.1 and 0.6.2 live; `changelog/v0.6.2.0.md`; `SYNC.md` last note; run README sections 6 and 9 | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

All seven criteria are met on Prompt Improver edecbed and Barter 07ca0122, with residency and parity passing on those commits. The header's fields, the `Platform:` field and a rerun were left out, as the operator scoped it.
<!-- /ANCHOR:closure -->
