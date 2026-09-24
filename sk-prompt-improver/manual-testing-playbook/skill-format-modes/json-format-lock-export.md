---
title: "SFM-001 -- Independent $json format lock"
description: "Validates that $json locks the format axis while $improve wins the mode axis, producing a valid JSON export with overhead reporting."
version: 1.0.0.0
---

# SFM-001 -- Independent $json format lock

`$improve` and `$json` live on different axes. The mode command wins the intent route and the format command locks the output format, so neither steals the other's decision.

---

## 1. OVERVIEW

Mode and format are independent in the router. This scenario proves the split: `$improve` binds the Improve lane at Standard energy while `$json` locks the file to valid JSON. The export carries the `.json` extension, opens with the required `Mode: $json` header, the payload below it parses as JSON and the chat reports the token overhead.

### Why this matters

If the format command competed for the primary route, `$improve $json` would collapse into one intent and either the mode or the syntax would be lost. The axis split is the only reason both survive the same request.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$json` locks format independently while `$improve` binds the mode
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I want a sharper version of this prompt and I need the result in JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, allow one conditional consolidated question and then inspect the reply and the saved `.json` file
- Expected signals: The Improve lane binds at Standard energy, the format locks to JSON, the runtime saves `export/[###] - enhanced-*.json` with the single-line `Mode: $json` header followed by a payload that parses as valid JSON and the reply leads with the path, reports the CLEAR result and reports roughly five to ten percent token overhead
- Desired user-visible outcome: One path-first reply whose saved `.json` file carries the required header and a payload below it that parses cleanly
- Pass/fail: PASS if the `.json` export carries the `Mode: $json` header and the payload below it parses, the format lock held and the overhead was reported. FAIL if the file is markdown, the header is missing, the payload is invalid JSON, the mode axis was stolen or the overhead is missing

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | Bind Improve, lock JSON, either deliver through a verified `.json` export or ask at most one consolidated question | Format locked to JSON regardless of any question | Response transcript and `export/` listing |
| 2, only when Turn 1 asked a question | `Valid JSON only, the action items are for a project manager.` | Complete the enhancement, save the `.json` export and reply path-first | JSON lock retained and project-manager audience kept | Response, score line, parsed file excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: allow at most one question -> user: submit conditional Turn 2 when asked`
4. `filesystem: check the Mode: $json header and parse the payload below it -> operator: grade format lock, syntax and overhead report`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and locks JSON, delivering or asking once. Step 3 completes delivery. Step 4 proves the header line exists and the payload below it parses as valid JSON.

### Evidence

Turn transcripts, the CLEAR score line, `export/` listings before and after, a parse check on the payload below the `.json` header, the token-overhead note in chat and the verdict.

### Pass / fail

- **Pass**: A `.json` export with the required header and a payload that parses, a reported CLEAR result, the overhead note and the path-first reply
- **Fail**: A markdown file, a missing header, invalid JSON payload syntax, format competing with mode, missing overhead report or a path that does not match disk
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the independent format axis in `SKILL.md` Smart Routing when the format or mode was lost
2. Re-check the JSON rules in `assets/format-guide-json.md` when the file fails to parse
3. Check the ALWAYS token-overhead rule in `SKILL.md` when the chat omits the overhead note

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFM-001 | Independent $json format lock | Verify format axis locks JSON while Improve binds mode | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Allow one question` -> 4. `Check header, parse payload` | Step 1: baseline known. Step 2: Improve bound, JSON locked. Step 3: delivery complete. Step 4: header and valid JSON payload | Transcripts, CLEAR line, export listings, parse result, overhead note | PASS if the .json header and payload are valid and the lock and overhead hold. FAIL on wrong format, missing header, invalid JSON or missing overhead | 1. Check format axis rule.<br>2. Check JSON format guide.<br>3. Check overhead rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`SKILL.md`](../../SKILL.md) | Independent format axis and command tables |
| [`format-guide-json.md`](../../assets/format-guide-json.md) | JSON file syntax and delivery rules |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR gate for the Improve lane |

---

## 5. SOURCE METADATA

- Group: Skill format modes
- Playbook ID: SFM-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-format-modes/json-format-lock-export.md`
