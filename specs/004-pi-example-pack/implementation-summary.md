---
title: "Implementation Summary: Prompt Improver example pack, playbook extension and scenario upgrade"
description: "Prompt Improver's benchmark pack now holds real run output only: the 18 improved exports and 48 framework-coverage prompts from a Sonnet 5 xhigh run, with a playbook of 78 scenarios."
trigger_phrases:
  - "implementation summary"
  - "prompt improver example pack"
  - "pi playbook thirty scenarios"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "004-pi-example-pack"
    last_updated_at: "2026-09-27T01:20:00Z"
    last_updated_by: "claude-code"
    recent_action: "Ran, checked and reviewed the 48 framework-coverage scenarios and wrote the run README"
    next_safe_action: "None; the operator decides the two open questions in the run README"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-004-pi-example-pack"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 004-pi-example-pack |
| **Completed** | 2026-09-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A reader of Prompt Improver's `export/benchmark/` now finds a strong prompt for every mode and format the system writes, not only `$text`, `$image` and `$json`. The 18 graded exports score higher on their own rubric with no added scope. The playbook that grades them now covers 30 scenarios instead of 14.

### Prompt Improver example pack, playbook extension and scenario upgrade

You get three things. The 18 run exports were improved in place, keeping every header, attestation, file name, supplied fact and scenario limit, and the two extras the run failed for were removed. Eight new examples in `export/benchmark/examples/` covered `$deep`, `$short`, `$refine`, `$raw`, `$text $yaml`, `$improve $markdown`, `$video $yaml` and `$vibe`, marked ungraded, until ADR-001 dropped them. The playbook gained eight skill and Project pairs, one per new example, and the 14 existing scenarios now state the scope test, the revision rule, one commentary definition and the advisory summary band. Their inputs did not change.

A re-collection can no longer undo this work: the collector keeps an edited export unless `--force` is given.

### Framework coverage

The operator then dropped the eight agent-written examples (ADR-001) and asked for medium, high and complex prompts that visibly use the library's frameworks. The pack now holds 48 more deliverables from a real run on `claude-sonnet-5` at effort `xhigh`: RCAF, COSTAR, CIDI, TIDD-EC, CRISPE and CRAFT at all three tiers, plus FRAME, MOTION, VIBE and VIBE-MP, from both the skill and the Project, in Markdown, JSON and YAML. Every one names its framework in its header and is in its target format. The run folder's README gives each ID's tier, structure verdict, fact check and reported score, and records what fell short: the runtime never rates a prompt above 8/10, the creative frameworks come out as prose or platform syntax, and 20 of 48 change a fact of the input.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `export/benchmark/skill/*` (9), `export/benchmark/claude project/*` (9) | Modified | The 18 graded exports improved in place |
| `export/benchmark/examples/*` (8 prompts, `README.md`) | Created | The example pack and its index |
| `sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md` | Modified | Root at 1.1.0.0 with 30 scenarios, waves, blocks and index rows |
| `sk-prompt-improver/manual-testing-playbook/*/` (14 modified, 16 created) | Modified, Created | Tightened scenarios and the eight new pairs |
| `benchmark/reports/2026-09-25--.../run/collect_exports.py`, `run/selftest.py` | Modified, Created | The edit guard and its proof |
| `benchmark/reports/2026-09-25--.../README.md` | Modified | Sections 9 to 12: the edit, the pack, the playbook and the next steps |
| `README.md` | Modified | The Local Output paragraph names both runs |
| `export/benchmark/examples/*` | Deleted | The eight examples and their index, under ADR-001 |
| `sk-prompt-improver/manual-testing-playbook/skill-framework-coverage/`, `project-framework-coverage/` (48), root | Created, Modified | The framework-coverage scenarios, root at 1.2.0.0 with 78 scenarios |
| `benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/` | Created | The run, its harness, the header checker and its targets, the structure review and the README |
| `export/benchmark/skill/SFW-*` (24), `export/benchmark/claude project/PFW-*` (24) | Created | The 48 deliverables, verbatim run output |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Opus agents wrote in parallel from one shared brief (`scratch/shared-brief.md`) that fixed the new inputs and the canonical rule wordings. One agent tightened the 14 scenarios, one wrote the 16 new ones and the root, three improved the exports by scenario pair and two wrote the examples through the skill. Two independent reviewers then checked the work against the snapshots in `scratch/before/` and the scenarios. The first scored all 18 exports before and after and made three repairs. The second checked the new scenarios, the root and the examples, fixed 11 findings and turned three failing examples into passes. After review, the scope test went into the 22 delivering scenarios that lacked it. The collector guard was committed first, as Prompt Improver `ba5f796` and Barter `4cd5d2ba`, so a separate code-alignment pass could not tangle with it.

For the framework coverage, a designer fixed the 24 inputs, frameworks, tiers and formats in one brief (`scratch/framework-brief.md`), and the 48 scenarios were written from it. The playbook runner ran a pilot of four, then the other 44, four sessions at a time. A header checker compared every deliverable with its target, and the 32 that rated their complexity below their tier got one rerun each, with the first attempts kept. Two reviewers who wrote none of the work judged the framework structure, facts, scope and format of all 48 in two batches.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Quality over conciseness, and no rule change | The operator redirected the work from conciseness to prompt quality and a varied pack, and ruled that the skill, kernel and knowledge stay as they are |
| Freeze the 14 existing inputs | Run-to-run comparison and each export's tie to the input it answers depend on them |
| Examples marked ungraded, apart from the run's folders | Agents wrote them, not the runtime under test, so only a rerun can grade them |
| Keep SFM-001 002's restored `Mode:` header | `assets/format-guide-json.md` requires it and kernel line 380 keeps it outside the JSON lock, so "valid JSON only" binds the body |
| Keep SCR-002's `audio:` field and SCR-003's UX floor, recorded and not graded | The rules add them while the scope test points the other way, and settling that needs a rule change that was out of scope |
| Accept the `# Mode: $yaml` comment header | The guide's literal header does not parse as YAML, and `SKILL.md` line 560 requires valid YAML syntax. A comment keeps the header on one line and the file parseable |
| Leave SIR-001's "four" and "seven" as words | Every user number is present, and restoring the placeholders would bring back the original's contradiction |
| Drop the examples for a real run (ADR-001) | The operator ruled that the pack holds run output only and asked for visible framework use |
| Record the 27 tier misses, never edit them | Goal D5 allows one rerun; a hand edit would make the pack stop being run output |
| Fix two extraction misses in the run's own collector | PFW-007's header sat above its fence and PFW-001 reported `export/[001]`; each change alters only its own file and leaves the 2026-09-25 collection byte-identical |
| Ship the header checker and its targets with the run | The brief lives in the ignored `specs/` tree, so the check could not be rerun from the repository otherwise |
| Narrow `manifest.json` to the 48 that ran | The runner writes all 78 scenarios, and `check_run.py` checks every entry |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Playbook validator | PASS scenarios=30 categories=12 violations=0 warnings=0 |
| Runner `load_playbook` and `load_waves` | 30 IDs, 30 unique, each in one wave, 2 turns each |
| Inputs | 14 of 14 existing turns identical to HEAD, 16 of 16 new turns identical to the brief |
| Export review | 18 of 18 at or above the original and past the gate, CLEAR 45 to 46 and VISUAL 54 to 55, no added scope |
| Example review | 8 of 8 pass their own scenario's Turn 1 lines after three repairs |
| Formats | 4 JSON payloads and 2 YAML examples parse, 0 files with an em or en dash |
| `deliverable_lint.py` on the 9 Project exports | 9 clean, against 8 clean in the snapshot (PTX-001 fixed) |
| `run/selftest.py` | 7 of 7 PASS, including the negative control |
| Collector dry run | 18 keep warnings, exit 0, `examples/` untouched |
| `validate_document.py` on `examples/README.md` | VALID, 0 issues |
| Commits and parity | Prompt Improver ba5f796 and 9257494, Barter 4cd5d2ba and 3ae67ce0; `run_parity.sh` PASSED 13/13, exit 0 |
| Push | Prompt Improver d473b93..9257494; Barter 8923ad82..3ae67ce0 with the route gate overridden once on the operator's approval |
| Playbook at 78 | `validate-playbook-package.cjs --repo-root <repo>`: PASS scenarios=78 categories=14 violations=0 warnings=0, exit 0; `load_waves` 78 IDs, none in two waves, the 48 in wave 6 |
| Framework-coverage run | 80 sessions ok, 34.45 USD; `check_run.py . --model claude-sonnet-5`: 48 scenarios, 48 event streams, 0 findings, exit 0 |
| Header check | 48 of 48 name their framework and match their format; 21 in tier, 27 misses after one rerun |
| Structure review | 39 PASS, 9 FAIL; facts 28 kept, 20 changed; scope 3 clean; spot checks of three fact findings confirmed |
| Payloads | 6 JSON and 8 YAML bodies parse |
| Collector | Dry run 48 lines, 0 keep warnings, exit 0 |
| `validate_document.py` | Run README and `structure-review.md` VALID, 0 issues |
| Framework-coverage commits and parity | Prompt Improver 02dbfe3 and Barter 5f711610, 390 files each; parity PASSED 13/13, exit 0 |
| Framework-coverage push | Prompt Improver 9257494..02dbfe3; Barter 3ae67ce0..5f711610, routing gate fresh with no override |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The 16 mode and format scenarios and the 48 framework-coverage scenarios are ungraded.** The framework-coverage run checked header, tier, format and structure, not the Pass/fail lines. Its README names a full grading as a next step.
2. **Eight rule gaps are recorded, not repaired.** They cover question routing, the `$vibe` library question, a format question under `$markdown`, Veo audio, the YAML header, the kernel's missing revision rule, the summary band and the identity carve-out. Each is listed with its lines in the run README section 11.
3. **The scores are reviewers' readings.** No second grader checked the rubric scores of the exports or the examples.
4. **Root section 19 overstates the parity benchmark.** It says the benchmark covers all thirty scenarios, while `benchmark/parity/` compares the Project package with the skill sources. HEAD made the same claim for fourteen, so it was left alone.
5. **27 deliverables rate their complexity below their tier.** The runtime never rates above 8/10, and the Project rates lower than the skill. Recorded under goal D5, with the tier test left to the operator.
6. **The VIBE and VIBE-MP scenarios contradict a skill rule.** They require labelled pillars, while `references/visual-mode.md` line 62 asks for prose. The operator decides which gives way.
<!-- /ANCHOR:limitations -->

---
