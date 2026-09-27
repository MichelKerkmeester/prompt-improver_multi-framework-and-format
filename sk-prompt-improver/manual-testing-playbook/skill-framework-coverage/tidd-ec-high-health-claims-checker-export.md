---
title: "SFW-011 -- TIDD-EC at High complexity for a health-claims checker"
description: "Validates that a single $improve $json prompt delivers an export in one turn whose header names TIDD-EC at High complexity, whose body is organised by TIDD-EC's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-011 -- TIDD-EC at High complexity for a health-claims checker

`$improve` binds the Improve lane and `$json` locks JSON, so the runtime writes one TIDD-EC prompt, scores it with CLEAR and saves it as a `.json` export before replying. The request names TIDD-EC and carries every essential, so the only correct reply is a delivery whose header and body both show TIDD-EC.

---

## 1. OVERVIEW

The user supplies a one-line checker prompt, the listing inputs, the approved-claims list, three fields per flag, two prohibitions and a worked example pair, and names TIDD-EC. The runtime improves that into one prompt organised by TIDD-EC, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A compliance checker with a JSON payload is the textbook TIDD-EC case. The test is whether Do's and Don'ts carry the user's rules exactly and Examples reuse the worked pair.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` delivers a High-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Please improve the prompt that checks our supplement listings against the 38 approved EU health claims: flag each unapproved claim with the sentence, the broken rule and a compliant rewrite, leave compliant text alone and never judge efficacy. TIDD-EC, in JSON.`
- Prompt: `$improve $json Improve the compliance prompt behind the listing checker for our supplement brand's marketplace listings. Current version: "Check if this product text is OK." GPT-4.1 receives the title, description and bullet points of one listing, plus our approved list of 38 EU-authorised health claims with each call. It flags every health claim that is not on the list, and for each flag returns the exact sentence, the rule it breaks (unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts. It must not touch text that is already compliant and must not judge whether the product works. Worked example: "Boosts your immune system" is unauthorised, while "Vitamin C contributes to the normal function of the immune system" is approved. Use TIDD-EC and keep the full scope. No questions, decide the open points yourself.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the format question `$improve` routes to (`references/interactive-mode.md` line 217), answered by the `$json` token; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming TIDD-EC. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`SKILL.md` lines 76, 346 and 374, `references/interactive-mode.md` lines 597-599), and `$json` locks JSON on its own axis (`SKILL.md` lines 71, 83 and 99). Framework: the prompt names TIDD-EC as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's selection logic lands on TIDD-EC here: its matrix names quality-critical and compliance work (`assets/framework-pattern-library.md` lines 61-65), its selection algorithm weights TIDD-EC up for precision and again for compliance needs (lines 136-140), its decision table recommends it from complexity 6 when precision drives the task (lines 181-186) and Quick Select places it at 6 to 8 (`references/patterns-evaluation.md` line 681). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names TIDD-EC; a fusion such as `TIDD-EC + CoT` passes when TIDD-EC comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 127), and it must sit inside the High tier: the label `High`, or 7 or 8 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-json.md` lines 127 and 436), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names TIDD-EC, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by TIDD-EC's elements, Task, Instructions, Do's, Don'ts, Examples and Context (`assets/framework-pattern-library.md` lines 61-65). Every element appears as its own JSON key, at the top level or under one wrapping key, in any letter case; Do's and Don'ts pass in any spelling that keeps the word, such as `Dos`, `do_s`, `Donts` or `dont_s`; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The TIDD-EC element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].json` before replying (`AGENTS.md` lines 34 and 48) and verifies its syntax (`AGENTS.md` line 41). The payload below the header and its `---` divider parses as valid JSON with no Markdown inside (`SKILL.md` lines 409 and 497, `assets/format-guide-json.md` lines 138-149 and 428-435). The JSON format guide writes the header as `Mode: $json` (`assets/format-guide-json.md` line 127) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$json` or `$improve` both pass. The reply reports roughly five to ten percent token overhead (`SKILL.md` lines 409 and 501). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: GPT-4.1 as the target, the current one-line prompt it replaces, one listing's title, description and bullet points as input, the approved list of 38 EU-authorised health claims passed in with each call, a flag on every claim not on the list, the exact sentence, the broken rule (exactly unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts for each flag, compliant text left untouched, no judgement of whether the product works, and the user's worked example pair. Examples builds on the example the user supplied; a further example passes only when it illustrates the user's own fields and rules, and one that adds a category, a field or an output is scope expansion (`assets/framework-pattern-library.md` lines 307-323 set out cascading examples). Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming TIDD-EC at High complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept, its payload parsing as JSON
- Pass/fail: PASS if all of these hold: the delivery is a verified `.json` export saved before a path-first reply; the header names TIDD-EC and a complexity inside the High tier (7 to 8); the prompt body is visibly organised by Task, Instructions, Do's, Don'ts, Examples and Context, each labelled; CLEAR passes its gate; the payload below the header and its `---` divider parses as JSON; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: an efficacy rating, translations into other EU languages or an SEO score are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Improve the compliance prompt behind the listing checker for our supplement brand's marketplace listings. Current version: "Check if this product text is OK." GPT-4.1 receives the title, description and bullet points of one listing, plus our approved list of 38 EU-authorised health claims with each call. It flags every health claim that is not on the list, and for each flag returns the exact sentence, the rule it breaks (unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts. It must not touch text that is already compliant and must not judge whether the product works. Worked example: "Boosts your immune system" is unauthorised, while "Vitamin C contributes to the normal function of the immune system" is approved. Use TIDD-EC and keep the full scope. No questions, decide the open points yourself.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .json export, then parse the payload below the single-line header and its --- divider -> operator: check the header's framework and complexity against the High tier`
4. `operator: map every TIDD-EC element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and delivers without a question. Step 3 proves the export exists and opens with a header that names TIDD-EC at a complexity inside the High tier, with a payload that parses as JSON. Step 4 proves every TIDD-EC element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each TIDD-EC element to its label in the file, the parse result for the payload below the header and its `---` divider and the token-overhead note, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.json` export and a path-first reply, a header naming TIDD-EC at a complexity inside the High tier, every TIDD-EC element labelled, a passing CLEAR result, a payload that parses as JSON, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 76 and 346 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 217, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the TIDD-EC entry in the framework matrix, `assets/framework-pattern-library.md` lines 61-65, and the Quick Select row in `references/patterns-evaluation.md` line 681 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-json.md` lines 123-149 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-011 | TIDD-EC at High complexity for a health-claims checker | Verify `$improve` delivers a High-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled | `$improve $json Improve the compliance prompt behind the listing checker for our supplement brand's marketplace listings. Current version: "Check if this product text is OK." GPT-4.1 receives the title, description and bullet points of one listing, plus our approved list of 38 EU-authorised health claims with each call. It flags every health claim that is not on the list, and for each flag returns the exact sentence, the rule it breaks (unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts. It must not touch text that is already compliant and must not judge whether the product works. Worked example: "Boosts your immune system" is unauthorised, while "Vitamin C contributes to the normal function of the immune system" is approved. Use TIDD-EC and keep the full scope. No questions, decide the open points yourself.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Improve bound, delivery with no question. Step 3: header names TIDD-EC at the High tier, payload parses. Step 4: TIDD-EC elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist, parse result | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and TIDD-EC patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$improve` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-json.md`](../../assets/format-guide-json.md) | JSON header, syntax and delivery rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-011
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/tidd-ec-high-health-claims-checker-export.md`
