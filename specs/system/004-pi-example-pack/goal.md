---
title: "Goal: Prompt Improver example pack, framework coverage and playbook upgrade"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "004-pi-example-pack"
    last_updated_at: "2026-09-27T00:40:00Z"
    last_updated_by: "claude-code"
    recent_action: "Pushed the framework-coverage run in Prompt Improver and Barter"
    next_safe_action: "None for this goal; the operator decides the two open questions in the run README"
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
# Goal: Prompt Improver example pack, framework coverage and playbook upgrade

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fill Prompt Improver's `export/benchmark/` with runtime-produced prompts that show medium, high and complex work organised by each framework in the skill's library, backed by playbook scenarios that grade them, without changing any skill, kernel or knowledge rule.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Prompt quality is the aim. No change to `SKILL.md`, `AGENTS.md`, `references/`, `assets/`, the kernel or knowledge |
| D2 | `export/benchmark/` holds only `skill/` and `claude project/`, as Product Owner's does. Deliverables come from real runs, never agent-written examples |
| D3 | 24 pairs SFW-001 to SFW-024 with PFW twins: RCAF, COSTAR, CIDI, TIDD-EC, CRISPE and CRAFT at Medium (5 to 6), High (7 to 8) and Complex (9 to 10), plus FRAME and MOTION at High and Complex, VIBE at High and VIBE-MP at Complex. One turn each, inputs fixed in `AI Systems/Prompt Improver/specs/004-pi-example-pack/scratch/framework-brief.md`, playbook root 1.2.0.0 |
| D4 | Run from `AI Systems/Prompt Improver/benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/`: `python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-sonnet-5 --effort xhigh --ids <48 IDs> --jobs 4`, then collect with its `run/collect_exports.py` into `export/benchmark` |
| D5 | A deliverable whose header names another framework or a complexity outside its tier gets one rerun. A second miss is recorded, never hand-edited |
| D6 | Stage explicit paths, commit in the Prompt Improver repo and Barter with no attribution line, never reset or stash. Push only on the operator's go-ahead, Barter through `gh auth switch --user michelkerkmeester-barter` and back |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `validate-playbook-package.cjs` on `sk-prompt-improver/manual-testing-playbook` prints PASS with scenarios=78 and violations=0, and the runner's `load_waves` puts every ID in one wave
- [x] `run/check_run.py --model claude-sonnet-5` in the framework-coverage run folder exits 0 across all 48 SFW and PFW scenarios
- [x] `export/benchmark/` holds exactly two directories, `skill/` and `claude project/`
- [x] Each of the 48 SFW and PFW IDs has a collected deliverable whose `Framework:` header names its target framework, or the run folder's README lists it as a miss after one rerun
- [x] The run folder's `README.md` has one row per SFW and PFW ID giving framework, tier, header check, reviewer verdict on framework structure and score
- [x] `validate.sh --strict` on `AI Systems/Prompt Improver/specs/004-pi-example-pack` prints `RESULT: PASSED`
- [x] The work is committed in the Prompt Improver repo and Barter, and pushed after the operator's go-ahead
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| First pass: 18 exports, 30 scenarios, collector guard | Pushed | 18 of 18 at or above the original on review; validator PASS at 30; selftest 7 of 7; Prompt Improver d473b93..9257494, Barter 8923ad82..3ae67ce0 |
| Agent-written examples | Dropped, uncommitted | Operator 2026-09-26: only `skill/` and `claude project/`, drop all eight. Deleted from `skill/`; git keeps them under `export/benchmark/examples/` at 9257494 |
| Framework-coverage scenarios | Done, uncommitted | 48 files in `skill-framework-coverage/` and `project-framework-coverage/`, root 1.2.0.0; validator PASS scenarios=78 categories=14 violations=0; 48 new IDs in wave 6 with 1 turn each; 0 mismatches against `scratch/framework-brief.json` |
| Pilot | Done | SFW-001, SFW-003, SFW-023 and PFW-003 all delivered in one turn with no question; frameworks RCAF, RCAF, VIBE, RCAF all on target; complexity 3/10, 7/10 and 8/10 fall below their tiers (SFW-001, SFW-003, PFW-003), SFW-023 High matches |
| Main run | Done | 44 of 44 ok; with the pilot, 48 scenarios; manifest narrowed 78 to 48; `check_run.py --model claude-sonnet-5` read 48 event streams, 0 findings, exit 0 |
| Collection | Done | 24 skill and 24 Project deliverables; PFW-007's header sat above its fence, so the run's collector gained a `framed()` step that keeps a header above and an attestation below a fence; it changes only PFW-007 and leaves the 2026-09-25 run's collection byte-identical |
| Header check | Done | `run/check_framework_headers.py` in the run folder (a copy of `scratch/check_framework_headers.py` that reads `run/framework-targets.json` and also checks the format): 48 of 48 name their target framework and match their format; 16 in tier on the first attempt, 5 more after the rerun, 27 misses recorded per D5. No deliverable rates itself above 8/10, and the four Complex items in tier pass on the label High |
| Reruns | Done | 32 of 32 ok, 13.06 USD; `check_run.py` 48 scenarios, 0 findings, exit 0; first attempts kept in `first-attempt/`. PFW-001's rerun reported `export/[001] - ...`, so the run's collector now reads a bracketed three-digit number as the sequence number; it adds only PFW-001, and the 2026-09-25 run still collects byte-identically. Dry-run collection: 48 lines, 0 warnings |
| Structure review | Batch 2 running | Batch 1, 16 reviewed: 13 PASS, 3 FAIL (SFW-020 FRAME, SFW-023 VIBE, SFW-024 VIBE-MP, where `visual-mode.md` line 62 asks for flowing prose); fact findings in SFW-004 (Dutch as first instead of second language) and PFW-017 (ticket target base); small scope additions in 15; all payloads parse. Batch 2 covers the 32 reruns |
| Run folder | Created, uncommitted | `benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/` with the committed `playbook_runner.py` (sha1 a0315dcd5b), `check_run.py` and `.gitignore`, the collector at sha1 0f39e06b72 (the committed 350e917d3f plus two changes), the header checker and `framework-targets.json`. README drafted, waiting for batch 2 |
| Old run README | Edited, uncommitted | Section 10 points to the new run folder, and section 11 names the 78 scenarios at 1.2.0.0 |
| `README.md` Local Output | Edited, uncommitted | Names both runs and what the 48 SFW and PFW files show |
| Packet docs | Updated | `decision-record.md` ADR-001 supersedes AC-004; spec REQ-007 to REQ-010; AC-008 to AC-013; tasks Phase 4 |
| Criterion 1 | Met | `validate-playbook-package.cjs --repo-root <repo> --package <playbook>`: PASS scenarios=78 categories=14 violations=0 warnings=0, exit 0. Without `--repo-root` it resolves through the `.skilled` symlink and reports 480 PATH_OUTSIDE_REPO violations. `load_waves`: 78 IDs, none in two wave rows, the 48 in wave 6 |
| Criterion 2 | Met | `check_run.py . --model claude-sonnet-5`: 48 scenarios, 48 event streams, 0 findings, exit 0 |
| Structure review batch 2 | Done | 32 reviewed: 26 PASS, 6 FAIL; totals 39 PASS, 9 FAIL, 20 fact changes, 45 with added scope; three fact findings spot-checked and confirmed; copied to the run folder as `structure-review.md` |
| Run README | Done | 48 rows; `validate_document.py` VALID; output format gate passed; 0 dashes. Records the scenario-rule conflict: the VIBE and VIBE-MP scenarios require labelled pillars while `visual-mode.md` line 62 asks for prose |
| Criteria 3 to 6 | Met | `export/benchmark/` lists `skill/` and `claude project/` only; 48 of 48 name their framework, 27 tier misses listed; README table; `validate.sh --strict` RESULT: PASSED |
| Commits | Done | Prompt Improver 02dbfe3 and Barter 5f711610, 390 files each; parity PASSED 13/13, exit 0; run logs and ID lists deleted before staging |
| Push | Done | Operator go-ahead 2026-09-27. Prompt Improver 9257494..02dbfe3; Barter 3ae67ce0..5f711610 through michelkerkmeester-barter, routing gate fresh, then back to MichelKerkmeester |
| Open for the operator | Recorded | The tier test (the runtime never rates above 8/10) and the VIBE scenario-rule conflict, both in the run README section 7 |

### Deviations and findings

| Item | Note |
|------|------|
| Packet name | Named `004-pi-example-pack` instead of `077-pi-concise-exports`, since the operator redirected the work from conciseness to quality |
| Scope test in 22 files | The first review found four tightened scenarios without the scope test; it went into every delivering scenario that lacked it |
| Rule gaps | Eight gaps between the skill's rules are recorded in the 2026-09-25 run README section 11 and not repaired, per D1 |
| Examples dropped | The eight agent-written examples were too simple and lacked a visible framework, and `export/benchmark/` holds real run output only (operator, 2026-09-26) |
| Engine | The operator answered "Sonnet 5 xhigh", read as real runs through the harness on `claude-sonnet-5` at effort `xhigh` |
| Parallel work | The 078 side quest aligns benchmark code in the older run folders. This packet never edits those scripts |
| Manifest scope | The runner writes all 78 playbook scenarios into `manifest.json`, and `check_run.py` checks every entry, so after the run the manifest is narrowed to the 48 IDs that ran and the README says so |
| Em dashes in output | The runtime's replies and exports carry em dashes. They are verbatim run output, and the skill states no voice rule for the prompts it writes, so they stay unedited and the run README counts them |
| Format-guide risk | The designer found the JSON, YAML and Markdown format guides name only RCAF or CRAFT in their header templates, so a runtime may reshape COSTAR, CIDI, TIDD-EC or CRISPE work. Recorded, not fixed, per D1 |
<!-- /ANCHOR:log -->
