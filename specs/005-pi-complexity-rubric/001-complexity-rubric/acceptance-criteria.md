---
title: "Acceptance Criteria: Prompt Improver complexity rubric and prose-friendly VIBE scenarios"
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
    packet_pointer: "005-pi-complexity-rubric/001-complexity-rubric"
    last_updated_at: "2026-09-27T05:35:23Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the acceptance criteria for this packet"
    next_safe_action: "Meet, waive or supersede the open criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "[SESSION-ID]"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Prompt Improver complexity rubric and prose-friendly VIBE scenarios

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 005-pi-complexity-rubric
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
| AC-001 | REQ-001 | Given the skill and Project DEPTH files, When the Complexity Rubric block is extracted from each, from its heading to the Bands line, Then the two are byte-identical and carry the five dimensions, the rating rule and the four bands | `cmp` of the two 19-line blocks reports no difference; `references/depth-framework.md` lines 147-165, Project lines 134-152 | Met | - |
| AC-002 | REQ-002 | Given the skill and the Project, When every complexity label scale is searched, Then each names Low, Medium, High and Complex with their ranges and points to the rubric, and no band table calls a rating below 9 Complex | Eight files carry `Complex (9 to 10)` with the rubric pointer; the JSON and YAML structure tiers read 1 to 3, 4 to 6 and 7 to 10 on both sides | Met | - |
| AC-003 | REQ-003 | Given the commits, When the residency check and `validate_parity.py prompt-improver` run, Then both pass, and the kernel H1, `SKILL.md` version and README claims agree | Residency PASSED, exit 0; `validate_parity.py prompt-improver` PASSED 13/13 on 4da1a1a, exit 0, reporting kernel v0.7.0 and Skill v0.6.0 live with README claims 0.7.0 and 0.6.0 | Met | - |
| AC-004 | REQ-004 | Given the four VIBE and VIBE-MP scenarios, When their Body, Pass/fail and step text is read and the validator runs, Then a pillar written as prose the operator can map to it passes, and the validator passes with 78 scenarios | The Body rule cites the natural-prose line and accepts a heading, a label or a mappable passage; validator PASS scenarios=78 categories=14 violations=0, exit 0 | Met | - |
| AC-005 | REQ-005 | Given the 2026-09-27 run folder, When `run/check_run.py . --model claude-sonnet-5` runs, Then it exits 0 across the 48 | `48 scenarios, 48 declared turns, 48 event streams read, 0 finding(s), expected model claude-sonnet-5`, exit 0 | Met | - |
| AC-006 | REQ-006 | Given the run README, When its per-ID table and findings are read, Then it has one row per ID with the new and old rating, tier check, structure verdict and reported score, and counts tier hits for both runs under one checker | README section 4, 48 rows with both ratings, the blind recount, tier check, structure, facts and score; section 2 counts 25 in tier against 13 first attempts and 17 after rerun, all under `run/check_framework_headers.py` | Met | - |
| AC-007 | REQ-007 | Given `export/benchmark/`, When it is listed, Then it holds the rerun's 48 deliverables and the 18 core exports, in `skill/` and `claude project/` only | `ls -A export/benchmark` lists `claude project` and `skill`; 33 files in each, 24 SFW or PFW and 9 core; collector dry run 0 keep warnings | Met | - |
| AC-008 | REQ-003 | Given the packet, When `validate.sh --strict` runs, Then it prints `RESULT: PASSED` | `validate.sh AI Systems/Prompt Improver/specs/005-pi-complexity-rubric --strict`: RESULT: PASSED, 0 errors, 0 warnings | Met | - |
| AC-009 | REQ-008 | Given the six creative pairs, When their tier lines, the root tier table and the validator are read, Then each targets the blind recount's band and the validator passes with 78 scenarios | SFW-019, SFW-021 and SFW-022 Low, SFW-020 and SFW-023 Medium, SFW-024 High, twins alike; root Low row; validator PASS scenarios=78 violations=0; runner loads 78 per side | Met | - |
| AC-010 | REQ-009 | Given the files each runtime reads, When they are searched for the company name and the version claims are read, Then none names it and every claim says skill 0.6.1 with kernel v0.7.0 | `grep -i barter` over `AGENTS.md`, `SKILL.md`, references, assets, kernel and knowledge finds nothing; `validate_parity.py prompt-improver` PASSED 13/13 on 4f55b66, exit 0, reporting kernel v0.7.0 and Skill v0.6.1 live with README claims 0.7.0 and 0.6.1 | Met | - |
| AC-011 | REQ-010 | Given the run folder, When `results.csv`, `grading-notes.md` and `check_report.sh` are read, Then there is one graded row per ID with its evidence, and the report check's twin disagreements match the adjudicated ones | 48 rows, 48 unique IDs, 6 PASS and 42 FAIL; `grading-notes.md` VALID with a section per ID; `check_report.sh` exit 2 with FW-001, FW-004, FW-006 and FW-009, the four adjudicated in section 5 | Met | - |

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

The rubric, its mirror, the playbook changes and the rerun are committed as Prompt Improver 4da1a1a and Barter ccd0425c, and every row is Met. Both were pushed on the operator's go-ahead on 2026-09-27. After the push the operator had the creative pairs re-tiered to the blind recount (AC-009), committed separately as Prompt Improver 13bdf85 and Barter 5b5c51d6 and pushed on the operator's go-ahead. The grading, the name removal as skill 0.6.1 and the wording trial are committed as Prompt Improver 4f55b66 and Barter ff3e5526 (AC-010, AC-011), and pushed on the operator's later go-ahead. The target-model reading and the path-first habit are recorded in the run README for the operator to decide.
<!-- /ANCHOR:closure -->
