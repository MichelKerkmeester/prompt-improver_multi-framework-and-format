---
title: "SFM-001 -- Independent $json format lock"
description: "Validates that $json locks the format axis while $improve wins the mode axis, producing a valid JSON export with overhead reporting."
version: 1.1.0.0
---

# SFM-001 -- Independent $json format lock

`$improve` and `$json` live on different axes. The mode command wins the intent route and the format command locks the output format, so neither steals the other's decision.

---

## 1. OVERVIEW

Mode and format are independent in the router. This scenario proves the split: `$improve` binds the Improve lane at Standard energy while `$json` locks the file to valid JSON. The export carries the `.json` extension, opens with the required single-line `Mode:` header, the payload below it parses as JSON and the chat reports the token overhead.

### Why this matters

If the format command competed for the primary route, `$improve $json` would collapse into one intent and either the mode or the syntax would be lost. The axis split is the only reason both survive the same request.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$json` locks format independently while `$improve` binds the mode
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I want a sharper version of this prompt and I need the result in JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and the saved `.json` file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. The Improve lane binds at Standard energy, the format locks to JSON, the runtime saves `export/[###] - enhanced-*.json` with a single-line `Mode:` header carrying complexity and framework, followed by a payload that parses as valid JSON, and the reply leads with the path, reports the CLEAR result and reports roughly five to ten percent token overhead. The format lock keeps the required header above the payload (`SKILL.md` line 412). The JSON format guide writes the header as `Mode: $json` (`assets/format-guide-json.md` line 127) while `SKILL.md` asks for the mode with its `$` prefix (`SKILL.md` line 559), so a header labelled `$json` or `$improve` both pass and only a missing header fails. The label used is recorded, and the source conflict is logged as a follow-up finding. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved `.json` file carries the required header and a payload below it that parses cleanly
- Pass/fail: PASS if the `.json` export carries the single-line `Mode:` header and the payload below it parses, the format lock held and the overhead was reported. FAIL if the file is markdown, the header is missing, the payload is invalid JSON, the mode axis was stolen, the overhead is missing, the payload fails the scope test or a revision edits the delivered export in place. A summary outside the two to three sentence band is recorded and never decides the verdict

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | Bind Improve, lock JSON, either deliver through a verified `.json` export or ask at most one consolidated question | Format locked to JSON regardless of any question | Response transcript and `export/` listing |
| 2 | `Valid JSON only, the action items are for a project manager.` | When Turn 1 asked, complete the enhancement, save the `.json` export and reply path-first. When Turn 1 already delivered, Turn 1 stays the graded delivery, and this turn may save the revision as a new `.json` export under the next number, never as an edit to the delivered export in place, or acknowledge the added context without a new file | JSON lock retained and project-manager audience kept | Response, score line, parsed file excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same session`
4. `filesystem: check the single-line Mode: header and parse the payload below it -> operator: grade format lock, syntax and overhead report`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and locks JSON, delivering or asking once. Step 3 completes delivery when Turn 1 asked. Step 4 proves the header line exists and the payload below it parses as valid JSON. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists and for the revision rule, so a Turn 1 export edited in place fails the run.

### Evidence

Turn transcripts, the CLEAR score line, `export/` listings before and after, a parse check on the payload below the `.json` header, the token-overhead note in chat and the verdict.

### Pass / fail

- **Pass**: A `.json` export with the required header and a payload that parses, a reported CLEAR result, the overhead note and the path-first reply. A summary outside the two to three sentence band is recorded and never decides the verdict
- **Fail**: A markdown file, a missing header, invalid JSON payload syntax, format competing with mode, missing overhead report, a payload that fails the scope test, a delivered export edited in place or a path that does not match disk
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the independent format axis in `SKILL.md` Smart Routing when the format or mode was lost
2. Re-check the JSON rules in `assets/format-guide-json.md` when the file fails to parse
3. Check the token-overhead rule in `SKILL.md` lines 409 and 501 when the chat omits the overhead note

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFM-001 | Independent $json format lock | Verify format axis locks JSON while Improve binds mode | `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Check header, parse payload` | Step 1: baseline known. Step 2: Improve bound, JSON locked. Step 3: delivery complete when Turn 1 asked. Step 4: header and valid JSON payload | Transcripts, CLEAR line, export listings, parse result, overhead note | PASS if the .json header and payload are valid and the lock and overhead hold. FAIL on wrong format, missing header, invalid JSON, missing overhead, a failed scope test or an export edited in place. The summary band never decides the verdict | 1. Check format axis rule.<br>2. Check JSON format guide.<br>3. Check overhead rule. |

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
