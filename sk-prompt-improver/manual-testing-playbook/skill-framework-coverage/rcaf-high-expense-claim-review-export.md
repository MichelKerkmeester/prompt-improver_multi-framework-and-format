---
title: "SFW-002 -- RCAF at High complexity for an expense claim review"
description: "Validates that a single $improve $json prompt delivers an export in one turn whose header names RCAF at High complexity, whose body is organised by RCAF's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-002 -- RCAF at High complexity for an expense claim review

`$improve` binds the Improve lane and `$json` locks JSON, so the runtime writes one RCAF prompt, scores it with CLEAR and saves it as a `.json` export before replying. The request names RCAF and carries every essential, so the only correct reply is a delivery whose header and body both show RCAF.

---

## 1. OVERVIEW

The user supplies a one-line expense-check prompt, three inputs, four classes with their actions, an override, hotel limits and two prohibitions, and names RCAF with a registry reason. The runtime improves that into one prompt organised by RCAF, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

RCAF above its usual band has to stretch through conditional logic rather than switch frameworks, because the user's registry stores only four keys. The test is whether the runtime keeps RCAF, fits four classes and an override into it and keeps the JSON parseable.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` delivers a High-tier RCAF prompt in one turn with every RCAF element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Please strengthen the expense-check prompt our tool sends to Claude. It should sort each claim line into four classes, act on each, send anything over EUR 750 to the controller, apply our hotel limits, only recommend and always quote the receipt line. Our registry only takes RCAF, so keep it RCAF.`
- Prompt: `$improve $json Our finance team calls this prompt through the Claude API from our expense tool: "Check this expense claim and say if it is fine." Make it much stronger. The model gets the claim lines, the receipts as text and the employee's grade. It sorts each line into within policy, missing receipt, over limit or not a business cost. Within policy gets a recommended approval, a missing receipt gets a receipt request, over limit goes to the finance controller, and a non-business cost goes back to the employee with the policy clause. Any line above EUR 750 goes to the controller whatever its class. Hotel limits are EUR 180 a night for grades 1 to 5 and EUR 240 above. It only recommends, never marks anything as paid, and always quotes the receipt line it relies on. Our prompt registry stores only the four RCAF keys, so keep it RCAF even for a prompt this size, and keep every rule rather than streamlining. No questions, use your judgment on the rest.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the format question `$improve` routes to (`references/interactive-mode.md` line 217), answered by the `$json` token; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming RCAF. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`SKILL.md` lines 76, 346 and 374, `references/interactive-mode.md` lines 597-599), and `$json` locks JSON on its own axis (`SKILL.md` lines 71, 83 and 99). Framework: the prompt names RCAF as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library ranks RCAF below this tier: its matrix says to avoid RCAF for over-complex scenarios (`assets/framework-pattern-library.md` lines 41-45), its decision table stops RCAF at complexity 6 (lines 169-174) and Quick Select places it at 1 to 4 (`references/patterns-evaluation.md` line 677). The input makes a credible case anyway: the library's own Conditional RCAF pattern covers context-dependent if-then responses (`assets/framework-pattern-library.md` lines 286-288), and the user's prompt registry stores only the four RCAF keys. The runtime may flag the fit or name an alternative such as TIDD-EC in chat; that note is recorded and does not decide the verdict, and a delivery built on another framework fails. Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names RCAF; a fusion such as `RCAF + CoT` passes when RCAF comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the High tier: the label `High`, or 7 or 8 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. Body: the prompt is visibly organised by RCAF's elements, Role, Context, Action and Format (`assets/framework-pattern-library.md` lines 41-45). Every element appears as its own JSON key, at the top level or under one wrapping key, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The RCAF element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].json` before replying (`AGENTS.md` lines 34 and 48) and verifies its syntax (`AGENTS.md` line 41). The payload below the header parses as valid JSON with no Markdown inside (`SKILL.md` lines 409 and 497, `assets/format-guide-json.md` lines 132-143 and 418-425). The JSON format guide writes the header as `Mode: $json` (`assets/format-guide-json.md` line 127) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$json` or `$improve` both pass. The reply reports roughly five to ten percent token overhead (`SKILL.md` lines 409 and 501). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: the Claude API called from the expense tool, the current one-line prompt it replaces, the three inputs claim lines, receipts as text and the employee's grade, exactly the four classes within policy, missing receipt, over limit and not a business cost, the four class actions (a recommended approval, a receipt request, the finance controller, and a return to the employee with the policy clause), any line above EUR 750 to the controller whatever its class, hotel limits of EUR 180 a night for grades 1 to 5 and EUR 240 above, recommendations only with nothing marked as paid, and a quoted receipt line for every decision. The four classes and their actions may sit inside Action as if-then rules, and the EUR 750 override must hold for every class. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming RCAF at High complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, its payload parsing as JSON
- Pass/fail: PASS if all of these hold: the delivery is a verified `.json` export saved before a path-first reply; the header names RCAF and a complexity inside the High tier (7 to 8); the prompt body is visibly organised by Role, Context, Action and Format, each labelled; CLEAR passes its gate; the payload below the header parses as JSON; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a fraud score, a per-diem rule or an email to the employee's manager are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Our finance team calls this prompt through the Claude API from our expense tool: "Check this expense claim and say if it is fine." Make it much stronger. The model gets the claim lines, the receipts as text and the employee's grade. It sorts each line into within policy, missing receipt, over limit or not a business cost. Within policy gets a recommended approval, a missing receipt gets a receipt request, over limit goes to the finance controller, and a non-business cost goes back to the employee with the policy clause. Any line above EUR 750 goes to the controller whatever its class. Hotel limits are EUR 180 a night for grades 1 to 5 and EUR 240 above. It only recommends, never marks anything as paid, and always quotes the receipt line it relies on. Our prompt registry stores only the four RCAF keys, so keep it RCAF even for a prompt this size, and keep every rule rather than streamlining. No questions, use your judgment on the rest.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .json export, then parse the payload below the single-line header -> operator: check the header's framework and complexity against the High tier`
4. `operator: map every RCAF element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and delivers without a question. Step 3 proves the export exists and opens with a header that names RCAF at a complexity inside the High tier, with a payload that parses as JSON. Step 4 proves every RCAF element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each RCAF element to its label in the file, the parse result for the payload below the header and the token-overhead note, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.json` export and a path-first reply, a header naming RCAF at a complexity inside the High tier, every RCAF element labelled, a passing CLEAR result, a payload that parses as JSON, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 76 and 346 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 217, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the RCAF entry in the framework matrix, `assets/framework-pattern-library.md` lines 41-45, and the Quick Select row in `references/patterns-evaluation.md` line 677 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-json.md` lines 123-143 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-002 | RCAF at High complexity for an expense claim review | Verify `$improve` delivers a High-tier RCAF prompt in one turn with every RCAF element labelled | `$improve $json Our finance team calls this prompt through the Claude API from our expense tool: "Check this expense claim and say if it is fine." Make it much stronger. The model gets the claim lines, the receipts as text and the employee's grade. It sorts each line into within policy, missing receipt, over limit or not a business cost. Within policy gets a recommended approval, a missing receipt gets a receipt request, over limit goes to the finance controller, and a non-business cost goes back to the employee with the policy clause. Any line above EUR 750 goes to the controller whatever its class. Hotel limits are EUR 180 a night for grades 1 to 5 and EUR 240 above. It only recommends, never marks anything as paid, and always quotes the receipt line it relies on. Our prompt registry stores only the four RCAF keys, so keep it RCAF even for a prompt this size, and keep every rule rather than streamlining. No questions, use your judgment on the rest.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Improve bound, delivery with no question. Step 3: header names RCAF at the High tier, payload parses. Step 4: RCAF elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist, parse result | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and RCAF patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$improve` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-json.md`](../../assets/format-guide-json.md) | JSON header, syntax and delivery rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/rcaf-high-expense-claim-review-export.md`
