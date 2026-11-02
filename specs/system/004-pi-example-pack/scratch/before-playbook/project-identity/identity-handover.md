---
title: "PID-001 -- Identity handover and Canvas delivery"
description: "Validates that the Project runtime proves its Custom Instructions identity string and delivers through a Canvas Artifact with no file claim."
version: 1.0.0.0
---

# PID-001 -- Identity handover and Canvas delivery

This scenario proves which packaging answered: the Project runtime must echo an identity string only `claude project/Custom Instructions.md` carries and deliver through the Canvas Artifact contract only the Project sets.

---

## 1. OVERVIEW

The skill runtime and the Claude Project share almost every rule, so most replies look alike. The handover has to show two things at once: the verbatim string `Canvas Artifact`, which lives in `claude project/Custom Instructions.md` and nowhere in `AGENTS.md`, and a delivery contract only the Project sets, meaning a Deliverable Block rendered in the side panel, an attestation footer and a chat report that claims no file was written.

### Why this matters

A reply that could have come from either runtime proves nothing about which packaging loaded, and a reply that could have come from either runtime is a FAIL in this file. Every other project-set scenario names this handover as a precondition, so a weak identity check contaminates all downstream evidence.

### Identity string proof

Re-run this split check from the worktree root before relying on the handover:

```text
$ grep -c "underpowered requests into clear" "AI Systems/Prompt Improver/AGENTS.md"
1
$ grep -c "underpowered requests into clear" "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
0
$ grep -c "Canvas Artifact" "AI Systems/Prompt Improver/AGENTS.md"
0
$ grep -c "Canvas Artifact" "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
5
```

A re-run shows the positive-count greps exit 0 and the zero-count greps exit 1.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the reply carries the Project-only identity string and the Canvas delivery contract only the Project runtime sets
- Preconditions: Global preconditions hold and a claude.ai Project is configured with `Custom Instructions.md` pasted into the project instructions and the system's knowledge documents attached. When a terminal runner stands in for the Project, the reply text stands in for the Artifact panel: a delimited Deliverable Block placed before any commentary counts as the rendered Artifact, and a reply without one counts as an empty panel
- Real user request: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect the Canvas Artifact and the chat report
- Expected signals: The Turn 1 reply carries the verbatim string `Canvas Artifact`. The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. Its Deliverable Block renders as a Canvas Artifact, carries the single-line header plus the enhanced prompt and closes with the attestation footer. The chat report names the export-equivalent path with the `[###]` placeholder and never claims a file was written, saved or verified on disk. A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The kernel puts the block before any commentary, and no rule says where the answer to a non-prompt question goes on a mixed request, so an identity answer placed before the block is recorded as an ordering note, does not count as commentary and does not decide this handover. A block that follows it still counts as the rendered Artifact
- Desired user-visible outcome: An identity answer plus a Canvas-first delivery only the Project runtime can produce
- Pass/fail: PASS if the string appears verbatim and the Artifact plus attestation and no-save claim all hold. FAIL if the string is missing or altered, the reply names a real path it wrote or the reply could have come from either runtime

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | Answer the identity question and either deliver through a Canvas Artifact or ask at most one consolidated question | Identity string appears verbatim and no Artifact exists before any needed answer | Response transcript and Artifact panel state |
| 2 | `For new member onboarding in our gym app.` | When Turn 1 asked, deliver the enhanced prompt as a Canvas Artifact with attestation and reply with the export-equivalent path. When Turn 1 already delivered, Turn 1 stays the graded delivery, and this turn may render a revised Deliverable Block or acknowledge the added context without one | Artifact content matches the chat report and no save is claimed | Artifact excerpt and transcript |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: check the identity string and whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read the Canvas Artifact -> operator: confirm attestation, export-equivalent path and the no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 returns the identity answer plus delivery or one allowed question. Step 3 completes the delivery when Turn 1 asked. Step 4 proves the Artifact, attestation and no-save contract. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the line carrying `Canvas Artifact`, an excerpt of the Artifact showing header, prompt body and attestation footer, the chat lines with the export-equivalent path and the verdict.

### Pass / fail

- **Pass**: The verbatim string is present, the Deliverable Block rendered as a Canvas Artifact, the attestation records no execution and no save and the chat claims no file was written
- **Fail**: The string is missing or altered, the reply names a real saved path, the prompt arrives only as loose inline chat text or the reply could have come from either runtime
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Ask the runtime to quote its role and compare the wording with `claude project/Custom Instructions.md` and `AGENTS.md`
2. Re-check the Delivery Protocol in `Custom Instructions.md` section 6 when the Artifact, attestation or export-equivalent path is missing
3. Treat a saved-path or verified-on-disk claim as the wrong packaging and re-check the Project configuration

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PID-001 | Identity handover and Canvas delivery | Verify the Project-only identity string plus Canvas Artifact delivery | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Check string, submit Turn 2` -> 4. `Read Artifact and chat` | Step 1: packaging fixed. Step 2: identity string verbatim. Step 3: delivery on the first delivering turn. Step 4: Artifact and no-save verified | Transcripts, string location, Artifact excerpt, attestation, path line | PASS if the string and the Canvas contract both hold. FAIL on a missing string, a claimed save or an either-runtime reply | 1. Compare quoted role with both identity files.<br>2. Re-check Delivery Protocol.<br>3. Re-check Project configuration. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Project runtime identity file and Canvas delivery contract |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | One-question flow and wait rules for the Project |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | Scoring gates consulted by the Project |
| [`AGENTS.md`](../../../AGENTS.md) | The other runtime identity file used to prove the split |

---

## 5. SOURCE METADATA

- Group: Project identity
- Playbook ID: PID-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-identity/identity-handover.md`
