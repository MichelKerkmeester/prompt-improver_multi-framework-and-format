---
title: "PIR-001 -- Conflicting mode commands ask one question"
description: "Validates that two conflicting mode commands in the Project runtime route to one clarifying question instead of a silent pick."
version: 1.0.0.0
---

# PIR-001 -- Conflicting mode commands ask one question

This scenario checks that `$short` and `$deep` in one request are treated as a conflict inside the Project: the runtime asks which mode was meant, waits and then delivers the chosen lane through a Canvas Artifact.

---

## 1. OVERVIEW

Two distinct mode commands in the same request are not silently resolved. The Project router sends the request to its Interactive fallback, which asks one question and waits. Only after the user picks does the runtime bind the mode, run the matching energy level and deliver the Deliverable Block.

### Why this matters

A silent pick would choose the user's DEPTH energy for them. If the Project quietly prefers `$deep` or `$short`, every downstream score and deliverable is built on a mode the user never confirmed.

---

## 2. SCENARIO CONTRACT

- Objective: Verify conflicting mode commands produce one clarifying question and no silent resolution in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached
- Real user request: `I want to improve my prompt for a weekly meal-plan generator, and I keep going back and forth on whether a quick pass or a deep rewrite would serve me better.`
- Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, confirm the question and the absent Artifact, then submit Turn 2 with the source prompt and inspect the Canvas delivery
- Expected signals: Turn 1 asks which of the two modes was meant in one question and renders no Deliverable Block. Turn 2 supplies the source prompt, binds Short, runs Quick energy, passes CLEAR, renders the Canvas Artifact with attestation and the chat reports the export-equivalent path with the `[###]` placeholder. The supplied prompt removes the smart-default branch, so the Artifact must enhance that prompt rather than inventing one
- Desired user-visible outcome: One question followed by a Short-mode Canvas delivery that honors the user's pick
- Pass/fail: PASS if the runtime asks rather than picks and the Turn 2 delivery enhances the supplied prompt at Short energy. FAIL if it silently binds either mode, asks more than one question, renders an Artifact before clarifying or delivers without the supplied prompt

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$short $deep improve my prompt for a weekly meal-plan generator` | Ask which of the two modes was meant in one question and wait, with no Deliverable Block rendered | Mode unresolved until the user answers | Response transcript and Artifact panel state |
| 2 | `Use short mode. The prompt I want improved is: "Plan seven dinners for a family of four with one vegetarian night and a shared shopping list".` | Run Short at Quick energy on the supplied prompt, pass CLEAR, render the Canvas Artifact and report the export-equivalent path | Short bound, supplied prompt retained and meal-plan subject kept | Response, score line, Artifact excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm one question and no Artifact -> user: submit Turn 2 in the same conversation`
4. `artifact: inspect the Canvas Artifact -> operator: grade mode binding, score and no-save report`

### Expected

Step 1 fixes the packaging under test. Step 2 produces one clarifying question and no Deliverable Block. Step 3 proves the wait. Step 4 finds one Short-mode Artifact consistent with the user's answer.

### Evidence

Both turn transcripts, the Artifact panel state showing nothing rendered on Turn 1, the CLEAR score line, the export-equivalent path and an Artifact excerpt showing the meal-plan subject and attestation footer.

### Pass / fail

- **Pass**: The runtime asks one question, waits and delivers Short at Quick energy on the supplied prompt through a Canvas Artifact with attestation
- **Fail**: The runtime silently picks a mode, splits the question across messages, renders early or ignores the Turn 2 answer
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the conflict rule in `Custom Instructions.md` Smart Routing and the Interactive fallback
2. Compare the Turn 1 reply with the one-question flow in the Interactive Mode knowledge doc
3. Reconcile the final response with the Artifact content and the reported CLEAR score

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PIR-001 | Conflicting mode commands ask one question | Verify conflict detection asks which mode instead of picking one | `$short $deep improve my prompt for a weekly meal-plan generator` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Confirm question, submit Turn 2` -> 4. `Inspect Artifact` | Step 1: packaging fixed. Step 2: one question, no Artifact. Step 3: wait held. Step 4: Short-mode Artifact | Two responses, panel state, score, Artifact excerpt | PASS if the runtime asks and then honors the pick on the supplied prompt. FAIL on a silent pick, multiple questions, early output or a delivery that ignores the supplied prompt | 1. Check conflict routing rule.<br>2. Check one-question flow.<br>3. Check Artifact and score evidence. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Conflict detection, command table and Interactive fallback |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | One comprehensive question and wait behavior |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Quick energy expectations for the resolved Short lane |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR scoring gate used after the pick |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/conflicting-commands-clarification.md`
