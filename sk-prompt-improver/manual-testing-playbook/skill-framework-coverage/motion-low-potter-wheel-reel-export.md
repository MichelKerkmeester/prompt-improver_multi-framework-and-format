---
title: "SFW-021 -- MOTION at Low complexity for a potter wheel reel"
description: "Validates that a single $video $markdown prompt delivers an export in one turn whose header names MOTION at Low complexity, whose body is organised by MOTION's elements and whose VISUAL gate passes with every supplied fact kept."
version: 1.1.0.0
---

# SFW-021 -- MOTION at Low complexity for a potter wheel reel

`$video` binds the Video lane and `$markdown` locks Markdown, so the runtime writes one MOTION prompt, scores it with VISUAL and saves it as a `.md` export before replying. The request names MOTION and carries every essential, so the only correct reply is a delivery whose header and body both show MOTION.

---

## 1. OVERVIEW

The user supplies the platform, an image-to-video source, duration and ratio, three subject motions, a camera move with a timed beat, the look and two framing rules, and names MOTION. The runtime improves that into one prompt organised by MOTION, scores it with VISUAL and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

Image-to-video prompts are short by nature, so the MOTION elements are easy to lose. The test is whether all six stay visible while the 8-second beat and the framing rules survive.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$video` delivers a Low-tier MOTION prompt in one turn with every MOTION element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Could you write a Runway Gen-4 image-to-video prompt from our potter still? Ten seconds for Reels: the bowl rising under her hands, slip flicking off, dust in the light, a slow push-in to her thumbs at 8 seconds, warm and calm, face out of frame. Use MOTION.`
- Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the route itself raises none, since `references/interactive-mode.md` lines 221 and 659 route `$video` straight to MOTION processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming MOTION; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$markdown` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$video` binds the Video lane at Creative energy with MOTION and VISUAL (`SKILL.md` lines 82, 353 and 376), and `$markdown` locks Markdown on its own axis (`SKILL.md` lines 71, 85 and 99). Framework: the prompt names MOTION as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's decision table assigns MOTION to video generation (`assets/framework-pattern-library.md` lines 211-216), and Video mode runs MOTION (`SKILL.md` line 353). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names MOTION; a fusion such as `MOTION + CoT` passes when MOTION comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 127), and it must sit inside the Low tier: the label `Low`, or 1 to 4 as a bare number or written n/10. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-markdown.md` lines 118 and 128), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names MOTION, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by MOTION's elements, Movement, Origin, Temporal, Intention, Orchestration and Nuance (`assets/framework-pattern-library.md` lines 91-95 and 409-428, `references/video-mode.md` lines 61-86). Every element appears as its own heading, bold label or list label, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The MOTION element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: VISUAL passes at 56 of 70 for a video prompt, which must carry explicit camera or subject motion (`SKILL.md` line 451, `references/video-mode.md` lines 42, 57 and 125-158); CLEAR or EVOKE on a video prompt is the wrong scorer (`SKILL.md` lines 515-516), a static prompt fails (lines 518-519) and a best-effort note below the gate fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), and the file holds only the header, its `---` divider and the prompt (`SKILL.md` lines 558-562). The reply leads with the saved path, reports the VISUAL result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The reply closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). The enhanced prompt carries every supplied fact: Runway Gen-4 as the platform, image-to-video from the still of a potter's hands at a spinning wheel in a sunlit studio, 10 seconds at 9:16 for Reels, the wet clay bowl rising and widening, a thin spiral of slip flicking off the rim, dust drifting through the window light, a slow push-in from waist height reaching a close-up of her thumbs smoothing the rim at 8 seconds and then holding, a calm and tactile look with warm natural light and shallow depth of field, her face out of frame and the studio clutter soft in the background. Runway has no audio (`assets/framework-pattern-library.md` lines 465-468) and the user asked for none, so an audio section is scope expansion. Runway image-to-video prompts run 20 to 40 words (line 459), so the word count of any assembled prompt line is recorded and does not decide the verdict. The camera wording Runway expects (`references/video-mode.md` lines 217-219) is recorded. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.md` file opens with a header naming MOTION at Low complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the delivery is a verified `.md` export saved before a path-first reply; the header names MOTION and a complexity inside the Low tier (1 to 4); the prompt body is visibly organised by Movement, Origin, Temporal, Intention, Orchestration and Nuance, each labelled; VISUAL passes its gate; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a music track, a second shot or on-screen captions are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .md export -> operator: check the header's framework and complexity against the Low tier`
4. `operator: map every MOTION element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Video and delivers without a question. Step 3 proves the export exists and opens with a header that names MOTION at a complexity inside the Low tier. Step 4 proves every MOTION element is labelled, the VISUAL gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the VISUAL score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each MOTION element to its label in the file, a fact checklist against the file, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export and a path-first reply, a header naming MOTION at a complexity inside the Low tier, every MOTION element labelled, a passing VISUAL result, every supplied fact intact, no scope expansion and the share-back invitation
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, a dropped or altered fact, scope expansion or a missing invitation
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 82 and 353 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 221, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the MOTION entry in the framework matrix, `assets/framework-pattern-library.md` lines 91-95 and 409-428, and the Quick Select row in `references/patterns-evaluation.md` line 686 when the header or the body names another framework or leaves an element out
3. Check the VISUAL gate in `SKILL.md` lines 450-451, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-markdown.md` lines 114-128 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-021 | MOTION at Low complexity for a potter wheel reel | Verify `$video` delivers a Low-tier MOTION prompt in one turn with every MOTION element labelled | `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Video bound, delivery with no question. Step 3: header names MOTION at the Low tier. Step 4: MOTION elements labelled, VISUAL passed, facts kept, no expansion | Transcript, VISUAL line, export listing, header, element map, fact checklist | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, framework coverage tiers, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, syntax check and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Lane binding, format axis, framework hints, interaction limits, scorer gates, header and scope rules |
| [`framework-pattern-library.md`](../../assets/framework-pattern-library.md) | Framework matrix, selection algorithm, decision table and MOTION patterns |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | Quick Select bands and the VISUAL rubric |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Question triggers, `$video` route and interaction limits |
| [`depth-framework.md`](../../references/depth-framework.md) | Energy levels and complexity assessment |
| [`video-mode.md`](../../references/video-mode.md) | MOTION workflow, VISUAL video rubric and platform anti-patterns |
| [`video-mode-library.md`](../../assets/video-mode-library.md) | Video platform syntax and temporal banks |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and complexity labels |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-021
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/motion-low-potter-wheel-reel-export.md`
