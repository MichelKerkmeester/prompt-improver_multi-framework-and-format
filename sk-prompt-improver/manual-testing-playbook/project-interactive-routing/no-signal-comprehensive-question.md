---
title: "PIR-002 -- No-signal request gets one comprehensive question"
description: "Validates that a plain-language request with no command and no keyword hit routes the Project to the single comprehensive question."
version: 1.1.1.0
---

# PIR-002 -- No-signal request gets one comprehensive question

Turn 1 carries no command token, no leading slash and no dollar-prefixed flag, and it scores zero on every router keyword. The Project must ask one comprehensive question covering the source prompt, target use case and mode, then wait.

---

## 1. OVERVIEW

Users name what they want in plain words. The fallback applies: no command and no keyword hit routes to the Interactive fallback (`Custom Instructions.md` line 61, mirrored in `SKILL.md` line 89), which asks once and waits rather than inventing a mode.

### Why this matters

This is the most common way real users arrive. A runtime that guesses a lane or asks drip-feed questions fails the interaction contract before any prompt work begins.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the no-command, no-keyword request produces exactly one comprehensive question and a wait in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Delivery shape: the reply opens with the Deliverable Block, one bare code fence with no language tag holding only the improved prompt, with no preamble (`Custom Instructions.md` DELIVERY PROTOCOL). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it. A fence placed before any commentary counts as the delivery, and a reply without one counts as no delivery
- Real user request: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, confirm the single question and the absent Deliverable Block, then submit Turn 2 and inspect the bare-fence delivery
- Expected signals: Turn 1 asks one consolidated question that covers every missing essential in a single message (`Prompt Improver - Interactive Mode.md` lines 41 and 395, `Custom Instructions.md` line 259) and renders no Deliverable Block. Asking for the source prompt, use case and mode in that one message is correct, and splitting them across messages is the failure. Turn 2 supplies the prompt and context, and the runtime improves it, passes CLEAR and renders the bare-fence Deliverable Block, then the chat reports the export-equivalent path. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One question followed by a fence delivery built only on what the user supplied
- Pass/fail: PASS if exactly one consolidated question message fires, the runtime waits and Turn 2 facts drive the Deliverable Block. FAIL if it guesses a mode, splits the question across messages, answers its own question, renders before Turn 2, puts commentary before the Turn 2 block or the Deliverable Block carries an invented requirement or fails the scope test. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Hey, I could use a hand with a draft I have been stuck on all week.` | Ask one consolidated question covering source prompt, use case and mode in a single message, then wait with no Deliverable Block rendered | No mode bound and no fence created | Response transcript and the opening fence |
| 2 | `It is a prompt for a support chatbot. Tighten it up: "Answer the customer nicely and fix their problem".` | Improve the supplied prompt, pass CLEAR, render the bare-fence Deliverable Block and report the export-equivalent path | Chatbot subject and tighten intent retained | Response, score line, fence excerpt, open items |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm one consolidated question message and no fence -> user: submit Turn 2 in the same conversation`
4. `artifact: inspect the opening fence -> operator: grade retained facts, gate and no-save report`

### Expected

Step 1 fixes the packaging under test. Step 2 produces exactly one comprehensive question and no Deliverable Block. Step 3 proves the wait. Step 4 finds one Deliverable Block built only on Turn 2 facts.

### Evidence

Both turn transcripts, the opening fence showing nothing rendered on Turn 1, the question itself, the CLEAR score line, the export-equivalent path and a Deliverable Block excerpt showing the chatbot subject.

### Pass / fail

- **Pass**: One consolidated question, a clean wait and a Turn 2-driven bare-fence Deliverable Block
- **Fail**: A guessed mode, a question split across messages, a self-answered question, commentary before the Turn 2 block, invented requirements, a Deliverable Block that fails the scope test or a Deliverable Block rendered before Turn 2. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the no-signal row in the `Custom Instructions.md` Smart Routing detection table and the disambiguation rule its Phase Detection pointer sends to `Prompt Improver - Interactive Mode.md`
2. Compare the Turn 1 reply with the comprehensive-question contract in `Prompt Improver - Interactive Mode.md` lines 41 and 395
3. Reconcile the Deliverable Block content with Turn 2 facts, and apply the scope test to any output, field or section the user did not ask for

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PIR-002 | No-signal request gets one comprehensive question | Verify the zero-signal request routes to one question and a wait | `Hey, I could use a hand with a draft I have been stuck on all week.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Confirm question, submit Turn 2` -> 4. `Inspect the opening fence` | Step 1: packaging fixed. Step 2: one question, no Deliverable Block. Step 3: wait held. Step 4: Deliverable Block from Turn 2 facts | Two responses, fence state, question, score, Deliverable Block excerpt | PASS if one question fires and Turn 2 drives the Deliverable Block. FAIL on a guessed mode, a question split across messages, early output, commentary before the block, invented requirements or a failed scope test. The summary band never decides the verdict | 1. Check no-signal fallback.<br>2. Check comprehensive-question contract.<br>3. Check Deliverable Block against Turn 2 facts. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | No-command, no-keyword fallback to the Interactive question |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | Comprehensive question, wait and state rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | CLEAR gate applied after the user answers |

---

## 5. SOURCE METADATA

- Group: Project interactive routing
- Playbook ID: PIR-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-interactive-routing/no-signal-comprehensive-question.md`
