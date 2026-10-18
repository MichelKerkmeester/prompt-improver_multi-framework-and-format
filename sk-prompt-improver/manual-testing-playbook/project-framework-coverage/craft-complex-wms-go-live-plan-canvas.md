---
title: "PFW-018 -- CRAFT at Complex complexity for a WMS go-live plan in the Project"
description: "Validates that a single $deep $markdown prompt delivers a Deliverable Block in one turn whose header names CRAFT at Complex complexity, whose body is organised by CRAFT's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.1.1.0
---

# PFW-018 -- CRAFT at Complex complexity for a WMS go-live plan in the Project

`$deep` binds the Deep lane in the Project router and `$markdown` locks Markdown, so the Project writes one CRAFT prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The request names CRAFT and carries every essential, so the only correct reply is a delivery whose header and body both show CRAFT.

---

## 1. OVERVIEW

The user supplies a one-line go-live prompt, two sites with volumes, the integrations, a blackout window, a pilot order and gate, five plan parts, a rollback limit and a success target, and names CRAFT. The Project improves that into one prompt organised by CRAFT, scores it with CLEAR and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A two-site go-live with gates, a blackout window and a rollback limit is the most planning-heavy prompt in the set. The test is whether CRAFT carries every dependency and gate without the runtime inventing scope.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` renders a Complex-tier CRAFT Deliverable Block in one turn with every CRAFT element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Delivery shape: the reply opens with the Deliverable Block, one bare code fence with no language tag holding only the improved prompt, with no preamble (`Custom Instructions.md` DELIVERY PROTOCOL). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it
- Real user request: `I need a proper go-live plan prompt for our new WMS across Tilburg and Liège: no go-live in peak season, Liège first, Tilburg only after four weeks above 99.5% pick accuracy, workstreams with dependencies, a go or no-go checklist, hypercare and a 12-hour rollback, aiming for no missed carrier cut-offs. Use CRAFT.`
- Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: a question goes out only when the request cannot be defaulted, and then it covers every missing essential in a single message (`Prompt Improver - Interactive Mode.md` line 395, `Custom Instructions.md` line 259). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode.md` line 180). Under the deliver-first rule no route raises a question here: format, framework, scope and library are soft gaps that take their defaults and become numbered open items after the deliverable, so a question asked anyway is recorded and the scenario fails for missing delivery. Lane: `$deep` binds the Deep lane with Deep energy, all five perspectives and CLEAR (`Custom Instructions.md` line 51, `Prompt Improver - DEPTH Thinking Framework.md` lines 46-50), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 73). Framework: the prompt names CRAFT, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 261). The library's selection logic lands on CRAFT here: its matrix names complex projects and planning (`Prompt Improver - Assets - Framework Pattern Library.md` lines 53-57), its decision table recommends CRAFT at 7 to 10 (lines 169-174), Quick Select places it at 7 to 10 (`Prompt Improver - Patterns and Evaluation.md` line 668) and the library pairs CRAFT with every technique for maximum power (`Prompt Improver - Assets - Framework Pattern Library.md` lines 540-542). Header: the chat line after the fence carries the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header facts (`Custom Instructions.md` line 231). Its Framework field names CRAFT; a fusion such as `CRAFT + CoT` passes when CRAFT comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown.md` line 113), and it must sit inside the Complex tier: the label `Complex`, or 9 or 10 as a bare number or written n/10, or another label above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. Body: the prompt is visibly organised by CRAFT's elements, Context, Role, Action, Format and Target (`Prompt Improver - Assets - Framework Pattern Library.md` lines 53-57). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CRAFT element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation.md` lines 302 and 447-455). The chat reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (same file, lines 307-308), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary as one bare code fence holding only the prompt, with no header line, divider or footer inside it (`Custom Instructions.md` lines 156-342, 413 and 422). After the fence the chat reports the `Mode: | Complexity: | Framework:` header line, the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR result with gate status, a short summary and the numbered open items, each a bold topic over a `- **Situation:**` and a `- **Open:**` bullet or `None identified`, and does not paste the prompt again (`Custom Instructions.md` lines 178 and 232-434). No save, export or file on disk is claimed (line 184). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: Claude as the target, the current one-line prompt it replaces, Tilburg at 38,000 order lines a day and Liège at 12,000, one WMS vendor, integrations with SAP ERP and three carriers, no go-live between 15 November and 10 January, Liège first as the pilot, Tilburg only after four weeks of pick accuracy above 99.5% in Liège, the workstreams data migration, integrations, training for 260 pickers in two languages and cutover, their dependencies, a go or no-go checklist, a hypercare plan, a rollback path that restores the old system within 12 hours, and the target of no missed carrier cut-off in the first two weeks. Target carries the success target as stated, no missed carrier cut-off in the first two weeks, and the 99.5% gate and the 12-hour rollback keep their numbers. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One fence-first reply whose chat header line names CRAFT at Complex complexity and whose Deliverable Block reads back as a CRAFT prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, one bare code fence holding only the prompt, the chat after it carries the header line and the numbered open items, and no save is claimed; the header line names CRAFT and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Context, Role, Action, Format and Target, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the fence is tagged or holds more than the prompt, the chat header line or the open items are missing, a question about a soft gap precedes the deliverable, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a vendor comparison, a budget or a third distribution centre are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every CRAFT element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Deep and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names CRAFT at a complexity inside the Complex tier. Step 4 proves every CRAFT element is labelled, the CLEAR gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the CLEAR score line with gate status, the opening fence, the header line with the framework, complexity and mode label used, a map from each CRAFT element to its label in the block, a fact checklist against the block, the export-equivalent path line, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A bare-fence Deliverable Block before commentary holding only the prompt, a chat header line naming CRAFT at a complexity inside the Complex tier, every CRAFT element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion, no save claimed
- **Fail**: A question instead of a delivery, commentary before the block, a tagged fence or one holding more than the prompt, a missing chat header line or open items, a soft-gap question before the deliverable, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 51 and the pre-answered routes in `Prompt Improver - Interactive Mode.md` lines 180, 195 and 625, plus lines 77-85, when the reply asked instead of delivering
2. Re-check the CRAFT entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library.md` lines 53-57, and the Quick Select row in `Prompt Improver - Patterns and Evaluation.md` line 668 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `Prompt Improver - Patterns and Evaluation.md` lines 302 and 447 and the Delivery Protocol in `Custom Instructions.md` lines 204-437 when the score, the block order, the header line or the open items are off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-018 | CRAFT at Complex complexity for a WMS go-live plan in the Project | Verify `$deep` renders a Complex-tier CRAFT Deliverable Block in one turn with every CRAFT element labelled | `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Deep bound, delivery with no question. Step 3: block first, header names CRAFT at the Complex tier. Step 4: CRAFT elements labelled, CLEAR passed, facts kept, no expansion, no save claimed | Transcript, CLEAR line, opening fence, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and open items |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library.md>) | Framework matrix, selection algorithm, decision table and CRAFT patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | Quick Select bands, the CLEAR gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | Question triggers, `$deep` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework.md>) | Energy levels and complexity assessment |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-018
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/craft-complex-wms-go-live-plan-canvas.md`
