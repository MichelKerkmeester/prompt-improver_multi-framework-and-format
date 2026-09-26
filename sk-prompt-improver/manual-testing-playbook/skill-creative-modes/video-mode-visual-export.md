---
title: "SCR-002 -- Video mode VISUAL gate with YAML lock and follow-up"
description: "Validates the $video lane with an independent $yaml lock: Creative energy, MOTION, VISUAL video scoring, explicit motion, a valid YAML export, the share-back invitation and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# SCR-002 -- Video mode VISUAL gate with YAML lock and follow-up

`$video` binds the Video lane at Creative energy, runs MOTION and scores with VISUAL at 56 of 70, never CLEAR or EVOKE. `$yaml` locks the file format on its own axis, so the export is a `.yaml` file whose payload parses. The reply closes with the mandatory invitation to share the generated result.

---

## 1. OVERVIEW

The user describes an eight-second Veo product shot in full: subject, setting, camera move, light, detail, final frame and two exclusions. The runtime turns that into a motion-first prompt, keeps explicit camera motion, scores it with VISUAL video and saves it as YAML. Turn 2 shortens the clip and changes the camera move, which is a revision of the delivered prompt.

### Why this matters

Video carries more rules than any other lane: a scorer of its own, a motion blocker, a positive-phrasing rule for exclusions, the creative follow-up and here a format lock as well. A runtime can satisfy most of them and still drop the one fact that makes the shot the user's.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$video $yaml` delivers a VISUAL-scored `.yaml` export with explicit motion, every supplied shot fact and the creative follow-up, then saves the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I need a Veo prompt in YAML for an eight-second product shot: our new matte black insulated water bottle on a wet rock by a mountain stream, the camera slowly orbiting in soft morning light with condensation on the bottle, ending on the logo side. No people and no text on screen.`
- Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved `.yaml` file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 is expected to deliver, since `references/interactive-mode.md` lines 221 and 659 route `$video` straight to MOTION processing; one consolidated question is still within the command-flow limit of one interaction (`SKILL.md` line 402) and is not a failure. The Video lane binds with Creative energy and VISUAL (`SKILL.md` lines 82, 353 and 376) and the format locks to YAML on its own axis (lines 71, 84 and 99). VISUAL video passes at 56 of 70 and the prompt must carry explicit camera or subject motion (`SKILL.md` line 451, `references/video-mode.md` lines 42 and 151-157); CLEAR or EVOKE on a video prompt is the wrong scorer (`SKILL.md` lines 515-517), and a static prompt fails (lines 518-519). The runtime saves `export/[###] - enhanced-[description].yaml` before replying (`AGENTS.md` lines 34 and 49), the file opens with a single-line `Mode:` header (`SKILL.md` lines 558-559) and the payload below it parses as valid YAML with no Markdown inside (`SKILL.md` line 497, `assets/format-guide-yaml.md` lines 133-141 and 451). The YAML format guide writes the header as `Mode: $yaml` (line 128) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$yaml` or `$video` both pass and only a missing header fails; the label used is recorded. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header and is not Markdown: the literal `Mode: $yaml | ...` line does not parse as YAML, so the comment form lets the whole file parse. Either form passes, and the form used is recorded. The reply leads with the path, reports the VISUAL result and roughly three to seven percent token overhead (`SKILL.md` lines 410 and 501), does not paste the prompt (`AGENTS.md` line 64) and closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). The enhanced prompt carries every supplied fact: Veo as the target, 8 seconds, a product shot of a new matte black insulated water bottle, a wet rock beside a mountain stream, a slow orbit, soft morning light, condensation drops and a final frame on the logo side of the bottle. The two exclusions, no people and no text on screen, must survive in meaning; video mode expects them phrased positively rather than as negative prompts (`references/video-mode.md` lines 50 and 190-192, `SKILL.md` lines 520-521, `references/patterns-evaluation.md` line 477), so literal negative wording is recorded as a follow-up finding and a dropped exclusion fails. An `Audio:` line is recorded and logged as a follow-up finding either way, and does not decide the verdict: the Veo row in `references/video-mode.md` lines 226-228 asks for one, while the scope test forbids a section the user did not ask for. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying the VISUAL score, the overhead note and the share-back invitation, whose saved `.yaml` file parses and keeps every shot fact, then a second `.yaml` export at 6 seconds ending on a slow push-in
- Pass/fail: PASS if the Turn 1 delivery is a `.yaml` export with the header, a payload that parses, explicit motion, every supplied shot fact and both exclusions in meaning, a VISUAL result, the overhead note and the share-back invitation, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if CLEAR or EVOKE scored instead, the prompt is static, the file is not `.yaml`, the header is missing, the payload does not parse, a shot fact or an exclusion is dropped or altered, the overhead or the invitation is missing, the path does not match disk, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a second scene, a voice-over script or on-screen copy are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.` | Bind Video at Creative energy, lock YAML, either deliver through a verified `.yaml` export with the VISUAL score and share-back invite or ask at most one consolidated question | Veo target, 8 seconds and every shot fact retained, format locked to YAML | Response transcript and `export/` listing |
| 2 | `Make it 6 seconds and end on a slow push-in instead of the orbit.` | When Turn 1 asked, complete the MOTION pass at 6 seconds ending on a slow push-in, save the `.yaml` export and reply path-first with the VISUAL score and follow-up invite. When Turn 1 delivered, treat this as a revision: save a new `.yaml` export under the next number at 6 seconds that ends on a slow push-in in place of the orbit and keeps every other shot fact, and leave the delivered export unchanged. Whether an orbit still opens the shot is recorded and not graded, since the input can be read either way | YAML lock, Veo target, bottle, rock, stream, light, condensation, logo-side ending and both exclusions retained, duration 6 seconds and a slow push-in ending | Response, score line, parse results for both exports and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: check the single-line Mode: header and parse the payload below it in every .yaml export, re-checksum the Turn 1 file -> operator: grade scorer, motion, shot facts, exclusions, overhead, follow-up and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Video and locks YAML, usually delivering at once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the header exists, the payload parses as YAML, motion and every shot fact are present and, when Turn 1 delivered, that Turn 2 saved a new `.yaml` file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the VISUAL score line with gate status, `export/` listings before and after each turn, the header label used, a parse check on the payload below each `.yaml` header, a shot-fact checklist including how the exclusions are phrased, a note of any `Audio:` line, the token-overhead note and the share-back sentence in chat, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A `.yaml` export with the header and a payload that parses, explicit motion, every shot fact and both exclusions in meaning, a VISUAL video result, the overhead note, the share-back invitation, the path-first reply and a Turn 2 revision saved as a new `.yaml` export
- **Fail**: The wrong scorer, a static prompt, a non-YAML file, a missing header, invalid YAML, a dropped or altered shot fact or exclusion, missing overhead or invitation, scope expansion, a path that does not match disk, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Video lane binding and scorer map in `SKILL.md` lines 82, 353 and 515-519 when the scorer or motion is wrong
2. Re-check MOTION, the VISUAL video rubric and the negative-prompt rule in `references/video-mode.md` lines 42-57, 125-158 and 187-192, and the YAML rules in `assets/format-guide-yaml.md` lines 124-156
3. Check the overhead and follow-up rules in `SKILL.md` lines 501-502 and the revision rule in lines 421-422

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SCR-002 | Video mode VISUAL gate with YAML lock and follow-up | Verify the video lane scores VISUAL with explicit motion in a valid YAML export, invites share-back and saves the revision as a new export | `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Check header, parse payloads, re-checksum` | Step 1: baseline known. Step 2: Video bound, YAML locked. Step 3: first delivery fixed. Step 4: VISUAL, motion, valid YAML, shot facts, revision in a new file | Transcripts, VISUAL line, export listings, parse results, shot-fact checklist, overhead note, invite, checksums | PASS if the .yaml export, VISUAL, motion, facts, overhead, invite and revision all hold. FAIL on wrong scorer, static prompt, invalid YAML, a lost fact or exclusion, missing invite or an in-place edit | 1. Check lane and scorer map.<br>2. Check MOTION, VISUAL and YAML rules.<br>3. Check overhead, follow-up and revision rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, `.yaml` naming and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Video binding, format axis, scorer bans, motion blocker, overhead, follow-up and revision rules |
| [`video-mode.md`](../../references/video-mode.md) | MOTION workflow, VISUAL video rubric, negative-prompt rule and Veo notes |
| [`video-mode-library.md`](../../assets/video-mode-library.md) | Veo platform detection and syntax |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$video` state route and conversation flow |
| [`format-guide-yaml.md`](../../assets/format-guide-yaml.md) | YAML file syntax, header and delivery rules |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | VISUAL video threshold and positive phrasing |

---

## 5. SOURCE METADATA

- Group: Skill creative modes
- Playbook ID: SCR-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-creative-modes/video-mode-visual-export.md`
