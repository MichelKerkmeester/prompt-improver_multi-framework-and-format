---
title: "SFW-020 -- FRAME at Complex complexity for a library science poster"
description: "Validates that a single $image $markdown prompt delivers an export in one turn whose header names FRAME at Complex complexity, whose body is organised by FRAME's elements and whose VISUAL gate passes with every supplied fact kept."
version: 1.0.0.0
---

# SFW-020 -- FRAME at Complex complexity for a library science poster

`$image` binds the Image lane and `$markdown` locks Markdown, so the runtime writes one FRAME prompt, scores it with VISUAL and saves it as a `.md` export before replying. The request names FRAME and carries every essential, so the only correct reply is a delivery whose header and body both show FRAME.

---

## 1. OVERVIEW

The user supplies the platform and its negative field, the event, format, style and exact palette, three depth layers, a no-lettering rule, texture, age and style limits and parameter requests, and names FRAME. The runtime improves that into one prompt organised by FRAME, scores it with VISUAL and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

A layered poster with a fixed palette and a separate negative prompt uses every FRAME element at once. The test is whether the runtime keeps the palette exact, the layers in order and the exclusions in the negative field.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$image` delivers a Complex-tier FRAME prompt in one turn with every FRAME element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `We need a Stable Diffusion XL prompt for the library's Night of Science poster: a flat 1960s screen print in four set colours, children with a telescope, the library facade and Orion in three layers, empty sky at the top for the title, paper grain, a separate negative prompt and suggested settings. Use FRAME.`
- Prompt: `$image $markdown We make event posters with Stable Diffusion XL in ComfyUI, which has a separate negative prompt field. I need a prompt for this year's Night of Science at the Leiden city library: a 2:3 portrait poster in a flat 1960s screen-print style, limited to four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper). Three depth layers: two children at a brass telescope in the foreground, the library's brick facade with lit windows in the middle, and Orion rising over the rooftops behind. The top quarter stays empty sky for the title we add later, so no lettering anywhere. Visible paper grain and slight ink misregistration. The children look about 8 to 10 and are not photoreal. Use weights where they help, give me the negative prompt separately and suggest CFG and steps. Build it with FRAME, keep all of it, no questions.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the route itself raises none, since `references/interactive-mode.md` lines 220 and 658 route `$image` straight to FRAME processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming FRAME; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$markdown` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$image` binds the Image lane at Creative energy with FRAME and VISUAL (`SKILL.md` lines 81, 352 and 376), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names FRAME as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's decision table assigns FRAME to image generation (`assets/framework-pattern-library.md` lines 205-210), and Image mode runs FRAME (`SKILL.md` line 352). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names FRAME; a fusion such as `FRAME + CoT` passes when FRAME comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Complex tier: 9 or 10 as a bare number or written n/10, or a label that names a level above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-markdown.md` lines 118 and 124), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names FRAME, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by FRAME's elements, Focus, Rendering, Atmosphere, Modifiers and Exclusions (`assets/framework-pattern-library.md` lines 86-90 and 325-341, `references/image-mode.md` lines 61-82). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The FRAME element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: VISUAL passes at 48 of 60 for an image prompt (`SKILL.md` line 450, `references/image-mode.md` lines 128-157); CLEAR or EVOKE on an image prompt is the wrong scorer (`SKILL.md` lines 515-516), and a best-effort note below the gate fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header and the prompt (`SKILL.md` lines 558-561). The reply leads with the saved path, reports the VISUAL result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The reply closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). The enhanced prompt carries every supplied fact: Stable Diffusion XL in ComfyUI with its separate negative prompt field, the Night of Science at the Leiden city library, a 2:3 portrait poster, a flat 1960s screen-print style, exactly four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper), the three depth layers in order (two children at a brass telescope, the brick facade with lit windows, Orion rising over the rooftops), the top quarter left as empty sky with no lettering anywhere, visible paper grain and slight ink misregistration, children of about 8 to 10 who are not photoreal, weights where they help, a separate negative prompt, and suggested CFG and steps. Exclusions become the separate negative prompt the user asked for, which Stable Diffusion reads from a dedicated field (`references/image-mode.md` lines 185-188, `assets/framework-pattern-library.md` lines 390-392). Modifiers carry the 2:3 ratio, the weights, CFG and steps. The four HEX colours stay exact. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.md` file opens with a header naming FRAME at Complex complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names FRAME and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Focus, Rendering, Atmosphere, Modifiers and Exclusions, each labelled; VISUAL passes its gate; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a title design, a second poster size or a social media variant are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$image $markdown We make event posters with Stable Diffusion XL in ComfyUI, which has a separate negative prompt field. I need a prompt for this year's Night of Science at the Leiden city library: a 2:3 portrait poster in a flat 1960s screen-print style, limited to four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper). Three depth layers: two children at a brass telescope in the foreground, the library's brick facade with lit windows in the middle, and Orion rising over the rooftops behind. The top quarter stays empty sky for the title we add later, so no lettering anywhere. Visible paper grain and slight ink misregistration. The children look about 8 to 10 and are not photoreal. Use weights where they help, give me the negative prompt separately and suggest CFG and steps. Build it with FRAME, keep all of it, no questions.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every FRAME element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Image and delivers without a question. Step 3 proves the export exists and opens with a header that names FRAME at a complexity inside the Complex tier. Step 4 proves every FRAME element is labelled, the VISUAL gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the VISUAL score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each FRAME element to its label in the file, a fact checklist against the file, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming FRAME at a complexity inside the Complex tier, every FRAME element labelled, a passing VISUAL result, every supplied fact intact, no scope expansion and the share-back invitation
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion or a missing invitation
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 81 and 352 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 220, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the FRAME entry in the framework matrix, `assets/framework-pattern-library.md` lines 86-90 and 325-341, and the Quick Select row in `references/patterns-evaluation.md` line 685 when the header or the body names another framework or leaves an element out
3. Check the VISUAL gate in `SKILL.md` lines 450-451, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-124 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-020 | FRAME at Complex complexity for a library science poster | Verify `$image` delivers a Complex-tier FRAME prompt in one turn with every FRAME element labelled | `$image $markdown We make event posters with Stable Diffusion XL in ComfyUI, which has a separate negative prompt field. I need a prompt for this year's Night of Science at the Leiden city library: a 2:3 portrait poster in a flat 1960s screen-print style, limited to four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper). Three depth layers: two children at a brass telescope in the foreground, the library's brick facade with lit windows in the middle, and Orion rising over the rooftops behind. The top quarter stays empty sky for the title we add later, so no lettering anywhere. Visible paper grain and slight ink misregistration. The children look about 8 to 10 and are not photoreal. Use weights where they help, give me the negative prompt separately and suggest CFG and steps. Build it with FRAME, keep all of it, no questions.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Image bound, delivery with no question. Step 3: header names FRAME at the Complex tier. Step 4: FRAME elements labelled, VISUAL passed, facts kept, no expansion | Transcript, VISUAL line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and FRAME patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the VISUAL rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$image` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`image-mode.md`](../../references/image-mode.md) | FRAME workflow, VISUAL image rubric and platform negatives |
| [`image-mode-library.md`](../../assets/image-mode-library.md) | Image platform syntax and FRAME banks |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-020
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/frame-complex-library-science-poster-export.md`
