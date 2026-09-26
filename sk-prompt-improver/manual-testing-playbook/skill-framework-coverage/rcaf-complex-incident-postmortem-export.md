---
title: "SFW-003 -- RCAF at Complex complexity for an incident postmortem"
description: "Validates that a single $deep $markdown prompt delivers an export in one turn whose header names RCAF at Complex complexity, whose body is organised by RCAF's elements and whose CLEAR gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-003 -- RCAF at Complex complexity for an incident postmortem

`$deep` binds the Deep lane and `$markdown` locks Markdown, so the runtime writes one RCAF prompt, scores it with CLEAR and saves it as a `.md` export before replying. The request names RCAF and carries every essential, so the only correct reply is a delivery whose header and body both show RCAF.

---

## 1. OVERVIEW

The user supplies a one-line postmortem prompt, three inputs, three audience layers, a timestamp rule, an evidence rule, action-item rules and a redaction rule, and names RCAF with a catalogue reason. The runtime improves that into one prompt organised by RCAF, scores it with CLEAR and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A Complex prompt in the simplest framework is the hardest case for framework discipline. The test is whether Layered RCAF carries three audiences, a timestamp rule and an evidence rule without dropping a fact or switching frameworks.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a Complex-tier RCAF prompt in one turn with every RCAF element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Our postmortem prompt is one line. I need it to turn a PagerDuty timeline, a Slack export and a deploy log into a blameless draft with layers for engineers, support leads and execs, UTC timestamps with gaps flagged, evidence-only root causes, owned action items and customer names replaced. Our catalogue needs RCAF.`
- Prompt: `$deep $markdown I want a serious upgrade of our postmortem prompt, currently just "Write a postmortem from these notes." We give Claude a PagerDuty timeline, a Slack incident-channel export and the deploy log for one SEV1 or SEV2 incident. It must produce one blameless draft in three layers: a technical timeline for engineers, an impact summary for support leads and a five-sentence brief for the exec team. Timestamps arrive in both UTC and Amsterdam time, so it normalises everything to UTC and flags any gap over 10 minutes. It may only state a root cause the logs support and labels everything else as a hypothesis. Action items need an owner from the responders list and a due week. Customer names become account IDs. Our SRE prompt catalogue lints for the four RCAF sections, so use RCAF, layered per audience, not another framework. Keep everything, no streamlining, and skip the questions.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the Question step the Deep flow draws (`references/interactive-mode.md` line 656), answered by the complete request, while line 215 routes `$deep` straight to processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming RCAF; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$markdown` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$deep` binds the Deep lane with Deep energy, all five perspectives and complexity-matched framework selection (`SKILL.md` lines 79, 349 and 375, `references/depth-framework.md` lines 59-63), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names RCAF as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library ranks RCAF below this tier: its matrix says to avoid RCAF for over-complex scenarios (`assets/framework-pattern-library.md` lines 41-45), its decision table stops RCAF at complexity 6 (lines 169-174) and Quick Select places it at 1 to 4 (`references/patterns-evaluation.md` line 677). The input makes a credible case anyway: the library's Layered RCAF pattern exists for complex multi-audience prompts (`assets/framework-pattern-library.md` lines 280-282), this prompt serves three audiences, and the user's catalogue lints for the four RCAF sections. The runtime may flag the fit or name an alternative such as CRAFT in chat; that note is recorded and does not decide the verdict, and a delivery built on another framework fails. Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names RCAF; a fusion such as `RCAF + CoT` passes when RCAF comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Complex tier: 9 or 10 as a bare number or written n/10, or a label that names a level above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. Body: the prompt is visibly organised by RCAF's elements, Role, Context, Action and Format (`assets/framework-pattern-library.md` lines 41-45). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The RCAF element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` lines 459-469). The reply reports a passing CLEAR result with gate status; EVOKE or VISUAL on a text prompt is the wrong scorer (`SKILL.md` lines 516-517), and a best-effort note below the gate after three repair cycles (`SKILL.md` lines 452-454) fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header and the prompt (`SKILL.md` lines 558-561). The reply leads with the saved path, reports the CLEAR result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: Claude as the target, the current one-line prompt it replaces, the three inputs PagerDuty timeline, Slack incident-channel export and deploy log, one SEV1 or SEV2 incident, one blameless draft, the three layers (a technical timeline for engineers, an impact summary for support leads, a five-sentence brief for the exec team), timestamps in UTC and Amsterdam time normalised to UTC, a flag on any gap over 10 minutes, a root cause only where the logs support it and a hypothesis label otherwise, action items with an owner from the responders list and a due week, and customer names replaced by account IDs. The three audience layers may appear as sub-layers inside Role, Context, Action or Format, which the library's Layered RCAF pattern allows (`assets/framework-pattern-library.md` lines 257-282); a top-level section per audience that replaces the RCAF elements fails the body check. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming RCAF at Complex complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names RCAF and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Role, Context, Action and Format, each labelled; CLEAR passes its gate; every supplied fact is kept; and the scope test holds. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a customer-facing status page update, a severity re-rating or a fourth audience layer are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep $markdown I want a serious upgrade of our postmortem prompt, currently just "Write a postmortem from these notes." We give Claude a PagerDuty timeline, a Slack incident-channel export and the deploy log for one SEV1 or SEV2 incident. It must produce one blameless draft in three layers: a technical timeline for engineers, an impact summary for support leads and a five-sentence brief for the exec team. Timestamps arrive in both UTC and Amsterdam time, so it normalises everything to UTC and flags any gap over 10 minutes. It may only state a root cause the logs support and labels everything else as a hypothesis. Action items need an owner from the responders list and a due week. Customer names become account IDs. Our SRE prompt catalogue lints for the four RCAF sections, so use RCAF, layered per audience, not another framework. Keep everything, no streamlining, and skip the questions.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every RCAF element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Deep and delivers without a question. Step 3 proves the export exists and opens with a header that names RCAF at a complexity inside the Complex tier. Step 4 proves every RCAF element is labelled, the CLEAR gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the CLEAR score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each RCAF element to its label in the file, a fact checklist against the file, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming RCAF at a complexity inside the Complex tier, every RCAF element labelled, a passing CLEAR result, every supplied fact intact, no scope expansion
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 79 and 349 and the pre-answered routes in `references/interactive-mode.md` lines 200, 215 and 656, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the RCAF entry in the framework matrix, `assets/framework-pattern-library.md` lines 41-45, and the Quick Select row in `references/patterns-evaluation.md` line 677 when the header or the body names another framework or leaves an element out
3. Check the CLEAR gate in `SKILL.md` lines 444-445, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-124 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-003 | RCAF at Complex complexity for an incident postmortem | Verify `$deep` delivers a Complex-tier RCAF prompt in one turn with every RCAF element labelled | `$deep $markdown I want a serious upgrade of our postmortem prompt, currently just "Write a postmortem from these notes." We give Claude a PagerDuty timeline, a Slack incident-channel export and the deploy log for one SEV1 or SEV2 incident. It must produce one blameless draft in three layers: a technical timeline for engineers, an impact summary for support leads and a five-sentence brief for the exec team. Timestamps arrive in both UTC and Amsterdam time, so it normalises everything to UTC and flags any gap over 10 minutes. It may only state a root cause the logs support and labels everything else as a hypothesis. Action items need an owner from the responders list and a due week. Customer names become account IDs. Our SRE prompt catalogue lints for the four RCAF sections, so use RCAF, layered per audience, not another framework. Keep everything, no streamlining, and skip the questions.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Deep bound, delivery with no question. Step 3: header names RCAF at the Complex tier. Step 4: RCAF elements labelled, CLEAR passed, facts kept, no expansion | Transcript, CLEAR line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and RCAF patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the CLEAR rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$deep` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/rcaf-complex-incident-postmortem-export.md`
