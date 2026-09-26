---
title: "SFW-013 -- CRISPE at Medium complexity for oat milk positioning"
description: "Validates that a single $improve $markdown prompt delivers an export in one turn whose header names CRISPE at Medium complexity, whose body is organised by CRISPE's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-013 -- CRISPE at Medium complexity for oat milk positioning

`$improve` binds the Improve lane and `$markdown` locks Markdown, so the runtime writes one CRISPE prompt, scores it with CLEAR and saves it as a `.md` export before replying. The request names CRISPE and carries every essential, so the only correct reply is a delivery whose header and body both show CRISPE.

---

## 1. OVERVIEW

The user supplies a one-line marketing prompt, the company, market and price position, a strategist persona, three barista concerns and three positioning routes with their fields, and names CRISPE. The runtime improves that into one prompt organised by CRISPE, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

CRISPE's Experiment element is its signature, and it only works when the prompt asks for the options the user wanted. The test is whether exactly three positioning routes with their tests come out of a visibly CRISPE prompt.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` delivers a Medium-tier CRISPE prompt in one turn with every CRISPE element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Can you make my oat-milk marketing prompt stronger? I want Claude to think like a B2B strategist about Belgian independent cafés and give three different positioning routes with a pitch, the café type and a cheap one-month test. Please use CRISPE.`
- Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the format question `$improve` routes to (`references/interactive-mode.md` line 217), answered by the `$markdown` token; the framework choice complexity 5 to 6 raises (`references/interactive-mode.md` lines 69-71 and 128-139), answered by naming CRISPE. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`SKILL.md` lines 76, 346 and 374, `references/interactive-mode.md` lines 597-599), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names CRISPE as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's selection logic lands on CRISPE here: its matrix names strategy and exploration (`assets/framework-pattern-library.md` lines 66-70) and Quick Select places CRISPE at 5 to 7 for creative and exploratory work (`references/patterns-evaluation.md` line 680). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names CRISPE; a fusion such as `CRISPE + CoT` passes when CRISPE comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-markdown.md` lines 118 and 124), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names CRISPE, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by CRISPE's elements, Capacity, Insight, Statement, Personality and Experiment (`assets/framework-pattern-library.md` lines 66-70). Every element appears as its own heading, bold label or list label, in any letter case; Capacity may read `Capacity and Role`; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CRISPE element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header and the prompt (`SKILL.md` lines 558-561). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: Claude as a sparring partner, the current one-line prompt it replaces, a small Ghent start-up, an oat barista milk for independent cafés in Belgium priced 15% above the market leader, a B2B food-and-beverage strategist persona, the three barista concerns foam stability, taste with espresso and price per cup, exactly three clearly different positioning routes, a one-line pitch, the café type it wins and a cheap one-month test for each, and a frank, practical style with no buzzwords. Experiment asks for exactly the three positioning routes with their three fields, and a fourth route is scope expansion. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRISPE at Medium complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names CRISPE and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Capacity, Insight, Statement, Personality and Experiment, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a full marketing plan, a price change or a consumer retail route are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every CRISPE element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and delivers without a question. Step 3 proves the export exists and opens with a header that names CRISPE at a complexity inside the Medium tier. Step 4 proves every CRISPE element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each CRISPE element to its label in the file, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming CRISPE at a complexity inside the Medium tier, every CRISPE element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 76 and 346 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 217, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the CRISPE entry in the framework matrix, `assets/framework-pattern-library.md` lines 66-70, and the Quick Select row in `references/patterns-evaluation.md` line 680 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-124 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-013 | CRISPE at Medium complexity for oat milk positioning | Verify `$improve` delivers a Medium-tier CRISPE prompt in one turn with every CRISPE element labelled | `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Improve bound, delivery with no question. Step 3: header names CRISPE at the Medium tier. Step 4: CRISPE elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and CRISPE patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$improve` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-013
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/crispe-medium-oat-milk-positioning-export.md`
