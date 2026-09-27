---
title: "SFW-023 -- VIBE at Medium complexity for a returns inspection screen"
description: "Validates that a single $vibe $markdown prompt delivers an export in one turn whose header names VIBE at Medium complexity, whose body carries VIBE's elements, labelled or as prose, and whose EVOKE gate passes with every supplied fact kept."
version: 1.2.0.0
---

# SFW-023 -- VIBE at Medium complexity for a returns inspection screen

`$vibe` binds the Visual lane and `$markdown` locks Markdown, so the runtime writes one VIBE prompt, scores it with EVOKE and saves it as a `.md` export before replying. The request names VIBE and carries every essential, so the only correct reply is a delivery whose header and body both show VIBE.

---

## 1. OVERVIEW

The user supplies the platform, the station, the inspector's moment and 20-second job, the screen contents, a reject state, the feel to avoid and the one to reach, the component library, and names VIBE. The runtime improves that into one prompt organised by VIBE, scores it with EVOKE and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

The Visual lane's library question is the usual reason a `$vibe` run stops to ask. The test is whether a pre-answered library lets the runtime deliver a VIBE brief in one turn with shadcn/ui written in.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$vibe` delivers a Medium-tier VIBE prompt in one turn with every VIBE element present, labelled or as prose
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Please write a v0 brief for our returns-inspection screen: the inspector grades each returned item A, B, C or reject in about 20 seconds on a 24-inch touchscreen, with the order photo, the return reason and big grade buttons, calm and fast, never spreadsheet-like. Use shadcn/ui and VIBE.`
- Prompt: `$vibe $markdown Screen concept for v0: the returns-inspection station in our fashion e-commerce warehouse. An inspector stands at a bench in cotton gloves, scans a returned item and has about 20 seconds to grade it A, B, C or reject on a 24-inch touchscreen. She needs the original order photo next to the item, the customer's return reason and a big tap target for each grade, and a reject asks for one damage photo. After 300 items a shift it must not feel like a spreadsheet or a dark developer tool: calm, tactile and fast. Use shadcn/ui components, so there is nothing to ask me. Shape the brief with VIBE and keep every state I described.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the component library question the Visual lane marks mandatory (`references/interactive-mode.md` lines 78-80, 165 and 219, `references/visual-mode.md` line 845), answered by naming shadcn/ui; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming VIBE; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$markdown` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$vibe` binds the Visual lane at Creative energy with VIBE and EVOKE (`SKILL.md` lines 80, 350 and 376), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names VIBE as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's decision table assigns VIBE to visual UI concepting (`assets/framework-pattern-library.md` lines 193-198) and its selection algorithm weights VIBE up for visual UI work (lines 142-146), and Visual mode runs VIBE (`SKILL.md` line 350). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names VIBE; a fusion such as `VIBE + CoT` passes when VIBE comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 127), and it must sit inside the Medium tier: the label `Medium`, or 5 or 6 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-markdown.md` lines 118 and 128), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names VIBE, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt carries VIBE's elements, Vision, Inspiration, Behavior and Experience (`assets/framework-pattern-library.md` lines 76-80, `references/visual-mode.md` lines 104-121). Visual prompts flow as natural prose (`references/visual-mode.md` line 62), so an element passes as its own heading, bold label or list label, in any letter case, or as a prose passage the operator can map to that element alone; `Behaviour` counts as Behavior; an element that is missing, or that cannot be told apart from another element's passage, fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The VIBE element sections or passages are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: EVOKE passes at 40 of 50 after the non-skippable grounding pre-check on subject, audience, single job and anti-default (`SKILL.md` lines 446-447, `references/visual-mode.md` lines 74 and 357-368); CLEAR or VISUAL on a visual UI prompt is the wrong scorer (`SKILL.md` lines 515 and 517), and a best-effort note below the gate fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header, its `---` divider and the prompt (`SKILL.md` lines 558-562). The reply leads with the saved path, reports the EVOKE result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The reply closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). The enhanced prompt carries every supplied fact: v0 as the platform, named in the header or the body, the returns-inspection station in a fashion e-commerce warehouse, an inspector standing at a bench in cotton gloves, a scan of each returned item, about 20 seconds to grade it A, B, C or reject, a 24-inch touchscreen, the original order photo next to the item, the customer's return reason, a big tap target for each grade, one damage photo on a reject, 300 items a shift, not like a spreadsheet or a dark developer tool, calm, tactile and fast, and shadcn/ui as the component library. The user chose shadcn/ui, so the brief carries the shadcn/ui library instruction (`references/visual-mode.md` lines 866-873), and an Untitled UI instruction or none alters a supplied fact. Whether the brief names the median default it steers away from (lines 370-381), the UX-floor constraints (lines 962-973) and the word count against the 100 to 300 words set for v0 (lines 767-770) are recorded and do not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing EVOKE result, whose saved `.md` file opens with a header naming VIBE at Medium complexity and reads back as a VIBE prompt with every element present, labelled or as prose, and every supplied fact kept, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names VIBE and a complexity inside the Medium tier (5 to 6); the prompt body is visibly organised by Vision, Inspiration, Behavior and Experience, each labelled or written as a prose passage the operator can map to it; EVOKE passes its gate; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or cannot be mapped, the scorer is wrong or below its gate, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a supervisor analytics page, a login screen or a refund workflow are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$vibe $markdown Screen concept for v0: the returns-inspection station in our fashion e-commerce warehouse. An inspector stands at a bench in cotton gloves, scans a returned item and has about 20 seconds to grade it A, B, C or reject on a 24-inch touchscreen. She needs the original order photo next to the item, the customer's return reason and a big tap target for each grade, and a reject asks for one damage photo. After 300 items a shift it must not feel like a spreadsheet or a dark developer tool: calm, tactile and fast. Use shadcn/ui components, so there is nothing to ask me. Shape the brief with VIBE and keep every state I described.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Medium tier`
4. `operator: map every VIBE element to its label or prose passage, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Visual and delivers without a question. Step 3 proves the export exists and opens with a header that names VIBE at a complexity inside the Medium tier. Step 4 proves every VIBE element is present, the EVOKE gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the EVOKE score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each VIBE element to its label or prose passage in the file, a fact checklist against the file, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming VIBE at a complexity inside the Medium tier, every VIBE element present, labelled or as prose, a passing EVOKE result, every supplied fact intact, no scope expansion and the share-back invitation
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing element or one that cannot be mapped, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion or a missing invitation
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 80 and 350 and the pre-answered routes in `references/interactive-mode.md` lines 78-80, 165 and 219, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the VIBE entry in the framework matrix, `assets/framework-pattern-library.md` lines 76-80, and the Quick Select row in `references/patterns-evaluation.md` line 683 when the header or the body names another framework or leaves an element out
3. Check the EVOKE gate in `SKILL.md` lines 446-448, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-128 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-023 | VIBE at Medium complexity for a returns inspection screen | Verify `$vibe` delivers a Medium-tier VIBE prompt in one turn with every VIBE element present, labelled or as prose | `$vibe $markdown Screen concept for v0: the returns-inspection station in our fashion e-commerce warehouse. An inspector stands at a bench in cotton gloves, scans a returned item and has about 20 seconds to grade it A, B, C or reject on a 24-inch touchscreen. She needs the original order photo next to the item, the customer's return reason and a big tap target for each grade, and a reject asks for one damage photo. After 300 items a shift it must not feel like a spreadsheet or a dark developer tool: calm, tactile and fast. Use shadcn/ui components, so there is nothing to ask me. Shape the brief with VIBE and keep every state I described.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Visual bound, delivery with no question. Step 3: header names VIBE at the Medium tier. Step 4: VIBE elements present, EVOKE passed, facts kept, no expansion | Transcript, EVOKE line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an element that cannot be mapped, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and VIBE patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the EVOKE rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$vibe` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`visual-mode.md`](../../references/visual-mode.md) | Grounding, VIBE, EVOKE, MagicPath calibration and the library question |
| [`visual-mode-library.md`](../../assets/visual-mode-library.md) | Visual UI vocabulary and platform templates |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-023
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/vibe-medium-returns-inspection-screen-export.md`
