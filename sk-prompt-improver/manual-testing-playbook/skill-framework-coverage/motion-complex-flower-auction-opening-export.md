---
title: "SFW-022 -- MOTION at Complex complexity for a flower auction opening shot"
description: "Validates that a single $video $yaml prompt delivers an export in one turn whose header names MOTION at Complex complexity, whose body is organised by MOTION's elements and whose VISUAL gate passes with every supplied fact kept."
version: 1.1.0.0
---

# SFW-022 -- MOTION at Complex complexity for a flower auction opening shot

`$video` binds the Video lane and `$yaml` locks YAML, so the runtime writes one MOTION prompt, scores it with VISUAL and saves it as a `.yaml` export before replying. The request names MOTION and carries every essential, so the only correct reply is a delivery whose header and body both show MOTION.

---

## 1. OVERVIEW

The user supplies the platform with native audio, one continuous 10-second shot, three timed camera beats, the moving elements, an audio bed with two exclusions, a light change and an anonymity rule, and names MOTION. The runtime improves that into one prompt organised by MOTION, scores it with VISUAL and saves it before replying. The runner sends this one prompt and nothing more, so the scenario has no second turn.

### Why this matters

One continuous shot with timed beats, three moving systems and native audio is MOTION at full load. The test is whether every beat lands in an element, the audio stays as asked and the YAML parses.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$video` delivers a Complex-tier MOTION prompt in one turn with every MOTION element labelled
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I need a Kling 2.6 prompt with sound for our flower-auction film's opening shot: one 10-second glide over tulip trolley trains at dawn, a rise at 4 seconds, the auction clock at 8, hum, wheels and a chime but no music or voices, blue light warming to gold. MOTION, in YAML.`
- Prompt: `$video $yaml Kling 2.6 prompt with native audio for the opening shot of a brand film about a flower auction near Aalsmeer. One continuous 10-second shot, 16:9, text-to-video. At dawn the camera glides forward about three metres above a hall full of trolley trains loaded with red and yellow tulips, the trains snaking past each other in two directions while three workers on electric tugs steer them. At 4 seconds the camera rises slowly to reveal the whole hall, and at 8 seconds it settles facing the big auction clock as its hand starts to sweep. Audio: electric hum, trolley wheels on concrete and a distant chime at the end, with no music and no voices. Cool blue daylight from the roof windows warms to gold by the end. The workers stay small and anonymous. Use MOTION, keep every beat and don't ask me questions.`
- Expected execution process: Start a fresh session in the disposable copy, submit the prompt once and then inspect the reply and every saved file. The runner sends this one prompt and nothing more
- Expected signals: The runner sends this one prompt and nothing more, so the single reply is the graded delivery, and a reply that asks instead of delivering fails for missing delivery. One consolidated question: when essentials are missing, the runtime asks one consolidated question that covers every missing essential in a single message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). This prompt leaves no essential missing: it carries the source prompt or goal, the target model or platform, the audience, the facts and the constraints, and it tells the runtime not to ask (`SKILL.md` line 383, `references/interactive-mode.md` line 200). It pre-answers every question its route could raise: the route itself raises none, since `references/interactive-mode.md` lines 221 and 659 route `$video` straight to MOTION processing; the simplification choice complexity 7 or more raises (`references/interactive-mode.md` lines 72-74 and 141-150, `SKILL.md` line 534), answered by asking to keep every part, and the framework doubt `SKILL.md` line 537 escalates, answered by naming MOTION; the format question (`references/interactive-mode.md` lines 75-77), answered by the `$yaml` token. Command flow allows at most one interaction (`SKILL.md` line 402), but this scenario has no second turn to spend it on, so a question asked anyway is recorded with the route that raised it and the scenario fails for missing delivery. Lane: `$video` binds the Video lane at Creative energy with MOTION and VISUAL (`SKILL.md` lines 82, 353 and 376), and `$yaml` locks YAML on its own axis (`SKILL.md` lines 71, 84 and 99). Framework: the prompt names MOTION as a hint the runtime detects (`SKILL.md` lines 332 and 381), and the runtime selects the simplest fitting framework, fit over complexity (`SKILL.md` lines 387 and 489). The library's decision table assigns MOTION to video generation (`assets/framework-pattern-library.md` lines 211-216), and Video mode runs MOTION (`SKILL.md` line 353). Header: the file opens with the single-line `Mode: [mode] | Complexity: [level] | Framework: [Framework]` header (`SKILL.md` lines 558-559). Its Framework field names MOTION; a fusion such as `MOTION + CoT` passes when MOTION comes first, and a header that names another framework first fails. Complexity may be a label or a 1 to 10 number (`assets/format-guide-markdown.md` line 123), and it must sit inside the Complex tier: the label `Complex`, or 9 or 10 as a bare number or written n/10, or another label above High, such as `Very High`; a bare `High` label names the High tier and fails here. The mode label may be the mode command or the format command. The framework, complexity and mode label used are recorded. The format guide shows RCAF or CRAFT in its header template and field checks (`assets/format-guide-yaml.md` lines 128 and 454), but `SKILL.md` line 559 asks only for the framework used, so that template is the guide's common case and not a limit: the header names MOTION, and a header or body that falls back to RCAF or CRAFT fails. Body: the prompt is visibly organised by MOTION's elements, Movement, Origin, Temporal, Intention, Orchestration and Nuance (`assets/framework-pattern-library.md` lines 91-95 and 409-428, `references/video-mode.md` lines 61-86). Every element appears as its own YAML key, at the top level or under one wrapping key, in any letter case; an element that is missing, unnamed or folded into another element's section fails. Sub-sections inside an element are fine, and an extra top-level section is recorded and passes only when it holds the user's own facts. The MOTION element sections are the structure the user asked for and never count as scope expansion; what goes inside them still has to come from the request. Scorer: VISUAL passes at 56 of 70 for a video prompt, which must carry explicit camera or subject motion (`SKILL.md` line 451, `references/video-mode.md` lines 42, 57 and 125-158); CLEAR or EVOKE on a video prompt is the wrong scorer (`SKILL.md` lines 515-516), a static prompt fails (lines 518-519) and a best-effort note below the gate fails this scenario. Delivery: the runtime saves `export/[###] - enhanced-[description].yaml` before replying (`AGENTS.md` lines 34 and 49) and verifies its syntax (`AGENTS.md` line 41). The payload below the header parses as valid YAML with no Markdown inside (`SKILL.md` lines 410 and 497, `assets/format-guide-yaml.md` lines 135-143 and 448-456). The YAML format guide writes the header as `Mode: $yaml` (`assets/format-guide-yaml.md` line 128) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$yaml` or `$video` both pass. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header and is not Markdown: the literal `Mode: $yaml | ...` line does not parse as YAML, so the comment form lets the whole file parse. Either form passes, and the form used is recorded. The reply reports roughly three to seven percent token overhead (`SKILL.md` lines 410 and 501). The reply leads with the saved path, reports the VISUAL result with gate status and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The reply closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). The enhanced prompt carries every supplied fact: Kling 2.6 with native audio as the platform, the opening shot of a brand film about a flower auction near Aalsmeer, one continuous 10-second shot at 16:9, text-to-video, a forward glide about three metres above trolley trains of red and yellow tulips at dawn, the trains snaking past each other in two directions, three workers on electric tugs steering them, a slow rise at 4 seconds revealing the hall, settling on the auction clock at 8 seconds as its hand starts to sweep, audio of electric hum, trolley wheels on concrete and a distant chime at the end, no music and no voices, cool blue daylight warming to gold, and the workers small and anonymous. Kling 2.6 carries native audio (`assets/framework-pattern-library.md` lines 473-476), so the audio the user described is a required fact. The shot stays one continuous scene (`references/video-mode.md` lines 193-195). No music and no voices must survive in meaning; video mode holds that most video AI ignores negative prompts (line 50), so positive phrasing is expected, literal negative wording is recorded as a follow-up finding and a dropped exclusion fails. Kling reverses pan and tilt terms (lines 223-225), so the camera wording used is recorded. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.yaml` file opens with a header naming MOTION at Complex complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, closing on the share-back invitation
- Pass/fail: PASS if all of these hold: the delivery is a verified `.yaml` export saved before a path-first reply; the header names MOTION and a complexity inside the Complex tier (9 to 10); the prompt body is visibly organised by Movement, Origin, Temporal, Intention, Orchestration and Nuance, each labelled; VISUAL passes its gate; the payload below the header parses as YAML; every supplied fact is kept; and the scope test holds; and the reply closes with the share-back invitation. FAIL if the reply asks a question instead of delivering (missing delivery), no export exists or output appears before saving, the reply does not lead with the saved path, the prompt is pasted, the header names another framework or a complexity outside the tier, an element is missing or unnamed, the scorer is wrong or below its gate, the payload does not parse, a supplied fact is dropped or altered, the invitation is missing or the prompt carries scope expansion. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a voice-over script, a second shot or a logo end card are examples

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$video $yaml Kling 2.6 prompt with native audio for the opening shot of a brand film about a flower auction near Aalsmeer. One continuous 10-second shot, 16:9, text-to-video. At dawn the camera glides forward about three metres above a hall full of trolley trains loaded with red and yellow tulips, the trains snaking past each other in two directions while three workers on electric tugs steer them. At 4 seconds the camera rises slowly to reveal the whole hall, and at 8 seconds it settles facing the big auction clock as its hand starts to sweep. Audio: electric hum, trolley wheels on concrete and a distant chime at the end, with no music and no voices. Cool blue daylight from the roof windows warms to gold by the end. The workers stay small and anonymous. Use MOTION, keep every beat and don't ask me questions.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit the prompt exactly, once`
3. `filesystem: list export/ and read the new .yaml export, then parse the payload below the single-line header -> operator: check the header's framework and complexity against the Complex tier`
4. `operator: map every MOTION element to its label, run the fact checklist and the scope test, and grade scorer, delivery and chat shape`

### Expected

Step 1 fixes the baseline. Step 2 binds Video and delivers without a question. Step 3 proves the export exists and opens with a header that names MOTION at a complexity inside the Complex tier, with a payload that parses as YAML. Step 4 proves every MOTION element is labelled, the VISUAL gate passed, every supplied fact survived and nothing unasked was added.

### Evidence

The transcript, the VISUAL score line with gate status, the `export/` listing before and after the turn, the header line with the framework, complexity and mode label used, a map from each MOTION element to its label in the file, the parse result for the payload below the header and the token-overhead note, a fact checklist against the file, the share-back sentence in chat, any fit note the runtime gave and the verdict.

### Pass / fail

- **Pass**: A verified `.yaml` export and a path-first reply, a header naming MOTION at a complexity inside the Complex tier, every MOTION element labelled, a passing VISUAL result, a payload that parses as YAML, every supplied fact intact, no scope expansion and the share-back invitation
- **Fail**: A question instead of a delivery, output shown before saving, a missing export or header, another framework in the header or the body, a complexity outside the tier, a missing or unnamed element, the wrong scorer or a result below its gate, an invalid payload, a dropped or altered fact, scope expansion or a missing invitation
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the lane binding in `SKILL.md` lines 82 and 353 and the pre-answered routes in `references/interactive-mode.md` lines 200 and 221, plus lines 69-77, when the reply asked instead of delivering
2. Re-check the MOTION entry in the framework matrix, `assets/framework-pattern-library.md` lines 91-95 and 409-428, and the Quick Select row in `references/patterns-evaluation.md` line 686 when the header or the body names another framework or leaves an element out
3. Check the VISUAL gate in `SKILL.md` lines 450-451, the export rules in `AGENTS.md` lines 34-42 and the header rules in `assets/format-guide-yaml.md` lines 124-143 when the score, the file or the header is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFW-022 | MOTION at Complex complexity for a flower auction opening shot | Verify `$video` delivers a Complex-tier MOTION prompt in one turn with every MOTION element labelled | `$video $yaml Kling 2.6 prompt with native audio for the opening shot of a brand film about a flower auction near Aalsmeer. One continuous 10-second shot, 16:9, text-to-video. At dawn the camera glides forward about three metres above a hall full of trolley trains loaded with red and yellow tulips, the trains snaking past each other in two directions while three workers on electric tugs steer them. At 4 seconds the camera rises slowly to reveal the whole hall, and at 8 seconds it settles facing the big auction clock as its hand starts to sweep. Audio: electric hum, trolley wheels on concrete and a distant chime at the end, with no music and no voices. Cool blue daylight from the roof windows warms to gold by the end. The workers stay small and anonymous. Use MOTION, keep every beat and don't ask me questions.` | 1. `Record export baseline` -> 2. `Submit the prompt once` -> 3. `Read the export, check header, parse payload` -> 4. `Map elements, check facts and scope` | Step 1: baseline known. Step 2: Video bound, delivery with no question. Step 3: header names MOTION at the Complex tier, payload parses. Step 4: MOTION elements labelled, VISUAL passed, facts kept, no expansion | Transcript, VISUAL line, export listing, header, element map, fact checklist, parse result | PASS if export, header, elements, gate, facts and scope all hold. FAIL on a question instead of a delivery, a missing export, another framework, a complexity outside the tier, an unnamed element, a failed gate, an invalid payload, a lost fact or scope expansion | 1. Check lane and question routes.<br>2. Check framework selection and elements.<br>3. Check scorer and delivery rules. |

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
| [`format-guide-yaml.md`](../../assets/format-guide-yaml.md) | YAML header, syntax and delivery rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Complexity labels for the header |

---

## 5. SOURCE METADATA

- Group: Skill framework coverage
- Playbook ID: SFW-022
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-framework-coverage/motion-complex-flower-auction-opening-export.md`
