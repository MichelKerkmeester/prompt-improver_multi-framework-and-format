---
title: "PFW-001 -- RCAF at Medium complexity for a warehouse shift handover in the Project"
description: "Validates that a single $text $markdown prompt delivers a Deliverable Block in one turn whose header names RCAF at Medium complexity, whose body is organised by RCAF's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# PFW-001 -- RCAF at Medium complexity for a warehouse shift handover in the Project

`$text` binds the Text lane in the Project router and `$markdown` locks Markdown, so the Project writes one RCAF prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The request names RCAF and carries every essential, so the only correct reply is a delivery whose header and body both show RCAF.

---

## 1. OVERVIEW

The user supplies a one-line handover prompt, the warehouse, the target model, the reader, the four exception types and four output rules, and names RCAF. The Project improves that into one prompt organised by RCAF, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A Medium request is where a runtime is most tempted to write a loose paragraph instead of a structured prompt. The test is whether RCAF's four elements become the prompt's actual structure while every handover fact survives.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$text` renders a Medium-tier RCAF Deliverable Block in one turn with every RCAF element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 394). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Can you make our warehouse handover prompt better? Each evening the day lead pastes the exception log into ChatGPT, and the night lead needs a short, factual summary at the 22:00 handover: grouped by type, open items flagged with dock door and pallet ID, under 200 words, no blame. Please use RCAF.`
- Prompt: `$text $markdown Improve this prompt we use in ChatGPT at our Rotterdam warehouse: "Summarise today's exceptions for the next shift." Every evening the day shift lead pastes the exception log (damaged pallets, short picks, late trucks, scanner faults), and the night lead reads the summary at the 22:00 handover. It should group exceptions by type, flag anything still open, give the dock door and pallet ID for each open item and stay under 200 words. No blame language, just facts. Structure it with RCAF. No questions, use your judgment on anything I left open.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode - v0.700.md` line 413, `Custom Instructions.md` line 402). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode - v0.700.md` line 186). It pre-answers every question its route could raise: the comprehensive question `$text` routes to (same file, line 208), answered by the complete request; the framework choice complexity 5 to 6 raises (`Prompt Improver - Interactive Mode - v0.700.md` lines 55-57 and 114-125), answered by naming RCAF; the format question (`Prompt Improver - Interactive Mode - v0.700.md` lines 61-63), answered by the `$markdown` token. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode - v0.700.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$text` binds the Text lane at Standard energy with CLEAR (`Custom Instructions.md` line 47, `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 41-45), and Text mode works in RCAF or COSTAR (`Prompt Improver - Interactive Mode - v0.700.md` lines 576-578), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 71). Framework: the prompt names RCAF, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 404). The library's selection logic lands on RCAF here: its decision table recommends RCAF for complexity 1 to 6 with no audience, creative or precision driver (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 151-156), and its selection algorithm weights RCAF up at complexity 6 or below and for a task that is not audience-specific (lines 99-103). RCAF is also the ordinary default (same file, line 81) and one of the two frameworks Text mode works in. Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 372). Its Framework field names RCAF; a fusion such as `RCAF + CoT` passes when RCAF comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown - v0.141.md` line 113), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. Body: the prompt is visibly organised by RCAF's elements, Role, Context, Action and Format (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 23-27). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The RCAF element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447-455). The chat reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (same file, lines 307-308), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, its `---` divider, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 379). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 388-391). No save, export or file on disk is claimed (line 347). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: ChatGPT as the target, the Rotterdam warehouse, the current one-line prompt it replaces, the day shift lead pasting the exception log, the four exception types damaged pallets, short picks, late trucks and scanner faults, the night lead as reader at the 22:00 handover, grouping by exception type, a flag on anything still open, the dock door and pallet ID for each open item, a limit of 200 words and no blame language, facts only. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming RCAF at Medium complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names RCAF and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Role, Context, Action and Format, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a root-cause analysis section, a KPI dashboard or a message to the carriers are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$text $markdown Improve this prompt we use in ChatGPT at our Rotterdam warehouse: "Summarise today's exceptions for the next shift." Every evening the day shift lead pastes the exception log (damaged pallets, short picks, late trucks, scanner faults), and the night lead reads the summary at the 22:00 handover. It should group exceptions by type, flag anything still open, give the dock door and pallet ID for each open item and stay under 200 words. No blame language, just facts. Structure it with RCAF. No questions, use your judgment on anything I left open.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every RCAF element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Text and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names RCAF at a complexity inside the Medium tier. Step 4 proves every RCAF element is labelled, the CLEAR gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the CLEAR score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each RCAF element to its label in the block, a fact checklist against the block, the export-equivalent path line, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming RCAF at a complexity inside the Medium tier, every RCAF element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion, no save claimed
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 47 and the pre-answered routes in `Prompt Improver - Interactive Mode - v0.700.md` lines 186 and 208, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the RCAF entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 23-27, and the Quick Select row in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 663 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-394 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-001 | RCAF at Medium complexity for a warehouse shift handover in the Project | Verify `$text` renders a Medium-tier RCAF Deliverable Block in one turn with every RCAF element labelled | `$text $markdown Improve this prompt we use in ChatGPT at our Rotterdam warehouse: "Summarise today's exceptions for the next shift." Every evening the day shift lead pastes the exception log (damaged pallets, short picks, late trucks, scanner faults), and the night lead reads the summary at the 22:00 handover. It should group exceptions by type, flag anything still open, give the dock door and pallet ID for each open item and stay under 200 words. No blame language, just facts. Structure it with RCAF. No questions, use your judgment on anything I left open.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Text bound, delivery with no question. Step 3: block first, header names RCAF at the Medium tier. Step 4: RCAF elements labelled, CLEAR passed, facts kept, no expansion, no save claimed | Transcript, CLEAR line, panel state, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) | Framework matrix, selection algorithm, decision table and RCAF patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Quick Select bands, the CLEAR gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Question triggers, `$text` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Energy levels and complexity assessment |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/rcaf-medium-warehouse-handover-canvas.md`
