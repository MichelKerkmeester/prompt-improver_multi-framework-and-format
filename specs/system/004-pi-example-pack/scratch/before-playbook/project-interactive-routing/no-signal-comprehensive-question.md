---
title: "PIR-002 -- No-signal request gets one comprehensive question"
description: "Validates that a plain-language request with no command and no keyword hit routes the Project to the single comprehensive question."
version: 1.0.0.0
---

# PIR-002 -- No-signal request gets one comprehensive question

Turn 1 carries no command token, no leading slash and no dollar-prefixed flag, and it scores zero on every router keyword. The Project must ask one comprehensive question covering the source prompt, target use case and mode, then wait.

---

## 1. OVERVIEW

Users name what they want in plain words. The fallback applies: no command and no keyword hit routes to the Interactive fallback (`Custom Instructions.md` line 60, mirrored in `SKILL.md` line 86), which asks once and waits rather than inventing a mode.

### Why this matters

This is the most common way real users arrive. A runtime that guesses a lane or asks drip-feed questions fails the interaction contract before any prompt work begins.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the no-command, no-keyword request produces exactly one comprehensive question and a wait in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. When a terminal runner stands in for the Project, the reply text stands in for the Artifact panel: a delimited Deliverable Block placed before any commentary counts as the rendered Artifact, and a reply without one counts as an empty panel
- Real user request: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, confirm the single question and the absent Artifact, then submit Turn 2 and inspect the Canvas delivery
- Expected signals: Turn 1 asks one consolidated question for the missing essentials and renders no Deliverable Block. Turn 2 supplies the prompt and context, and the runtime improves it, passes CLEAR and renders the Canvas Artifact with attestation plus the export-equivalent path
- Desired user-visible outcome: One question followed by a Canvas delivery built only on what the user supplied
- Pass/fail: PASS if exactly one question fires, the runtime waits and Turn 2 facts drive the Artifact. FAIL if it guesses a mode, asks several questions, answers its own question or renders before Turn 2

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Hey, I could use a hand with a draft I have been stuck on all week.` | Ask one comprehensive question covering source prompt, use case and mode, then wait with no Deliverable Block rendered | No mode bound and no Artifact created | Response transcript and Artifact panel state |
| 2 | `It is a prompt for a support chatbot. Tighten it up: "Answer the customer nicely and fix their problem".` | Improve the supplied prompt, pass CLEAR, render the Canvas Artifact and report the export-equivalent path | Chatbot subject and tighten intent retained | Response, score line, Artifact excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm one question and no Artifact -> user: submit Turn 2 in the same conversation`
4. `artifact: inspect the Canvas Artifact -> operator: grade retained facts, gate and no-save report`

### Expected

Step 1 fixes the packaging under test. Step 2 produces exactly one comprehensive question and no Deliverable Block. Step 3 proves the wait. Step 4 finds one Artifact built only on Turn 2 facts.

### Evidence

Both turn transcripts, the Artifact panel state showing nothing rendered on Turn 1, the question itself, the CLEAR score line, the export-equivalent path and an Artifact excerpt showing the chatbot subject.

### Pass / fail

- **Pass**: One consolidated question, a clean wait and a Turn 2-driven Canvas Artifact
- **Fail**: A guessed mode, multiple questions, a self-answered question, invented requirements or an Artifact rendered before Turn 2
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the no-signal row in the `Custom Instructions.md` Smart Routing detection table and the disambiguation rule its Phase Detection pointer sends to `Prompt Improver - Interactive Mode.md`
2. Compare the Turn 1 reply with the comprehensive-question contract in `Prompt Improver - Interactive Mode.md`
3. Reconcile the Artifact content with Turn 2 facts to catch invented requirements

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PIR-002 | No-signal request gets one comprehensive question | Verify the zero-signal request routes to one question and a wait | `Hey, I could use a hand with a draft I have been stuck on all week.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Confirm question, submit Turn 2` -> 4. `Inspect Artifact` | Step 1: packaging fixed. Step 2: one question, no Artifact. Step 3: wait held. Step 4: Artifact from Turn 2 facts | Two responses, panel state, question, score, Artifact excerpt | PASS if one question fires and Turn 2 drives the Artifact. FAIL on a guessed mode, split questions or early output | 1. Check no-signal fallback.<br>2. Check comprehensive-question contract.<br>3. Check Artifact against Turn 2 facts. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | No-command, no-keyword fallback to the Interactive question |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | Comprehensive question, wait and state rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR gate applied after the user answers |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/no-signal-comprehensive-question.md`
