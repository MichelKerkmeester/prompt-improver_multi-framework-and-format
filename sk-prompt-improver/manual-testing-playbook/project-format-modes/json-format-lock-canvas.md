---
title: "PFM-001 -- Independent $json format lock in the Project"
description: "Validates that $json locks the format axis while $improve wins the mode axis, producing a JSON Deliverable Block with overhead reporting."
version: 1.2.1.0
---

# PFM-001 -- Independent $json format lock in the Project

`$improve` and `$json` live on different axes in the Project router. The mode command wins the intent route and the format command locks the output format, so neither steals the other's decision.

---

## 1. OVERVIEW

Mode and format are independent in the Project router, exactly as in the skill. This scenario proves the split on the Project surface: `$improve` binds the Improve lane at Standard energy while `$json` locks the prompt payload to valid JSON inside the Deliverable Block. The fence holds the payload alone, so the format lock covers everything inside it, and the `Mode:` header and the token overhead follow in chat.

### Why this matters

If the format command competed for the primary route, `$improve $json` would collapse into one intent and either the mode or the syntax would be lost. The axis split is the only reason both survive the same request.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$json` locks format independently while `$improve` binds the mode in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. Delivery shape: the reply opens with the Deliverable Block, one bare code fence with no language tag holding only the improved prompt, with no preamble (`Custom Instructions.md` DELIVERY PROTOCOL). Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it. A fence placed before any commentary counts as the delivery, and a reply without one counts as no delivery
- Real user request: `I want a sharper version of this prompt and I need the result in JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect the opening fence and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. The Improve lane binds at Standard energy, the format locks to JSON, the bare-fence Deliverable Block holds only a prompt payload that parses as valid JSON, and the chat after the fence reports the single-line `Mode:` header, the export-equivalent path, the CLEAR result, roughly five to ten percent token overhead and the open items (`Custom Instructions.md` section 6). The chat header may be labelled `$json` or `$improve`; both pass and only a missing header fails, and the label used is recorded. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 128). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One fence-first reply whose fenced payload parses cleanly and whose chat claims no file was written
- Pass/fail: PASS if the fence holds only the payload, the payload parses as JSON, the `Mode:` header follows the fence in chat, the format lock held and the overhead was reported. FAIL if the chat header is missing or anything besides the prompt sits in the fence, the payload is markdown, the JSON is invalid, the mode axis was stolen, the overhead is missing, the payload fails the scope test, commentary precedes the block or a save is claimed. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | Bind Improve, lock JSON, deliver through the bare-fence Deliverable Block in Turn 1 with no question, listing every default as an open item | Format locked to JSON regardless of any question | Response transcript and the opening fence |
| 2 | `Valid JSON only, the action items are for a project manager.` | Turn 1 stays the graded delivery, and this turn may render the revision as a new Deliverable Block under the next export-equivalent name or acknowledge the added context without one | JSON lock retained and project-manager audience kept | Response, score line, parsed Deliverable Block excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record that Turn 1 delivered with no question first -> user: submit Turn 2 in the same conversation`
4. `artifact: parse the JSON payload inside the opening fence -> operator: grade format lock, syntax and overhead report`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and locks JSON, delivering with no question first. Step 3 records the Turn 1 delivery. Step 4 proves the chat header follows the fence and the payload inside the fence parses as valid JSON. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the CLEAR score line, the opening fence, a parse check on the payload inside the Deliverable Block, the token-overhead note in chat and the verdict.

### Pass / fail

- **Pass**: A bare-fence Deliverable Block whose payload parses as valid JSON, the `Mode:` header in chat after it, a reported CLEAR result, the overhead note and no save claimed. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Fail**: A missing chat header, anything besides the payload in the fence, a markdown payload, invalid JSON syntax, format competing with mode, missing overhead report, a payload that fails the scope test, commentary before the block or any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the independent format axis in `Custom Instructions.md` Smart Routing when the format or mode was lost
2. Re-check the JSON rules in `Prompt Improver - Format Guide JSON.md` when the payload fails to parse, and the Delivery Protocol template in `Custom Instructions.md` section 6 when the chat header is missing or anything besides the prompt sits in the fence
3. Check the token-overhead rule in `Custom Instructions.md` line 234 when the chat omits the overhead note

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFM-001 | Independent $json format lock in the Project | Verify format axis locks JSON while Improve binds mode | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Check header, parse payload` | Step 1: packaging fixed. Step 2: Improve bound, JSON locked. Step 3: Turn 1 delivery recorded. Step 4: chat header, a prompt-only fence and valid JSON payload | Transcripts, CLEAR line, fence state, parse result, overhead note | PASS if the chat header, a prompt-only fence and payload are valid and the lock and overhead hold. FAIL on wrong format, missing chat header, anything besides the prompt in the fence, invalid JSON, missing overhead, a failed scope test or commentary before the block. The summary band never decides the verdict | 1. Check format axis rule.<br>2. Check JSON format guide.<br>3. Check overhead rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Independent format axis, command tables and the Delivery Protocol |
| [Format Guide JSON knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide JSON.md>) | JSON syntax and delivery rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | CLEAR gate for the Improve lane |

---

## 5. SOURCE METADATA

- Group: Project format modes
- Playbook ID: PFM-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-format-modes/json-format-lock-canvas.md`
