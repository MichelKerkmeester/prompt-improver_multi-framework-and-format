---
title: "PTX-001 -- Natural-language improve with CLEAR and fence delivery"
description: "Validates the plain-language improve request in the Project: Standard energy, the CLEAR gate and bare-fence delivery."
version: 1.1.1.0
---

# PTX-001 -- Natural-language improve with CLEAR and fence delivery

Turn 1 names the job in plain words with no command token, no leading slash and no dollar-prefixed flag. The semantic route binds a text-family intent, Standard energy runs and the CLEAR gate guards a Deliverable Block rendered as the bare-fence Deliverable Block.

---

## 1. OVERVIEW

The user supplies a rough prompt and asks for a better one in natural language. The Project router scores `prompt` on a word boundary, binds the text lane and proceeds. No question comes before delivery, and the Deliverable Block comes before any chat commentary.

### Why this matters

This is the delivery shape most Project users see first: the bare fence first, then the export-equivalent path, compact score and short summary, and never the full prompt pasted again into chat. A Project that skips the gate or claims a saved file breaks the delivery protocol.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the natural-language improve flow delivers a CLEAR-gated bare-fence Deliverable Block in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Delivery shape: the reply opens with the Deliverable Block, one bare code fence with no language tag holding only the improved prompt, with no preamble (`Custom Instructions.md` DELIVERY PROTOCOL). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it. A fence placed before any commentary counts as the delivery, and a reply without one counts as no delivery
- Real user request: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect the opening fence and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. The runtime improves at Standard energy, applies CLEAR with its 40 of 50 pass threshold and dimension floors, renders the Deliverable Block as the bare-fence Deliverable Block before commentary and the chat reports the export-equivalent path with the `[###]` placeholder, the score and a two to three sentence summary without pasting the prompt again. The single-line header is the `Mode: $[mode] | Complexity: [level] | Framework: [Framework]` line of the kernel's Delivery Protocol template (`Custom Instructions.md` line 231), and bold markup on that line does not change it. A bold transparency line that opens with `Mode:` but lacks `Complexity:` and `Framework:` on the same line is commentary, not the header. A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 128). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One fence-first reply whose block reads back as a better version of the supplied prompt and whose chat claims no file was written
- Pass/fail: PASS if the Deliverable Block holds the enhanced prompt, the CLEAR gate ran and the chat shape holds. FAIL if commentary precedes the block, the full prompt is pasted again, the score is absent, a save is claimed, requirements were invented or the block fails the scope test. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | Bind the text lane, deliver through the bare-fence Deliverable Block in Turn 1 with no question, listing every default as an open item | No more than one question and no fence before it is answered | Response transcript and the opening fence |
| 2 | `For a general audience blog post, markdown is fine.` | Turn 1 stays the graded delivery, and this turn may render the revision as a new Deliverable Block under the next export-equivalent name or acknowledge the added context without one | Coffee subject and general-audience intent retained | Response, score line, fence excerpt, open items |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record that Turn 1 delivered with no question first -> user: submit Turn 2 in the same conversation`
4. `artifact: read the opening fence -> operator: grade gate, chat shape and no-save report`

### Expected

Step 1 fixes the packaging under test. Step 2 binds the text lane and delivers with no question. Step 3 records the Turn 1 delivery. Step 4 proves the Deliverable Block holds the enhanced prompt and the chat honors the delivery contract. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the opening fence, an excerpt showing the prompt body, the single-line header in chat, the export-equivalent path line, the open items and the verdict.

### Pass / fail

- **Pass**: A bare-fence Deliverable Block holding only the enhanced prompt, a reported CLEAR result and the export-equivalent path with no save claimed. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Fail**: Commentary before the block, the prompt pasted again in chat, missing score, invented requirements, a block that fails the scope test or any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Delivery Protocol in `Custom Instructions.md` section 6 against the observed ordering
2. Re-check the CLEAR thresholds and floors in `Prompt Improver - Patterns and Evaluation.md` when the score is missing or off
3. Compare the Deliverable Block body with the supplied prompt, and apply the scope test to any output, field or section the user did not ask for

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-001 | Natural-language improve with CLEAR and fence delivery | Verify plain-word improve delivers a gated bare-fence Deliverable Block | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read the opening fence` | Step 1: packaging fixed. Step 2: text lane bound. Step 3: Turn 1 delivery recorded. Step 4: Deliverable Block verified | Transcripts, CLEAR line, fence state, Deliverable Block excerpt | PASS if Deliverable Block, gate and chat shape all hold. FAIL on commentary before the block, inline-only delivery, pasted prompt, missing score, a claimed save or invented scope. The summary band never decides the verdict | 1. Check delivery ordering.<br>2. Check CLEAR thresholds.<br>3. Check Deliverable Block against supplied prompt. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Semantic routing, Standard energy and the Delivery Protocol |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | CLEAR rubric, floors and repair rules |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown.md>) | Markdown deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/improve-flow-clear-canvas.md`
