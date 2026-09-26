---
title: "PFW-021 -- MOTION at High complexity for a potter wheel reel in the Project"
description: "Validates that a single $video $markdown prompt delivers a Deliverable Block in one turn whose header names MOTION at High complexity, whose body is organised by MOTION's elements and whose VISUAL gate passes with every supplied fact kept."
version: 1.0.0.0
---

# PFW-021 -- MOTION at High complexity for a potter wheel reel in the Project

`$video` binds the Video lane in the Project router and `$markdown` locks Markdown, so the Project writes one MOTION prompt, scores it with VISUAL and renders it as a Deliverable Block before any commentary. The request names MOTION and carries every essential, so the only correct reply is a delivery whose header and body both show MOTION.

---

## 1. OVERVIEW

The user supplies the platform, an image-to-video source, duration and ratio, three subject motions, a camera move with a timed beat, the look and two framing rules, and names MOTION. The Project improves that into one prompt organised by MOTION, scores it with VISUAL and renders it as a Deliverable Block before any commentary. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Image-to-video prompts are short by nature, so the MOTION elements are easy to lose. The test is whether all six stay visible while the 8-second beat and the framing rules survive.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$video` renders a High-tier MOTION Deliverable Block in one turn with every MOTION element labelled
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Canvas stand-in: with no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble (`Custom Instructions.md` line 390). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Could you write a Runway Gen-4 image-to-video prompt from our potter still? Ten seconds for Reels: the bowl rising under her hands, slip flicking off, dust in the light, a slow push-in to her thumbs at 8 seconds, warm and calm, face out of frame. Use MOTION.`
- Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`
- Expected execution process: Start a fresh conversation in the configured Project, submit the prompt once and then inspect the Deliverable Block and the chat report. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`Prompt Improver - Interactive Mode - v0.700.md` line 413, `Custom Instructions.md` line 398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`Prompt Improver - Interactive Mode - v0.700.md` line 186). It pre-answers every question its route could raise: the route itself raises none, since lines 207 and 645 of the same file route `$video` straight to MOTION processing; the simplification choice complexity 7 or more raises (`Prompt Improver - Interactive Mode - v0.700.md` lines 58-60 and 127-136, `Custom Instructions.md` line 354), answered by asking to keep every part, and the framework doubt answered by naming MOTION; the format question (`Prompt Improver - Interactive Mode - v0.700.md` lines 61-63), answered by the `$markdown` token. Command flow allows at most one interaction (`Prompt Improver - Interactive Mode - v0.700.md` line 405), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$video` binds the Video lane at Creative energy with VISUAL (`Custom Instructions.md` line 54, `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 51-55), and `$markdown` locks Markdown on its own axis (`Custom Instructions.md` lines 43, 57 and 71). Framework: the prompt names MOTION, and the kernel checklist requires the correct framework, the simplest fitting one preferred (`Custom Instructions.md` line 400). The library's decision table assigns MOTION to video generation (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 193-198), and Video mode runs MOTION (`Custom Instructions.md` line 54 with `Prompt Improver - Video Mode - v0.123.md` lines 47-72). Header: the Deliverable Block opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`Custom Instructions.md` line 372). Its Framework field names MOTION; a fusion such as `MOTION + CoT` passes when MOTION comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`Prompt Improver - Format Guide Markdown - v0.141.md` line 109), and it must sit inside the High tier: the label `High`, or 7 or 8 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`Prompt Improver - Format Guide Markdown - v0.141.md` lines 104 and 110), but the kernel template asks only for the framework used (`Custom Instructions.md` line 372), so that template is the guide's common case and not a limit: the header names MOTION, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by MOTION's elements, Movement, Origin, Temporal, Intention, Orchestration and Nuance (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 73-77 and 391-410, `Prompt Improver - Video Mode - v0.123.md` lines 47-72). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The MOTION element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: VISUAL passes at 56 of 70 for a video prompt, which must carry explicit camera or subject motion (`Prompt Improver - Patterns and Evaluation - v0.212.md` line 463, `Prompt Improver - Video Mode - v0.123.md` lines 43 and 111-144); CLEAR or EVOKE on a video prompt is the wrong scorer (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306-307), and a best-effort note below the gate fails this scenario. Delivery: the Deliverable Block comes before any commentary and holds only the single-line header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the VISUAL result with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 384-387). No save, export or file on disk is claimed (line 347). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The chat closes by inviting the user to share the generated result (`Custom Instructions.md` lines 323 and 388). The enhanced prompt carries every supplied fact: Runway Gen-4 as the platform, image-to-video from the still of a potter's hands at a spinning wheel in a sunlit studio, 10 seconds at 9:16 for Reels, the wet clay bowl rising and widening, a thin spiral of slip flicking off the rim, dust drifting through the window light, a slow push-in from waist height reaching a close-up of her thumbs smoothing the rim at 8 seconds and then holding, a calm and tactile look with warm natural light and shallow depth of field, her face out of frame and the studio clutter soft in the background. Runway has no audio (`Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 447-450) and the user asked for none, so an audio section is scope expansion. Image-to-video prompts run 20 to 40 words (line 441), so the word count of any assembled prompt line is recorded and does not decide the verdict. The camera wording Runway expects (`Prompt Improver - Video Mode - v0.123.md` lines 203-205) is recorded. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming MOTION at High complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the reply opens with the Deliverable Block before any commentary, with the header, the prompt and the attestation footer, and claims no save; the header names MOTION and a complexity inside the High tier (7 to 8); the prompt body is visibly organised by Movement, Origin, Temporal, Intention, Orchestration and Nuance, each labelled; VISUAL passes its gate; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), commentary precedes the block, the header or the attestation is missing, the prompt is pasted again, a save is claimed, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a music track, a second shot or on-screen captions are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `artifact: read the Deliverable Block -> operator: check the header's framework and complexity against the High tier`
4. `operator: map every MOTION element to its label, run the fact checklist and the scope test, and grade scorer, block order, chat report and no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Video and delivers without a question. Step 3 proves the Deliverable Block comes first and opens with a header that names MOTION at a complexity inside the High tier. Step 4 proves every MOTION element is labelled, the VISUAL gate passed, every supplied fact survived, nothing unasked was added and no save was claimed.

### Evidence

The transcript, the VISUAL score line with gate status, the Artifact panel state, the header line with the framework, complexity and mode label used, a map from each MOTION element to its label in the block, a fact checklist against the block, the export-equivalent path line, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a header naming MOTION at a complexity inside the High tier, every MOTION element labelled, a passing VISUAL result, every supplied fact intact, no scope expansion, no save claimed and the share-back invitation
- **Fail**: A question instead of a delivery, commentary before the block, a missing header or attestation, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion, any claim that a file was written or a missing invitation
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the lane binding in `Custom Instructions.md` line 54 and the pre-answered routes in `Prompt Improver - Interactive Mode - v0.700.md` lines 186 and 207, plus lines 55-63, when the reply asked instead of delivering
2. Re-check the MOTION entry in the framework matrix, `Prompt Improver - Assets - Framework Pattern Library - v0.100.md` lines 73-77 and 391-410, and the Quick Select row in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 672 when the header or the body names another framework or leaves an element out
3. Check the VISUAL gate in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 463 and the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 when the score, the block order, the header or the attestation is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFW-021 | MOTION at High complexity for a potter wheel reel in the Project | Verify `$video` renders a High-tier MOTION Deliverable Block in one turn with every MOTION element labelled | `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.` | 1. `Configure Project` -> 2. `Submit the prompt once` -> 3. `Read the block, check header` -> 4. `Map elements, check facts and scope` | Step 1: packaging fixed. Step 2: Video bound, delivery with no question. Step 3: block first, header names MOTION at the High tier. Step 4: MOTION elements labelled, VISUAL passed, facts kept, no expansion, no save claimed | Transcript, VISUAL line, panel state, header, element map, fact checklist | PASS if block, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, commentary before the block, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact, scope expansion or a claimed save | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Lane binding, format axis, scope rule, framework checklist, Delivery Protocol and No Canvas panel rule |
| [Framework Pattern Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) | Framework matrix, selection algorithm, decision table and MOTION patterns |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Quick Select bands, the VISUAL gate and scorer bans |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Question triggers, `$video` route and interaction limits |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Energy levels and complexity assessment |
| [Video Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Video Mode - v0.123.md>) | MOTION workflow, VISUAL video rubric and platform anti-patterns |
| [Video Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Video Mode Library - v0.101.md>) | Video platform syntax and temporal banks |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, complexity labels and format lock |

---

## 5. SOURCE METADATA

- Group: Project framework coverage
- Playbook ID: PFW-021
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-framework-coverage/motion-high-potter-wheel-reel-canvas.md`
