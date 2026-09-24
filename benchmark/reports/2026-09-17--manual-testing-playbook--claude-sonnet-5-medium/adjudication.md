# Twin divergence adjudication, Prompt Improver, 2026-09-17 run

Adjudicates the one twin pair `twin_divergence.py` reported as disagreeing over this report directory. Report only, nothing repaired, nothing committed. Paths are relative to `AI Systems/Prompt Improver/` unless stated otherwise.

Verdict in one line: `TX-001` is a **runtime fault** on the defect that decides the FAIL, and the second recorded reason for that FAIL, the missing `Score:` header field, is a **rule gap** that should never have been carried as a co-cause because this scenario's own pass line does not fail on it.

| Pair | Skill | Project | Class | The defect that decides it |
|---|---|---|---|---|
| `STX-001` / `PTX-001` | PASS | FAIL | runtime fault | transparency reporting rendered before the Deliverable Block |

Two recorded reasons, adjudicated separately because they do not share a class:

| Recorded reason | Class | Decides the FAIL |
|---|---|---|
| transparency summary before the Mode line, prompt and Attestation | runtime fault | yes, named first in the scenario's own fail line |
| header line carries no `Score:` field | rule gap | no, the scenario fails on an absent score and the score is present in chat |

---

## 1. Evidence base

Five sources. Three are independent of this report's own files.

- both replies read in full: `replies/PTX-001.md` (33 lines, one turn) and `replies/STX-001-turn1.md` plus `replies/STX-001-turn2.md`
- both scenario files read in full, plus `sk-prompt-improver/manual-testing-playbook/manual-testing-playbook.md`
- the rule documents of both packagings: `AGENTS.md`, `sk-prompt-improver/SKILL.md`, `claude project/Custom Instructions.md`, and on each side the DEPTH, Interactive Mode and Format Guide Markdown documents
- the live session transcript the committed run left behind, recovered from `~/.claude/projects/-private-var-folders-3c-...-T-packaging-harness-Prompt-Improver-project/59E9BA57-286F-4FF9-88AF-38EB502A8D2E.jsonl`. It carries every tool call the committed `PTX-001` run made, which `replies/PTX-001.md` does not
- three fresh harness runs made for this adjudication, all through `z — Parity Gate/run_packaging.sh` at the harness defaults this report used:
  - Project, session `268C2720-D75B-4B8E-928F-C719D3396776`, `--no-write`, both playbook turns
  - skill, session `EB01B26F-633E-4738-8A75-E3E67837584C`, both playbook turns

The harness was not edited. `deliverable_lint.py` was read, not modified.

### What the committed run actually opened

From the transcript, in call order, `PTX-001` turn 1 made one `Bash` discovery call, then read four knowledge documents with one `ToolSearch` call between the second and the third:

1. `Prompt Improver - DEPTH Thinking Framework - v0.200.md`
2. `Prompt Improver - Interactive Mode - v0.700.md`
3. `Prompt Improver - Assets - Framework Pattern Library - v0.100.md`
4. `Prompt Improver - Format Guide Markdown - v0.141.md`

It wrote no file. This read list is load-bearing twice below, once because the last document read is the one that specifies a three-field header, and once because the two documents that order delivery ahead of reporting were both in view.

---

## 2. What the two replies did

The pair is not as clean a comparison as `results.csv` makes it look, and that is worth stating before either defect.

- `STX-001` turn 1 asked one consolidated question and wrote no file. Turn 2 delivered
- `PTX-001` delivered on turn 1 and never needed a turn 2

Both are permitted. Each conversation chain's turn 1 row allows either a delivery or one consolidated question. So the two committed twins were not graded on the same delivery event. The fresh runs settle which way that cuts: the Project side asked one consolidated question on turn 1 and delivered on turn 2, the same shape the committed skill side took, and the skill side did the same. The turn 1 branch is within-packaging variance at a permitted fork, not a packaging difference. Nothing in the divergence follows from it.

What each delivery looked like:

- `replies/PTX-001.md:1` to `:8` is a `# Phase D–E–P–T–H Summary (Standard Energy)` section carrying **Detected** (mode, energy, complexity, framework, with the COSTAR-beats-RCAF score), **Perspectives applied (3)** and **Assumptions flagged**. The `<DELIVERABLE>` tag opens at `:11`, the header line sits at `:13`, the attestation at `:23`. The chat report follows at `:29` to `:31` with the export-equivalent path, `CLEAR 42/50 (C:8 L:8 E:12 A:8 R:4) | Perspectives: 3 | Gate passed` and a two sentence summary
- `replies/STX-001-turn2.md:1` is `Saved: ` and the export path. Line `:3` is the compact score, `:5` the summary. No transparency section precedes the path

Everything else on the Project side is correct and worth recording so the repair phase does not chase it: CLEAR passed at 42 of 50 with every floor met, the attestation carries both `execution = did not occur` and `save = did not occur`, no save was claimed, the coffee subject and the beginner audience were retained, and no requirement was invented.

---

## 3. The ordering defect: runtime fault

### The rule, on both sides

Project side, five statements in two documents, all putting the report after the deliverable:

- `claude project/Custom Instructions.md:321` "16. ALWAYS render the Deliverable Block as a Canvas Artifact before any commentary, because this Project cannot write files."
- `claude project/Custom Instructions.md:323` "18. ALWAYS put transparency reporting (score, assumptions, docs consulted) in chat after the Deliverable Block."
- `claude project/Custom Instructions.md:404` "The Deliverable Block came before any commentary, and no execution, save or verification was claimed."
- `claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md:26` "Start --> Single Question (ALL info) --> Wait --> Process (DEPTH) --> Deliver --> Report"
- the same document at `:237` and `:240`, the state machine: `delivery: action: create_artifact` then `reporting: action: show_transparency_report`

Skill side, the same rule in the form its packaging can carry:

- `sk-prompt-improver/SKILL.md:496` "24. ALWAYS put transparency reporting in chat after file delivery."
- `AGENTS.md:34` "**BLOCKING REQUIREMENT**: Save ALL enhanced prompts to `export/` before responding to the user. This is non-negotiable." with the numbered Strict Sequence at `:38` to `:42` ending "5. Only then respond with the file path and a brief 2-3 sentence summary", `:61` "Start with the saved file path" and `:68` "Prohibited: Showing output before saving"
- `sk-prompt-improver/references/interactive-mode.md:40`, `:251` and `:254` carry the Project's flow and state machine unchanged

So the rule reached both packagings. This is not a parity gap.

The word **assumptions** in `Custom Instructions.md:323` is the one that settles the reading. `PTX-001`'s prefix carries a flagged-assumptions paragraph, which that line places after the block by name, not by inference.

### Why the wording does not permit it

There is real pressure in the other direction and it should be named rather than waved off, because it is what the repair has to resolve.

- `claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md:105` and `:138` give per-phase `**User-Facing Update:**` templates, for example `" **Phase D - Discover:** Analysing from [X] perspectives | **Synthesis:** [findings]"`. The reply's prefix is written in exactly that register
- the same document at `:210`, inside the Harmonize phase, requires "Mode, Framework, Perspectives, CLEAR score in deliverable", with "On Fail: Add missing fields"
- `Custom Instructions.md:342` NEVER 11 forbids "scoring breakdowns, processing notes or format options inside the Deliverable Block", and `:375`'s header template names four fields, none of them Perspectives

So the Project packaging requires Perspectives in the deliverable while forbidding the block from carrying it. That is a real contradiction and it is section 5's first item. What it does not do is license the ordering the runtime chose. A phase-update template is a register for a live conversational update, not an instruction about where a single reply's deliverable sits, and `Interactive Mode - v0.700.md:26` already places the DEPTH process ahead of Deliver and Report both. Nothing on either side says the transparency report may precede the block, and four Project statements say it may not. The wording does not permit it.

### Second direction, two of them

**Behaviour, from three fresh runs.** Same model and effort, fresh sessions, write tools withheld on the Project side so the reply under test is one the deployed packaging could produce:

| run | leads with | block or path position |
|---|---|---|
| committed `PTX-001` | Phase D-E-P-T-H Summary, 8 lines | block at line 11 |
| fresh Project turn 2 | `**Phase D–E (Discover/Engineer) — condensed:**` | block at line 5 |
| committed `STX-001` turn 2 | `Saved: export/001 - ...` | path at line 1 |
| fresh skill turn 2 | `Saved: export/001 - ...` | path at line 1 |

Two Project deliveries out of two lead with a phase summary. Two skill deliveries out of two lead with the path. The fresh Project run read the same DEPTH and Interactive Mode documents as the committed one, so the pressure and the prohibition were both in view in both cases. Reproducibility of a fault is not permission to commit it, and this is the shape it takes here: the Project runtime resolves a genuine tension the wrong way each time it meets it, while the skill runtime never gets the chance to, because `AGENTS.md:38` to `:42` sequences the file write ahead of any chat token.

**The same runtime, the same packaging, five other replies in this run.** Walking the six Project replies that carry a `<DELIVERABLE>` tag and printing everything before it:

| reply | what precedes the block |
|---|---|
| `PIR-001-turn2.md` | nothing |
| `PFM-001.md` | nothing |
| `PCR-001.md` | `## Deliverable`, a bare heading |
| `PIR-002-turn2.md` | one sentence disclosing that this sandbox has no Canvas panel |
| `PID-001.md` | an identity answer and a delivery-contract explanation |
| `PTX-001.md` | the eight-line transparency section |

`PTX-001` is the only one whose prefix is the transparency reporting `Custom Instructions.md:323` places after the block. Two of the six carry nothing at all. The instruction set is followable inside this packaging, by this runtime, in this run. That is what separates a fault from a rule gap.

### On the advisory carve-out

`manual-testing-playbook.md:143` makes advisory "Response ordering beyond the required Artifact-first or path-first shape". Read literally, commentary before the Artifact is not ordering *beyond* the required shape, it is a breach *of* the required shape, so the carve-out never reaches it and the question of whether `PTX-001` exists to test delivery shape does not need answering. The report arrives at the right place by the longer route. Recorded because the shorter route is the one a repair should rely on.

---

## 4. The `Score:` header field: rule gap, and not a fail condition

### The two templates disagree inside one packaging

- `claude project/Custom Instructions.md:375`, the DELIVERY PROTOCOL template: `Mode: $[mode] | Complexity: [level] | Framework: [Framework] | Score: [CLEAR/EVOKE/VISUAL score]`, four fields
- `claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md:104`, the template that document calls the markdown deliverable header: `Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT]`, three fields, no Score

The three-field form is not a slip in that document. Every worked example in it repeats it, at `:125`, `:135`, `:163`, `:207` and `:244`. The JSON and YAML guides carry the same three-field header at `:113` and `:114`. `Custom Instructions.md:317` tells the runtime "11. ALWAYS consult the relevant mode Knowledge before its library asset", so the document that disagrees with the kernel is one the kernel sends the runtime to.

The skill side has no `Score:` header rule at all. `sk-prompt-improver/SKILL.md:555` reads "Header includes mode with `$` prefix, complexity and framework", and `sk-prompt-improver/assets/format-guide-markdown.md:118` carries the same three-field template. A grep for `Score:` across `AGENTS.md`, `SKILL.md` and the skill assets returns hits only in the mode libraries, every one of them a `**VISUAL Score:**` or `**EVOKE Score:**` line sitting outside the fenced example it annotates. No header rule on the skill side names the field.

So the wording permits a three-field header on both sides. That is the rule gap definition, met.

### Second direction, two of them

**The transcript's read order.** The committed `PTX-001` run read `Format Guide Markdown - v0.141.md` last, immediately before composing the reply, and the header it produced at `replies/PTX-001.md:13` is `Mode: $text | Complexity: 3 | Framework: COSTAR`, which is that document's template exactly. The runtime followed the more specific document it had just opened. That is not a runtime acting otherwise than instructed, it is a runtime choosing between two instructions.

**The same instruction set produces both headers.** The fresh Project run read the same four documents, including the same Format Guide, and produced `Mode: $improve | Complexity: 3/10 (Low) | Framework: COSTAR | Score: CLEAR 43/50`, four fields. Counting every Project reply in this run that renders a header line, by grep rather than by eye:

| reply | header |
|---|---|
| `PCR-001.md:4` | `**Mode:** $image \| **Platform:** Midjourney v6.1 \| **Complexity:** 3 \| **Framework:** FRAME \| **Score:** VISUAL 54/60` |
| `PID-001.md:14` | `**Mode: $improve \| Complexity: 2/10 \| Framework: RCAF \| Score: CLEAR 44/50**` |
| `PIR-001-turn2.md:3` | `Mode: $short \| Complexity: 2/7 \| Framework: RCAF \| Score: CLEAR 44/50` |
| `PIR-002-turn2.md:5` | `Mode: $short \| Complexity: 2/10 \| Framework: RCAF \| Score: CLEAR 44/50` |
| `PTX-001.md:13` | `Mode: $text \| Complexity: 3 \| Framework: COSTAR` |

Four of five carry Score, five of six including the fresh run. A rule that the same runtime satisfies most of the time and drops the rest of the time, under a document set that states it both ways, is permissive wording rather than a violated instruction.

### It is not this scenario's fail condition

`project-text-modes/improve-flow-clear-canvas.md:32` fails on "the score is absent", and `:67` on "missing score". `:30` places the score in chat: "the chat reports the export-equivalent path with the `NNN` placeholder, the score and a two to three sentence summary". `replies/PTX-001.md:30` reads `**Score and gate status:** CLEAR 42/50 (C:8 L:8 E:12 A:8 R:4) | Perspectives: 3 | Gate passed`. The score is present, in the place the scenario asks for it.

`deliverable_lint.py:64` enforces `REQUIRED_HEADER_FIELDS = ("Complexity:", "Framework:", "Score:")` and cites `Custom Instructions.md`'s template in the comment above it. The check is faithful to the kernel. It is not the scenario's question. `header_malformed` on `PTX-001` is a real finding about a document conflict and it is not evidence for the FAIL. The FAIL stands on the ordering defect alone.

---

## 5. Rule defects found on the way, none of which decides this pair

Recorded for the repair phase, not regraded.

**Perspectives has no lawful home in the Project's Deliverable Block.** `DEPTH Thinking Framework - v0.200.md:210` requires "Mode, Framework, Perspectives, CLEAR score in deliverable" and `:487` onward repeats it as "Proof Through Output Metadata: Every deliverable must include these fields. If missing, thinking has not been proven". `Custom Instructions.md:322` limits the block to a single-line header plus prompt plus attestation, `:342` forbids processing notes inside it, and `:375`'s header has no Perspectives field. `deliverable_lint.py:77` bans the literal token `Perspectives:` from inside the block. The skill side carries the identical requirement at `sk-prompt-improver/references/depth-framework.md:223` and the identical restriction at `SKILL.md:495`, so this is a shared rule gap, not a parity gap. Decide once whether the Perspectives proof belongs in the header, in the attestation line or in the chat report, then say so in one place.

**The export-equivalent path placeholder is specified twice, differently, inside one document.** `Custom Instructions.md:291` says `export/[###] - enhanced-[description].[md|json|yaml]`. `Custom Instructions.md:387` says `export/NNN - ...`, "where `NNN` is a placeholder the human reconciles". `PTX-001:29` and `PID-001` both used a guessed number. The scenario's expected signals at `:30` ask for `NNN`, its pass and fail lines do not, so no verdict turns on it, but two Project scenarios deviated from a requirement the kernel contradicts itself about.

**The enforcement framing is asymmetric, and it is the most likely reason the ordering fault is Project-only.** The skill carries its delivery contract in `AGENTS.md` section 2 as a `BLOCKING REQUIREMENT` with a five-step Strict Sequence, a Prohibited list and the closing line "Violation of this protocol invalidates the response." The Project carries the same substance as items 16 to 18 in a twenty-five item ALWAYS list plus a DELIVERY PROTOCOL section and a checklist bullet. The rule reached both, so this is not a parity gap, but the skill's version is structurally unbreakable (the file write precedes any chat token) and the Project's is a preference stated three times. If the repair wants the Project runtime to stop leading with the phase summary, moving the ordering rule into a numbered blocking sequence is the change with evidence behind it.

**`Custom Instructions.md`'s RULES section has holes.** ALWAYS 4 to 10, 12 to 14 and 22, and NEVER 6 to 10, 14 and 15, are absent as text and replaced by bare `Full detail: the X knowledge doc` lines, leaving a numbered list that skips numbers. Nothing in this pair turns on a missing item, and the compaction is clearly deliberate, but a reader counting the ALWAYS list will not find 25 items in it.

---

## 6. Defects in the report and in the framing

**`README.md:58` treats the missing `Score:` field as a second independent defect supporting the FAIL.** It writes "Running `deliverable_lint.py` on the isolated reply also caught a second, independent defect ... Every other project reply in this run that renders a header keeps Score on that line." The count is correct, verified above. The inference is not: this scenario's own fail line fails on an absent score, the score is in chat where `:30` asks for it, and the Project's own Format Guide specifies the three-field header the reply used. The report's own section 7 then says the finding is "real, and already reflected in the verdicts above", which promotes a document conflict into verdict evidence. The verdict is right, one of its two stated grounds is not.

**`README.md:58` and `results.csv` reach for the playbook carve-out the long way.** Both argue the advisory carve-out "does not apply here" because `PTX-001` exists to test delivery shape. `manual-testing-playbook.md:143` makes advisory only "Response ordering **beyond** the required Artifact-first or path-first shape", so a breach of the required shape is never advisory and the scenario-purpose test is not needed. Same answer, weaker reasoning, and the weaker version is the one another system's lane could copy wrongly.

**`README.md:165` credits the lint with signal the manual read missed, and that credit is misdirected.** "The `PTX-001` header-malformed finding was caught only by running the tool." True, and what the tool found is that the kernel template and the Format Guide disagree. Read as the report reads it, the tool added a defect. Read against the documents, it added a rule conflict. Evidence rule 1 applies here in the report's own words: where a check disagrees with a document, suspect the check first. The check agrees with one document and disagrees with another, which is the finding.

**`README.md:163` is accurate and should be kept.** The `header_missing` findings on `PCR-001` and `PID-001` are a `MODE_LINE` regex blind spot for a bolded label. Confirmed independently here: both lines exist, both begin with `**Mode:`, and `deliverable_lint.py:63` anchors on `^\s*Mode:`. The suggestion at `:196` to look at this fleet-wide is sound, and `PID-001:14` shows a second variant the regex will also miss, a header where the bold wraps the entire line rather than the label.

**`README.md:32`'s multi-turn count holds.** Walking the fourteen scenario files and then the replies directory gives seven scenarios that actually ran two turns and seven that resolved inside turn 1, and `replies/` contains exactly fourteen turn-suffixed files plus seven single-file captures, which is the same seven. Counted from the directory, not from the prose.

**On the framing given to me.** The brief describes the Project failure as "a transparency summary rendered before the Mode and prompt and the Attestation block ... and a missing `Score:` field". The first half is exact. The second half is a real observation about the reply and a wrong attribution about its cause, and it does not belong in the same sentence as the first, because the two have different classes and only one of them fails the scenario. The brief also notes that this system's lint checks deliverable structure rather than Human Voice, and that the earlier lane restructured its capture format mid-run. Both are true and both were verified: `deliverable_lint.py` contains no vocabulary or punctuation list, and `replies/` holds one file per captured reply with no title or metadata wrapper, which is what makes `deliverable_not_first` measure the reply instead of the document.

---

## 7. Nothing unsettled

Both determinations rest on rule text confirmed from a second direction, and both second directions are behavioural rather than another reading of the same sentences. The one thing this adjudication does not settle is whether the Perspectives contradiction in section 5 would still pull the Project runtime ahead of the block once the ordering rule is hoisted into a blocking sequence. That is a question for the repair, and the test that answers it is the same two fresh runs made here, repeated after the change.
