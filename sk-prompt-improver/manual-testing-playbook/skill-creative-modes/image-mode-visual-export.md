---
title: "SCR-001 -- Image mode VISUAL gate and follow-up"
description: "Validates the $image lane: Creative energy, FRAME workflow, VISUAL image scoring and the mandatory share-back invitation."
version: 1.0.0.0
---

# SCR-001 -- Image mode VISUAL gate and follow-up

`$image` binds the Image lane at Creative energy, runs the FRAME workflow and scores with VISUAL, never CLEAR or EVOKE. The reply closes with the mandatory invitation to share the generated result.

---

## 1. OVERVIEW

The image lane has its own scorer and its own follow-up rule. The runtime loads the image mode reference and library, builds a platform-aware prompt for the named generator and passes it through the VISUAL image gate at 48 of 60 before export.

### Why this matters

Creative modes carry two obligations beyond the export: the correct scorer and the share-back invitation. Swapping VISUAL for CLEAR or dropping the follow-up are quiet failures a text-mode check would never catch.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$image` delivers a VISUAL-scored export with the creative follow-up
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I want a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`
- Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and the saved `.md` file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. The Image lane binds at Creative energy, FRAME runs, the VISUAL image gate applies at 48 of 60, the runtime saves `export/[###] - enhanced-*.md` and the reply leads with the path, reports the score and closes by inviting the user to share the generated result for refinement
- Desired user-visible outcome: One path-first reply carrying the VISUAL score and the share-back invitation
- Pass/fail: PASS if the export exists, VISUAL ran and the follow-up invite appears. FAIL if CLEAR or EVOKE scored instead, the invite is missing, the prompt drops the named platform or the path does not match disk

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` | Bind Image at Creative energy, either deliver through a verified `.md` export or ask at most one consolidated question | Midjourney target and cabin subject retained | Response transcript and `export/` listing |
| 2 | `Photorealistic style, landscape orientation.` | When Turn 1 asked, complete the FRAME pass, save the export and reply path-first with the VISUAL score and follow-up invite. When Turn 1 already delivered, Turn 1 stays the graded delivery, and this turn may save a revised export under the next number or acknowledge the added context without a new file | Style and orientation facts retained | Response, score line, export excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same session`
4. `filesystem: read the saved .md export -> operator: grade scorer, platform fit and follow-up`

### Expected

Step 1 fixes the baseline. Step 2 binds the Image lane and either delivers or asks once. Step 3 completes delivery when Turn 1 asked. Step 4 proves the file exists and the scorer was VISUAL. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the VISUAL score line with gate status, `export/` listings before and after, a file excerpt showing the platform-aware prompt and the follow-up sentence in the reply.

### Pass / fail

- **Pass**: A verified export, a VISUAL image score and the mandatory share-back invitation
- **Fail**: The wrong scorer, a missing invitation, dropped platform context or a path that does not match disk
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Image lane binding and scorer map in `SKILL.md` Mode Mapping
2. Re-check FRAME and the VISUAL image rubric in `references/image-mode.md` and `references/patterns-evaluation.md`
3. Check the creative follow-up rule in `SKILL.md` ALWAYS list when the invite is absent

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SCR-001 | Image mode VISUAL gate and follow-up | Verify the image lane scores VISUAL and invites share-back | `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read saved export` | Step 1: baseline known. Step 2: Image bound. Step 3: delivery complete when Turn 1 asked. Step 4: VISUAL verified | Transcripts, VISUAL line, export listings, file excerpt, invite | PASS if export, VISUAL and invite all hold. FAIL on wrong scorer, missing invite or dropped platform | 1. Check lane and scorer map.<br>2. Check FRAME and VISUAL rubric.<br>3. Check follow-up rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`SKILL.md`](../../SKILL.md) | Image lane binding, scorer map and follow-up rule |
| [`image-mode.md`](../../references/image-mode.md) | FRAME workflow and image platform routing |
| [`image-mode-library.md`](../../assets/image-mode-library.md) | Platform syntax and FRAME banks |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | VISUAL image rubric and threshold |

---

## 5. SOURCE METADATA

- Group: Skill creative modes
- Playbook ID: SCR-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-creative-modes/image-mode-visual-export.md`
