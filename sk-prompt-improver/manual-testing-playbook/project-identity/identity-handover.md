---
title: "PID-001 -- Identity handover and fence delivery"
description: "Validates that the Project runtime proves its Custom Instructions identity string and delivers through the bare-fence Deliverable Block with no file claim."
version: 1.1.1.0
---

# PID-001 -- Identity handover and fence delivery

This scenario proves which packaging answered: the Project runtime must echo an identity string only `claude project/Custom Instructions.md` carries and deliver through the bare-fence contract only the Project sets.

---

## 1. OVERVIEW

The skill runtime and the Claude Project share almost every rule, so most replies look alike. The handover has to show two things at once: the verbatim string `bare code fence`, which lives in `claude project/Custom Instructions.md` and nowhere in `AGENTS.md`, and a delivery contract only the Project sets, meaning a reply that opens with one bare code fence holding only the prompt, then a chat report with the header line, the export-equivalent path and the open items that claims no file was written.

### Why this matters

A reply that could have come from either runtime proves nothing about which packaging loaded, and a reply that could have come from either runtime is a FAIL in this file. Every other project-set scenario names this handover as a precondition, so a weak identity check contaminates all downstream evidence.

### Identity string proof

Re-run this split check from the worktree root before relying on the handover:

```text
$ grep -c "underpowered requests into clear" "AI Systems/Prompt Improver/AGENTS.md"
1
$ grep -c "underpowered requests into clear" "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
0
$ grep -c "bare code fence" "AI Systems/Prompt Improver/AGENTS.md"
0
$ grep -c "bare code fence" "AI Systems/Prompt Improver/claude project/Custom Instructions.md"
4
```

A re-run shows the positive-count greps exit 0 and the zero-count greps exit 1.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the reply carries the Project-only identity string and the bare-fence delivery contract only the Project runtime sets
- Preconditions: Global preconditions hold and a claude.ai Project is configured with `Custom Instructions.md` pasted into the project instructions and the system's knowledge documents attached. Delivery shape: the reply opens with the Deliverable Block, one bare code fence with no language tag holding only the improved prompt, with no preamble (`Custom Instructions.md` DELIVERY PROTOCOL). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it. A fence placed before any commentary counts as the delivery, and a reply without one counts as no delivery
- Real user request: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect the opening fence and the chat report
- Expected signals: The Turn 1 reply carries the verbatim string `bare code fence`. The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. Its Deliverable Block is one bare code fence with no language tag holding only the enhanced prompt, with no header line, divider or footer inside it. The chat report after it carries the `Mode: | Complexity: | Framework:` header line, the numbered open items and the export-equivalent path with the `[###]` placeholder and never claims a file was written, saved or verified on disk. A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The kernel puts the block before any commentary (`Custom Instructions.md` lines 156 and 239), and no rule says where the answer to a non-prompt question goes on a mixed request, so this scenario makes one exception to the definition of commentary: an identity answer placed before the block is recorded as an ordering note, does not count as commentary and does not decide this handover. A fence that follows it still counts as the delivery, and any other text before the block stays commentary. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 128). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: An identity answer plus a fence-first delivery only the Project runtime can produce
- Pass/fail: PASS if the string appears verbatim, the fence holds only the prompt, the chat carries the header line and the open items and no save is claimed. FAIL if the string is missing or altered, the reply names a real path it wrote, the fence is tagged or holds a header or footer, a question about a soft gap precedes the deliverable, the prompt carries scope expansion or the reply could have come from either runtime. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | Answer the identity question and deliver through the bare-fence Deliverable Block in Turn 1 with no question, listing every default as an open item | Identity string appears verbatim and no fence exists before any needed answer | Response transcript and the opening fence |
| 2 | `For new member onboarding in our gym app.` | Turn 1 stays the graded delivery, and this turn may render the revision as a new Deliverable Block under the next export-equivalent name or acknowledge the added context without one | Fence content matches the chat report and no save is claimed | Fence excerpt and transcript |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: check the identity string and whether Turn 1 delivered with no question first -> user: submit Turn 2 in the same conversation`
4. `artifact: read the opening fence -> operator: confirm it holds only the prompt, then the header line, open items, export-equivalent path and the no-save claim`

### Expected

Step 1 fixes the packaging under test. Step 2 returns the identity answer plus the delivery, with no question, because the request carries a prompt. Step 3 records the Turn 1 delivery. Step 4 proves the fence, the chat report and the no-save contract. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the line carrying `bare code fence`, an excerpt of the fence showing it holds only the prompt body, the chat lines with the header line, the open items and the export-equivalent path and the verdict.

### Pass / fail

- **Pass**: The verbatim string is present, the Deliverable Block rendered as one bare code fence holding only the prompt, the chat carries the header line and the open items and claims no file was written. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Fail**: The string is missing or altered, the reply names a real saved path, the prompt carries scope expansion, the prompt arrives only as loose inline chat text or a Canvas Artifact, or the reply could have come from either runtime
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Ask the runtime to quote its role and compare the wording with `claude project/Custom Instructions.md` and `AGENTS.md`
2. Re-check the Delivery Protocol in `Custom Instructions.md` section 6 when the fence, the header line, the open items or the export-equivalent path is missing
3. Treat a saved-path or verified-on-disk claim as the wrong packaging and re-check the Project configuration

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PID-001 | Identity handover and fence delivery | Verify the Project-only identity string plus bare-fence delivery | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Check string, submit Turn 2` -> 4. `Read the fence and chat` | Step 1: packaging fixed. Step 2: identity string verbatim. Step 3: delivery on the first delivering turn. Step 4: fence, open items and no-save verified | Transcripts, string location, fence excerpt, header line, open items, path line | PASS if the string and the bare-fence contract both hold. FAIL on a missing string, a claimed save or an either-runtime reply. The summary band never decides the verdict | 1. Compare quoted role with both identity files.<br>2. Re-check Delivery Protocol.<br>3. Re-check Project configuration. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Project runtime identity file and bare-fence delivery contract |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | Deliver-first flow, open items and wait rules for the Project |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | Scoring gates consulted by the Project |
| [`AGENTS.md`](../../../AGENTS.md) | The other runtime identity file used to prove the split |

---

## 5. SOURCE METADATA

- Group: Project identity
- Playbook ID: PID-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-identity/identity-handover.md`
