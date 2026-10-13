---
title: "Implementation Summary: Prompt Improver complexity rubric and prose-friendly VIBE scenarios"
description: "Prompt Improver now rates complexity with a scored rubric on both runtimes, so Complex text work reaches 9 or 10. A rerun of the 48 framework-coverage scenarios puts 25 in tier against 13, a grading passes 6 of 48, and skill 0.6.1 removes the company name two Project prompts copied."
trigger_phrases:
  - "implementation summary"
  - "prompt improver complexity rubric"
  - "complexity rubric rerun results"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "005-pi-complexity-rubric/001-complexity-rubric"
    last_updated_at: "2026-09-27T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Committed grading and skill 0.6.1 as 4f55b66 and ff3e5526"
    next_safe_action: "Operator picks the target-model reading"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "scaffold-005-pi-complexity-rubric"
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
| **Spec Folder** | 001-complexity-rubric |
| **Completed** | 2026-09-27 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Prompt Improver can now call a request Complex and say why. Before, no rule defined a 9 or a 10, and no deliverable rated above 8. Now 12 of 48 rate 9 or 10, and the Complex tier goes from 0 of 18 to 9 of 18.

### Prompt Improver complexity rubric and prose-friendly VIBE scenarios

The DEPTH Complexity Assessment scores five dimensions 0 to 2 from what the user stated: Outputs, Inputs, Rules, Audience and Stakes. The rating is 1 plus the sum, capped at 10, and the bands are Low 1 to 4, Medium 5 to 6, High 7 to 8 and Complex 9 to 10. The same rubric sits byte for byte in the Claude Project's DEPTH knowledge file, and every header label scale on both sides names Complex and points to it. The JSON and YAML guides no longer call a 7 Complex in their structure tiers.

The four VIBE and VIBE-MP scenarios now pass a pillar written as prose, as the skill's visual mode asks, and the Complex-tier scenarios accept the label `Complex`.

The rerun shows what the rubric does and does not fix. Text frameworks land in tier 23 of 36 times, against 12. The skill and the Project agree within a point on 23 of 24 inputs. Three things still fall short. Medium inputs overshoot to 7. The runtime lands within a point of a blind reader only about half the time, while two blind readers agree with each other on every input. And no creative input reaches its High or Complex tier, because a single image or clip scores low on most of the five dimensions. The blind reader agrees with the runtime on that last point.

### Grading and the company name

All 48 were then graded against their Pass/fail lines as the run's playbook stood. 6 pass, three on each runtime. Facts fail most, in 27, then the tier in 23 and scope in 17. A third of the skill replies open with the check they just ran instead of the saved path. Twins agree on 20 of 24.

Two Project prompts called the user's company "Barter". The event streams show that the closing line of the Interactive Mode knowledge file was the only place any Project session could read that name. Skill 0.6.1 removes it from that line on both sides and from two skill reference titles, with the kernel unchanged.

A tighter rubric wording, written from the first rater's readings, was recounted by two new blind raters. Readers agreed within a point with or without it, and it moved five more inputs out of their tier, so the operator kept the rubric as it was.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-prompt-improver/references/depth-framework.md` | Modified | The Complexity Rubric in the Complexity Assessment |
| `sk-prompt-improver/SKILL.md`, `description.json`, `README.md`, `changelog/v0.6.0.0.md` | Modified, Created | Header label scale, version 0.6.0 and its changelog |
| `sk-prompt-improver/assets/format-guide-{markdown,json,yaml}.md` | Modified | Label scale, rubric pointer, bare-range structure tiers |
| `claude project/Custom Instructions.md`, `claude project/knowledge/*` (4), `claude project/README.md` | Modified | The Project mirror, kernel v0.7.0 |
| `SYNC.md`, `README.md` | Modified | Maintenance record and Local Output |
| `sk-prompt-improver/manual-testing-playbook/` (66 files) | Modified | Prose VIBE pillars, the `Complex` label, 222 remapped citations, root 1.3.0.0 |
| `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/` | Created | The rerun, its harness, the strict header checker, the blind recount, the structure review and the README |
| `benchmark/reports/2026-09-26--framework-coverage--claude-sonnet-5-xhigh/README.md` | Modified | Notes that its deliverables were replaced and its two decisions taken |
| `export/benchmark/skill/SFW-*`, `export/benchmark/claude project/PFW-*` | Replaced | The 48 deliverables of the rerun |
| `sk-prompt-improver/manual-testing-playbook/*-framework-coverage/{frame,motion,vibe}-*` (12), root | Modified, Renamed | The creative pairs at the recount's tier, root 1.4.0.0 with a Low tier |
| `sk-prompt-improver/references/{depth-framework,interactive-mode}.md`, `Prompt Improver - Interactive Mode - v0.700.md` | Modified | The company name removed |
| `SKILL.md`, `description.json`, both READMEs, `changelog/v0.6.1.0.md`, `SYNC.md` | Modified, Created | Skill 0.6.1 and its records |
| Run folder `results.csv`, `results.md`, `grading-notes.md`, `deliverable-lint.csv`, `rubric-recount-b.md`, `rubric-wording-trial.md`, `README.md` | Created, Modified | The grading, the second recount and the wording trial |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The rule went in on the skill side first, then by hand into the Project mirror under the `SYNC.md` parity method, with the kernel line placed after a residency-declared statement so the declared text stayed verbatim. The inserts shifted line numbers that 222 playbook citations point at, so a HEAD-to-working line map remapped them. The first run start was stopped after 2 of 48 sessions when the JSON and YAML guides turned out to name a 7 Complex. Once they were fixed, all 48 ran in one call. While it ran, a rater who saw no tier or deliverable scored the 24 inputs with the rubric alone. Afterwards one strict header checker scored the new pack, the old pack and the old first attempts. Two reviewers who wrote none of the work judged structure, facts, scope and format by twin pair.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| A scored rubric with five dimensions | The operator chose scored dimensions, so a rating can be recounted from the request |
| Every point must rest on something the user stated | Keeps the skill's rule against unrequested complexity, and makes the recount possible |
| Name the structure tiers in the JSON and YAML guides by range alone | Their Complex 7-10 would have called a 7 Complex. The thresholds stay, so framework selection does not change |
| Stop and restart the run after 2 sessions | The run should measure the rules that ship. Stopping cost 0.93 USD |
| One strict checker for both runs, first attempts compared | The 2026-09-26 checker let `High` pass Complex, and that run reran its misses. Only the same checker on first attempts compares like for like |
| A blind recount before the results | Separates a runtime that reads the rubric badly from a scenario tier the rubric does not support |
| Leave the rubric unchanged after the recount | Changing it mid-run would have measured nothing. The creative tiers go to the operator |
| Leave the two unparseable YAML bodies as they are | Deliverables are verbatim run output, and the README records the defect |
| Grade against the playbook the run used | A verdict should test the scenario the runtime was given. The notes also read the creative pairs against the re-tier |
| Keep the rubric wording as it was | The operator's decision after the trial: readers already agreed, and the new wording moved five inputs out of their tier with no runtime evidence |
| Ship the name removal alone as 0.6.1 | It is the one change the grading proved, and it touches no rule |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Rubric parity | The 19-line block is byte-identical in the skill and the Project, `cmp` clean |
| Residency | `run_residency.sh` PASSED, exit 0, after the guide fix |
| Playbook validator | PASS scenarios=78 categories=14 violations=0 warnings=0, exit 0 |
| Runner parse and router | `load_waves` 78 IDs with the 48 in wave 6; router fixtures PASSED 25/25 |
| Run check | 48 scenarios, 48 event streams, 0 findings, model `claude-sonnet-5`, exit 0 |
| Header check | 48 of 48 name their framework and match their format; 25 of 48 in tier, against 13 first attempts before the rubric |
| Structure review | 45 PASS, 3 FAIL; 29 fact changes; four findings spot-checked and confirmed |
| Pack | `export/benchmark/` holds `skill/` and `claude project/` only, 33 files each; collector dry run 0 keep warnings |
| Docs | Run README, structure review and recount VALID with 0 issues; 0 em or en dashes in authored files |
| Commits and parity | Prompt Improver 4da1a1a and Barter ccd0425c, the same 318 paths; `validate_parity.py prompt-improver` PASSED 13/13, exit 0 |
| Grading | 48 rows, 6 PASS and 42 FAIL; `check_report.sh` exit 2 with the four adjudicated twins; the failing-item map matches `facts_intact` and the header checker |
| Name removal | `grep -i barter` over every file either runtime reads finds nothing; every Project event stream read the removed line |
| Second commits and parity | Prompt Improver 4f55b66 and Barter ff3e5526, the same 17 paths; parity PASSED 13/13, exit 0, Skill v0.6.1 live; residency exit 0; router 25/25; validator 78, 0 violations. Pushed on the operator's go-ahead |
| Packet | `validate.sh --strict` RESULT: PASSED |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Creative tiers.** No FRAME, MOTION or VIBE-MP input reached its High or Complex tier on the runtime or on the blind recount. The operator had the six pairs re-tiered to the recount, three of them to a new Low tier. Read against the new tiers the pack puts 30 of 48 in tier with no rerun, and the next run needs new targets and a Low band in its header checker.
2. **Runtime against readers.** Two blind raters agree within a point on 24 of 24 inputs, so a reader can recount the rubric. The runtime lands within a point of them on 26 of 48 and rates about one point higher. A tighter wording changed nothing for readers and was not kept, so whether wording can pull the runtime closer is still unmeasured.
3. **Medium overshoot.** Seven Medium inputs rate 7, and the runtime rates about one point above a blind reader, most on the Project.
4. **Kernel review.** Michel Kerkmeester has not yet reviewed kernel v0.7.0, and `SYNC.md` records that.
5. **Graded pass rate.** 6 of 48 pass. Five of the six name no target model and pass because the graders read the target as kept by fit. A strict reading leaves one pass, and the operator has not yet chosen between the two readings.
<!-- /ANCHOR:limitations -->

---
