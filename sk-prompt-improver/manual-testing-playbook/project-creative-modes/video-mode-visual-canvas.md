---
title: "PCR-002 -- Video mode VISUAL gate with YAML lock and follow-up in the Project"
description: "Validates the $video lane with an independent $yaml lock in the Project: Creative energy, MOTION, VISUAL video scoring, explicit motion, a YAML Deliverable Block, the share-back invitation and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PCR-002 -- Video mode VISUAL gate with YAML lock and follow-up in the Project

`$video` binds the Video lane at Creative energy in the Project router, runs MOTION and scores with VISUAL at 56 of 70, never CLEAR or EVOKE. `$yaml` locks the prompt payload on its own axis, so the Deliverable Block carries a payload that parses. The chat closes with the mandatory invitation to share the generated result.

---

## 1. OVERVIEW

The user describes an eight-second Veo product shot in full: subject, setting, camera move, light, detail, final frame and two exclusions. The Project turns that into a motion-first prompt, keeps explicit camera motion, scores it with VISUAL video and renders it as a YAML Deliverable Block before any commentary. Turn 2 shortens the clip and changes the camera move, which is a revision of the delivered prompt.

### Why this matters

Video carries more rules than any other lane: a scorer of its own, a motion blocker, a positive-phrasing rule for exclusions, the creative follow-up and here a format lock as well. A runtime can satisfy most of them and still drop the one fact that makes the shot the user's.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$video $yaml` delivers a VISUAL-scored YAML Deliverable Block with explicit motion, every supplied shot fact and the creative follow-up in the Project runtime, then renders the Turn 2 revision as a new block
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `I need a Veo prompt in YAML for an eight-second product shot: our new matte black insulated water bottle on a wet rock by a mountain stream, the camera slowly orbiting in soft morning light with condensation on the bottle, ending on the logo side. No people and no text on screen.`
- Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 is expected to deliver, since `Prompt Improver - Interactive Mode - v0.700.md` lines 207 and 645 route `$video` straight to MOTION processing; one consolidated question is still within the command-flow limit of one interaction (same file, line 405) and is not a failure. The Video lane binds with Creative energy and VISUAL (`Custom Instructions.md` line 54) and the format locks to YAML on its own axis (lines 43, 56 and 71). VISUAL video passes at 56 of 70 and the prompt must carry explicit camera or subject motion (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 463, `Prompt Improver - Video Mode - v0.123.md` lines 28 and 43); CLEAR or EVOKE on a video prompt is the wrong scorer (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306-307), and a static prompt fails. The Deliverable Block comes before any commentary and holds the single-line `Mode:` header, a prompt payload that parses as valid YAML with no Markdown inside and the attestation footer with `format = YAML` and ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372, 377 and 380; `Prompt Improver - Format Guide YAML - v0.142.md` lines 125 and 434-437); the fence that delimits the block in a no-panel session is not part of the payload. The kernel template writes the header as `Mode: $[mode]` (`Custom Instructions.md` line 372) while the YAML format guide writes `Mode: $yaml` (`Prompt Improver - Format Guide YAML - v0.142.md` line 114), so a header labelled `$yaml` or `$video` both pass and only a missing header fails; the label used is recorded. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header, since the header sits outside the format lock in either form; the form used is recorded. After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].yaml`, the VISUAL result, roughly three to seven percent token overhead and a short summary, does not paste the prompt again and closes by inviting the user to share the generated result (`Custom Instructions.md` lines 322-323, 341 and 384-388). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: Veo as the target, 8 seconds, a product shot of a new matte black insulated water bottle, a wet rock beside a mountain stream, a slow orbit, soft morning light, condensation drops and a final frame on the logo side of the bottle. The two exclusions, no people and no text on screen, must survive in meaning; video mode expects them phrased positively rather than as negative prompts (`Prompt Improver - Video Mode - v0.123.md` lines 36 and 176-178, `Prompt Improver - Patterns and Evaluation - v0.212.md` line 463), so literal negative wording is recorded as a follow-up finding and a dropped exclusion fails. An `Audio:` line is recorded and logged as a follow-up finding either way, and does not decide the verdict: the Veo row in `Prompt Improver - Video Mode - v0.123.md` lines 212-214 asks for one, while the scope test forbids a section the user did not ask for. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply carrying the VISUAL score, the overhead note and the share-back invitation with no file claimed, whose YAML payload parses and keeps every shot fact, then a second block at 6 seconds ending on a slow push-in
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block with header and attestation before any commentary, a payload that parses as YAML, explicit motion, every supplied shot fact and both exclusions in meaning, a VISUAL result, the overhead note, the share-back invitation and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if CLEAR or EVOKE scored instead, the prompt is static, commentary precedes the block, the header or attestation is missing, the payload is Markdown or invalid YAML, a shot fact or an exclusion is dropped or altered, the overhead or the invitation is missing, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a second scene, a voice-over script or on-screen copy are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.` | Bind Video at Creative energy, lock YAML, either deliver through a Deliverable Block with the VISUAL score and share-back invite or ask at most one consolidated question | Veo target, 8 seconds and every shot fact retained, format locked to YAML | Response transcript and Artifact panel state |
| 2 | `Make it 6 seconds and end on a slow push-in instead of the orbit.` | When Turn 1 asked, complete the MOTION pass at 6 seconds ending on a slow push-in, render the block and reply with the VISUAL score and follow-up invite. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name at 6 seconds that ends on a slow push-in in place of the orbit and keeps every other shot fact. Whether an orbit still opens the shot is recorded and not graded, since the input can be read either way | YAML lock, Veo target, bottle, rock, stream, light, condensation, logo-side ending and both exclusions retained, duration 6 seconds and a slow push-in ending | Response, score line, parse results for both blocks |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: parse the YAML payload inside every Deliverable Block -> operator: grade scorer, motion, shot facts, exclusions, overhead, follow-up, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Video and locks YAML, usually delivering at once. Step 3 records the first delivery. Step 4 proves the header and attestation lines are present, the payload between them parses as YAML, motion and every shot fact are present and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the VISUAL score line with gate status, the Artifact panel state, the header label used, a parse check on the payload inside each Deliverable Block, a shot-fact checklist including how the exclusions are phrased, a note of any `Audio:` line, the token-overhead note and the share-back sentence in chat, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation whose payload parses as YAML, explicit motion, every shot fact and both exclusions in meaning, a VISUAL video result, the overhead note, the share-back invitation, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: The wrong scorer, a static prompt, commentary before the block, a missing header or attestation, a Markdown or invalid YAML payload, a dropped or altered shot fact or exclusion, missing overhead or invitation, scope expansion, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Video lane binding in `Custom Instructions.md` line 54 and the scorer bans in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306-308 when the scorer or motion is wrong
2. Re-check MOTION, the VISUAL video rubric and the negative-prompt rule in `Prompt Improver - Video Mode - v0.123.md` lines 28-43 and 173-178, and the YAML rules in `Prompt Improver - Format Guide YAML - v0.142.md` lines 110-142
3. Check the overhead and follow-up rules in `Custom Instructions.md` lines 322-323 and 386-388, and the delivery override in line 291 when Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PCR-002 | Video mode VISUAL gate with YAML lock and follow-up in the Project | Verify the video lane scores VISUAL with explicit motion in a valid YAML block, invites share-back and renders the revision as a new block | `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Check header, parse payloads` | Step 1: packaging fixed. Step 2: Video bound, YAML locked. Step 3: first delivery fixed. Step 4: VISUAL, motion, valid YAML, shot facts, revision in a new block | Transcripts, VISUAL line, panel state, parse results, shot-fact checklist, overhead note, invite | PASS if block, attestation, VISUAL, motion, facts, overhead, invite and revision all hold. FAIL on wrong scorer, static prompt, invalid YAML, a lost fact or exclusion, missing invite, a claimed save or a patch in place of a block | 1. Check lane and scorer bans.<br>2. Check MOTION, VISUAL and YAML rules.<br>3. Check overhead, follow-up and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Video binding, format axis, overhead and follow-up rules, delivery override and the Delivery Protocol |
| [Video Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Video Mode - v0.123.md>) | MOTION workflow, VISUAL video rubric, negative-prompt rule and Veo notes |
| [Video Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Video Mode Library - v0.101.md>) | Veo platform detection and syntax |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$video` route, conversation flow and interaction limits |
| [Format Guide YAML knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide YAML - v0.142.md>) | YAML syntax, header and delivery rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | VISUAL video threshold, scorer bans and positive phrasing |

---

## 5. SOURCE METADATA

- Group: Project creative modes
- Playbook ID: PCR-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-creative-modes/video-mode-visual-canvas.md`
