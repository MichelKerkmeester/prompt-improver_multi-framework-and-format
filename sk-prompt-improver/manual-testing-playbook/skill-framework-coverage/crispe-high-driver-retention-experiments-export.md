---
title: "SFW-014 -- CRISPE at High complexity for driver retention experiments"
description: "Validates that a single $improve $yaml prompt delivers an export in one turn whose header names CRISPE at High complexity, whose body is organised by CRISPE's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-014 -- CRISPE at High complexity for driver retention experiments

`$improve` binds the Improve lane and `$yaml` locks YAML, so the runtime writes one CRISPE prompt, scores it with CLEAR and saves it as a `.yaml` export before replying. The request names CRISPE and carries every essential, so the only correct reply is a delivery whose header and body both show CRISPE.

---

## 1. OVERVIEW

The user supplies a one-line retention prompt, the fleet, turnover and exit-interview facts, a strategist persona, four experiments with five fields each, a budget and an assumption to challenge, and names CRISPE. The runtime improves that into one prompt organised by CRISPE, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Retention strategy with a budget and a challenged assumption is CRISPE at full stretch. The test is whether the four experiments keep all five fields and the pay assumption stays challenged in a YAML payload that parses.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$improve` delivers a High-tier CRISPE prompt in one turn with every CRISPE element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Please improve my driver-retention prompt: 210 drivers, 38% gone in a year, mostly in the first 90 days. I want four retention experiments within EUR 120,000 a year, each with a hypothesis, pilot depot, metric, 10-week read-out and schedule risk, and I want pay challenged as the lever. CRISPE, in YAML.`
- Prompt: `$improve $yaml Improve this: "How do we keep our drivers?" We run 210 parcel-delivery drivers from four depots around Antwerp, and 38% left in the last 12 months, mostly within their first 90 days. Exit interviews point at route density, the 06:00 start and pay per stop. I want ChatGPT to act as a workforce strategist with last-mile experience, reason about why early-tenure drivers leave, then propose four distinct retention experiments that fit a EUR 120,000 yearly budget. Each experiment needs the hypothesis, the depot to pilot it in, the metric, a 10-week read-out point and the main risk to the delivery schedule. It should challenge our assumption that pay is the main lever. Build it with CRISPE and keep the full scope. No questions, fill in the gaps yourself.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the format question `$improve` routes to (`references/interactive-mode.md` line 217), answered by the `$yaml` token; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming CRISPE. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$improve` binds the Improve lane at Standard energy with CLEAR and automatic framework selection (`SKILL.md` lines 76, 346 and 374, `references/interactive-mode.md` lines 597-599), and `$yaml` locks YAML on its own axis (`SKILL.md` lines 71, 84 and 99). Framework: the prompt names CRISPE as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's selection logic lands on CRISPE here: its matrix names strategy and exploration (`assets/framework-pattern-library.md` lines 66-70) and Quick Select places CRISPE at 5 to 7 (`references/patterns-evaluation.md` line 680), which reaches complexity 7. At 8 the runtime may note that CRAFT's 7 to 10 band (line 682) overlaps; that note is recorded and does not decide the verdict, and a delivery built on another framework fails. Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names CRISPE; a fusion such as `CRISPE + CoT` passes when CRISPE comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 127), and it must sit inside the High tier: the label `High`, or 7 or 8 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-yaml.md` lines 128 and 466), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names CRISPE, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by CRISPE's elements, Capacity, Insight, Statement, Personality and Experiment (`assets/framework-pattern-library.md` lines 66-70). Every element appears as its own YAML key, at the top level or under one wrapping key, in any letter case; Capacity may read `Capacity and Role`; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The CRISPE element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].yaml` before replying (`AGENTS.md` lines 34 and 49) and verifies its syntax (`AGENTS.md` line 41). The payload below the header and its `---` divider parses as valid YAML with no Markdown inside (`SKILL.md` lines 410 and 497, `assets/format-guide-yaml.md` lines 141-149 and 460-468). The YAML format guide writes the header as `Mode: $yaml` (`assets/format-guide-yaml.md` line 128) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$yaml` or `$improve` both pass. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header and is not Markdown: the literal `Mode: $yaml | ...` line does not parse as YAML, so the comment form lets the whole file parse. Either form passes, and the form used is recorded. The reply reports roughly three to seven percent token overhead (`SKILL.md` lines 410 and 501). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: ChatGPT as the target, the current one-line prompt it replaces, 210 parcel-delivery drivers from four depots around Antwerp, 38% leaving in the last 12 months, mostly within 90 days, the exit-interview causes route density, the 06:00 start and pay per stop, a workforce strategist persona with last-mile experience, reasoning about early-tenure leavers, exactly four distinct retention experiments within a EUR 120,000 yearly budget, the hypothesis, pilot depot, metric, 10-week read-out point and main schedule risk for each, and a challenge to the assumption that pay is the main lever. Experiment asks for exactly four experiments with their five fields, and the challenge to the pay assumption survives. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.yaml` file opens with a header naming CRISPE at High complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, its payload parsing as YAML
- Pass/fail: PASS if all of these hold: the delivery is a verified `.yaml` export saved before a path-first reply; the header names CRISPE and a complexity inside the High tier (7 to 8); the prompt body is visibly organised by Capacity, Insight, Statement, Personality and Experiment, each labelled; CLEAR passes its gate; the payload below the header and its `---` divider parses as YAML; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a recruitment campaign, a revised pay scale or a fifth experiment are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $yaml Improve this: "How do we keep our drivers?" We run 210 parcel-delivery drivers from four depots around Antwerp, and 38% left in the last 12 months, mostly within their first 90 days. Exit interviews point at route density, the 06:00 start and pay per stop. I want ChatGPT to act as a workforce strategist with last-mile experience, reason about why early-tenure drivers leave, then propose four distinct retention experiments that fit a EUR 120,000 yearly budget. Each experiment needs the hypothesis, the depot to pilot it in, the metric, a 10-week read-out point and the main risk to the delivery schedule. It should challenge our assumption that pay is the main lever. Build it with CRISPE and keep the full scope. No questions, fill in the gaps yourself.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .yaml export, then parse the payload below the single-line header and its --- divider -> operator: check the header's framework and complexity against the High tier`
4. `operator: map every CRISPE element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and delivers without a question. Step 3 proves the export exists and opens with a header that names CRISPE at a complexity inside the High tier, with a payload that parses as YAML. Step 4 proves every CRISPE element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each CRISPE element to its label in the file, the parse result for the payload below the header and its `---` divider and the token-overhead note, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.yaml` export and a path-first reply, a header naming CRISPE at a complexity inside the High tier, every CRISPE element labelled, a passing CLEAR result, a payload that parses as YAML, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 76 and 346 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 217, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the CRISPE entry in the framework matrix, `assets/framework-pattern-library.md` lines 66-70, and the Quick Select row in `references/patterns-evaluation.md` line 680 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-yaml.md` lines 124-149 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-014 | CRISPE at High complexity for driver retention experiments | Verify `$improve` delivers a High-tier CRISPE prompt in one turn with every CRISPE element labelled | `$improve $yaml Improve this: "How do we keep our drivers?" We run 210 parcel-delivery drivers from four depots around Antwerp, and 38% left in the last 12 months, mostly within their first 90 days. Exit interviews point at route density, the 06:00 start and pay per stop. I want ChatGPT to act as a workforce strategist with last-mile experience, reason about why early-tenure drivers leave, then propose four distinct retention experiments that fit a EUR 120,000 yearly budget. Each experiment needs the hypothesis, the depot to pilot it in, the metric, a 10-week read-out point and the main risk to the delivery schedule. It should challenge our assumption that pay is the main lever. Build it with CRISPE and keep the full scope. No questions, fill in the gaps yourself.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Improve bound, delivery with no question. Step 3: header names CRISPE at the High tier, payload parses. Step 4: CRISPE elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist, parse result | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

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
| [`format-guide-yaml.md`](../../assets/format-guide-yaml.md) | YAML header, syntax and delivery rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-014
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/crispe-high-driver-retention-experiments-export.md`
