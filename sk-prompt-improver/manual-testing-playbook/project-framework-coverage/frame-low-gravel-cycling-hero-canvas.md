---
title: "PFW-019 -- FRAME at Low complexity for a gravel cycling hero image in the Project"
description: "Validates that a single $image $markdown prompt delivers a Deliverable Block in one turn whose header names FRAME at Low complexity, whose body is organised by FRAME's elements and whose VISUAL gate passes with every supplied fact kept."
version: 1.1.0.0
---

# PFW-019 -- FRAME at Low complexity for a gravel cycling hero image in the Project

`$image` binds the Image lane in the Project router and `$markdown` locks Markdown, so the Project writes one FRAME prompt, scores it with VISUAL and renders it as a Deliverable Block before any commentary. The request names FRAME and carries every essential, so the only correct reply is a delivery whose header and body both show FRAME.

---

## 1. OVERVIEW

The user supplies the platform, the subject, the angle, the style, the light, a 21:9 banner rule and three exclusions, and names FRAME. The Project improves that into one prompt organised by FRAME, scores it with VISUAL and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Image prompts tend to collapse into one comma list where the framework disappears. The test is whether the five FRAME elements stay visible and the banner's composition rule and exclusions survive.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$image` renders a Low-tier FRAME Deliverable Block in one turn with every FRAME element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 394). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `I need a Midjourney prompt for our cycling-tour homepage banner: one gravel rider on a Zeeland dyke at golden hour, low angle, photorealistic, 21:9 with the left third empty for the headline, an olive jersey, and no logos, text or other people. Organise it by FRAME.`
- Prompt: `$image $markdown Midjourney v6.1 prompt for the homepage hero of our Zeeland gravel-cycling tours: one rider on a gravel dyke path at golden hour, shot from a low angle, riding toward the camera with the Oosterschelde behind. Photorealistic, like an outdoor-apparel catalogue photo, warm light with long shadows. It is a 21:9 banner, so the left third stays calm and empty for our headline. The rider wears an olive jersey, and there are no visible logos, no text in the image and no other people. Organise it by FRAME so I can tweak each part, and keep every detail. No questions, pick sensible parameters yourself.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode - v0.700.md` line 413, `Custom Instructions.md` line 402). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode - v0.700.md` line 186). It pre-answers every question its route could raise: the route itself raises none, since lines 206 and 644 of the same file route `$image` straight to FRAME processing; the simplification choice complexity 7 or more raises (`Prompt Improver - Interactive Mode - v0.700.md` lines 58-60 and 127-136, `Custom Instructions.md` line 354), answered by asking to keep every part, and the framework doubt answered by naming FRAME; the format question (`Prompt Improver - Interactive Mode - v0.700.md` lines 61-63), answered by the `$markdown` token. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode - v0.700.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$image` binds the Image lane at Creative energy with VISUAL (`Custom Instructions.md` line 53, `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 51-55), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 71). Framework: the prompt names FRAME, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 404). The library's decision table assigns FRAME to image generation (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 187-192), and Image mode runs FRAME (`Custom Instructions.md` line 53 with `Prompt Improver - Image Mode - v0.123.md` lines 47-68). Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 372). Its Framework field names FRAME; a fusion such as `FRAME + CoT` passes when FRAME comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown - v0.141.md` line 113), and it must sit inside the Low tier: the label `Low`, or 1 to 4 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`Prompt Improver - Format Guide Markdown - v0.141.md` lines 104 and 114), but the kernel template asks only for the framework used (`Custom Instructions.md` line 372), so that template is the guide's common case and not a limit: the header names FRAME, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by FRAME's elements, Focus, Rendering, Atmosphere, Modifiers and Exclusions (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 68-72 and 307-323, `Prompt Improver - Image Mode - v0.123.md` lines 47-68). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The FRAME element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: VISUAL passes at 48 of 60 for an image prompt (`Prompt Improver - Patterns and Evaluation - v0.212.md` line 463, `Prompt Improver - Image Mode - v0.123.md` lines 114-143); CLEAR or EVOKE on an image prompt is the wrong scorer (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306-307), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, its `---` divider, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 379). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the VISUAL result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 388-391). No save, export or file on disk is claimed (line 347). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The chat closes by inviting the user to share the generated result (`Custom Instructions.md` lines 323 and 392). The enhanced prompt carries every supplied fact: Midjourney v6.1 as the platform, the homepage hero for Zeeland gravel-cycling tours, one rider on a gravel dyke path at golden hour, a low angle with the rider coming toward the camera, the Oosterschelde behind, a photorealistic outdoor-apparel catalogue look, warm light with long shadows, a 21:9 banner with the left third calm and empty for the headline, an olive jersey, and no visible logos, no text in the image and no other people. Exclusions: Midjourney reads negatives only partly, through `--no` (`Prompt Improver - Image Mode - v0.123.md` lines 163-166, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 366-368), so the three exclusions may appear as `--no` terms, as positive phrasing or both; each must survive in meaning, and the form used is recorded. Modifiers carry the 21:9 ratio. Labelled FRAME sections followed by one assembled Midjourney prompt line pass, since Midjourney favours concise comma-separated prompts (`Prompt Improver - Image Mode - v0.123.md` lines 413-415) and the assembled line is the platform payload, not an added output. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming FRAME at Low complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names FRAME and a complexity inside the Low tier (1 to 4); the prompt body is visibly organised by Focus, Rendering, Atmosphere, Modifiers and Exclusions, each labelled; VISUAL passes its gate; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a second rider, a sunset variant or a mobile crop are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$image $markdown Midjourney v6.1 prompt for the homepage hero of our Zeeland gravel-cycling tours: one rider on a gravel dyke path at golden hour, shot from a low angle, riding toward the camera with the Oosterschelde behind. Photorealistic, like an outdoor-apparel catalogue photo, warm light with long shadows. It is a 21:9 banner, so the left third stays calm and empty for our headline. The rider wears an olive jersey, and there are no visible logos, no text in the image and no other people. Organise it by FRAME so I can tweak each part, and keep every detail. No questions, pick sensible parameters yourself.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the Low tier`
4. `operator: map every FRAME element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Image and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names FRAME at a complexity inside the Low tier. Step 4 proves every FRAME element is labelled, the VISUAL gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the VISUAL score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each FRAME element to its label in the block, a fact checklist against the block, the export-equivalent path line, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming FRAME at a complexity inside the Low tier, every FRAME element labelled, a passing VISUAL result, every supplied fact intact, no scope expansion, no save claimed and the share-back invitation
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written or a missing invitation
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 53 and the pre-answered routes in `Prompt Improver - Interactive Mode - v0.700.md` lines 186 and 206, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the FRAME entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 68-72 and 307-323, and the Quick Select row in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 671 when the header or the body names another framework or leaves an element out
3. Check the VISUAL gate in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 463 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-394 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-019 | FRAME at Low complexity for a gravel cycling hero image in the Project | Verify `$image` renders a Low-tier FRAME Deliverable Block in one turn with every FRAME element labelled | `$image $markdown Midjourney v6.1 prompt for the homepage hero of our Zeeland gravel-cycling tours: one rider on a gravel dyke path at golden hour, shot from a low angle, riding toward the camera with the Oosterschelde behind. Photorealistic, like an outdoor-apparel catalogue photo, warm light with long shadows. It is a 21:9 banner, so the left third stays calm and empty for our headline. The rider wears an olive jersey, and there are no visible logos, no text in the image and no other people. Organise it by FRAME so I can tweak each part, and keep every detail. No questions, pick sensible parameters yourself.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Image bound, delivery with no question. Step 3: block first, header names FRAME at the Low tier. Step 4: FRAME elements labelled, VISUAL passed, facts kept, no expansion, no save claimed | Transcript, VISUAL line, panel state, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) | Framework matrix, selection algorithm, decision table and FRAME patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Quick Select bands, the VISUAL gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Question triggers, `$image` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Energy levels and complexity assessment |
| [Image Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) | FRAME workflow, VISUAL image rubric and platform negatives |
| [Image Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md>) | Image platform syntax and FRAME banks |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-019
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/frame-low-gravel-cycling-hero-canvas.md`
