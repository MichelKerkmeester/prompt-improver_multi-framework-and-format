# Grading notes: Prompt Improver complexity-rubric run, 2026-09-27

## 1. OVERVIEW

Evidence behind every verdict in `results.csv`. Paths are relative to this run folder unless they start with a system path. Reply quotes cite `replies/<ID>-turn1.txt`. Deliverable quotes cite the copy in `export/benchmark/skill/` or `export/benchmark/claude project/`, which is byte-identical to the run's own copy. Rule citations give file and line at Prompt Improver `136cf51`, the commit that holds the rules this run tested.

---

## 2. HOW THE GRADING WAS DONE

### Sources read

- The playbook at Prompt Improver `136cf51`, as the run used it: the root `manual-testing-playbook.md` and the 48 files in `skill-framework-coverage/` and `project-framework-coverage/`. The six creative pairs were re-tiered and renamed later, in `534bc67`, so their verdicts here use the tiers the run was checked against. Section 7 reads them against the new tiers
- The rules: `AGENTS.md`, `sk-prompt-improver/SKILL.md` 1.5.0 and its references on the skill side, and `claude project/Custom Instructions.md` v1.6.0 and its knowledge files on the Project side
- Run output: every reply, every `meta.json`, the skill sandbox `exports/` copies and the event streams wherever a save, a parse or the order of a reply had to be proven
- The structure review, as a list of leads only. No verdict rests on it

### Who graded

Four graders took six twin pairs each: 001 to 006, 007 to 012, 013 to 018 and 019 to 024. None of them wrote a scenario, a deliverable or the structure review. Each applied the scenario's own Pass/fail line item by item and wrote the evidence for every item. Section 4 holds their notes as they wrote them. Section 6 lists the claims rerun before the merge.

### Graded delivery

Every scenario runs one turn, so the one reply is the graded delivery. No reply asked a question instead of delivering, so no scenario fails for missing delivery, and `after_failed_gate` is `no` on every row.

### Readings applied to every scenario

- **Target model and replaced one-liner.** The text scenarios list "ChatGPT as the target", or another model, and "the current one-line prompt it replaces" among the facts the prompt carries. A prompt pasted into a model rarely names that model or quotes the prompt it replaces. So the three graders who met these items read both as kept when the deliverable is a replacement prompt fit for that target. The VIBE and VIBE-MP scenarios say more: "v0 as the platform, named in the header or the body" and "MagicPath as the platform, named in the header or the body". Those two were graded strictly. Five of the six PASS verdicts rest on the lenient reading, since PFW-001, SFW-003, PFW-003, SFW-004 and SFW-006 name no target model. PFW-009 names GPT-4.1 and would pass either way
- **Scope test.** `SKILL.md` line 511 and kernel line 335 ban scope expansion, and line 511 defines it: "An output, field or section the user did not ask for is scope expansion, even when the reply flags it." A detail inside a requested output that serves a requested rule, such as a paste slot for a named input, a status tag or a source citation, was read as a default. A new output, a new top-level section holding no user fact, or a field that serves no requested rule was read as scope expansion. Each grader marked its close calls "judgment call"
- **Facts.** Narrowing, widening or recasting a stated number, constraint, place or party counts as altered. A default that fills a gap the user left counts as kept
- **Scores.** The reported score and gate status decide the scorer item, as the scenarios' Evidence sections ask. Where a reply gave sub-scores, the floors were checked. Approximate scores written with `~` or `≈` were read as reported passes. No reply reported a score below its gate
- **Canvas stand-in.** Every Project scenario counts any text before the Deliverable Block as commentary, an environment note included, and a reply with commentary first fails
- **Advisory items.** Summary length, word ranges, token-overhead notes, em dash counts and the `NNN` file-number placeholder are recorded and decide nothing

### facts_intact

`yes` means every fact the user supplied appears unchanged in the deliverable, under the readings above.

---

## 3. WHAT FAILED

6 of 48 pass: PFW-001, SFW-003, PFW-003, SFW-004, SFW-006 and PFW-009, three on each runtime. The 42 failures break down by the item that failed below. Most fail more than one item, so the rows add up to more than 42.

| Failing item | Skill | Project | All | Scenarios |
|---|---:|---:|---:|---|
| A supplied fact dropped or altered | 13 | 14 | 27 | SFW-005, 008, 009, 010, 012, 013, 014, 015, 017, 021, 022, 023, 024 and PFW-005, 006, 008, 010, 011, 013, 014, 015, 016, 017, 019, 020, 022, 023 |
| Complexity outside the tier | 10 | 13 | 23 | SFW-002, 013, 015, 016, 018, 019, 020, 021, 022, 024 and PFW-002, 004, 005, 007, 010, 013, 016, 018, 019, 020, 021, 022, 024 |
| Scope expansion | 9 | 8 | 17 | SFW-005, 013, 014, 015, 016, 017, 018, 020, 022 and PFW-007, 012, 013, 014, 015, 016, 017, 018 |
| Reply does not lead with the saved path | 8 | none | 8 | SFW-001, 002, 007, 009, 011, 017, 022, 023 |
| Commentary before the Deliverable Block | none | 5 | 5 | PFW-007, 010, 016, 019, 020 |
| An element missing or unlabelled | 1 | 2 | 3 | SFW-020 and PFW-020, 022 |
| JSON or YAML payload does not parse | 0 | 2 | 2 | PFW-005, 007 |

The 23 tier failures are the 23 misses `run/check_framework_headers.py` reports, and the 27 fact failures are the 27 rows with `facts_intact` `no`.

16 scenarios fail on one item alone:
- Tier alone: PFW-002, PFW-004, SFW-019, PFW-021 and PFW-024
- Path-first alone: SFW-001, SFW-007 and SFW-011
- A fact alone: PFW-006, SFW-008, PFW-008, SFW-010, PFW-011, SFW-012 and PFW-023
- Scope alone: PFW-012

What stands out:
- **Facts fail most, 27 of 48.** The rubric does not touch fact handling. Every changed fact is quoted in section 4
- **Path-first is an effort habit, not a new one.** 8 of 24 skill replies open with a sentence about the check the runtime just ran, such as "File verified" or "JSON validated", and put the path on line 3. `AGENTS.md` line 61 says "Start with the saved file path." The same first-line test finds 10 of 24 in the 2026-09-26 run at the same effort
- **Commentary first is a Project habit.** Five Project replies open with an environment note or a lead-in sentence. `lint_replies` catches only PFW-016 (section 8)
- **"Barter" reached two Project prompts.** PFW-006 opens "Barter runs 14 physiotherapy clinics" where the user wrote "We run 14 physiotherapy clinics", and PFW-010 has "Barter, an employment-law firm" where the user wrote "our employment-law firm". The only Barter text any Project session saw is line 676 of `Prompt Improver - Interactive Mode - v0.700.md`, "Interactive framework for Barter prompt enhancement". All 24 Project sessions read it, per their event streams. Skill sessions read the same line and two reference titles, "Barter - Prompt Improver - ...", and no skill deliverable names Barter

---

## 4. PER SCENARIO

Each section below is the grader's own record, in pair order.

### SFW-001, skill, FAIL

- Verified `.md` export saved before the reply: holds. `meta.json` shows one turn, `completed: true`, created `export/001 - enhanced-warehouse-exception-handover-prompt.md`, and `exports/export/` lists that file. The event log holds one assistant text block after the Write call, and the sandbox file is byte-identical to `export/benchmark/skill/SFW-001 - 001 - enhanced-warehouse-exception-handover-prompt.md`
- Path-first reply: FAILS. The reply's first line reads "File verified" followed by "valid Markdown, header + RCAF content only, no forbidden metadata sections." and names no path. The path appears on line 3 as "**Saved:** `export/001 - enhanced-warehouse-exception-handover-prompt.md`". The scenario defines path-first as the first line naming the saved `export/` path
- Prompt not pasted: holds
- Header: holds. "Mode: $text | Complexity: Medium (5/10) | Framework: RCAF", inside the Medium tier
- Elements: holds. **Role:**, **Context:**, **Action:** and **Format:** are bold labels
- CLEAR: holds. "CLEAR: 46/50 | Gate: passed", no sub-scores given
- Facts: holds. Rotterdam warehouse, day shift lead pasting the log, the four exception types, the night lead at the 22:00 handover, grouping by type, OPEN flag, dock door and pallet ID per open item, "under 200 words total" and "no causes, names, or blame language" are all present
- Scope: holds, judgment call. The CLOSED tag and one line per resolved entry render the non-open exceptions of a summary the user asked for, read as a default
- Recorded: summary is two sentences plus three `[Assumes:]` notes

### PFW-001, project, PASS

- Block first, header and attestation, no save claimed: holds. The reply opens with a fence, then "Mode: $text | Complexity: Medium (6/10) | Framework: RCAF", and the attestation inside the fence ends "execution = did not occur | save = did not occur". After the block: "**Export-equivalent path:**", no save claim
- Prompt not pasted again: holds
- Header: holds, Medium (6/10) is inside the Medium tier
- Elements: holds. **Role:**, **Context:**, **Action:** and **Format:** are bold labels
- CLEAR: holds. "CLEAR 43/50 (C9·L8·E13·A9·R4)", every floor cleared, "Gate passed"
- Facts: holds, judgment call. All four exception types appear, written as "covering incidents such as damaged pallets, short picks, late trucks and scanner faults", which keeps each type while leaving other log categories possible. Rotterdam, 22:00 handover, dock door and pallet ID for each OPEN item, under 200 words and no blame are present
- Scope: holds, judgment call. The "Exception log: [PASTE TODAY'S EXCEPTION LOG HERE]" slot is a paste slot for the input the user described, read as a default
- Deliverable file is identical to the reply block

### SFW-002, skill, FAIL

- Verified `.json` export saved before the reply: holds. `meta.json` created `export/001 - enhanced-expense-claim-review-prompt.json`, listed in `exports/export/`, byte-identical to the benchmark copy
- Path-first reply: FAILS. The first line reads "JSON validated (top-level keys are exactly `role`, `context`, `action`, `format`) and the file is saved." and names no path. The path sits on line 3
- Prompt not pasted: holds
- Header: FAILS. "Mode: $json | Complexity: Complex (9/10) | Framework: RCAF". RCAF passes, but 9 sits outside the High tier of 7 to 8
- Elements: holds. Top-level JSON keys `role`, `context`, `action`, `format`
- CLEAR: holds. "CLEAR 44/50 | Gate: passed", no sub-scores given
- Payload parses: holds. Python `json.loads` on the body below the header returned the four keys
- Facts: holds. Claude API and expense tool in `role`, the three inputs, the four classes, the four actions, the EUR 750 override "regardless of its classification", hotel limits 180 and 240, recommend-only and verbatim receipt quote are all present
- Scope: holds, judgment call. The `amount_eur` and `escalation_applied` output fields echo the input amount and record whether the requested EUR 750 override fired, read as part of the default output schema. `other_category_limits` defers to the organisation's own policy rather than inventing values
- Recorded: the reply gives no token-overhead figure, which the expected signals mention but the Pass/fail line does not list

### PFW-002, project, FAIL

- Block first, header and attestation, no save claimed: holds. The reply starts at the header with no fence, and the block ends after "Attestation: ... execution = did not occur | save = did not occur". The path is written as "`export/[###] - enhanced-expense-claim-triage.json`", not presented as saved
- Prompt not pasted again: holds
- Header: FAILS. "Mode: $json | Complexity: Complex (9/10) | Framework: RCAF", outside the High tier of 7 to 8
- Elements: holds. Top-level keys `role`, `context`, `action`, `format`
- CLEAR: holds. "CLEAR 43/50 (Correctness 9, Logic 9, Expression 12, Arrangement 9, Reusability 4)", every floor cleared, "Gate passed"
- Payload parses: holds. `json.loads` on the payload between the header and `---` returned the four keys
- Facts: holds. The three inputs, the four classes with their actions, the override "whatever its class", both hotel limits, recommend-only and the receipt quote are present. The Claude API is not named, covered by the standing judgment call
- Scope: holds. Output fields map to requested content and `why_this_matters` is rationale, not an output
- Recorded: token overhead "roughly 5-10%" reported, file number is the placeholder `NNN`

### SFW-003, skill, PASS

- Verified `.md` export saved before a path-first reply: holds. First line "Saved: `export/001 - enhanced-sev-postmortem-prompt.md`", the file is in `exports/export/` and matches the benchmark copy
- Prompt not pasted: holds
- Header: holds. "Mode: $deep | Complexity: Complex (10/10) | Framework: RCAF"
- Elements: holds. Four bold labels, with the three audience layers nested under **Format:**
- CLEAR: holds. "CLEAR 46/50 | Gate: passed (floors clear: C9 L9 E14 A9 R5)"
- Facts: holds, judgment call. Context reads "one resolved SEV1 or SEV2 incident". I read "resolved" as a default a postmortem presupposes, since no supplied word was changed or removed. The three inputs, UTC normalisation with the 10-minute gap flag, root cause only where logs support it and `Hypothesis:` otherwise, owner from the responders list and a due week, account IDs, blameless draft and the five-sentence exec brief are all present
- Scope: holds, judgment call. The per-event source citation serves the logs-only root-cause rule, and the flag on action items missing an owner or due week covers the gap case, both read as defaults
- Recorded: five em dashes in the deliverable, reply lists no perspectives

### PFW-003, project, PASS

- Block first, header and attestation, no save claimed: holds. The reply opens with a fence, the attestation ends "execution = did not occur | save = did not occur", then the export-equivalent path
- Prompt not pasted again: holds
- Header: holds. "Mode: $deep | Complexity: Complex (9/10) | Framework: RCAF"
- Elements: holds. Four bold labels, audience layers under **Format:**. The closing line "Use RCAF only" restates the user's own instruction
- CLEAR: holds. "CLEAR 44/50 (C9 L9 E13 A9 R4)", every floor cleared, "Gate passed"
- Facts: holds. "One SEV1 or SEV2 incident", the three inputs, UTC and Amsterdam time normalised to UTC, gaps over 10 minutes, root cause or "Hypothesis:", owner and due week, account IDs and the five-sentence exec brief are all present
- Scope: holds, judgment call. The original time beside each UTC time, discrepancy notes, support-relevant action items in the Impact Summary and the top action item in the exec brief all sit inside requested layers and serve requested rules, read as defaults. The bracketed request for the responders list and name-to-ID mapping supplies inputs the user's own rules need

### SFW-004, skill, PASS

- Verified `.md` export saved before a path-first reply: holds. First line "**Saved:** `export/001 - enhanced-parent-newsletter-prompt.md`", listed in `exports/export/`, matches the benchmark copy
- Prompt not pasted: holds
- Header: holds. "Mode: $improve | Complexity: Medium (5/10) | Framework: COSTAR"
- Elements: holds. Six bold labels, Context, Objective, Style, Tone, Audience and Response
- CLEAR: holds. "CLEAR: 44/50 | Gate: passed", no sub-scores given
- Facts: holds, judgment call. "maximum 350 words" stands for "under 350 words", read as kept. The three inputs, phones, second-language readers with "Plain B1-level Dutch", short paragraphs, warm but not chatty, event dates at the very top and no pupil named are all present
- Scope: holds. The three paste slots are inputs the user named, and the line stating there are no lunch or bus changes fills the empty-month gap. Dutch as output language is a flagged default for an unstated language

### PFW-004, project, FAIL

- Block first, header and attestation, no save claimed: holds. Fence first, attestation ends "execution = did not occur | save = did not occur", export-equivalent path after the block
- Prompt not pasted again: holds
- Header: FAILS. "Mode: $improve | Complexity: High (7/10) | Framework: COSTAR", outside the Medium tier of 5 to 6
- Elements: holds. Six bold labels
- CLEAR: holds. "CLEAR 42/50" with "Gate passed", no sub-scores given
- Facts: holds, judgment call. Context reads "any changes to the lunch menu or bus timetable" while Response keeps "lunch or bus timetable changes". The user's phrase "lunch or bus timetable changes" allows both readings, so I read it as kept. Dutch as a second language, B1, short paragraphs, warm not chatty, dates first, under 350 words and no pupil named are present
- Scope: holds, judgment call. The closing line sits inside the requested newsletter, and the paste-slot block after Response holds the user's own three inputs
- Recorded: the attestation mentions "GPT-4 class", outside the prompt

### SFW-005, skill, FAIL

- Verified `.yaml` export saved before a path-first reply: holds. First line "**Saved:** `export/001 - enhanced-hybrid-work-policy-announcement-prompt.yaml`", listed in `exports/export/`, matches the benchmark copy
- Prompt not pasted: holds
- Header: holds. "Mode: $text | Complexity: High (8/10) | Framework: COSTAR"
- Elements: holds. Six top-level keys `context`, `objective`, `style`, `tone`, `audience`, `response`
- CLEAR: holds. "CLEAR 44/50 | Gate: passed", no sub-scores given
- Payload parses: holds. `yaml.safe_load` returned seven top-level keys
- Facts: FAILS. Context states as fact "warehouse and operations crew who are already on-site full time", which the user never said. The allowance line adds "for everyone who currently claims it", and although an `[Assumes:]` note sits beside it in context, `section_1_announcement.must_include` requires the announcement to say "that it applies to everyone currently claiming the allowance". That makes the draft promise something beyond the policy text, which the user forbade
- Scope: FAILS. The extra top-level `placeholders` key lists `${COMPANY_NAME}`, `${HR_CONTACT_CHANNEL}` and `${INTRANET_ANNOUNCEMENT_LINK}`. The scenario lets an extra top-level section pass only when it holds the user's own facts, and none of these is a user fact
- Recorded: the three outputs are kept, exactly six FAQ items and two teaser lines

### PFW-005, project, FAIL

- Block first, header and attestation, no save claimed: holds. The reply opens on the header line, then a ```yaml fence, then `---` and the attestation ending "execution = did not occur | save = did not occur"
- Prompt not pasted again: holds
- Header: FAILS. "Mode: $yaml | Complexity: Complex (9/10) | Framework: COSTAR", outside the High tier of 7 to 8
- Elements: holds. Six top-level keys
- CLEAR: holds. "CLEAR 44/50 (C9 L8 E14 A9 R4)", every floor cleared, "Gate passed"
- Payload parses: FAILS. `yaml.safe_load` raised ScannerError "mapping values are not allowed here" at the deliverable's line 54, `format: Three clearly labeled sections in this order: announcement, faq, slack_teaser`, an unquoted colon inside a plain scalar
- Facts: FAILS. "From 1 March" became `effective_date: 2026-03-01` for both the office days and the allowance, a year the user never gave. 420 staff, Utrecht and Ghent, Tuesday and Thursday, two exceptions per quarter and the flat EUR 60 are kept
- Scope: holds, judgment call. `output_language: English` fills an unstated language gap and `validation_before_delivery` is a self-check. The FAQ topic "Why the allowance changed from per-kilometre to flat-rate" asks for a reason the policy text does not give, recorded but read as a topic inside the requested FAQ
- Recorded: token overhead "+3-7%" reported

### SFW-006, skill, PASS

- Verified `.md` export saved before a path-first reply: holds. First line "**Saved:** `export/001 - enhanced-outage-communication-prompt.md`", listed in `exports/export/`, matches the benchmark copy
- Prompt not pasted: holds
- Header: holds. "Mode: $deep | Complexity: Complex (9/10) | Framework: COSTAR"
- Elements: holds. Context, Objective, Style and Tone are bold labels, and each channel heading carries a separate "Audience:" and "Response:" list label, the per-channel shape the user asked for
- CLEAR: holds. "CLEAR 45/50 (C9 · L9 · E13 · A9 · R5)", every floor cleared, "Gate: passed"
- Facts: holds. 14 physiotherapy clinics, booking-platform failure, pasted incident facts, the SMS of at most 300 characters to patients with appointments in the next 48 hours, the email to all active patients, the front-desk phone script, Dutch and English, teenage athletes to people in their 80s, B1, known, unknown and next update, no guessed cause, no data exposure unless stated, the direct clinic phone number and formal but empathetic are all present
- Scope: holds, judgment call. The email subject and closing line are parts of an email, and the two to four scripted follow-up answers enforce the no-cause and no-data-exposure rules inside the requested phone script. Pause marks are delivery guidance
- Recorded: ten em dashes in the deliverable

### PFW-006, project, FAIL

- Block first, header and attestation, no save claimed: holds. Fence first, attestation ends "execution = did not occur | save = did not occur", export-equivalent path after the block
- Prompt not pasted again: holds
- Header: holds. "Mode: $deep | Complexity: Complex (10/10) | Framework: COSTAR"
- Elements: holds. Context, Objective, Style, Tone and per-channel "Audience" and "Response" bold labels. The extra "Non-negotiable ground rules" section holds only the user's own rules
- CLEAR: holds. "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4" with every floor cleared, and "Gate passed on first pass"
- Facts: FAILS. Context opens "Barter runs 14 physiotherapy clinics." The user wrote "We run 14 physiotherapy clinics" and named no company, so the operator is altered. The other facts are kept
- Scope: holds, judgment call. The character count after each SMS surfaces the requested 300-character cap, the subject cap and word target are length defaults for the requested email, and the "Do not say" reminder enforces the user's own rules inside the requested script. The u/uw rule fills the formal-register gap
- Recorded: fourteen em dashes and seven en dashes in the deliverable

### SFW-007, skill, FAIL

- **Verified `.yaml` export saved before a path-first reply: FAIL.** `meta.json` records `turns_run` 1, no failures and a ledger that creates `export/001 - enhanced-ap-credit-note-sop-prompt.yaml`. The sandbox `exports/export/` holds that file, byte-identical to the benchmark copy. But the reply's first line is "The YAML body (everything below the single-line header, per the format guide's own convention) parses cleanly and matches the intended CIDI structure." The path only appears on line 3 (`**Saved:** ...`). The scenario defines path-first as "the first line of the reply names the saved `export/` path"
- **Prompt pasted: no**, holds
- **Header names CIDI and a Medium complexity: PASS.** `Mode: $improve $yaml | Complexity: Medium (6/10) | Framework: CIDI`
- **Context, Instructions, Details and Input labelled: PASS.** The four top-level YAML keys are `context`, `instructions`, `details` and `input`
- **CLEAR passes its gate: PASS.** "CLEAR: 46/50 | Gate: passed (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4)", every floor met
- **Payload parses as YAML: PASS.** `yaml.safe_load` on the lines below the header returns the four keys
- **Every supplied fact kept: PASS (facts_intact yes).** Transcript input as a placeholder, new AP clerks, supplier credit note against an open invoice, one action plus screen or field plus result per step, the EUR 5,000 second-approver flag, verbatim field names, chit-chat excluded and Confluence as the destination are all present. Claude and the old one-liner fall under the shared judgment call above
- **Scope test: PASS.** The `document_shape` title line is read as a default per the shared judgment call. Nothing else unasked is added
- **Advisory, recorded:** summary of three sentences, inside the band. No token-overhead figure is reported, which the expected signals ask for but the Pass/fail line does not

### PFW-007, project, FAIL

- **Block before any commentary: FAIL.** The reply opens "No Canvas panel is available in this environment (terminal/API surface), so per protocol the Deliverable Block is rendered as a single fenced block first, with no preamble." The Canvas stand-in counts "an environment note" as commentary
- **Header, prompt and attestation present, no save claimed: PASS.** The attestation ends `execution = did not occur | save = did not occur`, and the chat gives an export-equivalent path only
- **Prompt pasted again: no**, holds
- **Header names CIDI and a Medium complexity: FAIL.** `Complexity: High (7/10)` sits outside the Medium band of 5 to 6
- **Four CIDI elements labelled: PASS.** Keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR 43/50 ... Gate passed", no sub-scores reported
- **Payload parses as YAML: FAIL.** With the header, the `---` and the attestation removed, `yaml.safe_load` raises "could not find expected ':'" at the plain list item that wraps after "completing the action: a"
- **Every supplied fact kept: PASS (facts_intact yes).** All ten listed facts are present, including the EUR 5,000 flag and Confluence
- **Scope test: FAIL.** Judgment call. The instruction "a short title, a one-line purpose statement, then the numbered steps" adds a purpose statement the user did not ask for, and "mark the approval step as conditional and instruct the clerk to confirm the value first" adds a clerk instruction the user did not ask for. The title is read as a default
- **Advisory, recorded:** summary of three sentences, token overhead "+3-7%" reported

### SFW-008, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "Saved: `export/001 - enhanced-onboarding-setup-guide-prompt.md`". The sandbox `exports/export/` holds the file and `meta.json` records it as the only creation
- **Prompt pasted: no**, holds
- **Header names CIDI and a High complexity: PASS.** `Complexity: High (8/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Bold labels Context, Instructions, Details, Input
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 | Gate: passed", no sub-scores
- **Every supplied fact kept: FAIL (facts_intact no).** The input said troubleshooting is "built only from errors the CI config or README mention". Instruction 6 reads "containing only failure modes drawn from the source files: error strings, named CI check failures, or problems the README explicitly calls out", and the source files include the Makefile, so Makefile error strings are admitted. A second, weaker point: instruction 4 allows a verify check "present in or directly derivable from the source files", which admits a command not copied verbatim
- **Scope test: PASS.** Judgment call. The "Secrets (1Password)" section in the section order holds only the 1Password handling the user asked for, so it is read as placement rather than a new output
- **Advisory, recorded:** summary of two sentences

### PFW-008, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence and the header directly inside it
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends with both "did not occur" fields, and the summary says "nothing was saved or executed"
- **Prompt pasted again: no**, holds
- **Header names CIDI and a High complexity: PASS.** `Complexity: High (8/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Bold labels Context, Instructions, Details, Input
- **CLEAR passes its gate: PASS.** "CLEAR 43/50 (C9, L8, E13, A9, R4)", every floor met
- **Every supplied fact kept: FAIL (facts_intact no).** The input asked for "separate paths for macOS and Ubuntu". Instruction 3 splits the paths only "anywhere a step differs by OS", and Details adds "If a command or step is identical on both platforms, state it once and note that it applies to both, rather than duplicating it under both OS paths". Claude in Cursor survives as "You are working inside Cursor"
- **Scope test: PASS.** Troubleshooting stays limited to the README and CI config, and nothing unasked is added
- **Advisory, recorded:** summary of two sentences

### SFW-009, skill, FAIL

- **Verified `.json` export saved before a path-first reply: FAIL.** The export exists in the sandbox and `meta.json` records it, but the first line is "JSON validated. The prompt is exported and CIDI-structured with all four required sections." The path is on line 3
- **Prompt pasted: no**, holds
- **Header names CIDI and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Top-level JSON keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR: 44/50 (C9 · L9 · E13 · A9 · R4) | Gate: passed"
- **Payload parses as JSON: PASS.** `json.loads` on the lines below the header succeeds
- **Every supplied fact kept: FAIL (facts_intact no).** The input covers "inbound sea containers carrying lithium batteries". `context.process` reads "clearing inbound sea containers declared under UN3480 (lithium batteries)", and `carrier_dg_rules` and its input slot are narrowed to "UN3480 lithium-battery shipments". That contradicts the file's own `un3480_gate`, which expects shipments outside UN3480. GPT-4.1, "Document this process", the three inputs, the role split, the four per-step fields, list-not-choose conflicts, the DG officer gate and bilingual step numbers are kept
- **Scope test: PASS.** The English section labels inside the Dutch version and the "Not specified in source" marker are flagged defaults that fill gaps, and the DG officer role comes from the input
- **Advisory, recorded:** one-sentence summary, below the band. No token-overhead figure reported

### PFW-009, project, PASS

- **Block before any commentary: PASS.** The reply opens with the fence, header on the next line
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends `execution = did not occur | save = did not occur`. The chat path is `export/[###] - ...` and not presented as saved. The benchmark copy's `NNN` file number is recorded, not decisive
- **Prompt pasted again: no**, holds
- **Header names CIDI and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (10/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Top-level JSON keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9·L9·E13·A9·R4, all floors met) ... Gate passed"
- **Payload parses as JSON: PASS.** `json.loads` succeeds with the header, `---` and attestation removed
- **Every supplied fact kept: PASS (facts_intact yes).** `target_model` GPT-4.1, "The current instruction is the placeholder 'Document this process'", the three inputs, "inbound sea containers carrying lithium batteries at the Port of Rotterdam", roles broker, planner and warehouse, trigger, system, document_produced and handoff per step, "do not pick a side: record the disagreement", the UN3480 DG officer step "before the planner's slot-booking step" and Dutch and English with identical step numbers are all present
- **Scope test: PASS.** Judgment call. `output_section_mapping` fills the CIDI output sections the importer requires, so it is read as a default. `step_requirements` lists three roles and `dangerous_goods_routing` then adds a DG officer step, an internal inconsistency that is recorded but drops no fact
- **Advisory, recorded:** summary of two sentences, token overhead "+5-10%" reported as the scenario expects

### SFW-010, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "File verified: `export/001 - enhanced-employment-law-intake-prompt.md`". The sandbox export exists and `meta.json` records it
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a Medium complexity: PASS.** `Complexity: Medium (6/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR: 42/50 (C:8 L:8 E:12 A:9 R:5) | Gate: passed"
- **Every supplied fact kept: FAIL (facts_intact no).** Judgment call on a clear case. The user's example note "Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag." is turned into an input line "Employee, dismissal on 3 June, employer Van Dijk Logistics." and its output is a five-line labelled block ending "Deadline flag: dismissal is over two months old - the claim window may have passed." The one-line note the user approved is no longer the target shape. The four issues, client type, every date, the other party for the conflict check, no advice and no chance estimate and the two-month flag are kept
- **Scope test: PASS.** The two added examples use invented parties (Meridian Retail Group, Elena Roussos) but illustrate only the user's own fields and rules, which the scenario allows
- **Advisory, recorded:** one-sentence summary plus assumptions, below the band

### PFW-010, project, FAIL

- **Block before any commentary: FAIL.** The reply opens "Here is the improved prompt, delivered as the Deliverable Block below." before the fence
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends with both "did not occur" fields, and the chat claims no file
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a Medium complexity: FAIL.** `Complexity: High (7/10)` sits outside the Medium band of 5 to 6
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Context, Instructions, Do's, Don'ts, Examples
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) ... Gate passed"
- **Every supplied fact kept: FAIL (facts_intact no).** Context reads "Barter, an employment-law firm", where the input said "our employment-law firm". The name is invented. The user's example note is kept verbatim as the first example output, and the other facts are kept
- **Scope test: PASS.** The second example (pay dispute, no dates, no counterpart) illustrates the user's own fields only
- **Advisory, recorded:** summary of two sentences

### SFW-011, skill, FAIL

- **Verified `.json` export saved before a path-first reply: FAIL.** The export exists in the sandbox and `meta.json` records it, but the first line is "JSON body validated successfully." The path is on line 3
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a High complexity: PASS.** `Mode: $json | Complexity: High (8/10) | Framework: TIDD-EC`. The `$json` mode label is allowed
- **Six TIDD-EC elements labelled: PASS.** Keys `task`, `context`, `instructions`, `dos`, `donts`, `examples`. The extra top-level `output_schema` holds only the user's three per-flag fields (sentence, rule broken, rewrite), so it passes as the scenario allows
- **CLEAR passes its gate: PASS.** "CLEAR 45/50 | Gate: passed (floors met: C9, L9, E13, A9, R5)"
- **Payload parses as JSON: PASS**
- **Every supplied fact kept: PASS (facts_intact yes).** GPT-4.1, title, description and bullet points, "Exactly 38 EU-authorised health claims, supplied fresh with every call", the three rules, exact sentence and compliant rewrite, compliant text untouched, no efficacy judgment and the worked example pair are all present
- **Scope test: PASS.** Judgment call. The citation of "EU Regulation (EC) No 1924/2006" in `context.domain` is invented context but adds no output, field or section, so it is recorded and not counted. The disease-claim and dosage-promise examples illustrate the user's own categories
- **Advisory, recorded:** summary of two sentences, no token-overhead figure reported

### PFW-011, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence
- **Header, prompt and attestation present, no save claimed: PASS**
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a High complexity: PASS.** `Mode: $improve | Complexity: High (8/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Keys `task`, `instructions`, `dos`, `donts`, `examples`, `context`
- **CLEAR passes its gate: PASS.** "CLEAR 45/50 (target 40+) ... Gate passed on first pass", no sub-scores
- **Payload parses as JSON: PASS**
- **Every supplied fact kept: FAIL (facts_intact no).** The task reads "the supplied list of up to 38 EU-authorised health claims" and `input_format` reads "approved_claims: array of up to 38 strings". The input fixed the list at 38. A weaker second point, recorded as judgment: the `compliant_paraphrase_edge_case` example passes a reworded claim as compliant, which loosens "flags every health claim that is not on the list"
- **Scope test: PASS.** The `violations` wrapper carries only the user's three per-flag fields, and the non-health marketing exclusion is a default
- **Advisory, recorded:** summary of two sentences, token overhead "+5-10%" reported

### SFW-012, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "File saved and verified: **`export/001 - enhanced-aml-alert-narrative-prompt.md`**". The bold markup does not change path-first. The sandbox export exists and `meta.json` records it
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 | Gate: passed", with Correctness 9, Logic 9, Expression 13, Arrangement 9 and Reusability 4, every floor met
- **Every supplied fact kept: FAIL (facts_intact no).** The input says "It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days". Instruction 3 says "do not attach a legal label to it", and Don'ts say "Never use conclusory AML labels such as \"structuring\"", so the prompt never flags structuring. Also "Every claim cites a transaction ID" is narrowed to "every claim drawn from the 90-day transaction data", with KYC and prior-alert claims citing other records. Mistral Large, the four inputs, the fixed section order, no laundering conclusion, no filing or closing recommendation, the currency rule, all three edge cases and the auditors' sentence verbatim are kept
- **Scope test: PASS.** The combined edge-case example covers only the three edge cases the user named, and "(EUR equivalent unavailable)" is a default
- **Advisory, recorded:** summary of two sentences

### PFW-012, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence. The "Advisory note" comes after the block
- **Header, prompt and attestation present, no save claimed: PASS.** The advisory note says "nothing was written to disk, executed or verified on any filesystem"
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) ... Gate passed"
- **Every supplied fact kept: PASS (facts_intact yes).** The structuring threshold is kept and flagged as "a potential structuring pattern", and "Cite a transaction ID for every specific factual claim in any section" keeps the citation rule. Mistral Large, the fixed order, both bans, the currency rule, all three edge cases and the auditors' sentence are kept. The missing-KYC example carries no transaction ID although the Do's require one, an internal inconsistency that is recorded but drops no fact
- **Scope test: FAIL.** Judgment call. The Do's add "Report the structuring check result every time (present or not observed), regardless of which rule fired". The user asked for a flag when the threshold is met, so a "not observed" line on every alert is an output the user did not ask for. Fixing the output language as English is read as a default
- **Advisory, recorded:** summary of two sentences

### SFW-013, skill, FAIL

Tier sentence: Medium, the label `Medium` or 5 or 6. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRISPE`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, `export/001 - enhanced-oat-milk-positioning-prompt.md`, the sandbox copy matches the deliverable, and the reply's first line is "Saved: `export/001 - enhanced-oat-milk-positioning-prompt.md`". The file holds only the header and the prompt, and the reply does not paste it
- Header names CRISPE inside the Medium tier: FAILS. CRISPE is named, but "High (7/10)" is the High tier
- Body organised by Capacity, Insight, Statement, Personality and Experiment, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 45/50 | Gate: passed"
- Every supplied fact kept: FAILS (judgment call). "a cheap way to test it within a month" became "one cheap way to test it within a month using close to zero budget", which narrows the user's constraint. Ghent, 15% above the market leader, the three barista concerns, three routes and their three fields, the persona, the sparring-partner framing and the frank, no-buzzwords style are all kept
- Scope test: FAILS. Personality adds "name the real trade-off or risk in each route", an output per route the user did not ask for. Experiment adds "(and why that type over another)" to the café-type field and a one-line assumption note. The Experiment element also says "give exactly three things", so the extra risk item contradicts its own element
- Recorded, not deciding: the summary is one long sentence plus an assumption tag, inside or near the advisory band

### PFW-013, project, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. The reply opens with a ```` ```markdown ```` fence, the attestation ending `execution = did not occur | save = did not occur` sits inside the fence, and the chat gives an "Export-equivalent path" with no save claim. The prompt is not pasted again. The block is byte-identical to the deliverable file once the fence lines are removed
- Header names CRISPE inside the Medium tier: FAILS. "High (7/10)"
- Body organised by the five CRISPE elements, each labelled: holds. All five are bold labels. The three route fields sit in Statement and Experiment holds the test design, which still reads as the Experiment element
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | ... | Gate passed"
- Every supplied fact kept: FAILS. The input prices the milk "15% above the market leader", a list-price premium, and Insight keeps that. Experiment then asks whether a barista would "accept paying 15% more per cup", which contradicts Insight's own point that per-cup cost can make the gap "disappear or explode". "a cheap way to test it" became "using only resources a small startup already has", and "the type of café it wins" became "the specific type of café or barista it wins"
- Scope test: FAILS (judgment call). Experiment adds a requirement that each test isolate the positioning story from milk performance ("A test that only proves the milk performs is not enough"). The user asked for a cheap one-month test, not a test design rule. I read this as an added requirement rather than a default
- Recorded, not deciding: the summary is three sentences plus a closing line, and it claims "No new sections or requirements were added"

### SFW-014, skill, FAIL

Tier sentence: High, the label `High` or 7 or 8. Header as written: `Mode: $yaml | Complexity: High (7/10) | Framework: CRISPE`

- Verified `.yaml` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "**Saved:** `export/001 - enhanced-driver-retention-strategy-prompt.yaml`". The prompt is not pasted
- Header names CRISPE inside the High tier: holds. "High (7/10)", mode label `$yaml`, which the scenario allows
- Body organised by the five CRISPE elements, each labelled: holds. Top-level keys `capacity`, `insight`, `statement`, `personality`, `experiment`
- CLEAR passes its gate: holds, with an arithmetic error recorded. The reply gives "C9/L9/E13/A9/R6 → total 46" and itself notes "Reusability 6/5 capped→5". Capped, the total is 45, still above 40, and every floor is met
- Payload below the header parses as YAML: holds. `yaml.safe_load` on the file minus its header line returns the five keys
- Every supplied fact kept: FAILS (judgment call). The input's assumption is "that pay is the main lever". `insight.standing_assumption_to_test` rewrites it as "Leadership currently treats pay per stop as the primary retention lever", and `experiment.pay_lever_guardrail` tests only pay per stop. Personality keeps "pay is the main lever", so the challenge survives, but the fact under challenge is narrowed from pay to one pay component
- Scope test: FAILS. `delivery_schedule_risk` adds "and how that risk is contained", a mitigation output per experiment. `readout_point` adds "what result counts as a go or no-go signal". `pilot_depot` adds "and why that depot is the right test site". `pay_lever_guardrail` adds a conditional explanation output. `reasoning_task` adds five causes the exit interviews never named (onboarding quality, schedule predictability, physical demands, manager relationship, route unfamiliarity)
- Recorded, not deciding: the reply gives no token-overhead figure, which the Expected signals mention but the Pass/fail line does not list. Depot A to D placeholders are a gap fill

### PFW-014, project, FAIL

Tier sentence: High. Header as written: `Mode: $yaml | Complexity: High (7/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds (judgment call on the block boundary). The reply opens on the header line with no preamble, so the block starts there under the stand-in rule. The YAML payload is fenced, then comes a `---` line and the attestation. The attestation is not inside the fence or on the line directly below it, but the `---` separator is the kernel's own template (`Custom Instructions.md` Delivery Protocol), no commentary precedes the block, and nothing sits between the fence and the attestation except that separator. I read the block as header through attestation. No save is claimed, and the prompt is not pasted again
- Header names CRISPE inside the High tier: holds. "High (7/10)"
- Body organised by the five CRISPE elements, each labelled: holds. Five top-level keys
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9/L9/E13/A9/R4) | Perspectives: 5 | Gate passed"
- Payload between the metadata lines parses as YAML: holds. `yaml.safe_load` returns the five keys. The token overhead line reports "+3-7%"
- Every supplied fact kept: FAILS. "route density" became "Route density perceived as unmanageable". `assumption_on_the_table` adds "this has not been tested against route density or shift start time", a claim the user did not make. Pay as the main lever, the 210 drivers, four depots, 38%, the 90 days, the budget and the five fields are kept
- Scope test: FAILS. `depot_allocation` adds "Assign each experiment to a different one of the four Antwerp depots", a constraint the user did not set. `condition_pay_not_primary` adds a new output, "name one additional low-cost signal worth testing in the following 10-week cycle". `required_output` adds a three-way causal verdict (primary, secondary, downstream symptom)
- Recorded, not deciding: the summary is three sentences

### SFW-015, skill, FAIL

Tier sentence: Complex, the label `Complex` or 9 or 10, or a label above High. A bare `High` fails. Header as written: `Mode: $deep | Complexity: High (8/10) | Framework: CRISPE`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line "File verified: **`export/001 - enhanced-germany-expansion-strategy-prompt.md`**" names the path. The prompt is not pasted
- Header names CRISPE inside the Complex tier: FAILS. "High (8/10)" is the High tier
- Body organised by the five CRISPE elements, each labelled: holds. "Capacity & Role", which the scenario allows for Capacity, then Insight, Statement, Personality and Experiment as bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | Gate: passed"
- Every supplied fact kept: FAILS. The CFO's route, "deepen in the Benelux mid-market first", became "deepen the Benelux mid-market as the CFO proposes, directly addressing the 4% monthly churn among sub-20-staff firms", tying the mid-market route to the small-firm segment the user never linked it to. Insight also adds that hosting cost and build timeline "are unknown"
- Scope test: FAILS. Statement adds "explain why it outweighs the other points of disagreement" and "state what evidence would resolve it" for every data gap. Personality adds an output, naming "which board position looks weakest given the data". None of these was asked for. The three named scenarios, their assumptions, tests and kill signals, the data-too-thin warning and "not a plan" are all present
- Recorded, not deciding: the "Q2" reading as Q2 2027 is flagged inline as an assumption. The summary runs four sentences and the reply closes with an offer of other variants

### PFW-015, project, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: Complex (9/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRISPE inside the Complex tier: holds. "Complex (9/10)"
- Body organised by the five CRISPE elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 | ... | Gate passed"
- Every supplied fact kept: FAILS. "4% monthly churn among firms under 20 staff" became "4% monthly churn concentrated in firms under 20 staff", which changes a segment rate into a claim about where overall churn sits. Insight adds an unsupplied fact about on-premise hosting, "a delivery model this business has not had to support at scale in NL/BE", right after telling the model to use "nothing you have to invent". The product, site-diary software for construction firms, appears only as "site-diary/construction-tech economics" in Capacity (recorded as kept)
- Scope test: FAILS (judgment call). The data-gap section is requested, but it is pre-seeded with invented gaps the input never raised: "German win rate, CAC, and sales-cycle length", "remaining Benelux mid-market TAM" and "German procurement or regulatory requirements such as GoBD or data-residency rules". The scenario says what goes inside an element "still has to come from the request", so I read these as invented requirements rather than illustrations
- Recorded, not deciding: the summary is two long sentences

### SFW-016, skill, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "**Saved:** `export/001 - enhanced-customer-workshop-planning-prompt.md`". The prompt is not pasted
- Header names CRAFT inside the Medium tier: FAILS. "High (7/10)"
- Body organised by Context, Role, Action, Format and Target, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR: 44/50 | Gate: passed"
- Every supplied fact kept: holds. Utrecht, 12 November, 25 HR managers from existing customers, 09:30 to 16:00, two hands-on sessions on the leave module, lunch, closing Q&A, the prep checklist for two trainers, and both targets ("at least 8/10" and "at least 10 sign-ups for the leave module pilot") are present. "in-person" and "internal trainers" are gap fills
- Scope test: FAILS. Action adds "an opening welcome/intro", "its own learning objective and activity" per session, "a one-line facilitation note" per session, "a quick feedback capture point after each hands-on session" and a "pilot sign-up call-to-action". Format fixes table columns and checklist groups the user did not specify. Each is an output or field the user did not ask for
- Recorded, not deciding: the summary is one sentence plus an assumption tag and a share-back line

### PFW-016, project, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Deliverable Block first, with no commentary before it: FAILS. The reply opens with a mode-detection paragraph ("Mode: $improve, format locked to $markdown by explicit command...") and an environment note ("This session has no Canvas panel available, so the Deliverable Block is rendered as a single fenced block below"). The scenario names a heading, a bold label or an environment note before the block as commentary. The header, attestation and no-save claim inside the block hold, and the prompt is not pasted again
- Header names CRAFT inside the Medium tier: FAILS. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (...) | Gate passed"
- Every supplied fact kept: FAILS. "at least 10 sign-ups for the module pilot" became "at least 10 attendee sign-ups for the leave module pilot by the end of the day", which adds a deadline. The year "[2026]" is a flagged placeholder
- Scope test: FAILS. Action adds "Add any short transition or break segments", a "weight session time toward guided hands-on practice" rule and checklist items for "demo environment/login access", "timing cues" and "how to make the pilot sign-up ask". Target adds "Mark on the run-of-show exactly where feedback is captured", although the user never asked for feedback capture
- Recorded, not deciding: the summary is two sentences

### SFW-017, skill, FAIL

Tier sentence: High. Header as written: `Mode: $improve | Complexity: High (8/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: FAILS on path-first. The export exists (`meta.json` lists one created file, and the sandbox copy matches), but the reply's first line is "File verified and saved.", which names no path. The path comes on line 3. The scenario defines path-first as "the first line of the reply names the saved `export/` path". The prompt is not pasted
- Header names CRAFT inside the High tier: holds. "High (8/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR: 46/50 | Gate: passed"
- Every supplied fact kept: FAILS. "under 5% of users raising a ticket in the first week" became "fewer than 5% of the 1,210 users logging a migration-related support ticket in the first week after their cutover". That counts the 60 shared mailboxes as users, filters by migration-related tickets and moves the window per batch. Context also adds "past Microsoft's extended support since October 2025" and GDPR/AVG obligations, neither supplied
- Scope test: FAILS. Format adds an executive summary of about 150 words, a weekend-by-weekend batching table with fixed columns, a customer-service sub-plan with "a go/no-go checkpoint partway through the 2-hour window", a mobile-only sub-plan and a "Success-target traceability section". The risk table adds an end-of-support row
- Recorded, not deciding: the summary is two sentences plus an assumption tag

### PFW-017, project, FAIL

Tier sentence: High. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRAFT inside the High tier: holds. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 / L9 / E13 / A9 / R4, all floors met) | ... | Gate passed"
- Every supplied fact kept: FAILS. "80 field staff use phones only" became "their mail access depends entirely on phone/tablet mail-app reconfiguration", which adds tablets. The customer-service mailbox becomes "mission-critical", which the input never said. The ticket target keeps the 1,150-user denominator, and the other counts, offices and targets are kept
- Scope test: FAILS. Format adds a "Scope summary" section, an "Execution Summary" per phase and a "Success-metrics tracking section". Exit criteria add "a mail-integrity or item-count reconciliation check". Action adds "a first-week post-migration monitoring step" with escalation triggers, and asks the model to "state the technique used" for the customer-service ceiling
- Recorded, not deciding: the reply reports four perspectives for an Improve lane at Standard energy. The summary is two sentences and claims "without adding unrequested scope"

### SFW-018, skill, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: High (7/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "Saved: `export/001 - enhanced-warehouse-go-live-plan-prompt.md`". The prompt is not pasted
- Header names CRAFT inside the Complex tier: FAILS. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 45/50 | Gate: passed"
- Every supplied fact kept: holds (judgment call). Tilburg 38,000 and Liège 12,000 lines a day, one vendor, SAP ERP and three carriers, the 15 November to 10 January blackout, Liège first, the 99.5% gate, the four workstreams, 260 pickers in two languages, dependencies, the checklist, hypercare, the 12-hour rollback and the cut-off target are all present. "four weeks" is written "four consecutive weeks", which I read as the same meaning
- Scope test: FAILS (judgment call). Format adds "time estimates summing to 12 hours or less" on each rollback step, a field the user did not ask for. The placeholders [Company], [WMS vendor] and [Carrier 1] to [Carrier 3] are gap fills. Sign-off criteria, monitoring cadence and trigger conditions sit inside requested parts and are recorded, not counted
- Recorded, not deciding: the summary is one sentence plus an assumption tag

### PFW-018, project, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: High (8/10) | Framework: CRAFT`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRAFT inside the Complex tier: FAILS. "High (8/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9, L9, E13, A9, R4) | ... | Gate passed"
- Every supplied fact kept: holds. Every site figure, the vendor, the integrations, the blackout, the Liège-first sequence, the "above 99.5% for four consecutive weeks" gate, the 260 pickers in two languages, the 12-hour rollback and the cut-off target are kept. Measuring the 12 hours "of a rollback decision" and the cut-off target per site are flagged assumptions
- Scope test: FAILS. Format adds an "Executive overview" section. Action adds milestones and "explicit Liège vs. Tilburg variants" per workstream and hypercare "exit criteria". Target adds a named "Primary audience". Context adds a meta paragraph about the old one-line request and the claim that Tilburg "cannot inherit Liège's risk tolerance"
- Recorded, not deciding: the summary is two sentences and claims "Nothing was added beyond what makes those requested elements executable"

### SFW-019, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` shows `created: ["export/001 - enhanced-zeeland-gravel-hero-midjourney-prompt.md"]`, the sandbox `exports/export/` holds the file and it is byte-identical to the benchmark copy. The transcript's last tool call is the `Write`, and the reply's first line is ``Saved: `export/001 - enhanced-zeeland-gravel-hero-midjourney-prompt.md` ``
- Prompt not pasted: holds. The reply quotes only the parameter string `--ar 21:9 --style raw --s 250 --q 2 --v 6.1`, recorded as a fragment and not the prompt (judgment call)
- Header names FRAME inside the High tier: FAILS. Header reads `Mode: $image | Complexity: Low (4/10) | Framework: FRAME`. FRAME holds, mode label `$image`, but 4 sits below the 7 to 8 band
- FRAME elements labelled: holds. Bold labels `Focus`, `Rendering`, `Atmosphere`, `Modifiers`, `Exclusions`, plus a `Full Prompt (copy-paste ready)` line the scenario allows as the Midjourney payload
- VISUAL passes: holds. `VISUAL 53/60 | Gate: passed`, gate 48
- Facts: holds. Midjourney v6.1, Zeeland, gravel dyke path, golden hour, low angle toward camera, Oosterschelde behind, photorealistic catalogue look, warm light and long shadows, 21:9 with the left third empty for the headline, and the three exclusions as positive phrasing plus `--no` terms. The olive jersey sits only in the full prompt line, not in Focus, recorded. The homepage hero purpose survives as the "headline overlay" banner rule, read as kept (judgment call)
- Scope: holds. The 85mm lens and DSLR, and the watermark and signature exclusions, are read as defaults inside the Rendering and Exclusions elements that the user's "pick sensible parameters yourself" invites, not as a new output or section (judgment call)
- Share-back invitation: holds. "Try it in Midjourney and share the result"
- Advisory: the summary is one long sentence plus the invitation, recorded

### PFW-019, project, FAIL

- Deliverable Block before any commentary: FAILS. The reply opens with "Confirmed FRAME is the correct framework for `$image`. Proceeding to deliver" and a second paragraph, "Since no Canvas panel exists in this environment, the Deliverable Block is rendered as a single fenced block first". The scenario counts an environment note as commentary
- Header, prompt and attestation, no save claimed: holds. The fenced block carries the header and ends with `execution = did not occur | save = did not occur`. The chat gives an "Export-equivalent path" with a guessed `001`, not presented as saved
- Prompt not pasted again: holds
- Header names FRAME inside the High tier: FAILS. `Complexity: Low (4/10)`, mode label `$image`
- FRAME elements labelled: holds. `F`, `R`, `A`, `M`, `E` each with its element name, plus a paste-ready full prompt
- VISUAL passes: holds. `VISUAL 55/60`, "Gate passed"
- Facts: FAILS. Zeeland is absent from the whole block (grep count 0), so the location in "Zeeland gravel-cycling tours" is dropped. The exclusion "no other people" became a bare `people` in `--no text, logo, branding, watermark, signature, people, crowd, second rider, cars, road signage`, which also works against the one rider, recorded as a second alteration (judgment call)
- Scope: holds. 24mm at f/5.6, about 3000K, clouds and calm air, and the cars and road signage exclusions are read as defaults inside the elements (judgment call)
- Share-back invitation: holds. "Try this prompt in Midjourney v6.1 and share the result with me"

### SFW-020, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-night-of-science-poster-prompt.md`, the sandbox copy matches the benchmark file, the `Write` precedes the reply and the first line is ``Saved: `export/001 - enhanced-night-of-science-poster-prompt.md` ``
- Prompt not pasted: holds
- Header names FRAME inside the Complex tier: FAILS. `Mode: $image | Complexity: Medium (5/10) | Framework: FRAME`
- FRAME elements labelled: FAILS. The file has three labels, `Positive Prompt`, `Negative Prompt` and `Parameters`. Exclusions maps to the negative prompt and Modifiers to Parameters, but Focus, Rendering and Atmosphere are merged into the unlabelled positive prompt. The reply's "Perspectives: 5 (Focus, Rendering, Atmosphere, Modifiers, Exclusions)" does not make them visible in the file
- VISUAL passes: holds. `VISUAL 55/60 | Gate: passed`
- Facts: holds. Leiden city library, Night of Science, 2:3, flat 1960s screen print, the four HEX codes exact, the three layers in order, the empty top quarter with no lettering, grain and misregistration, children about 8 to 10 and non-photoreal, weights, separate negative prompt, CFG and steps. ComfyUI is not named, but SDXL is named and the negative prompt is split for its separate field, read as kept (judgment call). The positive prompt asks for Orion's stars "scattered across" the sky while the negative excludes "random scattered stars", recorded as an internal conflict
- Scope: FAILS. "Sampler suggestion: DPM++ 2M Karras or Euler a" is a settings field the user did not ask for, since the request names only CFG and steps, and the reply flags it as an assumption (judgment call, since a sampler could be read as a default)
- Share-back invitation: holds. "Share the generated result when you want refinement"

### PFW-020, project, FAIL

- Deliverable Block before any commentary: FAILS. The reply opens with a routing paragraph, "Mode/format resolved from routing: `$image` → Image Mode", and a no-Canvas note before the fence
- Header, prompt and attestation, no save claimed: holds. The attestation ends `execution = did not occur | save = did not occur`, the path is written `export/[###] - enhanced-night-of-science-poster.md` and nothing is claimed saved. The captured file carries `NNN` in its name, recorded
- Prompt not pasted again: holds
- Header names FRAME inside the Complex tier: FAILS. `Complexity: Medium (5/10)`, mode label `$image`
- FRAME elements labelled: FAILS. Only `Positive Prompt`, `Negative Prompt` and `Suggested Settings`, with `Foreground`, `Midground` and `Background` as inline layer labels. Focus, Rendering and Atmosphere have no labelled part
- VISUAL passes: holds. `VISUAL 55/60`, "Gate passed"
- Facts: FAILS. "the Leiden city library" became "a public library" (Leiden count 0), and the foreground children now stand "on a rooftop terrace at a (large brass telescope:1.2)", which relocates the first layer. ComfyUI is not named while SDXL is, read as kept
- Scope: holds. The 1024x1536 resolution is read as the pixel form of the requested 2:3 ratio, and the halftone pattern and "Masterpiece, best quality" as defaults inside the positive prompt (judgment call). The rooftop terrace is graded under facts
- Share-back invitation: holds. "Try this prompt in ComfyUI and share what you get"

### SFW-021, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-runway-potter-bowl-video-prompt.md`, the sandbox copy matches, the `Write` is the last tool call and the reply opens with the `Saved:` path
- Prompt not pasted: holds. The reply names the `"Dolly forward:"` prefix only
- Header names MOTION inside the High tier: FAILS. `Mode: $video | Complexity: Medium (5/10) | Framework: MOTION`
- MOTION elements labelled: holds. Bold `Movement`, `Origin`, `Temporal`, `Intention`, `Orchestration`, `Nuance`
- VISUAL passes: holds. `VISUAL 62/70 | Gate: passed`, gate 56, and the prompt carries camera and subject motion
- Facts: FAILS. The user's beat "a close-up of her thumbs smoothing the rim at 8 seconds" became "a tight close-up on her thumbs by second 8", so "smoothing the rim" is dropped (grep count 0). All other facts hold, including Runway Gen-4 image-to-video, the sunlit studio, 10 seconds at 9:16 for Reels, the rising bowl, the slip spiral, the dust in window light, waist height, the hold, warm light, shallow depth of field, the face out of frame and the soft clutter
- Scope: holds. No audio section and nothing unasked
- Share-back invitation: holds. "Try this prompt in Runway and share the result with me"

### PFW-021, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens directly with the ```` ```markdown ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the chat gives an "Export-equivalent path" with a guessed `001`, not presented as saved
- Prompt not pasted again: holds. The chat summary describes beats and does not repeat the prompt
- Header names MOTION inside the High tier: FAILS. `Complexity: Medium (5/10)`, mode label `$video`
- MOTION elements labelled: holds. `M`, `O`, `T`, `I`, `O`, `N` each with its element name under "MOTION Breakdown". The extra `Platform`, `Reference Image`, `Duration`, `Aspect Ratio` fields and the paste-ready prompt hold the user's own facts, recorded
- VISUAL passes: holds. "VISUAL ~64/70", "Gate passed". The score is approximate, read as a reported pass above 56 (judgment call)
- Facts: holds. "a close-up on her thumbs smoothing the rim at 8 seconds, then holds steady" is kept, along with every other beat
- Scope: holds. "intimate documentary style" is read as a style default. The Nuance line "No audio track (Runway Gen-4 has no native audio)" is a note that no audio is added, not an audio section (judgment call)
- Share-back invitation: holds. "Try this prompt in Runway Gen-4 and share the result with me!"
- Advisory: the summary runs two sentences, inside the band

### SFW-022, skill, FAIL

- Delivery, export saved before a path-first reply: FAILS on path-first. The `.yaml` export exists (`meta.json`, sandbox copy identical to the benchmark file, `Write` then a `Bash` syntax check before the reply), but the reply's first line is "YAML body parses cleanly, no tabs, valid syntax. VISUAL scoring self-check landed at 62/70", and the `**Saved:**` path comes on the third line
- Prompt not pasted: holds
- Header names MOTION inside the Complex tier: FAILS. `Mode: $video | Complexity: Low (3/10) | Framework: MOTION`, plain form, not a YAML comment
- MOTION elements labelled: holds. `movement`, `origin`, `temporal`, `intention`, `orchestration`, `nuance` sit as keys under one `motion` wrapper
- VISUAL passes: holds. `VISUAL 62/70 | Gate: passed`
- Payload parses: holds. Python `yaml.safe_load` on the lines below the header returns a mapping with top-level keys `platform` through `constraints`
- Facts: FAILS. "a distant chime at the end" became "one distant chime as the clock starts moving", and the 8 second beat reads "Distant chime marks the sweep", so the chime moves from the end of a 10 second shot to 8 seconds. No music and no voices survive as "No score, no dialogue" in the prompt and `dialogue or voices` in `audio.excluded`. The Kling camera wording used is "[move up]" and "crane up", recorded
- Scope: FAILS. The extra top-level `constraints` section adds "No on-screen text or logos" and "No negative or quality-keyword prompting", and `nuance.physics` adds "no slow motion or speed ramps", none of which the user asked for. Under the scenario's rule an extra top-level section passes only when it holds the user's own facts (judgment call on the physics line). The `audio` and `visual_style` sections hold user facts and pass as recorded extras
- Share-back invitation: holds. "Share the generated result when you want refinement"
- Recorded, not in the Pass/fail line: the three to seven percent token overhead is not reported

### PFW-022, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```yaml ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, path given as `export/[###] - enhanced-aalsmeer-flower-auction-opening-shot.yaml`. The captured file carries `NNN`, recorded
- Prompt not pasted again: holds
- Header names MOTION inside the Complex tier: FAILS. `Mode: $video $yaml | Complexity: Low (4/10) | Framework: MOTION`
- MOTION elements labelled: FAILS. Only `intention` and `camera.origin` carry element names. Movement is spread across `camera` and `subject`, Temporal across `duration`, `beat_4s` and `beat_8s`, and Orchestration and Nuance have no key of their own
- VISUAL passes: holds. `VISUAL 62/70`, "Gate passed (56+ threshold...)"
- Payload parses: holds. `yaml.safe_load` on the lines between the header and the `---` before the attestation returns a mapping
- Facts: FAILS. "a distant chime at the end" became "a single distant chime as the clock hand starts to move", and "no voices" became "no spoken dialogue", which narrows the exclusion (judgment call on the second). "about three metres" became "three metres", recorded as minor
- Scope: holds. `style: naturalistic documentary aesthetic` is flagged in the attestation as a default for the unstated style, and `mood` and "before trading begins" are read as defaults (judgment call)
- Share-back invitation: holds. "Try this prompt in Kling 2.6 and share the generated clip with me"
- Recorded: token overhead "+3-7%" is reported

### SFW-023, skill, FAIL

- Delivery, export saved before a path-first reply: FAILS on path-first. The export exists (`meta.json`, identical sandbox copy, `Write` before the final `Grep`), but the reply opens with "No quality-spam language, and the file exports as valid Markdown with the required single-line header." and the `**Saved:**` path is on line three. The transcript confirms that sentence opens the final assistant message after the last tool call
- Prompt not pasted: holds
- Header names VIBE inside the High tier: holds. `Mode: $vibe | Complexity: High (7/10) | Framework: VIBE`
- VIBE elements: holds as prose. Vision maps to "warm-neutral surfaces, generous breathing room, typography sized to be caught in a glance", Inspiration to "a well-lit instrument panel in a photo lab", Behavior to the grade-card and reject-capture paragraphs, Experience to "item 40 or item 300" and "Nothing here should feel gamified"
- EVOKE passes: holds. `EVOKE 44/50 (Standard, threshold 40+) | Gate: passed`, grounding pre-check reported passed
- Facts: FAILS. v0 is named in neither the header nor the body (grep for `v0` returns nothing in the file), which the scenario requires. "An inspector stands at a bench" lost "stands", and "fashion e-commerce warehouse" became "a fashion warehouse". shadcn/ui is kept with its library line
- Scope: holds. The avoid-list naming and the UX-floor paragraph are rule-mandated and recorded. The record waiting on scan, the between-item transition and "a paired scanner or keyboard" are read as defaults inside the Behavior and floor passages (judgment call)
- Share-back invitation: holds. "Share the result once you generate it in v0"
- Advisory: 350 words against the v0 range of 100 to 300, recorded

### PFW-023, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```markdown ```` fence, and the no-Canvas note follows the block
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the export-equivalent path uses a guessed `001` not presented as saved
- Prompt not pasted again: holds
- Header names VIBE inside the High tier: holds. `Mode: $vibe | Complexity: High (7/10) | Framework: VIBE`
- VIBE elements: holds as prose. Vision in "warm neutral surfaces, generous single-glance zones, and typography", Inspiration in "a boarding-gate scanner crossed with the tactile satisfaction of a photo booth's countdown", Behavior in the `Layout:` and reject-capture paragraphs, Experience in "trust builds tap after tap" and "steady and unhurried at item 300"
- EVOKE passes: holds. "EVOKE ~44/50", "Gate passed at 40+ threshold", approximate score read as a reported pass (judgment call)
- Facts: FAILS. v0 appears only in the attestation ("target platform read as v0.dev"), which is neither header nor body, so the scenario's "named in the header or the body" does not hold. The standing inspector is dropped ("a gloved inspector"). "300 items a shift" became "300 returned garments a shift", recorded as a minor narrowing (judgment call)
- Scope: holds. The avoid-list, "customized rather than left in their default state" and the UX-floor paragraph are rule-mandated and recorded. One colour family for A to C with a distinct reject zone is the named aesthetic choice, read as a default
- Share-back invitation: holds. "Try this prompt in v0 and share what it generates"
- Advisory: 377 words against the v0 range, recorded. The "Complexity note" offers a streamlined version "just ask", an offer after delivery and not a question instead of delivery

### SFW-024, skill, FAIL

- Delivery, export saved before a path-first reply: holds. `meta.json` lists `export/001 - enhanced-ebike-theft-claim-magicpath-brief.md`, the sandbox copy matches, and the reply opens with the `Saved:` path
- Prompt not pasted: holds
- Header names VIBE-MP inside the Complex tier: FAILS. `Mode: $vibe | Complexity: Medium (6/10) | Framework: VIBE-MP`
- VIBE-MP elements and MagicPath calibration: holds as prose. Vision in the amber-on-asphalt palette and transit-board type, Inspiration in the station high-vis signage and the parcel or flight-status board, Behavior in the screen and back-arrow paragraphs, Experience in the opening paragraph. The avoid-list names Duolingo/Headspace and Stripe/Mercury. The single aesthetic risk, the safety-vest amber accent, is implied rather than named as the risk, read as mappable (judgment call)
- EVOKE passes: holds. "EVOKE (MagicPath) ≈ 45/50 | Gate: passed", gate 42, approximate score read as a reported pass (judgment call)
- Facts: FAILS. MagicPath appears nowhere in the file (grep count 0) and the scenario requires it in the header or body. "No component library, let MagicPath choose" became "No pre-built component library, let the composition stay native to this brief". "our e-bike insurance app" became "a Dutch e-bike insurance app", an unstated fact. The five screens, back links, signal-loss draft, Dutch and English and the tone are kept in meaning
- Scope: holds. The avoid-list and UX floor are rule-mandated. One-handed use, the station correction affordance and the named tracker milestones are read as defaults inside the requested screens (judgment call)
- Share-back invitation: holds. "Share your result for refinement once you generate the MagicPath output"
- Advisory: 448 words against the MagicPath range of 150 to 400, recorded. The reply's "It stays framework-free per your instruction" misstates the request, recorded

### PFW-024, project, FAIL

- Deliverable Block before any commentary: holds. The reply opens with the ```` ```markdown ```` fence
- Header, prompt and attestation, no save claimed: holds. Attestation ends `execution = did not occur | save = did not occur`, and the export-equivalent path uses a guessed `001` not presented as saved
- Prompt not pasted again: holds
- Header names VIBE-MP inside the Complex tier: FAILS. `Complexity: High (7/10)`. The Complex tier needs the label `Complex`, 9 or 10, or a label above High
- VIBE-MP elements and MagicPath calibration: holds as prose. Vision in "graphite, slate, paper-white", Inspiration in "a well-run intake desk" and "a case file being assembled", Behavior in the back-link, draft and page-turn passages, Experience in the opening paragraph. The avoid-list and "As the one deliberate risk" are both named
- EVOKE passes: holds. "EVOKE-MP 46/50", "Gate passed at 42+/50 threshold"
- Facts: holds. MagicPath named ("let MagicPath choose its own materials"), all five screens in order, back links, signal-loss draft, steady and competent, Dutch and English, no component library. "generic fintech gradient" rendered as "the purple-to-blue gradient fintech-onboarding look" is read as the named default, not an alteration (judgment call)
- Scope: holds. The numbered progress rail is the rule-mandated single aesthetic risk, and "not as a bolted-on toggle" is flagged as an assumption about bilingual support, read as a default
- Share-back invitation: holds. "Try this in MagicPath and share what it generates"
- Advisory: 385 words, inside the MagicPath range

---

## 5. TWIN ADJUDICATIONS

`twin_divergence.py` names the same four disagreements this grading found: FW-001, FW-004, FW-006 and FW-009. The other 20 pairs agree, FW-003 on PASS and 19 on FAIL.

### FW-001: SFW-001 FAIL, PFW-001 PASS, runtime fault

- The skill's reply rule is `AGENTS.md` line 61, "Start with the saved file path", and `SKILL.md` line 438 gives its form, `Saved: export/[###] - enhanced-[description].[md|json|yaml]`. The Project writes no file, so the item exists on one side only
- SFW-001 opens with "File verified" and a note on the file's format, and names the path on line 3. Both deliverables pass every other item
- Second direction: 16 of 24 skill replies open with the path, so the rule works. The eight that do not all open with the check the runtime just ran. `AGENTS.md` asks the runtime to verify the file before replying (step 4 of its Strict Sequence), and the reply then reports that check first. That is a reading of the pattern, not a proven cause

### FW-004: SFW-004 PASS, PFW-004 FAIL, scenario tier

- Both twins read the same rubric, `references/depth-framework.md` lines 147 to 165 and `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 134 to 152, byte-identical
- The skill rated Medium (5/10), inside the scenario's Medium tier. The Project rated High (7/10). Both blind recounts put this input in High, at 7 and 8
- So the Project's miss matches the rubric and the skill's pass matches the scenario. The text scenarios were never re-tiered to the recount, and this is the one twin pair more than a point apart
- Second direction: nothing in either package gives the two runtimes a reason to differ here. The difference is how each model read the same rubric

### FW-006: SFW-006 PASS, PFW-006 FAIL, runtime fault with a package source

- The fact rule is the same on both sides: `SKILL.md` line 478 and kernel line 308, "ALWAYS preserve user intent and stated scope", and the invention ban in `SKILL.md` line 512 and kernel line 335
- PFW-006 names the user's clinics "Barter". The user wrote "We run 14 physiotherapy clinics" and named no company
- The name reached the Project model from its own package, line 676 of the Interactive Mode knowledge file, the only Barter text any Project session saw. The skill package carried the same line and two reference titles with the name, and no skill deliverable used it
- Second direction: 22 of 24 Project deliverables left the name out after reading the same line, so the text does not force it. Removing the name from both packages removes the source

### FW-009: SFW-009 FAIL, PFW-009 PASS, runtime fault

- The same fact rule on both sides, `SKILL.md` line 478 and kernel line 308
- The skill narrowed "inbound sea containers carrying lithium batteries" to containers "declared under UN3480", which contradicts its own `un3480_gate`. It also opened with "JSON validated." and named the path on line 3
- The Project kept the process scope, named GPT-4.1 and quoted "Document this process", and passes every item
- Second direction: no source on either side asks for a scope narrowed to one UN number, so the change came from the model

---

## 6. CHECKS ON THE GRADERS' CLAIMS

These key claims were rerun from the files before the merge, and each held:
- `grep -c -i zeeland` on PFW-019 returns 0. `grep -c -w v0` returns 0 on SFW-023 and 1 on PFW-023, in the attestation line only. `grep -c -i magicpath` on SFW-024 returns 0
- `grep -n -i barter` across `export/benchmark/` finds PFW-006 line 4 and PFW-010 line 5 and no skill file
- PFW-005 carries `effective_date: 2026-03-01` on lines 6 and 12
- `replies/SFW-001-turn1.txt` and `replies/SFW-002-turn1.txt` open with a verification note and a validation note, with the path on line 3. A first-line test over all 24 skill replies finds the same eight that fail path-first
- The VIBE and VIBE-MP fact lists say "named in the header or the body", and no text scenario's fact list does
- Every Project event stream shows a Read of the Interactive Mode knowledge file, and line 676 is the only Barter string in any Project tool result
- The merged `results.csv` has 48 rows and 48 unique IDs. Its `facts_intact` column matches the fact row of section 3 on every ID, and its tier failures match the header checker's misses

---

## 7. AGAINST THE CURRENT TIERS

The re-tier in Prompt Improver `534bc67` changed the tier sentence in the Expected signals and Pass/fail lines of the six creative pairs, and their file names, and nothing else. A line-by-line comparison of the twelve files before and after shows no other change.

Read against the new tiers:
- SFW-019 (Low 4 against Low) and PFW-024 (High 7 against High) would pass, since tier was their only failing item. That makes 8 of 48
- PFW-019, SFW-020, PFW-020, SFW-022 and PFW-022 move into their tier and still fail on other items
- SFW-021 and PFW-021 (5 against Low), SFW-023 and PFW-023 (7 against Medium) and SFW-024 (6 against High) stay outside their tier

---

## 8. WHAT CHECK_REPORT.SH FOUND

`bash benchmark/grader/check_report.sh "<this folder>"`, run from `AI Systems/Prompt Improver/`, exited 2: both of its checks reported findings. That number counts checks with findings, not defects.

`twin_divergence` reported "FW-001: skill FAIL, Project PASS", "FW-004: skill PASS, Project FAIL", "FW-006: skill PASS, Project FAIL" and "FW-009: skill FAIL, Project PASS", with 20 agreed, 4 disagreed, 0 not settled and 0 run on one runtime only. That matches section 5.

`lint_replies` wrote `deliverable-lint.csv` and reported 22 clean of 48:
- All 24 skill replies show `attestation_missing` and `header_missing`. That is by design, since a skill reply carries a path and never a block, and the linter checks the kernel's contract
- PFW-012 shows `claimed_execution`, a false positive. Its note after the block says "nothing was written to disk, executed or verified on any filesystem", a denial the pattern reads as a claim
- PFW-016 shows `header_malformed`. Its first line is a mode-detection sentence that starts "Mode: $improve, format locked to $markdown", the same line the grading fails as commentary before the block
- The other 22 Project replies are clean. That does not cover order: `deliverable_not_first` runs only inside `<DELIVERABLE>` tags (`deliverable_lint.py` lines 50 and 196 to 198), which this runner does not write. So PFW-007, PFW-010, PFW-019 and PFW-020 read clean although each opens with commentary

No linter finding changes a verdict.
