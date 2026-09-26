---
title: "SFW-009 -- CIDI at Complex complexity for a customs work instruction"
description: "Validates that a single $deep $json prompt delivers an export in one turn whose header names CIDI at Complex complexity, whose body is organised by CIDI's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-009 -- CIDI at Complex complexity for a customs work instruction

`$deep` binds the Deep lane and `$json` locks JSON, so the runtime writes one CIDI prompt, scores it with CLEAR and saves it as a `.json` export before replying. The request names CIDI and carries every essential, so the only correct reply is a delivery whose header and body both show CIDI.

---

## 1. OVERVIEW

The user supplies a one-line documentation prompt, three sources, the port process, role-split steps with four fields each, a conflict rule, a routing rule and two languages, and names CIDI with an importer reason. The runtime improves that into one prompt organised by CIDI, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A compliance-heavy work instruction with conflicting sources tests whether CIDI can hold reconciliation, routing and bilingual output while a JSON importer needs the CIDI keys. The test is structure, facts and a parseable payload together.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a Complex-tier CIDI prompt in one turn with every CIDI element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `We need a much stronger prompt for the lithium-battery customs work instruction: three sources in, steps by role with triggers, systems, documents and hand-offs, conflicts listed and not resolved, UN3480 to the DG officer, Dutch and English. Our importer needs CIDI, in JSON.`
- Prompt: `$deep $json Our freight-forwarding team needs a far better prompt for work instructions; today it is "Document this process." GPT-4.1 gets three inputs: a call transcript with a senior customs broker, our current checklist and the carrier's dangerous-goods rules. It must write the work instruction for clearing inbound sea containers carrying lithium batteries at the port of Rotterdam. Steps are split by role (broker, planner, warehouse), and each has its trigger, the system it happens in, the document it produces and the hand-off. Where the transcript and the checklist disagree, it lists the conflict instead of choosing. Any shipment declared under UN3480 goes to the DG officer before the planner books a slot. Dutch and English versions with the same step numbers. The result feeds our knowledge-base importer, which maps CIDI sections to fields, so it has to be CIDI. Keep the full scope and don't ask questions.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the Question step the Deep flow draws (`references/interactive-mode.md` line 656), answered by the complete request, while line 215 routes `$deep` straight to processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming CIDI; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$json` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$deep` binds the Deep lane with Deep energy, all five perspectives and complexity-matched framework selection (`SKILL.md` lines 79, 349 and 375, `references/depth-framework.md` lines 59-63), and `$json` locks JSON on its own axis (`SKILL.md` lines 71, 83 and 99). Framework: the prompt names CIDI as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The task is CIDI's own ground, process documentation (`assets/framework-pattern-library.md` lines 56-60), but the tier sits well above the 4 to 6 band Quick Select gives CIDI (`references/patterns-evaluation.md` line 679). The input makes a credible case anyway: the user's knowledge-base importer maps CIDI sections to fields. The runtime may flag the fit or suggest CRAFT or TIDD-EC in chat; that note is recorded and does not decide the verdict, and a delivery built on another framework fails. Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names CIDI; a fusion such as `CIDI + CoT` passes when CIDI comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Complex tier: 9 or 10 as a bare number or written n/10, or a label that names a level above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-json.md` lines 127 and 424), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names CIDI, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by CIDI's elements, Context, Instructions, Details and Input (`assets/framework-pattern-library.md` lines 56-60). Every element appears as its own JSON key, at the top level or under one wrapping key, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CIDI element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].json` before replying (`AGENTS.md` lines 34 and 48) and verifies its syntax (`AGENTS.md` line 41). The payload below the header parses as valid JSON with no Markdown inside (`SKILL.md` lines 409 and 497, `assets/format-guide-json.md` lines 130-141 and 416-423). The JSON format guide writes the header as `Mode: $json` (`assets/format-guide-json.md` line 127) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$json` or `$deep` both pass. The reply reports roughly five to ten percent token overhead (`SKILL.md` lines 409 and 501). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: GPT-4.1 as the target, the current one-line prompt it replaces, the three inputs (a call transcript with a senior customs broker, the current checklist, the carrier's dangerous-goods rules), clearing inbound sea containers carrying lithium batteries at the port of Rotterdam, steps split by the roles broker, planner and warehouse, a trigger, system, document and hand-off for each step, conflicts between transcript and checklist listed rather than resolved, any UN3480 shipment routed to the DG officer before the planner books a slot, and Dutch and English versions with the same step numbers. The conflict rule is list, not choose: a prompt that tells the model to prefer either source alters a supplied fact. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming CIDI at Complex complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as JSON
- Pass/fail: PASS if all of these hold: the delivery is a verified `.json` export saved before a path-first reply; the header names CIDI and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Context, Instructions, Details and Input, each labelled; CLEAR passes its gate; the payload below the header parses as JSON; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a customs tariff lookup, a cost estimate or a training quiz are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep $json Our freight-forwarding team needs a far better prompt for work instructions; today it is "Document this process." GPT-4.1 gets three inputs: a call transcript with a senior customs broker, our current checklist and the carrier's dangerous-goods rules. It must write the work instruction for clearing inbound sea containers carrying lithium batteries at the port of Rotterdam. Steps are split by role (broker, planner, warehouse), and each has its trigger, the system it happens in, the document it produces and the hand-off. Where the transcript and the checklist disagree, it lists the conflict instead of choosing. Any shipment declared under UN3480 goes to the DG officer before the planner books a slot. Dutch and English versions with the same step numbers. The result feeds our knowledge-base importer, which maps CIDI sections to fields, so it has to be CIDI. Keep the full scope and don't ask questions.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .json export, then parse the payload below the single-line header -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every CIDI element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Deep and delivers without a question. Step 3 proves the export exists and opens with a header that names CIDI at a complexity inside the Complex tier, with a payload that parses as JSON. Step 4 proves every CIDI element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each CIDI element to its label in the file, the parse result for the payload below the header and the token-overhead note, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.json` export and a path-first reply, a header naming CIDI at a complexity inside the Complex tier, every CIDI element labelled, a passing CLEAR result, a payload that parses as JSON, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 79 and 349 and the pre-answered routes in `references/interactive-mode.md` lines 200, 215 and 656, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the CIDI entry in the framework matrix, `assets/framework-pattern-library.md` lines 56-60, and the Quick Select row in `references/patterns-evaluation.md` line 679 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-json.md` lines 123-141 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-009 | CIDI at Complex complexity for a customs work instruction | Verify `$deep` delivers a Complex-tier CIDI prompt in one turn with every CIDI element labelled | `$deep $json Our freight-forwarding team needs a far better prompt for work instructions; today it is "Document this process." GPT-4.1 gets three inputs: a call transcript with a senior customs broker, our current checklist and the carrier's dangerous-goods rules. It must write the work instruction for clearing inbound sea containers carrying lithium batteries at the port of Rotterdam. Steps are split by role (broker, planner, warehouse), and each has its trigger, the system it happens in, the document it produces and the hand-off. Where the transcript and the checklist disagree, it lists the conflict instead of choosing. Any shipment declared under UN3480 goes to the DG officer before the planner books a slot. Dutch and English versions with the same step numbers. The result feeds our knowledge-base importer, which maps CIDI sections to fields, so it has to be CIDI. Keep the full scope and don't ask questions.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Deep bound, delivery with no question. Step 3: header names CIDI at the Complex tier, payload parses. Step 4: CIDI elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist, parse result | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and CIDI patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$deep` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-json.md`](../../assets/format-guide-json.md) | JSON header, syntax and delivery rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-009
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/cidi-complex-lithium-customs-instruction-export.md`
