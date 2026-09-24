---
title: "PFM-001 -- Independent $json format lock in the Project"
description: "Validates that $json locks the format axis while $improve wins the mode axis, producing a JSON Deliverable Block with overhead reporting."
version: 1.0.0.0
---

# PFM-001 -- Independent $json format lock in the Project

`$improve` and `$json` live on different axes in the Project router. The mode command wins the intent route and the format command locks the output format, so neither steals the other's decision.

---

## 1. OVERVIEW

Mode and format are independent in the Project router, exactly as in the skill. This scenario proves the split on the Canvas surface: `$improve` binds the Improve lane at Standard energy while `$json` locks the prompt payload to valid JSON inside the Deliverable Block. The header and attestation lines sit outside the format lock, and the chat reports the token overhead.

### Why this matters

If the format command competed for the primary route, `$improve $json` would collapse into one intent and either the mode or the syntax would be lost. The axis split is the only reason both survive the same request.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$json` locks format independently while `$improve` binds the mode in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached
- Real user request: `I want a sharper version of this prompt and I need the result in JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, allow one conditional consolidated question and then inspect the Canvas Artifact and the chat report
- Expected signals: The Improve lane binds at Standard energy, the format locks to JSON, the Canvas Artifact carries the header line, a prompt payload that parses as valid JSON and the attestation footer, and the chat reports the export-equivalent path, the CLEAR result and roughly five to ten percent token overhead
- Desired user-visible outcome: One Artifact-first reply whose payload between the metadata lines parses cleanly and whose chat claims no file was written
- Pass/fail: PASS if the payload parses as JSON, the format lock held and the overhead was reported. FAIL if the payload is markdown, the JSON is invalid, the mode axis was stolen, the overhead is missing or a save is claimed

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | Bind Improve, lock JSON, either deliver through a Canvas Artifact or ask at most one consolidated question | Format locked to JSON regardless of any question | Response transcript and Artifact panel state |
| 2, only when Turn 1 asked a question | `Valid JSON only, the action items are for a project manager.` | Complete the enhancement, render the Artifact with a valid JSON payload and reply with the export-equivalent path | JSON lock retained and project-manager audience kept | Response, score line, parsed Artifact excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: allow at most one question -> user: submit conditional Turn 2 when asked`
4. `artifact: parse the JSON payload inside the Canvas Artifact -> operator: grade format lock, syntax and overhead report`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and locks JSON, delivering or asking once. Step 3 completes delivery. Step 4 proves the payload between the header and attestation lines parses as valid JSON.

### Evidence

Turn transcripts, the CLEAR score line, the Artifact panel state, a parse check on the payload inside the Deliverable Block, the token-overhead note in chat and the verdict.

### Pass / fail

- **Pass**: A Canvas Artifact whose payload parses as valid JSON, a reported CLEAR result, the overhead note and no save claimed
- **Fail**: A markdown payload, invalid JSON syntax, format competing with mode, missing overhead report or any claim that a file was written
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the independent format axis in `Custom Instructions.md` Smart Routing when the format or mode was lost
2. Re-check the JSON rules in the Format Guide JSON knowledge doc when the payload fails to parse
3. Check the token-overhead rule in `Custom Instructions.md` section 6 when the chat omits the overhead note

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFM-001 | Independent $json format lock in the Project | Verify format axis locks JSON while Improve binds mode | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Allow one question` -> 4. `Parse Artifact payload` | Step 1: packaging fixed. Step 2: Improve bound, JSON locked. Step 3: delivery complete. Step 4: valid JSON payload | Transcripts, CLEAR line, panel state, parse result, overhead note | PASS if the payload parses and the lock and overhead hold. FAIL on wrong format, invalid JSON or missing overhead | 1. Check format axis rule.<br>2. Check JSON format guide.<br>3. Check overhead rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Independent format axis, command tables and the Delivery Protocol |
| [Format Guide JSON knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide JSON - v0.142.md>) | JSON syntax and delivery rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR gate for the Improve lane |

---

## 5. SOURCE METADATA

- Group: Project format modes
- Playbook ID: PFM-001
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-format-modes/json-format-lock-canvas.md`
