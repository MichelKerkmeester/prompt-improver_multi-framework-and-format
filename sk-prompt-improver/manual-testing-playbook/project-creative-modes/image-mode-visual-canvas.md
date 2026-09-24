---
title: "PCR-001 -- Image mode VISUAL gate and follow-up in the Project"
description: "Validates the $image lane in the Project: Creative energy, FRAME workflow, VISUAL image scoring and the mandatory share-back invitation."
version: 1.0.0.0
---

# PCR-001 -- Image mode VISUAL gate and follow-up in the Project

`$image` binds the Image lane at Creative energy, runs the FRAME workflow and scores with VISUAL, never CLEAR or EVOKE. The Project reply closes with the mandatory invitation to share the generated result.

---

## 1. OVERVIEW

The image lane has its own scorer and its own follow-up rule in the Project exactly as in the skill. The runtime consults the Image Mode knowledge and its library, builds a platform-aware prompt for the named generator and passes it through the VISUAL image gate at 48 of 60 before rendering the Deliverable Block.

### Why this matters

Creative modes carry two obligations beyond the Artifact: the correct scorer and the share-back invitation. Swapping VISUAL for CLEAR or dropping the follow-up are quiet failures a text-mode check would never catch.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$image` delivers a VISUAL-scored Canvas Artifact with the creative follow-up in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached
- Real user request: `I want a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`
- Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, allow one conditional consolidated question and then inspect the Canvas Artifact and the chat report
- Expected signals: The Image lane binds at Creative energy, FRAME runs, the VISUAL image gate applies at 48 of 60, the Deliverable Block renders as a Canvas Artifact and the chat reports the export-equivalent path and the score, then closes by inviting the user to share the generated result for refinement
- Desired user-visible outcome: One Artifact-first reply carrying the VISUAL score and the share-back invitation with no file claimed
- Pass/fail: PASS if the Artifact holds the prompt, VISUAL ran and the follow-up invite appears. FAIL if CLEAR or EVOKE scored instead, the invite is missing, the prompt drops the named platform or a save is claimed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` | Bind Image at Creative energy, either deliver through a Canvas Artifact or ask at most one consolidated question | Midjourney target and cabin subject retained | Response transcript and Artifact panel state |
| 2, only when Turn 1 asked a question | `Photorealistic style, landscape orientation.` | Complete the FRAME pass, render the Artifact and reply with the VISUAL score and follow-up invite | Style and orientation facts retained | Response, score line, Artifact excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: allow at most one question -> user: submit conditional Turn 2 when asked`
4. `artifact: read the Canvas Artifact -> operator: grade scorer, platform fit and follow-up`

### Expected

Step 1 fixes the packaging under test. Step 2 binds the Image lane and either delivers or asks once. Step 3 completes delivery. Step 4 proves the Artifact holds the platform-aware prompt and the scorer was VISUAL.

### Evidence

Turn transcripts, the VISUAL score line with gate status, the Artifact panel state, an excerpt showing the platform-aware prompt and attestation footer and the follow-up sentence in the reply.

### Pass / fail

- **Pass**: A Canvas Artifact with the image prompt, a VISUAL image score and the mandatory share-back invitation
- **Fail**: The wrong scorer, a missing invitation, dropped platform context or any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Image lane binding and scorer map in `Custom Instructions.md` Mode Mapping
2. Re-check FRAME and the VISUAL image rubric in the Image Mode knowledge doc and the Patterns and Evaluation knowledge doc
3. Check the creative follow-up rule in `Custom Instructions.md` ALWAYS list when the invite is absent

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PCR-001 | Image mode VISUAL gate and follow-up in the Project | Verify the image lane scores VISUAL and invites share-back | `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Allow one question` -> 4. `Read Artifact` | Step 1: packaging fixed. Step 2: Image bound. Step 3: delivery complete. Step 4: VISUAL verified | Transcripts, VISUAL line, panel state, Artifact excerpt, invite | PASS if Artifact, VISUAL and invite all hold. FAIL on wrong scorer, missing invite or dropped platform | 1. Check lane and scorer map.<br>2. Check FRAME and VISUAL rubric.<br>3. Check follow-up rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Image lane binding, scorer map, follow-up rule and the Delivery Protocol |
| [Image Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) | FRAME workflow and image platform routing |
| [Image Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Image Mode Library - v0.101.md>) | Platform syntax and FRAME banks |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | VISUAL image rubric and threshold |

---

## 5. SOURCE METADATA

- Group: Project creative modes
- Playbook ID: PCR-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-creative-modes/image-mode-visual-canvas.md`
