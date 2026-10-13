# Grading 1: SFW-001 to SFW-006 and PFW-001 to PFW-006

Graded against the playbook as it stood at the run, at `graded-playbook/sk-prompt-improver/manual-testing-playbook`. Run folder `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh`. Every item below was checked against the reply, the deliverable and, for SFW, the sandbox `exports/` listing and `meta.json`. The structure review was used as a lead only.

```csv
id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note
SFW-001,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The reply's first line is a verification note and not the saved export path, so path-first fails while header, elements, CLEAR, facts and scope all hold."
PFW-001,project,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Block first with header and attestation, RCAF at Medium (6/10), four labelled elements, CLEAR 43/50 passed, facts kept and no scope expansion."
SFW-002,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The header complexity Complex (9/10) sits outside the High tier and the reply's first line does not name the saved path."
PFW-002,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The header complexity Complex (9/10) sits outside the High tier while every other item holds."
SFW-003,skill,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Path-first export with RCAF at Complex (10/10), four labelled elements, CLEAR 46/50 passed, facts kept and no scope expansion."
PFW-003,project,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Block first with header and attestation, RCAF at Complex (9/10), four labelled elements, CLEAR 44/50 passed, facts kept and no scope expansion."
SFW-004,skill,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Path-first export with COSTAR at Medium (5/10), six labelled elements, CLEAR 44/50 passed, facts kept and no scope expansion."
PFW-004,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The header complexity High (7/10) sits outside the Medium tier while every other item holds."
SFW-005,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The prompt states unsupplied facts as settled and requires the announcement to promise the allowance to everyone currently claiming it, and it adds a top-level placeholders section that holds no user fact."
PFW-005,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The header complexity Complex (9/10) sits outside the High tier, the YAML payload does not parse and the invented year 2026 alters the 1 March date."
SFW-006,skill,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Path-first export with COSTAR at Complex (9/10), all six elements labelled with Audience and Response per channel, CLEAR 45/50 passed, facts kept and no scope expansion."
PFW-006,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The prompt rewrites the user's own clinics as Barter's clinics, an altered fact, while header, elements, CLEAR and delivery hold."
```

## Standing judgment calls

These readings apply to every scenario below, so each pair meets the same standard.

- Target model and replaced one-liner: every scenario lists the target model (ChatGPT, the Claude API, Claude, GPT-4.1, Gemini 2.5 Pro) and the current one-line prompt as facts the enhanced prompt carries. A prompt addressed to a model does not normally name its host or quote the prompt it replaces, so I read these two as kept when the deliverable is a replacement prompt fit for that platform and does not contradict it. Under the strict reading, the deliverables that omit the model name would fail the facts item on both runtimes alike
- Scope defaults: a detail inside a requested output that serves a requested rule, such as a status tag, a source citation, a paste slot for a supplied input or a self-check, is read as a default filling a gap. A new output, a new top-level section that holds no user fact, or a data field that serves no requested rule is read as scope expansion
- CLEAR gate: where a reply reports a total and `Gate: passed` without sub-scores, the reported pass is accepted. Where sub-scores are given, each was checked against the floors C7, L7, E10, A7 and R3
- Advisory items recorded only: summary length, perspective counts, token-overhead notes, em dash counts in deliverables and the `NNN` file-number placeholder never decided a verdict

## Scenario results

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

## Twin comparison

- SFW-001 and PFW-001 disagree. Both deliverables pass header, elements, CLEAR, facts and scope. Only the skill reply fails, because it opens with a verification line instead of the saved path, a delivery item the Project twin does not have
- SFW-002 and PFW-002 agree on FAIL. Both headers read Complex (9/10) against the High tier. The skill side also fails path-first
- SFW-003 and PFW-003 agree on PASS. The skill side's "resolved" qualifier and the Project side's extra timeline details were both read as defaults under the same standard
- SFW-004 and PFW-004 disagree. The skill header reads Medium (5/10) and passes, the Project header reads High (7/10) and fails the Medium tier. The deliverables otherwise meet the same standard
- SFW-005 and PFW-005 agree on FAIL for different reasons. The skill side adds facts and a top-level `placeholders` section. The Project side has a Complex header against the High tier, a YAML payload that does not parse and an invented year
- SFW-006 and PFW-006 disagree. Both pass header, elements, CLEAR and scope, and the Project side fails only because it names the user's clinics as Barter's
