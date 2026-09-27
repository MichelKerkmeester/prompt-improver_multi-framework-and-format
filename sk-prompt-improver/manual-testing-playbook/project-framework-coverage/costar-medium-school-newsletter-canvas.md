---
title: "PFW-004 -- COSTAR at Medium complexity for a school parent newsletter in the Project"
description: "Validates that a single $improve $markdown prompt delivers a Deliverable Block in one turn whose header names COSTAR at Medium complexity, whose body is organised by COSTAR's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# PFW-004 -- COSTAR at Medium complexity for a school parent newsletter in the Project

`$improve` binds the Improve lane in the Project router and `$markdown` locks Markdown, so the Project writes one COSTAR prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The request names COSTAR and carries every essential, so the only correct reply is a delivery whose header and body both show COSTAR.

---

## 1. OVERVIEW

The user supplies a one-line newsletter prompt, three inputs, the parents' reading situation, the language level, tone, layout and length rules and a privacy rule, and names COSTAR. The Project improves that into one prompt organised by COSTAR, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Audience-driven content is COSTAR's home ground, so a runtime that falls back to RCAF here is not using the library. The test is whether all six COSTAR elements appear and the parents' constraints survive.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` renders a Medium-tier COSTAR Deliverable Block in one turn with every COSTAR element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 394). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Could you improve our school's newsletter prompt? Parents read it on their phones, many speak Dutch as a second language, so plain language, event dates at the top, under 350 words and no pupil names. COSTAR would be good.`
- Prompt: `$improve $markdown Please improve the prompt our primary school office uses in ChatGPT for the monthly parent newsletter: "Write a newsletter for parents about this month." The office pastes in the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes. Parents read it on their phones, and many speak Dutch as a second language, so it needs plain B1-level language, short paragraphs and a warm but not chatty tone. Event dates go in a list at the top. Keep it under 350 words and never name individual pupils. Use COSTAR for the structure. Don't ask me anything, just make sensible calls where I left gaps.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode - v0.700.md` line 413, `Custom Instructions.md` line 402). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode - v0.700.md` line 186). It pre-answers every question its route could raise: the format question `$improve` routes to (same file, line 203), answered by the `$markdown` token; the framework choice complexity 5 to 6 raises (`Prompt Improver - Interactive Mode - v0.700.md` lines 55-57 and 114-125), answered by naming COSTAR. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode - v0.700.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`Custom Instructions.md` line 48, `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 41-45, `Prompt Improver - Interactive Mode - v0.700.md` lines 583-585), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 71). Framework: the prompt names COSTAR, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 404). The library's selection logic lands on COSTAR here: its decision table recommends COSTAR at any complexity when audience and a creative element drive the task (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 157-162), its selection algorithm weights COSTAR up for an audience-specific task (lines 105-109) and Quick Select places COSTAR at 3 to 6 with an audience (`Prompt Improver - Patterns and Evaluation - v0.212.md` line 664). Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 372). Its Framework field names COSTAR; a fusion such as `COSTAR + CoT` passes when COSTAR comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown - v0.141.md` line 113), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`Prompt Improver - Format Guide Markdown - v0.141.md` lines 104 and 114), but the kernel template asks only for the framework used (`Custom Instructions.md` line 372), so that template is the guide's common case and not a limit: the header names COSTAR, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by COSTAR's elements, Context, Objective, Style, Tone, Audience and Response (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 28-32). Every element appears as its own heading, bold label or list label, in any letter case; Style and Tone may share one label that names both, since the library's own COSTAR optimisation merges them (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` line 559); an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The COSTAR element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447-455). The chat reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (same file, lines 307-308), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, its `---` divider, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 379). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 388-391). No save, export or file on disk is claimed (line 347). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: ChatGPT as the target, the primary school office, the monthly parent newsletter, the current one-line prompt it replaces, the three inputs (the headteacher's bullet notes, upcoming event dates, lunch or bus timetable changes), parents reading on their phones, many with Dutch as a second language, plain B1-level language, short paragraphs, a warm but not chatty tone, event dates in a list at the top, a limit of 350 words and no pupil named. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming COSTAR at Medium complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names COSTAR and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Context, Objective, Style, Tone, Audience and Response, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: an English translation, a parent survey or a social media post are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $markdown Please improve the prompt our primary school office uses in ChatGPT for the monthly parent newsletter: "Write a newsletter for parents about this month." The office pastes in the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes. Parents read it on their phones, and many speak Dutch as a second language, so it needs plain B1-level language, short paragraphs and a warm but not chatty tone. Event dates go in a list at the top. Keep it under 350 words and never name individual pupils. Use COSTAR for the structure. Don't ask me anything, just make sensible calls where I left gaps.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every COSTAR element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names COSTAR at a complexity inside the Medium tier. Step 4 proves every COSTAR element is labelled, the CLEAR gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the CLEAR score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each COSTAR element to its label in the block, a fact checklist against the block, the export-equivalent path line, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming COSTAR at a complexity inside the Medium tier, every COSTAR element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion, no save claimed
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 48 and the pre-answered routes in `Prompt Improver - Interactive Mode - v0.700.md` lines 186 and 203, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the COSTAR entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 28-32, and the Quick Select row in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 664 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-394 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-004 | COSTAR at Medium complexity for a school parent newsletter in the Project | Verify `$improve` renders a Medium-tier COSTAR Deliverable Block in one turn with every COSTAR element labelled | `$improve $markdown Please improve the prompt our primary school office uses in ChatGPT for the monthly parent newsletter: "Write a newsletter for parents about this month." The office pastes in the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes. Parents read it on their phones, and many speak Dutch as a second language, so it needs plain B1-level language, short paragraphs and a warm but not chatty tone. Event dates go in a list at the top. Keep it under 350 words and never name individual pupils. Use COSTAR for the structure. Don't ask me anything, just make sensible calls where I left gaps.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Improve bound, delivery with no question. Step 3: block first, header names COSTAR at the Medium tier. Step 4: COSTAR elements labelled, CLEAR passed, facts kept, no expansion, no save claimed | Transcript, CLEAR line, panel state, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) | Framework matrix, selection algorithm, decision table and COSTAR patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Quick Select bands, the CLEAR gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Question triggers, `$improve` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Energy levels and complexity assessment |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/costar-medium-school-newsletter-canvas.md`
