---
title: "PFW-013 -- CRISPE at Medium complexity for oat milk positioning in the Project"
description: "Validates that a single $improve $markdown prompt delivers a Deliverable Block in one turn whose header names CRISPE at Medium complexity, whose body is organised by CRISPE's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# PFW-013 -- CRISPE at Medium complexity for oat milk positioning in the Project

`$improve` binds the Improve lane in the Project router and `$markdown` locks Markdown, so the Project writes one CRISPE prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The request names CRISPE and carries every essential, so the only correct reply is a delivery whose header and body both show CRISPE.

---

## 1. OVERVIEW

The user supplies a one-line marketing prompt, the company, market and price position, a strategist persona, three barista concerns and three positioning routes with their fields, and names CRISPE. The Project improves that into one prompt organised by CRISPE, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

CRISPE's Experiment element is its signature, and it only works when the prompt asks for the options the user wanted. The test is whether exactly three positioning routes with their tests come out of a visibly CRISPE prompt.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` renders a Medium-tier CRISPE Deliverable Block in one turn with every CRISPE element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 390). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Can you make my oat-milk marketing prompt stronger? I want Claude to think like a B2B strategist about Belgian independent cafés and give three different positioning routes with a pitch, the café type and a cheap one-month test. Please use CRISPE.`
- Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode - v0.700.md` line 413, `Custom Instructions.md` line 398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode - v0.700.md` line 186). It pre-answers every question its route could raise: the format question `$improve` routes to (same file, line 203), answered by the `$markdown` token; the framework choice complexity 5 to 6 raises (`Prompt Improver - Interactive Mode - v0.700.md` lines 55-57 and 114-125), answered by naming CRISPE. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode - v0.700.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`Custom Instructions.md` line 48, `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 41-45, `Prompt Improver - Interactive Mode - v0.700.md` lines 583-585), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 71). Framework: the prompt names CRISPE, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 400). The library's selection logic lands on CRISPE here: its matrix names strategy and exploration (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 48-52) and Quick Select places CRISPE at 5 to 7 for creative and exploratory work (`Prompt Improver - Patterns and Evaluation - v0.212.md` line 666). Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 372). Its Framework field names CRISPE; a fusion such as `CRISPE + CoT` passes when CRISPE comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown - v0.141.md` line 109), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`Prompt Improver - Format Guide Markdown - v0.141.md` lines 104 and 110), but the kernel template asks only for the framework used (`Custom Instructions.md` line 372), so that template is the guide's common case and not a limit: the header names CRISPE, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by CRISPE's elements, Capacity, Insight, Statement, Personality and Experiment (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 48-52). Every element appears as its own heading, bold label or list label, in any letter case; Capacity may read `Capacity and Role`; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CRISPE element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447-455). The chat reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (same file, lines 307-308), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 384-387). No save, export or file on disk is claimed (line 347). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: Claude as a sparring partner, the current one-line prompt it replaces, a small Ghent start-up, an oat barista milk for independent cafés in Belgium priced 15% above the market leader, a B2B food-and-beverage strategist persona, the three barista concerns foam stability, taste with espresso and price per cup, exactly three clearly different positioning routes, a one-line pitch, the café type it wins and a cheap one-month test for each, and a frank, practical style with no buzzwords. Experiment asks for exactly the three positioning routes with their three fields, and a fourth route is scope expansion. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRISPE at Medium complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names CRISPE and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Capacity, Insight, Statement, Personality and Experiment, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a full marketing plan, a price change or a consumer retail route are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every CRISPE element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names CRISPE at a complexity inside the Medium tier. Step 4 proves every CRISPE element is labelled, the CLEAR gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the CLEAR score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each CRISPE element to its label in the block, a fact checklist against the block, the export-equivalent path line, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming CRISPE at a complexity inside the Medium tier, every CRISPE element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion, no save claimed
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 48 and the pre-answered routes in `Prompt Improver - Interactive Mode - v0.700.md` lines 186 and 203, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the CRISPE entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 48-52, and the Quick Select row in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 666 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-013 | CRISPE at Medium complexity for oat milk positioning in the Project | Verify `$improve` renders a Medium-tier CRISPE Deliverable Block in one turn with every CRISPE element labelled | `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Improve bound, delivery with no question. Step 3: block first, header names CRISPE at the Medium tier. Step 4: CRISPE elements labelled, CLEAR passed, facts kept, no expansion, no save claimed | Transcript, CLEAR line, panel state, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) | Framework matrix, selection algorithm, decision table and CRISPE patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Quick Select bands, the CLEAR gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Question triggers, `$improve` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Energy levels and complexity assessment |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-013
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/crispe-medium-oat-milk-positioning-canvas.md`
