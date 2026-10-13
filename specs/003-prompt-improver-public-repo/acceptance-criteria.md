---
title: "Acceptance Criteria: Publish Prompt Improver as its own public repo"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "acceptance criteria"
  - "prompt improver public repo closure"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "003-prompt-improver-public-repo"
    last_updated_at: "2026-09-24T12:00:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Verified the follow-up criterion on 8b9714c and monorepo 6f49fabb"
    next_safe_action: "None required. Follow-ups are listed in implementation-summary.md"
    blockers: []
    key_files:
      - "AI Systems/Prompt Improver/README.md"
      - "AI Systems/Prompt Improver/.gitignore"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "57a20eaa-0fc8-4c05-99d5-39e79963f536"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "README placement: a real root README, the skill README unchanged"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Publish Prompt Improver as its own public repo

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 003-prompt-improver-public-repo
**Level:** 2
**Status:** Complete
**Date:** 2026-09-24
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the public repo, When GitHub renders its root, Then it shows a regular `README.md` in the Skilled style whose local links all resolve | `gh api repos/MichelKerkmeester/prompt-improver_multi-framework-and-format/readme` returns `README.md` opening `# Prompt Improver - Multi-Framework & Format`. Link scan: 17 local links, 0 broken | Met | - |
| AC-002 | REQ-002 | Given the `.gitignore`, When `export/` holds prompts, Then only `.gitkeep` and `export/benchmark/` are tracked | `git check-ignore -v` names `.gitignore:5` for export entries. The contents API lists `.gitkeep` under `export/` | Met | - |
| AC-003 | REQ-003 | Given the pushed tree, When symlinks are listed, Then none exist | `git ls-files -s` shows 0 entries with mode `120000` | Met | - |
| AC-004 | REQ-004 | Given the staged set, When scanned, Then it holds no credentials | Pattern scan for tokens, keys and `.env` values returned no hits | Met | - |
| AC-005 | REQ-005 | Given the README counts, When compared with the files, Then they match | 11 frameworks, 13 knowledge files, 7 assets, 6 references and 25 fixtures, each counted on disk or from command output. Perspective names, confidence bands and platform lists copied from `SKILL.md`, `depth-framework.md`, `image-mode.md` and `video-mode.md` | Met | - |
| AC-006 | REQ-006 | Given the README, When validated, Then it passes sk-doc and HVR | `validate_document.py` VALID with 0 issues. `hvr_lint.py` clean. No em dash, en dash, prose semicolon or Oxford comma | Met | - |
| AC-007 | REQ-007 | Given the commit, When inspected, Then it follows sk-git | `542207e feat(prompt-improver): add the skill, Project package and front-page README`, staged by explicit paths, hooks ran, no bypass | Met | - |
| AC-008 | Follow-up | Given the skill README, When searched for the retired sync compiler, Then it no longer names it as the mirror writer | Section 8 and the related documents rows rewritten. sk-doc 0 issues, HVR clean. Pushed as `8b9714c` and monorepo `6f49fabb` | Met | - |

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

All eight criteria are met. The first seven hold on `542207e`, the follow-up criterion on `8b9714c` and monorepo `6f49fabb`. The monorepo carries the front page, the ignore rules and the `LICENSE` as `ee3536c2`, and the benchmark parity scripts still need the monorepo.
<!-- /ANCHOR:closure -->
