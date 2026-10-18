---
title: "SFW-018 -- CRAFT at Complex complexity for a WMS go-live plan"
description: "Validates that a single $deep $markdown prompt delivers an export in one turn whose header names CRAFT at Complex complexity, whose body is organised by CRAFT's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.1.1.0
---

# SFW-018 -- CRAFT at Complex complexity for a WMS go-live plan

`$deep` binds the Deep lane and `$markdown` locks Markdown, so the runtime writes one CRAFT prompt, scores it with CLEAR and saves it as a `.md` export before replying. The request names CRAFT and carries every essential, so the only correct reply is a delivery whose header and body both show CRAFT.

---

## 1. OVERVIEW

The user supplies a one-line go-live prompt, two sites with volumes, the integrations, a blackout window, a pilot order and gate, five plan parts, a rollback limit and a success target, and names CRAFT. The runtime improves that into one prompt organised by CRAFT, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A two-site go-live with gates, a blackout window and a rollback limit is the most planning-heavy prompt in the set. The test is whether CRAFT carries every dependency and gate without the runtime inventing scope.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a Complex-tier CRAFT prompt in one turn with every CRAFT element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I need a proper go-live plan prompt for our new WMS across Tilburg and Liège: no go-live in peak season, Liège first, Tilburg only after four weeks above 99.5% pick accuracy, workstreams with dependencies, a go or no-go checklist, hypercare and a 12-hour rollback, aiming for no missed carrier cut-offs. Use CRAFT.`
- Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: a question goes out only when the request cannot be defaulted, and then it covers every missing essential in a single message (`SKILL.md` line 434). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 416, `references/interactive-mode.md` line 194). Under the deliver-first rule no route raises a question here: format, framework, scope and library are soft gaps that take their defaults and become numbered open items after the deliverable, so a question asked anyway is recorded and the scenario fails for missing delivery. Lane: `$deep` binds the Deep lane with Deep energy, all five perspectives and complexity-matched framework selection (`SKILL.md` lines 79, 382 and 408, `references/depth-framework.md` lines 59-63), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 101). Framework: the prompt names CRAFT as a hint the runtime detects (`SKILL.md` lines 365 and 414), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 420 and 546). The library's selection logic lands on CRAFT here: its matrix names complex projects and planning (`assets/framework-pattern-library.md` lines 71-75), its decision table recommends CRAFT at 7 to 10 (lines 187-192), Quick Select places it at 7 to 10 (`references/patterns-evaluation.md` line 682) and the library pairs CRAFT with every technique for maximum power (`assets/framework-pattern-library.md` lines 558-560). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 615-616). Its Framework field names CRAFT; a fusion such as `CRAFT + CoT` passes when CRAFT comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 127), and it must sit inside the Complex tier: the label `Complex`, or 9 or 10 as a bare number or written n/10, or another label above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. Body: the prompt is visibly organised by CRAFT's elements, Context, Role, Action, Format and Target (`assets/framework-pattern-library.md` lines 71-75). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CRAFT element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 501-502, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 573-574), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 509-511) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header, its `---` divider and the prompt (`SKILL.md` lines 615-619). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-65). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: Claude as the target, the current one-line prompt it replaces, Tilburg at 38,000 order lines a day and Liège at 12,000, one WMS vendor, integrations with SAP ERP and three carriers, no go-live between 15 November and 10 January, Liège first as the pilot, Tilburg only after four weeks of pick accuracy above 99.5% in Liège, the workstreams data migration, integrations, training for 260 pickers in two languages and cutover, their dependencies, a go or no-go checklist, a hypercare plan, a rollback path that restores the old system within 12 hours, and the target of no missed carrier cut-off in the first two weeks. Target carries the success target as stated, no missed carrier cut-off in the first two weeks, and the 99.5% gate and the 12-hour rollback keep their numbers. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRAFT at Complex complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names CRAFT and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Context, Role, Action, Format and Target, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a vendor comparison, a budget or a third distribution centre are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every CRAFT element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Deep and delivers without a question. Step 3 proves the export exists and opens with a header that names CRAFT at a complexity inside the Complex tier. Step 4 proves every CRAFT element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each CRAFT element to its label in the file, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming CRAFT at a complexity inside the Complex tier, every CRAFT element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 79 and 382 and the pre-answered routes in `references/interactive-mode.md` lines 194, 209 and 639, plus lines 91-99, when the reply asked instead of delivering
2. Re-check the CRAFT entry in the framework matrix, `assets/framework-pattern-library.md` lines 71-75, and the Quick Select row in `references/patterns-evaluation.md` line 682 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 501-502, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-128 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-018 | CRAFT at Complex complexity for a WMS go-live plan | Verify `$deep` delivers a Complex-tier CRAFT prompt in one turn with every CRAFT element labelled | `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Deep bound, delivery with no question. Step 3: header names CRAFT at the Complex tier. Step 4: CRAFT elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and CRAFT patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$deep` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-018
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/craft-complex-wms-go-live-plan-export.md`
