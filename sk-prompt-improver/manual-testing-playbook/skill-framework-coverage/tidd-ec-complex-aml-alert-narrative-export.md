---
title: "SFW-012 -- TIDD-EC at Complex complexity for an AML alert narrative"
description: "Validates that a single $deep $markdown prompt delivers an export in one turn whose header names TIDD-EC at Complex complexity, whose body is organised by TIDD-EC's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.1.0.0
---

# SFW-012 -- TIDD-EC at Complex complexity for an AML alert narrative

`$deep` binds the Deep lane and `$markdown` locks Markdown, so the runtime writes one TIDD-EC prompt, scores it with CLEAR and saves it as a `.md` export before replying. The request names TIDD-EC and carries every essential, so the only correct reply is a delivery whose header and body both show TIDD-EC.

---

## 1. OVERVIEW

The user supplies a one-line narrative prompt, four inputs, a fixed section order, citation, prohibition, currency and structuring rules, three edge cases and an example sentence, and names TIDD-EC. The runtime improves that into one prompt organised by TIDD-EC, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

An AML narrative prompt carries hard prohibitions, a numeric trigger and named edge cases, all of which TIDD-EC can hold. The test is whether every rule lands in an element and nothing that decides for the analyst is added.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a Complex-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Our AML alert-narrative prompt needs rebuilding: a fixed section order, a transaction ID for every claim, no conclusions or filing advice, original currency plus EUR, a structuring flag and handling for joint, incomplete and closed accounts. I have one sentence the auditors liked. Use TIDD-EC.`
- Prompt: `$deep $markdown Rebuild our AML alert-narrative prompt for Mistral Large; today it is just "Explain why this alert fired." The model gets one transaction-monitoring alert: the rule that fired, 90 days of transactions, the KYC profile and prior alerts. It writes the analyst's case narrative in our fixed order: trigger, customer profile, observed pattern, expected activity, open questions. Every claim cites a transaction ID. It never concludes that the customer is laundering money and never recommends filing or closing, which stays the analyst's call. Amounts keep their original currency with the EUR equivalent in brackets. It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days, and it handles joint accounts, missing KYC fields and accounts closed mid-window. Auditors liked this sentence: "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month." Use TIDD-EC, keep the full scope and don't ask me anything.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the Question step the Deep flow draws (`references/interactive-mode.md` line 656), answered by the complete request, while line 215 routes `$deep` straight to processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming TIDD-EC; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$markdown` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$deep` binds the Deep lane with Deep energy, all five perspectives and complexity-matched framework selection (`SKILL.md` lines 79, 349 and 375, `references/depth-framework.md` lines 59-63), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names TIDD-EC as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's selection logic lands on TIDD-EC here: its matrix names compliance-critical work (`assets/framework-pattern-library.md` lines 61-65), its selection algorithm weights TIDD-EC up for precision and compliance (lines 136-140) and its decision table recommends it from complexity 6 upward when precision drives the task (lines 181-186). Quick Select stops TIDD-EC at 8 (`references/patterns-evaluation.md` line 681), so a fit note naming CRAFT is recorded and does not decide the verdict, and a delivery built on another framework fails. Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names TIDD-EC; a fusion such as `TIDD-EC + CoT` passes when TIDD-EC comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Complex tier: the label `Complex`, or 9 or 10 as a bare number or written n/10, or another label above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-markdown.md` lines 118 and 124), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names TIDD-EC, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by TIDD-EC's elements, Task, Instructions, Do's, Don'ts, Examples and Context (`assets/framework-pattern-library.md` lines 61-65). Every element appears as its own heading, bold label or list label, in any letter case; Do's and Don'ts pass in any spelling that keeps the word, such as `Dos`, `do_s`, `Donts` or `dont_s`; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The TIDD-EC element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header and the prompt (`SKILL.md` lines 558-562). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: Mistral Large as the target, the current one-line prompt it replaces, one alert with the rule that fired, 90 days of transactions, the KYC profile and prior alerts, the fixed order trigger, customer profile, observed pattern, expected activity and open questions, a transaction ID for every claim, no conclusion that the customer is laundering money, no recommendation to file or close, original currency with the EUR equivalent in brackets, a structuring flag at three or more cash deposits between EUR 9,000 and 9,999 within 10 days, handling for joint accounts, missing KYC fields and accounts closed mid-window, and the auditors' example sentence. Examples builds on the example the user supplied; a further example passes only when it illustrates the user's own fields and rules, and one that adds a category, a field or an output is scope expansion (`assets/framework-pattern-library.md` lines 307-323 set out cascading examples). The three named edge cases must each appear, and the narrative sections stay in the user's order. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming TIDD-EC at Complex complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names TIDD-EC and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Task, Instructions, Do's, Don'ts, Examples and Context, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a risk score, a recommendation to file or an edge case the user did not name are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep $markdown Rebuild our AML alert-narrative prompt for Mistral Large; today it is just "Explain why this alert fired." The model gets one transaction-monitoring alert: the rule that fired, 90 days of transactions, the KYC profile and prior alerts. It writes the analyst's case narrative in our fixed order: trigger, customer profile, observed pattern, expected activity, open questions. Every claim cites a transaction ID. It never concludes that the customer is laundering money and never recommends filing or closing, which stays the analyst's call. Amounts keep their original currency with the EUR equivalent in brackets. It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days, and it handles joint accounts, missing KYC fields and accounts closed mid-window. Auditors liked this sentence: "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month." Use TIDD-EC, keep the full scope and don't ask me anything.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every TIDD-EC element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Deep and delivers without a question. Step 3 proves the export exists and opens with a header that names TIDD-EC at a complexity inside the Complex tier. Step 4 proves every TIDD-EC element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each TIDD-EC element to its label in the file, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming TIDD-EC at a complexity inside the Complex tier, every TIDD-EC element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 79 and 349 and the pre-answered routes in `references/interactive-mode.md` lines 200, 215 and 656, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the TIDD-EC entry in the framework matrix, `assets/framework-pattern-library.md` lines 61-65, and the Quick Select row in `references/patterns-evaluation.md` line 681 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-124 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-012 | TIDD-EC at Complex complexity for an AML alert narrative | Verify `$deep` delivers a Complex-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled | `$deep $markdown Rebuild our AML alert-narrative prompt for Mistral Large; today it is just "Explain why this alert fired." The model gets one transaction-monitoring alert: the rule that fired, 90 days of transactions, the KYC profile and prior alerts. It writes the analyst's case narrative in our fixed order: trigger, customer profile, observed pattern, expected activity, open questions. Every claim cites a transaction ID. It never concludes that the customer is laundering money and never recommends filing or closing, which stays the analyst's call. Amounts keep their original currency with the EUR equivalent in brackets. It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days, and it handles joint accounts, missing KYC fields and accounts closed mid-window. Auditors liked this sentence: "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month." Use TIDD-EC, keep the full scope and don't ask me anything.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Deep bound, delivery with no question. Step 3: header names TIDD-EC at the Complex tier. Step 4: TIDD-EC elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and TIDD-EC patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$deep` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-012
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/tidd-ec-complex-aml-alert-narrative-export.md`
