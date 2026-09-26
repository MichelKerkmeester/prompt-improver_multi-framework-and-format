---
title: "SIR-002 -- No-signal request gets one comprehensive question"
description: "Validates that a plain-language request with no command and no keyword hit routes to the single comprehensive question."
version: 1.1.0.0
---

# SIR-002 -- No-signal request gets one comprehensive question

Turn 1 carries no command token, no leading slash and no dollar-prefixed flag, and it scores zero on every router keyword. The runtime must ask one comprehensive question covering the source prompt, target use case and mode, then wait.

---

## 1. OVERVIEW

Users name what they want in plain words. The fallback applies: no command and no keyword hit routes to Interactive Mode (`SKILL.md` line 88, mirrored in `Custom Instructions.md` line 60), which asks once and waits rather than inventing a mode.

### Why this matters

This is the most common way real users arrive. A runtime that guesses a lane or asks drip-feed questions fails the interaction contract before any prompt work begins.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the no-command, no-keyword request produces exactly one comprehensive question and a wait
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, confirm the single question and clean ledger, then submit Turn 2 and inspect the export
- Expected signals: Turn 1 asks one consolidated question that covers every missing essential in a single message (`SKILL.md` lines 397 to 398, `AGENTS.md` line 28) and writes no file. Asking for the source prompt, use case and mode in that one message is correct, and splitting them across messages is the failure. Turn 2 supplies the prompt and context, and the runtime improves it, passes CLEAR, saves the next `.md` export and replies path-first. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One question followed by a delivery built only on what the user supplied
- Pass/fail: PASS if exactly one consolidated question message fires, the runtime waits and Turn 2 facts drive the export. FAIL if it guesses a mode, splits the question across messages, answers its own question, writes before Turn 2 or the export carries an invented requirement or fails the scope test. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Hey, I could use a hand with a draft I have been stuck on all week.` | Ask one consolidated question covering source prompt, use case and mode in a single message, then wait with no file written | No mode bound and no artifact created | Response transcript and unchanged `export/` listing |
| 2 | `It is a prompt for a support chatbot. Tighten it up: "Answer the customer nicely and fix their problem".` | Improve the supplied prompt, pass CLEAR, save the next `.md` export and reply path-first | Chatbot subject and tighten intent retained | Response, score line, export excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm one consolidated question message and no artifact -> user: submit Turn 2 in the same session`
4. `filesystem: inspect the next .md export -> operator: grade retained facts and the gate`

### Expected

Step 1 fixes the baseline. Step 2 produces exactly one comprehensive question and nothing on disk. Step 3 proves the wait. Step 4 finds one export built only on Turn 2 facts.

### Evidence

Both turn transcripts, the side-effect ledger showing no Turn 1 artifact, the question itself, the CLEAR score line, the export path and an excerpt showing the chatbot subject.

### Pass / fail

- **Pass**: One consolidated question, a clean wait and a Turn 2-driven export
- **Fail**: A guessed mode, a question split across messages, a self-answered question, invented requirements, an export that fails the scope test or a file written before Turn 2. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the no-signal fallback in `SKILL.md` Smart Routing phase detection
2. Compare the Turn 1 reply with the comprehensive-question contract in `references/interactive-mode.md` lines 53 and 427
3. Reconcile the export content with Turn 2 facts, and apply the scope test to any output, field or section the user did not ask for

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SIR-002 | No-signal request gets one comprehensive question | Verify the zero-signal request routes to one question and a wait | `Hey, I could use a hand with a draft I have been stuck on all week.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Confirm question, submit Turn 2` -> 4. `Inspect export` | Step 1: baseline known. Step 2: one question, no file. Step 3: wait held. Step 4: export from Turn 2 facts | Two responses, ledger, question, score, export excerpt | PASS if one question fires and Turn 2 drives the export. FAIL on a guessed mode, a question split across messages, early output, invented requirements or a failed scope test. The summary band never decides the verdict | 1. Check no-signal fallback.<br>2. Check comprehensive-question contract.<br>3. Check export against Turn 2 facts. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`SKILL.md`](../../SKILL.md) | No-command, no-keyword fallback to Interactive Mode |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Comprehensive question, wait and state rules |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR gate applied after the user answers |

---

## 5. SOURCE METADATA

- Group: Skill interactive routing
- Playbook ID: SIR-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/no-signal-comprehensive-question.md`
