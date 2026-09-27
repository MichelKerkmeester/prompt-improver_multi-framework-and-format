# Prompt Improver: complexity-rubric run, 2026-09-27, claude-sonnet-5 at effort xhigh

## 1. OVERVIEW

The [2026-09-26 framework-coverage run](../2026-09-26--framework-coverage--claude-sonnet-5-xhigh/README.md) found that the runtime never rated a prompt above 8/10, because no rule said what a 9 or 10 is. The operator chose to give the skill a complexity rubric. The DEPTH Complexity Assessment now scores five dimensions 0 to 2 from what the user stated (Outputs, Inputs, Rules, Audience and Stakes), rates 1 plus the sum capped at 10, and bands the rating Low 1 to 4, Medium 5 to 6, High 7 to 8 and Complex 9 to 10. The skill moved to 1.5.0 and the Project kernel to v1.6.0 with the same rule. The operator also chose to let the four VIBE and VIBE-MP scenarios accept pillars written as prose.

This run sends the same 48 inputs again, SFW-001 to SFW-024 and their Project twins PFW-001 to PFW-024, one turn each, and measures the rating against three references:
- **The scenario tier**, the tier each scenario was written for
- **The 2026-09-26 rating**, the same input before the rubric
- **A blind recount**, the rubric applied to each input by a rater who saw no tier, target or deliverable ([`rubric-recount.md`](rubric-recount.md))

**What this run checks and what it does not.** It checks the header, the rating, the file format, the framework structure and the facts. It does not grade the scenarios against their Pass/fail lines, and it does not test framework selection, since every input names its framework.

---

## 2. RESULTS

| Check | 2026-09-27 | 2026-09-26 |
|---|---|---|
| Framework header | 48 of 48 name their target framework | 48 of 48 |
| Rating of 9 or 10 | 12 of 48 | 0 of 48 |
| Complexity tier, first attempt | 25 of 48 | 13 of 48 |
| Complexity tier, after one rerun per miss | no reruns | 17 of 48 |
| Framework structure | 45 PASS, 3 FAIL | 39 PASS, 9 FAIL |
| Facts | 19 kept, 29 changed | 28 kept, 20 changed |
| Scope | 10 clean, 38 add something | 3 clean, 45 add something |
| JSON and YAML bodies | 12 of 14 parse | 14 of 14 |
| Reported score | 48 of 48 pass their own gate | 48 of 48 |

Every tier count uses one checker, `run/check_framework_headers.py` in this folder, whose Complex tier accepts `Complex`, 9, 10 or a label above High and fails a bare `High`. The 2026-09-26 README counted 21 in tier because its checker let `High` pass a Complex item.

**Complexity tier by tier, first attempts:**

| Tier | 2026-09-27 | 2026-09-26 | Misses now |
|---|---:|---:|---|
| Medium (5 to 6), 12 deliverables | 5 | 8 | 7 above tier, all rated High (7/10) |
| High (7 to 8), 18 deliverables | 11 | 5 | 3 above tier (9/10), 4 below |
| Complex (9 to 10), 18 deliverables | 9 | 0 | 9 below tier |
| Text frameworks, 36 deliverables | 23 | 12 | |
| Creative frameworks, 12 deliverables | 2 | 1 | |
| Skill, 24 deliverables | 14 | 9 | |
| Project, 24 deliverables | 11 | 4 | |

**Against the blind recount:**

| Measure | Result |
|---|---|
| Rating within one point of the recount | 26 of 48, skill 14 and Project 12 |
| Same band as the recount | 22 of 48 |
| Mean rating minus recount | +0.96, skill +0.75 and Project +1.17 |
| Recount inside the scenario tier | 11 of 24 inputs, 11 of 18 text and 0 of 6 creative |
| Twins within one point of each other | 23 of 24 |

---

## 3. HOW THE RUN WAS MADE

- **Rules under test:** Prompt Improver `sk-prompt-improver/SKILL.md` 1.5.0 and `claude project/Custom Instructions.md` v1.6.0, uncommitted when the run started and committed with this record. The rubric sits in `references/depth-framework.md` lines 147-165 and in `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 134-152, byte-identical
- **Scenarios:** `skill-framework-coverage/` and `project-framework-coverage/`, 24 files each, in wave 6 of the playbook root at version 1.3.0.0 (78 scenarios). Each input is the scenario's `Prompt` line, unchanged from the 2026-09-26 run
- **Engine:** Claude Code 2.1.283 per `manifest.json`, model `claude-sonnet-5`, effort `xhigh`, 4 parallel sessions
- **Runner:** `run/playbook_runner.py` at sha1 `a0315dcd5b`, the file the 2026-09-26 run used. One call from this folder, `python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-sonnet-5 --effort xhigh --ids <48 IDs> --jobs 4`: 48 sessions, 22.38 USD and 118.6 minutes of session time. Every session ended `ok` with exit code 0, and the runner retried none of them
- **A stopped first start:** the first start was stopped after 2 of 48 sessions (0.93 USD for those two), because the JSON and YAML format guides still named their structure tiers Simple 1-3, Medium 4-6 and Complex 7-10, which would call a 7 Complex. Those tiers now read as bare ranges with the same thresholds, and the run was restarted on the final rules. The stopped output is not in this folder
- **No reruns:** the 2026-09-26 run reran each tier miss once. This run did not, so its tier counts are first attempts, compared with that run's first attempts in section 2
- **Sandboxes:** as in the 2026-09-26 run, the skill side in a copy of the system with `AGENTS.md` as the system prompt, the Project side in a copy of `claude project/` with the kernel as the system prompt
- **Manifest:** the runner writes all 78 playbook scenarios into `manifest.json`, which was narrowed to the 48 that ran
- **Run check:** `python3 run/check_run.py . --model claude-sonnet-5` prints `48 scenarios, 48 declared turns, 48 event streams read, 0 finding(s), expected model claude-sonnet-5` and exits 0
- **Collection:** the 48 SFW and PFW files of the 2026-09-26 run were removed from `export/benchmark/`, then `python3 run/collect_exports.py . ../../../export/benchmark` collected this run with the 2026-09-26 collector (sha1 `0f39e06b72`). A `--dry-run` afterwards prints 48 lines and no keep warning
- **Header check:** `python3 run/check_framework_headers.py ../../../export/benchmark` (sha1 `24737b2b9d`), the 2026-09-26 checker with one change: a bare `High` no longer passes a Complex item, since the skill's label scale now reaches Complex. It exits 1 while any ID misses, so it exits 1 on this run. The same checker read the 2026-09-26 pack from git and its first attempts from that run's `first-attempt/collected/`
- **Blind recount:** [`rubric-recount.md`](rubric-recount.md). One rater read only the rubric and the 24 inputs and scored every dimension with the stated thing it rests on, so any reader can recount it
- **Structure review:** [`structure-review.md`](structure-review.md). Two reviewers, neither of whom wrote a scenario or a deliverable, each read one half, a twin pair at a time, against the framework definitions. VIBE and VIBE-MP pillars pass as prose, per the scenarios since 2026-09-27

### Files in this folder

| File | What it holds |
|---|---|
| `README.md` | This record |
| `structure-review.md` | The independent structure and fact review, one row per deliverable |
| `rubric-recount.md` | The blind rubric recount of the 24 inputs |
| `manifest.json`, `run-status.json` | The run's scenario list and per-scenario status, 48 each |
| `replies/` | The 48 replies, one per scenario |
| `skill/`, `claude project/` | One folder per scenario with its meta and turn record |
| `run/` | The runner, the run check, the collector, the header checker and its targets |

Raw event streams, stderr and each scenario's copy of its exports stay local, per `.gitignore`.

---

## 4. PER-ID RESULTS

The 2026-09-26 rating is that run's final header value, after its rerun where it had one. The rating now is this run's header value. The blind recount is the same for both twins, since they share an input. Tier check compares the rating now with the scenario tier. Structure and facts come from [`structure-review.md`](structure-review.md), which quotes every changed fact and every addition, and the reported score is copied from the reply.

| ID | Framework | Tier | Format | Rating, 2026-09-26 | Rating now | Blind recount | Tier check | Structure | Facts | Reported score |
|---|---|---|---|---|---|---|---|---|---|---|
| SFW-001 | RCAF | Medium (5 to 6) | Markdown | Low | Medium (5/10) | 4 | in tier | PASS, 4 of 4 labelled | kept | CLEAR 46/50, gate passed |
| SFW-002 | RCAF | High (7 to 8) | JSON | High | Complex (9/10) | 8 | above tier | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| SFW-003 | RCAF | Complex (9 to 10) | Markdown | High | Complex (10/10) | 10 | in tier | PASS, 4 of 4 labelled | changed | CLEAR 46/50, gate passed |
| SFW-004 | COSTAR | Medium (5 to 6) | Markdown | Medium | Medium (5/10) | 7 | in tier | PASS, 6 of 6 labelled | kept | CLEAR 44/50, gate passed |
| SFW-005 | COSTAR | High (7 to 8) | YAML | Medium | High (8/10) | 7 | in tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| SFW-006 | COSTAR | Complex (9 to 10) | Markdown | 8/10 | Complex (9/10) | 9 | in tier | PASS, 6 of 6 labelled | kept | CLEAR 45/50, gate passed |
| SFW-007 | CIDI | Medium (5 to 6) | YAML | Medium | Medium (6/10) | 5 | in tier | PASS, 4 of 4 labelled | kept | CLEAR 46/50, gate passed |
| SFW-008 | CIDI | High (7 to 8) | Markdown | 6/10 | High (8/10) | 8 | in tier | PASS, 4 of 4 labelled | changed | CLEAR 44/50, gate passed |
| SFW-009 | CIDI | Complex (9 to 10) | JSON | High | Complex (9/10) | 10 | in tier | PASS, 4 of 4 labelled | changed | CLEAR 44/50, gate passed |
| SFW-010 | TIDD-EC | Medium (5 to 6) | Markdown | 6/10 | Medium (6/10) | 5 | in tier | PASS, 6 of 6 labelled | changed | CLEAR 42/50, gate passed |
| SFW-011 | TIDD-EC | High (7 to 8) | JSON | High | High (8/10) | 6 | in tier | PASS, 6 of 6 labelled | kept | CLEAR 45/50, gate passed |
| SFW-012 | TIDD-EC | Complex (9 to 10) | Markdown | 8/10 | Complex (9/10) | 9 | in tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| SFW-013 | CRISPE | Medium (5 to 6) | Markdown | 6/10 | High (7/10) | 5 | above tier | PASS, 5 of 5 labelled | changed | CLEAR 45/50, gate passed |
| SFW-014 | CRISPE | High (7 to 8) | YAML | High | High (7/10) | 5 | in tier | PASS, 5 of 5 labelled | changed | CLEAR 46/50, gate passed |
| SFW-015 | CRISPE | Complex (9 to 10) | Markdown | 8/10 | High (8/10) | 7 | below tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| SFW-016 | CRAFT | Medium (5 to 6) | Markdown | 6/10 (Medium-High) | High (7/10) | 5 | above tier | PASS, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| SFW-017 | CRAFT | High (7 to 8) | Markdown | High | High (8/10) | 6 | in tier | PASS, 5 of 5 labelled | changed | CLEAR 46/50, gate passed |
| SFW-018 | CRAFT | Complex (9 to 10) | Markdown | High (8/10) | High (7/10) | 5 | below tier | PASS, 5 of 5 labelled | kept | CLEAR 45/50, gate passed |
| SFW-019 | FRAME | High (7 to 8) | Markdown | High | Low (4/10) | 3 | below tier | PASS, 5 of 5 labelled | kept | VISUAL 53/60, gate passed |
| SFW-020 | FRAME | Complex (9 to 10) | Markdown | High | Medium (5/10) | 5 | below tier | FAIL, 2 of 5 labelled | kept | VISUAL 55/60, gate passed |
| SFW-021 | MOTION | High (7 to 8) | Markdown | Medium | Medium (5/10) | 3 | below tier | PASS, 6 of 6 labelled | changed | VISUAL 62/70, gate passed |
| SFW-022 | MOTION | Complex (9 to 10) | YAML | 7/10 | Low (3/10) | 3 | below tier | PASS, 6 of 6 labelled | changed | VISUAL 62/70, gate passed |
| SFW-023 | VIBE | High (7 to 8) | Markdown | High | High (7/10) | 5 | in tier | PASS, as prose | changed | EVOKE 44/50, gate passed |
| SFW-024 | VIBE-MP | Complex (9 to 10) | Markdown | High | Medium (6/10) | 8 | below tier | PASS, as prose | changed | EVOKE (MagicPath) ≈ 45/50, gate passed |
| PFW-001 | RCAF | Medium (5 to 6) | Markdown | 3/10 | Medium (6/10) | 4 | in tier | PASS, 4 of 4 labelled | kept | CLEAR 43/50, gate passed |
| PFW-002 | RCAF | High (7 to 8) | JSON | 6 | Complex (9/10) | 8 | above tier | PASS, 4 of 4 labelled | kept | CLEAR 43/50, gate passed |
| PFW-003 | RCAF | Complex (9 to 10) | Markdown | 8/10 | Complex (9/10) | 10 | in tier | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-004 | COSTAR | Medium (5 to 6) | Markdown | 4/10 (Low-Medium) | High (7/10) | 7 | above tier | PASS, 6 of 6 labelled | changed | CLEAR 42/50, gate passed |
| PFW-005 | COSTAR | High (7 to 8) | YAML | 6/10 | Complex (9/10) | 7 | above tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| PFW-006 | COSTAR | Complex (9 to 10) | Markdown | 8/10 | Complex (10/10) | 9 | in tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| PFW-007 | CIDI | Medium (5 to 6) | YAML | Medium (5/10) | High (7/10) | 5 | above tier | PASS, 4 of 4 labelled | kept | CLEAR 43/50, gate passed |
| PFW-008 | CIDI | High (7 to 8) | Markdown | 7/10 | High (8/10) | 8 | in tier | PASS, 4 of 4 labelled | changed | CLEAR 43/50, gate passed |
| PFW-009 | CIDI | Complex (9 to 10) | JSON | 8/10 | Complex (10/10) | 10 | in tier | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-010 | TIDD-EC | Medium (5 to 6) | Markdown | 4/10 | High (7/10) | 5 | above tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| PFW-011 | TIDD-EC | High (7 to 8) | JSON | High (7/10) | High (8/10) | 6 | in tier | PASS, 6 of 6 labelled | changed | CLEAR 45/50, gate passed |
| PFW-012 | TIDD-EC | Complex (9 to 10) | Markdown | 8/10 | Complex (9/10) | 9 | in tier | PASS, 6 of 6 labelled | kept | CLEAR 44/50, gate passed |
| PFW-013 | CRISPE | Medium (5 to 6) | Markdown | Medium | High (7/10) | 5 | above tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-014 | CRISPE | High (7 to 8) | YAML | 6/10 | High (7/10) | 5 | in tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-015 | CRISPE | Complex (9 to 10) | Markdown | 8/10 | Complex (9/10) | 7 | in tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-016 | CRAFT | Medium (5 to 6) | Markdown | 6 (Medium-High) | High (7/10) | 5 | above tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-017 | CRAFT | High (7 to 8) | Markdown | High (8/10) | High (7/10) | 6 | in tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-018 | CRAFT | Complex (9 to 10) | Markdown | 8/10 | High (8/10) | 5 | below tier | PASS, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| PFW-019 | FRAME | High (7 to 8) | Markdown | 5 | Low (4/10) | 3 | below tier | PASS, 5 of 5 labelled | changed | VISUAL 55/60, gate passed |
| PFW-020 | FRAME | Complex (9 to 10) | Markdown | 7/10 | Medium (5/10) | 5 | below tier | FAIL, 2 of 5 labelled | changed | VISUAL 55/60, gate passed |
| PFW-021 | MOTION | High (7 to 8) | Markdown | 5/10 | Medium (5/10) | 3 | below tier | PASS, 6 of 6 labelled | kept | VISUAL ~64/70, gate passed |
| PFW-022 | MOTION | Complex (9 to 10) | YAML | 6/10 | Low (4/10) | 3 | below tier | FAIL, 2 of 6 labelled | changed | VISUAL 62/70, gate passed |
| PFW-023 | VIBE | High (7 to 8) | Markdown | Medium | High (7/10) | 5 | in tier | PASS, as prose | changed | EVOKE ~44/50, gate passed |
| PFW-024 | VIBE-MP | Complex (9 to 10) | Markdown | 6/10 | High (7/10) | 8 | below tier | PASS, as prose | kept | EVOKE-MP 46/50, gate passed |

---

## 5. FINDINGS

1. **The rubric lifts the ceiling.** 12 deliverables rate 9 or 10, where none did before. The Complex tier goes from 0 of 18 to 9 of 18, and all nine are text frameworks, 9 of the 12 text inputs at that tier. SFW-015, SFW-018 and PFW-018 still rate 7 or 8, and the blind recount rates those inputs 7, 5 and 5, so their scenarios ask for more than the rubric finds in them
2. **It overshoots at Medium.** Seven Medium-tier deliverables rate High (7/10): SFW-013, SFW-016, PFW-004, PFW-007, PFW-010, PFW-013 and PFW-016. Three High-tier ones rate 9: SFW-002, PFW-002 and PFW-005. The Medium tier falls from 8 of 12 to 5 of 12. The runtime rates 0.96 points above the blind recount on average, and the Project 1.17. The rubric asks that every point rest on something the user stated, so the gap is where the runtime counts more than the input says
3. **The creative tiers do not fit the rubric.** FRAME, MOTION and VIBE-MP rate 3 to 7 against High and Complex tiers, and the blind recount agrees, 3 to 8, with 0 of 6 creative inputs inside their tier. The five dimensions describe text work: several outputs, sources that disagree, many rules, several audiences and high stakes. One image or one clip scores low on most of them however detailed its brief. These misses come from the scenario tiers, not from the runtime's reading
4. **The two runtimes now agree.** 23 of 24 twins rate within one point of each other. On first attempts before the rubric the Project met its tier 4 times and the skill 9 times. Now the Project meets it 11 times and the skill 14, and the Project rates a little higher on average, 7.33 against 6.92
5. **The rubric is only partly recountable.** 26 of 48 ratings sit within one point of the blind recount, and 22 of 48 share its band. The rater named the wording that moved scores: "distinct sections", how finely a constraint is counted, "kinds of source", what counts as financial stakes, and whether Outputs and Inputs describe the downstream task or the prompt being written. Spec success criterion SC-002, the same number within one point, holds for about half
6. **More facts change than before, 29 of 48 against 20.** The ones that change what the prompt produces:
   - PFW-006 and PFW-010 name the user's company "Barter", which no input says. The only "Barter" in the Project package is the closing line of `Prompt Improver - Interactive Mode - v0.700.md`, "Interactive framework for Barter prompt enhancement", the likely source but not a proven one
   - PFW-005 dates the policy 2026-03-01, a year the input never gave
   - PFW-011 turns "38 EU-authorised health claims" into "up to 38"
   - SFW-017 counts the ticket target against 1,210 users, the 60 shared mailboxes included, where the input has 1,150
   - PFW-020 drops Leiden and puts the children on a rooftop terrace, SFW-021 drops the thumbs "smoothing the rim", and SFW-022 and PFW-022 move the chime from the end to the 8-second beat
   - PFW-019 excludes "people", which also works against the one rider, and PFW-015 adds a hosting fact the input never gave
   - SFW-012 bans the word "structuring" that the input uses and narrows its citation rule

   [`structure-review.md`](structure-review.md) lists all 29 with the exact wording. The rubric does not touch fact handling, so this rise is run-to-run variation or a side effect of heavier prompts, and this run cannot tell which
7. **Structure holds.** 45 PASS and 3 FAIL. The text frameworks pass 36 of 36. SFW-020 and PFW-020 again merge Focus, Rendering and Atmosphere into one unlabelled Stable Diffusion prompt, and PFW-022 spreads MOTION over platform keys. The four VIBE and VIBE-MP deliverables pass because the scenarios now accept prose. Their 2026-09-26 twins also wrote every pillar as prose, so that is a scenario change, not a runtime one
8. **Two YAML bodies do not parse.** PFW-005 line 54 and PFW-007 lines 22 to 23 hold an unquoted colon inside a plain value. Every JSON body and the other six YAML bodies parse once the header, and on Project files the `---` separator and attestation, are stripped
9. **Format details.**
   - SFW-023 (350 words) and PFW-023 (377) run over v0's 100 to 300, and SFW-024 (448) over MagicPath's 150 to 400
   - 23 files carry 130 em dashes and 11 en dashes. They are verbatim run output, and the skill states no voice rule for the prompts it writes
   - PFW-002, PFW-009, PFW-020 and PFW-022 carry `NNN` as their file number, the slot the Project writes for a number it cannot know
   - Several headers put the format command in the mode slot, `Mode: $json`, `Mode: $yaml` or `Mode: $video $yaml`, which the scenarios allow
10. **Self-reported scores still do not track the review.** All 48 pass their own gate, including the 3 structure FAILs, the 29 fact changes and the two YAML bodies that do not parse. SFW-014's own breakdown gives Reusability 6 on a 5-point dimension

---

## 6. DELIVERABLES

The 48 deliverables sit in `export/benchmark/skill/` and `export/benchmark/claude project/` under `<ID> - <number> - <name>`, next to the 18 core exports of the 2026-09-25 run. They are verbatim run output. Nobody edited them, and the collector would warn on any file that differs from the run's copy. They replace the 2026-09-26 deliverables, which stay in git history, last at Prompt Improver `44e5982`.

---

## 7. NEXT STEPS

1. **Operator decision on the creative tiers.** Neither the runtime nor the blind recount puts FRAME, MOTION or VIBE-MP inputs at High or Complex. The options are to re-tier those scenarios to what the rubric gives, to give the rubric a reading for creative work, or to drop the tier test for creative scenarios
2. **Tighten the rubric's wording.** Define distinct sections, one constraint, kinds of source and financial stakes, and say that Outputs and Inputs describe what the user asked for, then recount and rerun to see whether agreement rises above half
3. **Look at the Medium overshoot.** The runtime rates about one point above a blind reader, most on the Project. A worked example per band in the rubric may pull the two together
4. **Trace the "Barter" name.** Check whether the closing line of the Interactive Mode knowledge file puts the company name into Project deliverables
5. **Grade the 48 against their Pass/fail lines.** A full grading decides whether the 29 fact changes, the added scope and the two YAML bodies that do not parse fail their scenarios
