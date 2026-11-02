---
title: "SIR-001 -- Conflicting mode commands ask one question"
description: "Validates that two conflicting mode commands route to one clarifying question instead of a silent pick."
version: 1.0.0.0
---

# SIR-001 -- Conflicting mode commands ask one question

This scenario checks that `$short` and `$deep` in one request are treated as a conflict: the runtime asks which mode was meant, waits and then delivers the chosen lane.

---

## 1. OVERVIEW

Two distinct mode commands in the same request are not silently resolved. The router sends the request to Interactive Mode, which asks one question and waits. Only after the user picks does the runtime bind the mode, run the matching energy level and export.

### Why this matters

A silent pick would choose the user's DEPTH energy for them. If the runtime quietly prefers `$deep` or `$short`, every downstream score and deliverable is built on a mode the user never confirmed.

---

## 2. SCENARIO CONTRACT

- Objective: Verify conflicting mode commands produce one clarifying question and no silent resolution
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I want to improve my prompt for a weekly meal-plan generator, and I keep going back and forth on whether a quick pass or a deep rewrite would serve me better.`
- Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, confirm the question and clean ledger, then submit Turn 2 with the source prompt and inspect the export
- Expected signals: Turn 1 asks which of the two modes was meant in one question and writes no file. Turn 2 supplies the source prompt, binds Short, runs Quick energy, passes CLEAR, saves one `.md` export and replies path-first. The supplied prompt removes the smart-default branch, so the export must enhance that prompt rather than inventing one
- Desired user-visible outcome: One question followed by a Short-mode delivery that honors the user's pick
- Pass/fail: PASS if the runtime asks rather than picks and the Turn 2 delivery enhances the supplied prompt at Short energy. FAIL if it silently binds either mode, asks more than one question, writes a file before clarifying or delivers without the supplied prompt

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$short $deep improve my prompt for a weekly meal-plan generator` | Ask which of the two modes was meant in one question and wait, with no file written | Mode unresolved until the user answers | Response transcript and unchanged `export/` listing |
| 2 | `Use short mode. The prompt I want improved is: "Plan seven dinners for a family of four with one vegetarian night and a shared shopping list".` | Run Short at Quick energy on the supplied prompt, pass CLEAR, save the next `.md` export and reply path-first with the score | Short bound, supplied prompt retained and meal-plan subject kept | Response, score line, export excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm one question and no artifact -> user: submit Turn 2 in the same session`
4. `filesystem: inspect the next .md export -> operator: grade mode binding and score`

### Expected

Step 1 fixes the baseline. Step 2 produces one clarifying question and nothing on disk. Step 3 proves the wait. Step 4 finds one Short-mode export consistent with the user's answer.

### Evidence

Both turn transcripts, the side-effect ledger showing no Turn 1 artifact, the CLEAR score line, the export path and an excerpt showing the meal-plan subject.

### Pass / fail

- **Pass**: The runtime asks one question, waits and delivers Short at Quick energy on the supplied prompt with a verified export
- **Fail**: The runtime silently picks a mode, splits the question across messages, writes early or ignores the Turn 2 answer
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the conflict rule in `SKILL.md` Smart Routing and the Interactive Mode disambiguation rule
2. Compare the Turn 1 reply with the one-question flow in `references/interactive-mode.md`
3. Reconcile the final response with the export ledger and the reported CLEAR score

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SIR-001 | Conflicting mode commands ask one question | Verify conflict detection asks which mode instead of picking one | `$short $deep improve my prompt for a weekly meal-plan generator` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Confirm question, submit Turn 2` -> 4. `Inspect export` | Step 1: baseline known. Step 2: one question, no file. Step 3: wait held. Step 4: Short-mode export | Two responses, ledger, score, export excerpt | PASS if the runtime asks and then honors the pick on the supplied prompt. FAIL on a silent pick, multiple questions, early output or a delivery that ignores the supplied prompt | 1. Check conflict routing rule.<br>2. Check one-question flow.<br>3. Check export and score evidence. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`SKILL.md`](../../SKILL.md) | Conflict detection, command table and Interactive fallback |
| [`interactive-mode.md`](../../references/interactive-mode.md) | One comprehensive question and wait behavior |
| [`depth-framework.md`](../../references/depth-framework.md) | Quick energy expectations for the resolved Short lane |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR scoring gate used after the pick |

---

## 5. SOURCE METADATA

- Group: Skill interactive routing
- Playbook ID: SIR-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-interactive-routing/conflicting-commands-clarification.md`
