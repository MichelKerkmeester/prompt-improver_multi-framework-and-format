---
title: "PFW-007 -- CIDI at Medium complexity for a credit-note procedure in the Project"
description: "Validates that a single $improve $yaml prompt delivers a Deliverable Block in one turn whose header names CIDI at Medium complexity, whose body is organised by CIDI's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# PFW-007 -- CIDI at Medium complexity for a credit-note procedure in the Project

`$improve` binds the Improve lane in the Project router and `$yaml` locks YAML, so the Project writes one CIDI prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The request names CIDI and carries every essential, so the only correct reply is a delivery whose header and body both show CIDI.

---

## 1. OVERVIEW

The user supplies a one-line SOP prompt, the transcript input, the procedure's audience and subject, three fields per step, an approval threshold and two fidelity rules, and names CIDI. The Project improves that into one prompt organised by CIDI, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Process documentation is CIDI's home ground, and a YAML lock makes the structure checkable key by key. The test is whether the four CIDI keys organise the prompt and the approval threshold survives.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` renders a Medium-tier CIDI Deliverable Block in one turn with every CIDI element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 229). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Can you improve the prompt that turns a clerk's screen-recording narration into a credit-note procedure for new accounts-payable staff? Each step needs the action, the screen and the expected result, with second-approver steps above EUR 5,000 marked. CIDI, in YAML please.`
- Prompt: `$improve $yaml Improve our SOP-writing prompt for Claude: "Turn this into a how-to for the team." We paste a transcript of a senior clerk narrating a screen recording, and Claude writes a step-by-step procedure for new accounts-payable clerks on booking a supplier credit note against an open invoice. Each step needs one action, the screen or field it happens in and what the clerk should see afterwards. Steps that need a second approver, for credit notes above EUR 5,000, must be marked. Keep the clerk's field names exactly as spoken and leave out the chit-chat. The result goes into Confluence. Use CIDI. No questions, just use your judgment.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode.md` line 413, `Custom Instructions.md` line 237). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode.md` line 186). It pre-answers every question its route could raise: the format question `$improve` routes to (same file, line 203), answered by the `$yaml` token; the framework choice complexity 5 to 6 raises (`Prompt Improver - Interactive Mode.md` lines 55-57 and 114-125), answered by naming CIDI. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`Custom Instructions.md` line 48, `Prompt Improver - DEPTH Thinking Framework.md` lines 41-45, `Prompt Improver - Interactive Mode.md` lines 583-585), and `$yaml` locks YAML on its own axis (`Custom Instructions.md` lines 43, 56 and 71). Framework: the prompt names CIDI, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 239). The library's selection logic lands on CIDI here: its matrix names process documentation and tutorials (`Prompt Improver - Assets - Framework Pattern Library.md` lines 38-42) and Quick Select places CIDI at 4 to 6 for instruction-led work (`Prompt Improver - Patterns and Evaluation.md` line 665). Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 207). Its Framework field names CIDI; a fusion such as `CIDI + CoT` passes when CIDI comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown.md` line 113), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`Prompt Improver - Format Guide YAML.md` lines 114 and 452), but the kernel template asks only for the framework used (`Custom Instructions.md` line 207), so that template is the guide's common case and not a limit: the header names CIDI, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by CIDI's elements, Context, Instructions, Details and Input (`Prompt Improver - Assets - Framework Pattern Library.md` lines 38-42). Every element appears as its own YAML key, at the top level or under one wrapping key, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CIDI element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation.md` lines 302 and 447-455). The chat reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (same file, lines 307-308), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, its `---` divider, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 154-320, 372 and 379). The header and attestation sit outside the format lock, which covers only the payload between the two `---` dividers (`Custom Instructions.md` line 217), and that payload parses as valid YAML with no Markdown inside (`Custom Instructions.md` line 241, `Prompt Improver - Format Guide YAML.md` lines 125-136 and 444-451); the fence that delimits the block in a no-panel session is not part of the payload. The kernel template writes the header as `Mode: $[mode]` (`Custom Instructions.md` line 207) while the YAML format guide writes `Mode: $yaml` (`Prompt Improver - Format Guide YAML.md` line 114), so a header labelled `$yaml` or `$improve` both pass. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header, since the header sits outside the format lock in either form; the form used is recorded. After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].yaml`, the CLEAR result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 176 and 223-391), plus roughly three to seven percent token overhead (lines 157 and 225). No save, export or file on disk is claimed (line 182). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: Claude as the target, the current one-line prompt it replaces, a transcript of a senior clerk narrating a screen recording as input, a step-by-step procedure for new accounts-payable clerks, booking a supplier credit note against an open invoice, one action per step with the screen or field and the expected result, second-approver steps marked for credit notes above EUR 5,000, field names kept exactly as spoken, the chit-chat left out and Confluence as the destination. Input describes the transcript the user pastes; a placeholder for it passes, and invented transcript content does not. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CIDI at Medium complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, with a passing CLEAR result in chat and no file claimed
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names CIDI and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Context, Instructions, Details and Input, each labelled; CLEAR passes its gate; the payload between the metadata lines and their `---` dividers parses as YAML; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a quiz for new clerks, a process flowchart or an escalation matrix are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $yaml Improve our SOP-writing prompt for Claude: "Turn this into a how-to for the team." We paste a transcript of a senior clerk narrating a screen recording, and Claude writes a step-by-step procedure for new accounts-payable clerks on booking a supplier credit note against an open invoice. Each step needs one action, the screen or field it happens in and what the clerk should see afterwards. Steps that need a second approver, for credit notes above EUR 5,000, must be marked. Keep the clerk's field names exactly as spoken and leave out the chit-chat. The result goes into Confluence. Use CIDI. No questions, just use your judgment.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block, then parse the payload between the metadata lines and their --- dividers -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every CIDI element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names CIDI at a complexity inside the Medium tier, with a payload that parses as YAML. Step 4 proves every CIDI element is labelled, the CLEAR gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the CLEAR score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each CIDI element to its label in the block, the parse result for the payload between the metadata lines and their `---` dividers and the token-overhead note, a fact checklist against the block, the export-equivalent path line, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming CIDI at a complexity inside the Medium tier, every CIDI element labelled, a passing CLEAR result, a payload that parses as YAML, every supplied fact intact, no scope expansion, no save claimed
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion, any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 48 and the pre-answered routes in `Prompt Improver - Interactive Mode.md` lines 186 and 203, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the CIDI entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library.md` lines 38-42, and the Quick Select row in `Prompt Improver - Patterns and Evaluation.md` line 665 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `Prompt Improver - Patterns and Evaluation.md` lines 302 and 447 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 202-394 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-007 | CIDI at Medium complexity for a credit-note procedure in the Project | Verify `$improve` renders a Medium-tier CIDI Deliverable Block in one turn with every CIDI element labelled | `$improve $yaml Improve our SOP-writing prompt for Claude: "Turn this into a how-to for the team." We paste a transcript of a senior clerk narrating a screen recording, and Claude writes a step-by-step procedure for new accounts-payable clerks on booking a supplier credit note against an open invoice. Each step needs one action, the screen or field it happens in and what the clerk should see afterwards. Steps that need a second approver, for credit notes above EUR 5,000, must be marked. Keep the clerk's field names exactly as spoken and leave out the chit-chat. The result goes into Confluence. Use CIDI. No questions, just use your judgment.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Improve bound, delivery with no question. Step 3: block first, header names CIDI at the Medium tier, payload parses. Step 4: CIDI elements labelled, CLEAR passed, facts kept, no expansion, no save claimed | Transcript, CLEAR line, panel state, header, element map, fact checklist, parse result | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library.md>) | Framework matrix, selection algorithm, decision table and CIDI patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | Quick Select bands, the CLEAR gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | Question triggers, `$improve` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework.md>) | Energy levels and complexity assessment |
| [Format Guide YAML knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide YAML.md>) | YAML header, syntax and delivery rules |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown.md>) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-007
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/cidi-medium-credit-note-procedure-canvas.md`
