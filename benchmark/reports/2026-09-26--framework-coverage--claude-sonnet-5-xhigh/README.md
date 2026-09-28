# Prompt Improver: framework-coverage run, 2026-09-26, claude-sonnet-5 at effort xhigh

## 1. OVERVIEW

The operator asked for medium, high and complex prompts in `export/benchmark/` that visibly use the frameworks in the skill's library. The pack before it held mostly simple prompts with no clear framework. This run gives each framework a real deliverable from both runtimes: 24 skill scenarios, SFW-001 to SFW-024, and their Project twins, PFW-001 to PFW-024, one turn each.

| Framework | Medium (5 to 6) | High (7 to 8) | Complex (9 to 10) |
|---|---|---|---|
| RCAF | SFW-001 | SFW-002 | SFW-003 |
| COSTAR | SFW-004 | SFW-005 | SFW-006 |
| CIDI | SFW-007 | SFW-008 | SFW-009 |
| TIDD-EC | SFW-010 | SFW-011 | SFW-012 |
| CRISPE | SFW-013 | SFW-014 | SFW-015 |
| CRAFT | SFW-016 | SFW-017 | SFW-018 |
| FRAME | - | SFW-019 | SFW-020 |
| MOTION | - | SFW-021 | SFW-022 |
| VIBE | - | SFW-023 | - |
| VIBE-MP | - | - | SFW-024 |

Each PFW ID is the Project twin of the SFW ID with the same number and the same input.

**What this run checks and what it does not.** Every input names the framework it wants, so the header check shows whether the runtime kept the requested framework. It does not test framework selection. The run checks the header, the tier, the file format and the framework structure. It does not grade the scenarios against their Pass/fail lines, which a full playbook grading still has to do (section 7).

---

## 2. RESULTS

| Check | Result |
|---|---|
| Framework header | 48 of 48 name their target framework |
| Format | 48 of 48 in their target format. The 6 JSON and 8 YAML bodies all parse once the header line, and on Project files the attestation, is stripped |
| Complexity tier | 21 of 48 inside their tier: 16 on the first attempt and 5 after one rerun. 27 miss after one rerun and are recorded, never edited |
| Framework structure | 39 PASS, 9 FAIL on the independent review |
| Facts | 28 keep every name, number and constraint of the input, and 20 change at least one |
| Scope | 3 clean, 45 add at least one output, field or section the input did not ask for |
| Reported score | 48 of 48 report a score that passes their own gate |

**Complexity tier by tier and by runtime:**

| Tier | In tier | Miss after rerun |
|---|---:|---:|
| Medium (5 to 6), 12 deliverables | 8 | 4 |
| High (7 to 8), 18 deliverables | 9 | 9 |
| Complex (9 to 10), 18 deliverables | 4 | 14 |
| Skill, 24 deliverables | 15 | 9 |
| Project, 24 deliverables | 6 | 18 |

**Framework structure by framework:**

| Framework | PASS | FAIL |
|---|---:|---:|
| RCAF, COSTAR, CIDI, TIDD-EC and CRAFT | 30 | 0 |
| CRISPE | 5 | 1 |
| FRAME | 2 | 2 |
| MOTION | 2 | 2 |
| VIBE and VIBE-MP | 0 | 4 |

The text frameworks pass 35 of 36. The creative frameworks pass 4 of 12.

---

## 3. HOW THE RUN WAS MADE

- **Scenarios:** `sk-prompt-improver/manual-testing-playbook/skill-framework-coverage/` and `project-framework-coverage/`, 24 files each, in wave 6 of the playbook root at version 1.2.0.0 (78 scenarios). Each scenario's `Prompt` line is the exact input the runtime got
- **Engine:** Claude Code 2.1.283 per `manifest.json`, model `claude-sonnet-5`, effort `xhigh`, 4 parallel sessions. Every event stream reports `claude-sonnet-5`
- **Runner:** `run/playbook_runner.py` at sha1 `a0315dcd5b`, the same file the 2026-09-25 run used. Three calls from this folder, each `python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-sonnet-5 --effort xhigh --ids <IDs> --jobs 4`:

| Call | IDs | Sessions | Cost | Session time |
|---|---|---:|---:|---:|
| Pilot | SFW-001, SFW-003, SFW-023, PFW-003 | 4 | 1.94 USD | 6.4 min |
| Main | the other 44 | 44 | 19.45 USD | 102.8 min |
| Rerun | the 32 tier misses of section 4 | 32 | 13.06 USD | 66.4 min |
| **Total** | | **80** | **34.45 USD** | **175.7 min** |

  Session time adds up each session's own wall time, so four parallel sessions finished in less elapsed time. Every session ended `ok` with exit code 0, and the runner retried none of them
- **Sandboxes:** as in the 2026-09-25 run. The skill side gets a copy of the system without `.git`, `benchmark/`, the playbook, `export/` or `changelog/`, with `AGENTS.md` as the system prompt and Read, Bash, Edit, Write, Glob and Grep. The Project side gets a copy of `claude project/`, with the kernel and the retrieval note as the system prompt and Read, Glob and Grep. A terminal has no Canvas panel, so the reply text stands in for it
- **Manifest:** the runner writes all 78 playbook scenarios into `manifest.json`, and `run/check_run.py` checks every entry in it. After each call the manifest was narrowed to the IDs that ran, 48 at the end
- **Run check:** `python3 run/check_run.py . --model claude-sonnet-5` prints `48 scenarios, 48 declared turns, 48 event streams read, 0 finding(s), expected model claude-sonnet-5` and exits 0
- **Reruns:** a rerun replaces the scenario's folder, reply and meta. The first attempts are kept in `first-attempt/`: `skill/`, `claude project/` and `replies/` as the runner wrote them, and `collected/` with the deliverables as first collected
- **Collection:** `python3 run/collect_exports.py . ../../../export/benchmark` from this folder. The collector is the 2026-09-25 one (sha1 `350e917d3f`) plus two changes, and is at sha1 `0f39e06b72`:
  - PFW-007's reply put the header line above its fence and the attestation below it. The collector now keeps a header directly above a fence and an attestation directly below it
  - PFW-001's rerun reported its path as `export/[001] - ...`. The collector now reads a bracketed three-digit number as the file's sequence number rather than as a template placeholder

  Each change alters only the file it was made for, and the 2026-09-25 run collects byte-identically under both collectors
- **Header check:** `python3 run/check_framework_headers.py ../../../export/benchmark` reads each ID's target from `run/framework-targets.json`. It passes a file when the header names the target framework, the complexity sits inside the tier and the extension matches the target format. Framework names are compared without case, spaces, hyphens, quotes or a bracketed qualifier, so `RCAF (Layered)` reads as RCAF. A number is read as n/10 against the tier. A label is read as its tier, and a Complex item also passes on High, because the skill's label scale ends at High. It exits 1 while any ID misses, so it exits 1 on this run
- **Structure review:** [`structure-review.md`](structure-review.md). Two reviewers, neither of whom wrote a scenario or a deliverable, read the 48 in two batches, each against the framework definitions in `assets/framework-pattern-library.md` sections 2 and 3, and against `references/visual-mode.md` and the image and video mode references for the creative frameworks. They judged whether every framework part appears as a labelled part and does its job, compared every name, number and constraint in the input with the deliverable, listed each addition the input did not ask for, parsed each JSON and YAML body and counted dashes

### Files in this folder

| File | What it holds |
|---|---|
| `README.md` | This record |
| `structure-review.md` | The independent structure review, one row per deliverable in two batches: first attempts that met their tier, then the reruns |
| `manifest.json`, `run-status.json` | The run's scenario list and per-scenario status, 48 each |
| `replies/` | The 48 final replies, one per scenario |
| `skill/`, `claude project/` | One folder per scenario with its meta and turn record |
| `first-attempt/` | The 32 first attempts that the rerun replaced, and their collected deliverables |
| `run/` | The runner, the run check, the collector, the header checker and its targets |

Raw event streams, stderr and each scenario's copy of its exports stay local, per `.gitignore`.

---

## 4. PER-ID RESULTS

Complexity is the header's own value. For the 16 IDs that met their tier on the first attempt, the first attempt is the final one and the rerun column reads `-`. Structure gives the reviewer's verdict and how many framework parts carry a label. Facts reads `changed` when at least one name, number or constraint of the input changed. The reported score is copied from the runtime's reply. [`structure-review.md`](structure-review.md) gives every finding behind these cells, with the exact wording of each changed fact and each addition.

| ID | Framework | Tier | Format | Complexity, first attempt | Complexity, rerun | Framework header | Tier check | Structure | Facts | Reported score |
|---|---|---|---|---|---|---|---|---|---|---|
| SFW-001 | RCAF | Medium (5 to 6) | Markdown | 3/10 | Low | names RCAF | miss after rerun | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| SFW-002 | RCAF | High (7 to 8) | JSON | High | - | names RCAF | in tier | PASS, 4 of 4 labelled | kept | CLEAR 46/50, gate passed |
| SFW-003 | RCAF | Complex (9 to 10) | Markdown | High (7/10) | High | names RCAF | in tier after rerun | PASS, 4 of 4 labelled | changed | CLEAR 44/50, gate passed |
| SFW-004 | COSTAR | Medium (5 to 6) | Markdown | Medium | - | names COSTAR | in tier | PASS, 6 of 6 labelled | changed | CLEAR 43/50, gate passed |
| SFW-005 | COSTAR | High (7 to 8) | YAML | Medium (5/10) | Medium | names COSTAR | miss after rerun | PASS, 6 of 6 labelled | kept | CLEAR 44/50, gate passed |
| SFW-006 | COSTAR | Complex (9 to 10) | Markdown | 8/10 | 8/10 | names COSTAR | miss after rerun | PASS, 6 of 6 labelled | kept | CLEAR 46/50, gate passed |
| SFW-007 | CIDI | Medium (5 to 6) | YAML | Medium | - | names CIDI | in tier | PASS, 4 of 4 labelled | kept | CLEAR 42/50, gate passed |
| SFW-008 | CIDI | High (7 to 8) | Markdown | 6/10 | 6/10 | names CIDI | miss after rerun | PASS, 4 of 4 labelled | changed | CLEAR 44/50, gate passed |
| SFW-009 | CIDI | Complex (9 to 10) | JSON | High | - | names CIDI | in tier | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| SFW-010 | TIDD-EC | Medium (5 to 6) | Markdown | 6/10 | - | names TIDD-EC | in tier | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| SFW-011 | TIDD-EC | High (7 to 8) | JSON | 6/10 | High | names TIDD-EC | in tier after rerun | PASS, 6 of 6 labelled | kept | CLEAR 45/50, gate passed |
| SFW-012 | TIDD-EC | Complex (9 to 10) | Markdown | High (8/10) | 8/10 | names TIDD-EC | miss after rerun | PASS, 6 of 6 labelled | changed | CLEAR 45/50, gate passed |
| SFW-013 | CRISPE | Medium (5 to 6) | Markdown | 6/10 | - | names CRISPE | in tier | PASS, 5 of 5 labelled | kept | CLEAR 42/50, gate passed |
| SFW-014 | CRISPE | High (7 to 8) | YAML | High | - | names CRISPE | in tier | PASS, 5 of 5 labelled | kept | CLEAR ~44/50, gate passed |
| SFW-015 | CRISPE | Complex (9 to 10) | Markdown | High (7/10) | 8/10 | names CRISPE | miss after rerun | PASS, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| SFW-016 | CRAFT | Medium (5 to 6) | Markdown | 6/10 (Medium-High) | - | names CRAFT | in tier | PASS, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| SFW-017 | CRAFT | High (7 to 8) | Markdown | High | - | names CRAFT | in tier | PASS, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| SFW-018 | CRAFT | Complex (9 to 10) | Markdown | High (8/10) | High (8/10) | names CRAFT | miss after rerun | PASS, 5 of 5 labelled | kept | CLEAR 46/50, gate passed |
| SFW-019 | FRAME | High (7 to 8) | Markdown | Medium | High | names FRAME | in tier after rerun | PASS, 5 of 5 labelled | changed | VISUAL 55/60, gate passed |
| SFW-020 | FRAME | Complex (9 to 10) | Markdown | High | - | names FRAME | in tier | FAIL, 2 of 5 labelled | changed | VISUAL 55/60, gate passed |
| SFW-021 | MOTION | High (7 to 8) | Markdown | Medium | Medium | names MOTION | miss after rerun | PASS, 6 of 6 labelled | kept | VISUAL 62/70, gate passed |
| SFW-022 | MOTION | Complex (9 to 10) | YAML | 6 | 7/10 | names MOTION | miss after rerun | FAIL, 2 of 6 labelled | changed | VISUAL (Video) 64/70, gate passed |
| SFW-023 | VIBE | High (7 to 8) | Markdown | High | - | names VIBE | in tier | FAIL, 0 of 4 labelled | changed | EVOKE 45/50, gate passed |
| SFW-024 | VIBE-MP | Complex (9 to 10) | Markdown | High | - | names VIBE-MP | in tier | FAIL, 0 of 4 labelled | kept | EVOKE ~46/50, gate passed |
| PFW-001 | RCAF | Medium (5 to 6) | Markdown | 3/10 | 3/10 | names RCAF | miss after rerun | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-002 | RCAF | High (7 to 8) | JSON | 6/10 | 6 | names RCAF | miss after rerun | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-003 | RCAF | Complex (9 to 10) | Markdown | 8/10 | 8/10 | names RCAF | miss after rerun | PASS, 4 of 4 labelled | kept | CLEAR 45/50, gate passed |
| PFW-004 | COSTAR | Medium (5 to 6) | Markdown | 4/10 | 4/10 (Low-Medium) | names COSTAR | miss after rerun | PASS, 6 of 6 labelled | changed | CLEAR 45/50, gate passed |
| PFW-005 | COSTAR | High (7 to 8) | YAML | 6/10 | 6/10 | names COSTAR | miss after rerun | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| PFW-006 | COSTAR | Complex (9 to 10) | Markdown | 7/10 | 8/10 | names COSTAR | miss after rerun | PASS, 6 of 6 labelled | changed | CLEAR 45/50, gate passed |
| PFW-007 | CIDI | Medium (5 to 6) | YAML | Medium (5/10) | - | names CIDI | in tier | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-008 | CIDI | High (7 to 8) | Markdown | 6/10 | 7/10 | names CIDI | in tier after rerun | PASS, 4 of 4 labelled | kept | CLEAR 43/50, gate passed |
| PFW-009 | CIDI | Complex (9 to 10) | JSON | 8/10 | 8/10 | names CIDI | miss after rerun | PASS, 4 of 4 labelled | kept | CLEAR 44/50, gate passed |
| PFW-010 | TIDD-EC | Medium (5 to 6) | Markdown | 4/10 | 4/10 | names TIDD-EC | miss after rerun | PASS, 6 of 6 labelled | changed | CLEAR 44/50, gate passed |
| PFW-011 | TIDD-EC | High (7 to 8) | JSON | 6 | High (7/10) | names TIDD-EC | in tier after rerun | PASS, 6 of 6 labelled | changed | CLEAR 45/50, gate passed |
| PFW-012 | TIDD-EC | Complex (9 to 10) | Markdown | 8 | 8/10 | names TIDD-EC | miss after rerun | PASS, 6 of 6 labelled | kept | CLEAR 46/50, gate passed |
| PFW-013 | CRISPE | Medium (5 to 6) | Markdown | Medium | - | names CRISPE | in tier | PASS, 5 of 5 labelled | changed | CLEAR 43/50, gate passed |
| PFW-014 | CRISPE | High (7 to 8) | YAML | 6 | 6/10 | names CRISPE | miss after rerun | FAIL, 5 of 5 labelled | kept | CLEAR 44/50, gate passed |
| PFW-015 | CRISPE | Complex (9 to 10) | Markdown | 8/10 | 8/10 | names CRISPE | miss after rerun | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-016 | CRAFT | Medium (5 to 6) | Markdown | 6 (Medium-High) | - | names CRAFT | in tier | PASS, 5 of 5 labelled | kept | CLEAR 43/50, gate passed |
| PFW-017 | CRAFT | High (7 to 8) | Markdown | High (8/10) | - | names CRAFT | in tier | PASS, 5 of 5 labelled | changed | CLEAR 44/50, gate passed |
| PFW-018 | CRAFT | Complex (9 to 10) | Markdown | 8/10 | 8/10 | names CRAFT | miss after rerun | PASS, 5 of 5 labelled | changed | CLEAR 45/50, gate passed |
| PFW-019 | FRAME | High (7 to 8) | Markdown | 4/10 | 5 | names FRAME | miss after rerun | PASS, 5 of 5 labelled | kept | VISUAL 53/60, gate passed |
| PFW-020 | FRAME | Complex (9 to 10) | Markdown | High (7/10) | 7/10 | names FRAME | miss after rerun | FAIL, 2 of 5 labelled | kept | VISUAL 56/60, gate passed |
| PFW-021 | MOTION | High (7 to 8) | Markdown | 6/10 | 5/10 | names MOTION | miss after rerun | PASS, 6 of 6 labelled | kept | VISUAL 62/70, gate passed |
| PFW-022 | MOTION | Complex (9 to 10) | YAML | 6/10 | 6/10 | names MOTION | miss after rerun | FAIL, 1 of 6 labelled | changed | VISUAL 63/70, gate passed |
| PFW-023 | VIBE | High (7 to 8) | Markdown | 4/10 | Medium | names VIBE | miss after rerun | FAIL, 0 of 4 labelled | changed | EVOKE ~45/50, threshold 40+ passed |
| PFW-024 | VIBE-MP | Complex (9 to 10) | Markdown | 6/10 | 6/10 | names VIBE-MP | miss after rerun | FAIL, 0 of 4 labelled | kept | EVOKE-MP 43/50, gate passed |

---

## 5. FINDINGS

1. **The runtime never rates a prompt above 8/10.** No Complex-tier deliverable says 9 or 10. The four Complex items that count as in tier (SFW-003, SFW-009, SFW-020 and SFW-024) say High, which the checker accepts only because the skill's label scale ends at High. The rerun moved 5 of 32 misses into tier, SFW-003 only by writing High where its first attempt wrote High (7/10), so the rating barely moves between runs. The skill rates the prompt's own complexity on a 1 to 10 scale with the constraint "Do not add unrequested complexity" (`references/depth-framework.md` lines 126 to 127), and no rule says what a 9 or 10 is. The tier test therefore compares the runtime's rating with the tier each scenario was written for, and the scenarios aim higher than the runtime rates. Each scenario also expects its header to name its tier, for example "a Medium-tier CIDI prompt" in SFW-007, so a full grading would likely fail the 27 misses on that line. The Project rates lower than the skill on the same input: 6 of 24 in tier against 15 of 24.
2. **Creative frameworks are written as prose or platform syntax, not as labelled parts.** VIBE and VIBE-MP label 0 of 4 pillars in all four deliverables, as `references/visual-mode.md` asks: line 62 says briefs "Flow as natural prose describing UI intent", and the line 1058 checklist asks for "Narrative prose (not keyword list)". The Complex FRAME pair merges Focus, Rendering and Atmosphere into one unlabelled positive prompt for Stable Diffusion XL in ComfyUI. The Complex MOTION pair writes Kling's parameter list, where only Movement and Orchestration map to a MOTION part. No rule was traced as the cause of the FRAME and MOTION failures. The High FRAME and MOTION pairs pass. The VIBE and VIBE-MP scenarios ask for "every VIBE element labelled" (SFW-023 line 25, SFW-024 line 25 and their twins), which the prose rule contradicts, so a grading would fail all four on that line whatever the runtime writes
3. **CRISPE's Experiment part is the weakest text part.** PFW-014 fails because its `experiment` key holds only the response layout. SFW-014 and PFW-013 pass thinly, with Experiment holding the output structure or restating the Statement
4. **20 of 48 change a fact.** The ones that change what the prompt produces:
   - SFW-004 and PFW-004 turn "many speak Dutch as a second language" into Dutch as a first language and set English as the output language
   - PFW-017 counts the 60 shared mailboxes in the ticket-rate base, 1,210 users instead of 1,150, and adds the Outlook mobile app
   - SFW-012 loosens "Every claim cites a transaction ID" to let profile-based claims cite the KYC profile
   - SFW-008 loosens "never invented" commands to inferred commands marked `[Assumes: ...]`
   - SFW-022 and PFW-022 drop "no music and no voices"
   - SFW-019 turns the gravel dyke path into a grass-topped one, SFW-020 drops Leiden, and SFW-023 and PFW-023 put two images on screen where the input had the order photo next to the item

   [`structure-review.md`](structure-review.md) lists every one with the exact wording
5. **45 of 48 add scope.** Most additions are small: an extra output field, an overview section or a checklist group. The review marks rule-mandated additions, such as the `$vibe` UX floor, as such
6. **Self-reported scores do not track structure or facts.** Every deliverable reports a passing score, CLEAR 42 to 46 of 50, VISUAL 53 to 56 of 60 for images and 62 to 64 of 70 for video, and EVOKE 43 to 46 of 50. That includes the 9 structure FAILs and the 20 fact changes. Three scores are approximate: SFW-014 `~44/50`, SFW-024 `~46/50` and PFW-023 `~45/50`
7. **Format details.**
   - The eight YAML files write the header as a plain line or, in SFW-007, as a quoted YAML key, so a whole-file parse needs the header stripped. That is rule gap 5 of the [2026-09-25 run README](../2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/README.md) section 11
   - Two briefs run over their word range: SFW-023 at 315 words against VIBE's 100 to 300, and SFW-024 at 484 against MagicPath's 150 to 400
   - 23 files carry 119 em dashes and 6 en dashes. They are verbatim run output, and the skill states no voice rule for the prompts it writes
8. **Every header named its framework, despite the format guides.** The header templates in `assets/format-guide-json.md` line 127, `format-guide-yaml.md` line 128 and `format-guide-markdown.md` line 118 all read `Framework: [RCAF/CRAFT]`, which could have pulled COSTAR, CIDI, TIDD-EC or CRISPE work toward them. No header drifted, but every input also named its framework
9. **Two extraction misses, fixed in this run's collector only.** PFW-007 put its header above the fence, and PFW-001's rerun reported `export/[001] - ...`. Section 3 gives both changes. The other run folders' collectors do not have them

---

## 6. DELIVERABLES

The 48 deliverables sit in `export/benchmark/skill/` and `export/benchmark/claude project/` under `<ID> - <number> - <name>`. They are verbatim run output. Nobody edited them, and the collector would warn on any file that differs from the run's copy. Four Project files carry `NNN` as their number, the slot the Project writes for a sequence number it cannot know, as the older PFM and PID files also do.

**Replaced on 2026-09-27.** The [2026-09-27 complexity-rubric run](../2026-09-27--complexity-rubric--claude-sonnet-5-xhigh/README.md) reran these 48 scenarios after the skill gained a complexity rubric, and its deliverables replaced these in `export/benchmark/`. These 48 stay in git history, last at Prompt Improver `4c3d25f`, and this record still describes them.

---

## 7. NEXT STEPS

1. **Operator decision on the tier test.** The runtime's own rating decides the tier, and it stops at 8/10. The options are to accept the rating as the skill's honest reading, to add a complexity rubric to the skill (a rule change outside this run), or to drop the tier from the check and keep the input's intent as the tier
2. **Operator decision on labelled creative parts.** The VIBE and VIBE-MP scenarios require labelled pillars, and the prose rule in `references/visual-mode.md` forbids the keyword-list shape labels tend to produce. Either the four scenarios accept pillars that are present as prose, or the rule allows labels. FRAME and MOTION at Complex fell back to platform syntax without a rule asking for it
3. **Grade the 48 against their Pass/fail lines.** This run checked header, tier, format and structure. A full grading decides whether the 20 fact changes and the added scope fail their scenarios, as the scope test says they should
4. **Carry the two collector changes forward.** Put the header-above-fence step and the bracketed number into the collector the next run copies
5. **Look at the Project's lower ratings.** The Project misses its tier 18 times against the skill's 9 on the same inputs. Knowing whether the kernel or the retrieval causes it tells the tier decision which side to trust

The operator decided items 1 and 2 on 2026-09-27: the skill gained a complexity rubric, and the VIBE and VIBE-MP scenarios now accept pillars written as prose. The 2026-09-27 run measures both.
