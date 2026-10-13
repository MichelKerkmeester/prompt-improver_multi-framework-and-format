---
title: "Acceptance Criteria: Prompt Improver example pack, playbook extension and scenario upgrade"
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
    packet_pointer: "004-pi-example-pack"
    last_updated_at: "2026-09-26T19:06:12Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "[SESSION-ID]"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Prompt Improver example pack, playbook extension and scenario upgrade

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 004-pi-example-pack
**Level:** 2
**Status:** Complete
**Date:** 2026-09-26
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the 18 snapshots, When a reviewer who wrote none of them scores each before and after on its routed rubric, Then each scores at or above its original, passes its gate, keeps every supplied fact and limit and adds no scope | Review table: 18 of 18, CLEAR 45 to 46 of 50 and VISUAL 54 to 55 of 60; PIR-001, SIR-002 and PIR-002 repaired | Met | - |
| AC-002 | REQ-002 | Given the extended playbook, When the validator and the runner's `load_playbook` and `load_waves` run, Then the validator passes with 30 scenarios and 0 violations and every ID sits in one wave | `PASS scenarios=30 categories=12 violations=0 warnings=0`; 30 IDs, 30 unique, none missing a wave, 2 turns each | Met | - |
| AC-003 | REQ-003 | Given a HEAD archive of the playbook, When the runner parses both trees, Then the 14 existing scenarios' turns are identical | 14 of 14 turn lists identical; 16 of 16 new turn lists identical to the brief | Met | - |
| AC-004 | REQ-004 | Given the 8 examples, When each is parsed and read against its own scenario's Turn 1 lines, Then each parses and would pass | 2 YAML parse with PyYAML; 8 of 8 PASS after the review turned SFM-003, SCR-002 and STX-005 from FAIL | Superseded | ADR-001 |
| AC-005 | REQ-005 | Given a synthetic run, When `run/selftest.py` runs, Then an edited export survives, `--force` restores it and the unguarded collector overwrites it | `selftest: all checks passed`, 7 of 7; the dry run over the real run prints 18 keep warnings | Met | - |
| AC-006 | REQ-006 | Given the run README, When sections 9 to 12 are read, Then they record the edit, the pack and the playbook change and name a rerun as the next step | README sections 9 to 12; next step 1 is the 30-scenario rerun | Met | - |
| AC-007 | REQ-002 | Given the commits, When `validate.sh --strict` and the parity gate run, Then both pass | `validate.sh --strict` RESULT: PASSED; `run_parity.sh` PASSED 13/13 on origin/main..HEAD (ba5f796, 9257494), exit 0 | Met | - |
| AC-008 | REQ-007 | Given the playbook at root 1.2.0.0, When the validator and the runner's `load_waves` run, Then the validator passes with 78 scenarios and 0 violations and every ID sits in one wave | `validate-playbook-package.cjs --repo-root <repo> --package <playbook>`: PASS scenarios=78 categories=14 violations=0 warnings=0, exit 0; `load_waves` 78 IDs, none in two wave rows, the 48 in wave 6 | Met | - |
| AC-009 | REQ-008 | Given the framework-coverage run folder, When `run/check_run.py . --model claude-sonnet-5` runs, Then it exits 0 across all 48 SFW and PFW scenarios | `48 scenarios, 48 declared turns, 48 event streams read, 0 finding(s), expected model claude-sonnet-5`, exit 0 | Met | - |
| AC-010 | REQ-007 | Given `export/benchmark/`, When its directories are listed, Then it holds exactly `skill/` and `claude project/` | `ls -A export/benchmark` lists `claude project` and `skill` only | Met | - |
| AC-011 | REQ-009 | Given the 48 collected deliverables, When `run/check_framework_headers.py` reads each header, Then each names its target framework, and each tier miss after one rerun is listed in the run README | 48 of 48 name their target framework and match their format; the 27 tier misses after one rerun are listed in README section 4 and counted in section 2 | Met | - |
| AC-012 | REQ-010 | Given the run README, When its per-ID table is read, Then it has one row per SFW and PFW ID with framework, tier, header check, structure verdict and reported score | README section 4: 48 rows with framework, tier, complexity per attempt, header, tier check, structure, facts and reported score | Met | - |
| AC-013 | REQ-010 | Given the commits, When `validate.sh --strict` and the parity gate run, Then both pass | `validate.sh --strict` RESULT: PASSED, 0 errors and 0 warnings; commits Prompt Improver 02dbfe3 and Barter 5f711610, 390 files each; `validate_parity.py prompt-improver` PASSED 13/13 on origin/main..HEAD, exit 0 | Met | - |

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

The first pass is committed and pushed. The operator then dropped the agent-written examples (ADR-001 supersedes AC-004) and asked for a framework-coverage run, which is committed as Prompt Improver 02dbfe3 and Barter 5f711610. Every row is Met or Superseded, and both commits were pushed on the operator's go-ahead on 2026-09-27.
<!-- /ANCHOR:closure -->
