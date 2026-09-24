---
title: "PTX-001 -- Natural-language improve with CLEAR and Canvas"
description: "Validates the plain-language improve request in the Project: Standard energy, the CLEAR gate and Canvas Artifact delivery."
version: 1.0.0.0
---

# PTX-001 -- Natural-language improve with CLEAR and Canvas

Turn 1 names the job in plain words with no command token, no leading slash and no dollar-prefixed flag. The semantic route binds a text-family intent, Standard energy runs and the CLEAR gate guards a Deliverable Block rendered as a Canvas Artifact.

---

## 1. OVERVIEW

The user supplies a rough prompt and asks for a better one in natural language. The Project router scores `prompt` on a word boundary, binds the text lane and proceeds. At most one consolidated question is allowed before delivery, and the Deliverable Block comes before any chat commentary.

### Why this matters

This is the delivery shape most Project users see first: Artifact first, then the export-equivalent path, compact score and short summary, and never the full prompt pasted again into chat. A Project that skips the gate or claims a saved file breaks the delivery protocol.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the natural-language improve flow delivers a CLEAR-gated Canvas Artifact in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached
- Real user request: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, allow one conditional consolidated question and then inspect the Canvas Artifact and the chat report
- Expected signals: The runtime improves at Standard energy, applies CLEAR with its 40 of 50 pass threshold and dimension floors, renders the Deliverable Block as a Canvas Artifact before commentary and the chat reports the export-equivalent path with the `[###]` placeholder, the score and a two to three sentence summary without pasting the prompt again
- Desired user-visible outcome: One Artifact-first reply whose block reads back as a better version of the supplied prompt and whose chat claims no file was written
- Pass/fail: PASS if the Artifact holds the enhanced prompt, the CLEAR gate ran and the chat shape holds. FAIL if commentary precedes the block, the full prompt is pasted again, the score is absent, a save is claimed or requirements were invented

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | Bind the text lane, either deliver through a Canvas Artifact or ask at most one consolidated question | No more than one question and no Artifact before it is answered | Response transcript and Artifact panel state |
| 2, only when Turn 1 asked a question | `For a general audience blog post, markdown is fine.` | Complete the enhancement, render the Artifact and reply with the export-equivalent path | Coffee subject and general-audience intent retained | Response, score line, Artifact excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: allow at most one question -> user: submit conditional Turn 2 when asked`
4. `artifact: read the Canvas Artifact -> operator: grade gate, chat shape and no-save report`

### Expected

Step 1 fixes the packaging under test. Step 2 binds the text lane and either delivers or asks once. Step 3 completes delivery. Step 4 proves the Artifact holds the enhanced prompt and the chat honors the delivery contract.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the Artifact panel state, an excerpt showing the single-line header plus prompt body and attestation footer, the export-equivalent path line and the verdict.

### Pass / fail

- **Pass**: A Canvas Artifact with the enhanced prompt and attestation, a reported CLEAR result and the export-equivalent path with no save claimed
- **Fail**: Commentary before the block, the prompt pasted again in chat, missing score, invented requirements or any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Delivery Protocol in `Custom Instructions.md` section 6 against the observed ordering
2. Re-check the CLEAR thresholds and floors in the Patterns and Evaluation knowledge doc when the score is missing or off
3. Compare the Artifact body with the supplied prompt to catch scope expansion

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-001 | Natural-language improve with CLEAR and Canvas | Verify plain-word improve delivers a gated Canvas Artifact | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Allow one question` -> 4. `Read Artifact` | Step 1: packaging fixed. Step 2: text lane bound. Step 3: delivery complete. Step 4: Artifact verified | Transcripts, CLEAR line, panel state, Artifact excerpt | PASS if Artifact, gate and chat shape all hold. FAIL on inline-only delivery, pasted prompt, missing score or invented scope | 1. Check delivery ordering.<br>2. Check CLEAR thresholds.<br>3. Check Artifact against supplied prompt. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Semantic routing, Standard energy and the Delivery Protocol |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR rubric, floors and repair rules |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/improve-flow-clear-canvas.md`
