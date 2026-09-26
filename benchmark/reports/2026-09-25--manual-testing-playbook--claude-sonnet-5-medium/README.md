# Prompt Improver: playbook run, 2026-09-25, claude-sonnet-5 at effort medium

## 1. Handover status

Both identity handovers passed. SID-001 is PASS on a real export path it wrote and verified, and PID-001 is PASS on the verbatim `Canvas Artifact` string plus the no-save Canvas contract. No handover failed, so no row in `results.csv` carries `after_failed_gate = yes`.

---

## 2. Verdict counts

| Runtime | Scenarios | PASS | FAIL | SKIP |
|---|---:|---:|---:|---:|
| Skill | 7 | 5 | 2 | 0 |
| Project | 7 | 6 | 1 | 0 |
| **Total** | **14** | **11** | **3** | **0** |

The three FAILs are STX-001 and SFM-001 on the skill side and PIR-002 on the Project side. No chain stopped short (28 of 28 turns ran), so no verdict is PARTIAL. Twins: 4 agree and 3 disagree.

Every count here and in `results.md` comes from `results.csv`. Run from this folder:

```bash
python3 -c "import csv,collections as c;r=list(csv.DictReader(open('results.csv')));print(len(r),'rows');[print(k,dict(sorted(c.Counter(x['result'] for x in r if x['runtime']==k).items()))) for k in ('skill','project')];print('all',dict(sorted(c.Counter(x['result'] for x in r).items())));print('after_failed_gate',dict(c.Counter(x['after_failed_gate'] for x in r)));print('facts_intact',dict(c.Counter(x['facts_intact'] for x in r)))"
```

```text
14 rows
skill {'FAIL': 2, 'PASS': 5}
project {'FAIL': 1, 'PASS': 6}
all {'FAIL': 3, 'PASS': 11}
after_failed_gate {'no': 14}
facts_intact {'yes': 12, 'n-a': 2}
```

The twin counts come from `python3 benchmark/grader/twin_divergence.py <this folder>`, run from `AI Systems/Prompt Improver/`, which reads the same `results.csv` (section 6).

---

## 3. How the run was made

- Runner: `run/playbook_runner.py` in this folder, at hash `a0315dcd5b`, started as `python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-sonnet-5 --effort medium --jobs N`. The phase 002 record gives both facts and sets Prompt Improver at 2 parallel sessions
- Engine `claude` (Claude Code 2.1.282 per `manifest.json`), model `claude-sonnet-5`, effort `medium`, 2 parallel sessions
- Playbook at Barter `4fb9dd88`
- 14 scenarios and 28 turns, every scenario on its first attempt. Every `meta.json` reports 2 of 2 turns, and every event stream reports `claude-sonnet-5`
- Skill sandbox: a copy of the system without `.git`, `benchmark/`, the playbook, `export/` or `changelog/`, with an empty `export/`. The system prompt is `AGENTS.md`, and the tools are Read, Bash, Edit, Write, Glob and Grep
- Project sandbox: a copy of `claude project/`. The system prompt is the kernel plus the retrieval note (`run/playbook_runner.py` lines 67 to 72 and 595), and the tools are Read, Glob and Grep. A terminal has no Canvas panel, so the reply text stands in for it under each Project precondition
- Grading read each scenario file whole, the root rules, the skill and Project rule files, every reply, every per-turn ledger in `meta.json`, the skill `exports/` copies and the event streams wherever a save, a parse or an edit had to be proven. `grading-notes.md` holds the evidence and the second reads

### Files in this folder

| File | What it holds |
|---|---|
| `results.csv` | One row per scenario, the verdict source for every count |
| `results.md` | The 14 verdicts and the twin table, printed from `results.csv` |
| `grading-notes.md` | Evidence, quotes, graded delivery, second reads and adjudications |
| `deliverable-lint.csv` | Written by `check_report.sh` through `lint_replies.py` |
| `hvr-lint.csv` | One row per reply. No HVR linter exists here, see section 7 |

---

## 4. Comparison with 2026-09-17

The earlier run used the same model and effort through a different harness, `run_packaging.sh` in the Claude Project Sync Loop folder, and wrapped each Project block in `<DELIVERABLE>` tags at capture. Commit `4fb9dd88` then changed every scenario file except SIR-001, so most rows below are not comparable.

| ID | 2026-09-17 | 2026-09-25 | Comparable | What changed in 4fb9dd88 |
|---|---|---|---|---|
| SID-001 | PASS | PASS | no | Unconditional Turn 2, identity ordering carve-out |
| PID-001 | PASS | PASS | no | Unconditional Turn 2, Canvas stand-in precondition, identity ordering carve-out |
| SIR-001 | PASS | PASS | yes | File unchanged, only the harness differs |
| PIR-001 | PASS | PASS | no | Canvas stand-in precondition added |
| SIR-002 | PASS | PASS | no | Turn 2 now must pass CLEAR, save the next `.md` export and reply path-first |
| PIR-002 | PASS | FAIL | no | Canvas stand-in precondition added, and it decides this run's FAIL |
| STX-001 | PASS | FAIL | no | Unconditional Turn 2, a reply that does not lead with the path added as a FAIL |
| PTX-001 | FAIL | PASS | no | Unconditional Turn 2, stand-in precondition, commentary defined |
| SFM-001 | FAIL | FAIL | no | Unconditional Turn 2, header label loosened to `$json` or `$improve` |
| PFM-001 | FAIL | PASS | no | Unconditional Turn 2, header and attestation made pass conditions |
| SCR-001 | PASS | PASS | no | Unconditional Turn 2 |
| PCR-001 | PASS | PASS | no | Unconditional Turn 2, stand-in precondition |
| SSB-001 | PASS | PASS | yes | One Overview sentence only (a stray "deal-like deliverable" dropped), Pass/fail unchanged |
| PSB-001 | PASS | PASS | no | Canvas stand-in precondition added |

The eight scenarios with an unconditional Turn 2 (SID, PID, STX, PTX, SFM, PFM, SCR and PCR) ran as one turn in 2026-09-17 and are not comparable. PIR-001, PIR-002, PSB-001 and SIR-002 had their criteria changed as well. Only SIR-001 and SSB-001 compare, and both passed both times. The totals happen to match (11 PASS and 3 FAIL both times), but they are built from different scenarios, and the skill and Project splits moved from 6 and 5 passes to 5 and 6.

---

## 5. Divergence summary

Three twins disagree. All three are runtime faults: both packagings carry the rule, and one model broke it.

| Pair | Skill | Project | Class | Deciding rule, both sides |
|---|---|---|---|---|
| IR-002 | PASS | FAIL | runtime fault | Deliverable first: `AGENTS.md` line 61 and kernel lines 319, 321 and 401. The Project model opened Turn 2 with a route disclosure and a no-Canvas note |
| TX-001 | FAIL | PASS | runtime fault | Scope ban: `SKILL.md` lines 507 to 508 and 621, kernel lines 291 and 335. Only the skill model added a meta description output |
| FM-001 | FAIL | PASS | runtime fault | Scope ban: `SKILL.md` lines 507 to 508, kernel line 335. The skill Turn 2 revision added a `risks_and_blockers` extraction |

Each class was tested from a second direction, recorded in `grading-notes.md` section 4. For IR-002, five other Project deliveries under the same kernel put the block first, and no Project source asks for a route disclosure. For TX-001 and FM-001, no source on either side mentions SEO, meta descriptions, risks or action items, so neither packaging seeded the addition.

---

## 6. What check_report.sh found

Run from `AI Systems/Prompt Improver/`:

```bash
bash benchmark/grader/check_report.sh "benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium"
```

It exited 2, meaning both of its two checks reported findings. The code counts checks, not defects.

- `twin_divergence`: "FM-001: skill FAIL, Project PASS", "IR-002: skill PASS, Project FAIL", "TX-001: skill FAIL, Project PASS", with 4 agreed, 3 disagreed, 0 not settled and 0 unpaired. This matches the manual adjudication exactly
- `lint_replies`: 8 clean of 28, written to `deliverable-lint.csv`. The 14 skill replies and 5 Project turns that correctly render no block show `attestation_missing` and `header_missing` by design, since the linter reads the kernel's block contract. PTX-001 Turn 1 shows `attestation_missing` although its attestation is present, because the line is italic and `deliverable_lint.py` line 58 matches only `^Attestation:`. The 8 clean replies include PIR-002 Turn 2, the one real ordering defect in the run, because `deliverable_not_first` runs only inside `<DELIVERABLE>` tags (`deliverable_lint.py` line 42) and this runner writes none

No linter finding changes a verdict. Both blind spots are follow-up findings below.

---

## 7. hvr-lint.csv

The 2026-09-17 folder has no `hvr-lint.csv`. Its only lint file is `deliverable-lint.csv` from `check_report.sh`, and its README records no HVR command. The fallback the brief names, `benchmark/grader/hvr_lint.py`, does not exist in Prompt Improver, and the system is not registered in the fleet format gate (`systems.cjs` in the Claude Project Sync Loop folder names four other systems at lines 30, 113, 144 and 167). Prompt Improver states no voice rule for the prompts it writes (grader `README.md` section 2). So no HVR lint ran. `hvr-lint.csv` has one row per reply marked `not run`, with raw counts of U+2014 and of semicolon characters, written by this command from this folder:

```bash
python3 -c "import csv,pathlib;rows=[{'file':p.name,'hvr_lint':'not run','em_dash_u2014':p.read_text(encoding='utf-8').count(chr(0x2014)),'semicolon':p.read_text(encoding='utf-8').count(chr(59)),'note':'no benchmark/grader/hvr_lint.py in Prompt Improver, counts are raw characters and decide nothing'} for p in sorted(pathlib.Path('replies').glob('*.txt'))];w=csv.DictWriter(open('hvr-lint.csv','w',newline='',encoding='utf-8'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)"
```

All 28 replies carry zero em dashes. Eight carry semicolons, five of them inside Project blocks.

---

## 8. Follow-up findings

Findings are reported, never repaired here. Each names the files on both sides.

### Recorded rule conflicts this run touched

1. **One comprehensive question against Standard flow's three interactions.** `references/interactive-mode.md` lines 45 and 418, and the knowledge mirror lines 31 and 404. Touched by SIR-001 Turn 1, which asks "two things" in one message, and by the questions PID-001 and PIR-001 asked after delivering on Turn 2. No verdict turned on it
2. **Perspectives inside the deliverable.** `references/depth-framework.md` lines 89 and 223, and the DEPTH knowledge lines 76 and 210, against kernel lines 320 and 340. Exercised by every Project delivery. All six kept scores and perspectives in chat, the kernel side. No verdict turned on it
3. **`SKILL.md` line 639 says the Project mirrors the skill.** Not exercised by any reply
4. **No rule places an identity answer relative to the delivery.** Touched by both handovers. SID-001 put the path first and PID-001 put the block first, each with the identity answer after it. Both scenario files carve the ordering out (line 47)
5. **The `$json` or `$improve` header label.** Touched. SFM-001 wrote `Mode: $json`, following `assets/format-guide-json.md` lines 125 to 128. PFM-001 wrote `Mode: $improve`, following kernel line 372. Both pass under line 30 of their scenario files

### New findings

1. **No rule decides whether a flagged extra output counts as a default or as an invented requirement.** `SKILL.md` lines 507 to 508 and 621 and kernel line 335 ban invented requirements. `SKILL.md` line 45 and kernel line 18 allow constraints that serve the stated outcome, and `SKILL.md` lines 461 and 500 allow flagged defaults. SFM-001 rests on this line alone (`risks_and_blockers`), and STX-001 in part (its meta description, beside the in-place edit). The test used is written out in `grading-notes.md` section 1 for the operator to confirm or replace
2. **No rule covers revising a delivered export.** `SKILL.md` line 417 names the next sequence number for a save, and `AGENTS.md` lines 34 to 50 cover saving, but nothing says whether a revision may edit an earlier file. The skill scenarios' Turn 2 rows (line 39) allow only a new number or no file. STX-001 Turn 2 edited `export/001` in place, so the collected `export/benchmark/skill/STX-001 - 001 - ...` is the Turn 2 edit, not the graded Turn 1 file
3. **The stand-in rule defines commentary in one of seven Project files.** Only `project-text-modes/improve-flow-clear-canvas.md` line 30 says a heading or an environment note before the header counts as commentary. The shared precondition (line 26 in six files, line 43 in PID-001) does not. PIR-001 Turn 2 opens with a bold "Canvas Artifact (side panel)" label and passes under its own file, but would fail under PTX-001's
4. **The stand-in rule says where a block starts, not where it ends.** PTX-001 Turn 1 fences the header and prompt and puts the attestation as an italic line below the fence. It was read as inside the block, by the same logic line 30 applies to a fence around the header, but no text says so
5. **Parity-gap candidate on the JSON header.** Kernel line 380 says the header and attestation sit outside the JSON format lock. The skill requires the header (`SKILL.md` lines 410 and 555, `assets/format-guide-json.md` lines 125 to 128 and 427) and never says whether it survives a user asking for valid JSON only. On the same Turn 2 input, SFM-001 dropped its header and PFM-001 kept its own
6. **The two to three sentence summary is exceeded almost everywhere.** `AGENTS.md` lines 42 and 63, `SKILL.md` line 421 and kernel line 387 ask for it. Ten of the twelve graded deliveries run past it. The root makes it advisory (line 144). STX-001 and PTX-001 name the band in their Expected signals (line 30) but not in their Pass/fail lines (32, 66 and 67), so whether it can decide those two is unsettled
7. **"One question" in SIR-001 and PIR-001.** Line 30 of both files asks for the mode "in one question", while `SKILL.md` lines 395 to 396 and `AGENTS.md` line 28 require one consolidated question covering every missing essential. When the prompt text is also missing, the consolidated message necessarily asks two things, as SIR-001 Turn 1 did. Graded as one question, since the Fail line (line 67) names a runtime that "splits the question across messages"
8. **The reply linter cannot see ordering in this runner's captures.** `deliverable_not_first` and `scoring_inside_block` need `<DELIVERABLE>` tags (`deliverable_lint.py` line 42, grader `README.md` section 2), which `run/playbook_runner.py` never writes. The attestation pattern at `deliverable_lint.py` line 58 misses an italic attestation, as the header pattern at line 67 missed a bold header in 2026-09-17
9. **No HVR linter for Prompt Improver.** See section 7. Either add one or drop `hvr-lint.csv` from this system's report contract
10. **`results.md` is renderer-owned by the root.** `manual-testing-playbook.md` line 14 says `results.md` is never hand-authored, while the phase 003 brief asks for one. The file here was printed from `results.csv` by a script, with the twin classes carried from `grading-notes.md`
11. **Three skill turns answered without reading `SKILL.md`.** `AGENTS.md` line 85 says to read it before processing any request. SIR-002 Turn 1 and both SSB-001 turns made zero tool calls. Their replies still held the contract, since `AGENTS.md` alone carries the boundary and question rules
12. **Route disclosure is a skill-only rule.** `SKILL.md` line 336 says to disclose a semantic route briefly when useful. The kernel and knowledge carry no counterpart, yet PIR-002 disclosed its route anyway, ahead of the block

---

## 9. Edited after grading

The 18 deliverables this run collected into `export/benchmark/skill/` and `export/benchmark/claude project/` were improved by hand on 2026-09-26. Every verdict in `results.csv`, `results.md` and `grading-notes.md` still describes the graded originals. Git history keeps those at Prompt Improver commit `59a50ac` and Barter commit `ab96eebb`, and the run's own copies under `skill/` and `claude project/` in this folder are unchanged.

- **Kept:** each file name, the `Mode:` header, the Project attestation footer, every fact the user supplied and each scenario's own limits, such as the 120 word cap in SID-001
- **Improved:** role, objective, success criteria, output shape and the handling of missing or unclear input, judged against the routed rubric
- **Removed:** the two extras this run failed for, STX-001's meta description and the `risks_and_blockers` extraction in SFM-001 Turn 2, since the scope test in `SKILL.md` now counts a flagged extra output as scope expansion
- **Changed by judgment:** STX-001 and PTX-001 now default the brewing method to French press, so STX-001's reply in `replies/` still names two methods where the export names one. SFM-001 002 carries its `Mode:` header again, which the graded Turn 2 revision had dropped. `assets/format-guide-json.md` requires the header, and kernel line 380 keeps it outside the JSON lock, so "valid JSON only" binds the body. SIR-001 now states the household size and the number of days as words rather than as placeholders

A collection over this folder now keeps an export that differs from the run's copy and prints one warning line for it. `--force` restores the run's copy. Run from `AI Systems/Prompt Improver/`:

```bash
python3 -B "benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/run/collect_exports.py" "benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium" export/benchmark --dry-run
```

It prints 18 lines like this one and exits 0:

```text
warning skill STX-001 - 001 - enhanced-coffee-brewing-beginners-blog-post.md differs from the run's copy, so it was edited after collection and is kept. --force overwrites it
```

`run/selftest.py` proves the guard on a synthetic run in a temporary folder. It checks a fresh collection, a dry run, a kept skill export, a kept Project export and `--force`. A negative control runs the collector as it was before the guard and shows that it overwrites the edited file. It ends `selftest: all checks passed`.

---

## 10. Example pack

`export/benchmark/examples/` holds eight prompts for the modes and formats this run does not show: `$deep`, `$short`, `$refine`, `$raw`, `$text $yaml`, `$improve $markdown`, `$video $yaml` and `$vibe`. Each answers the Turn 1 input of one new skill scenario (section 11). They were written through the skill on 2026-09-26, and no run graded them. [Its README](../../../export/benchmark/examples/README.md) lists each command, format and the writer's own score.

---

## 11. Playbook after this run

The playbook grew from 14 to 30 scenarios after this run, at root version 1.1.0.0.

- **New:** eight skill and Project pairs, STX-002 to STX-005, SFM-002, SFM-003, SCR-002 and SCR-003 with their Project twins, one per mode or format named in section 10
- **Tightened:** the 14 scenarios graded here keep their IDs, purposes and exact Turn inputs. The 28 scenarios that grade a delivered prompt state the scope test, and the 24 whose Turn 2 asks for a revision state the revision rule. All 15 Project files share one commentary definition that also says where the block ends. The 14 keep the summary band advisory in every Pass/fail line, and SIR-001 and PIR-001 ask for one consolidated question. That settles findings 3, 4, 6 and 7 of section 8 in the scenario files
- **Not comparable:** a rerun grades the 14 against changed criteria, so its verdicts compare with section 2 only as section 4 compares this run with 2026-09-17

Writing the new scenarios and examples surfaced eight rule gaps. They are recorded here and not repaired, since the skill and kernel rules stayed unchanged:

1. **Question routing for `$short`, `$refine` and `$deep`.** `references/interactive-mode.md` routes `$short` to a format question and `$refine` to a refinement-type question, and its flow pattern shows a question step for Deep. `SKILL.md` line 383 asks only when essential context is missing. The new scenarios accept either path
2. **The `$vibe` library question.** `references/visual-mode.md` lines 843 to 845 make the component library question mandatory, while `SKILL.md` line 383 asks only when essential context is missing. SCR-003 and PCR-003 record a skipped question as a finding, not a FAIL
3. **A format question under `$markdown`.** `references/interactive-mode.md` line 217 routes `$improve` to a format question, while `SKILL.md` line 71 hands the format decision to a format command. SFM-003 and PFM-003 record such a question rather than fail it
4. **Veo audio against the scope test.** `references/video-mode.md` lines 226 to 228 tell every Veo prompt to include an `Audio:` section, while `SKILL.md` line 511 counts a section the user did not ask for as scope expansion. The Veo and `$vibe` scenarios record these rule-added sections and never grade them
5. **The YAML header does not parse.** `assets/format-guide-yaml.md` section 4 gives a header line starting `Mode:`, which breaks a YAML parser. The YAML examples use the comment form `# Mode: $yaml | ...`. The likely fix is to make the guide's header a comment
6. **No revision rule in the kernel.** `SKILL.md` lines 421 to 422 and `AGENTS.md` line 70 save a revision under the next number. The kernel says nothing, so the Project side states the rule only in its scenario Turn 2 rows
7. **Summary band against delivery shape.** The root's Advisory list (line 141) lets an advisory item fail a scenario that exists to test delivery shape, and STX-001 and PTX-001 test delivery shape. The scenarios now keep the band advisory, which the operator may overrule
8. **The identity ordering carve-out.** SID-001 and PID-001 still carve out where the identity answer sits relative to the delivery, since no rule places it (section 8, conflict 4)

---

## 12. Next steps

1. Rerun the 30-scenario playbook on the skill and the Project, then grade it. That grades the eight new scenarios for the first time and gives the examples in `export/benchmark/examples/` a verdict
2. Operator decision on the eight rule gaps in section 11, starting with the YAML header, the question routing and Veo audio, which the new scenarios exercise
3. Operator decision: whether a heading label before the header counts as commentary in every Project file. The tightened scenarios say it does, so PIR-001's Turn 2 reply here would now fail
4. Follow-up repair outside the playbook: a header rule for "valid JSON only" on the skill side to match kernel line 380
5. Tooling: have `run/playbook_runner.py` wrap Project blocks in `<DELIVERABLE>` tags, or teach `deliverable_lint.py` to find a fenced block, so the ordering check runs. Widen the attestation pattern at line 58 to allow markup
6. Decide whether `hvr-lint.csv` belongs in this system's report contract
