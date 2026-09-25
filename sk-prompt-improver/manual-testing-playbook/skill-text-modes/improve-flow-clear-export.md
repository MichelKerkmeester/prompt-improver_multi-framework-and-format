---
title: "STX-001 -- Natural-language improve with CLEAR and export"
description: "Validates the plain-language improve request, Standard energy, the CLEAR gate and the markdown export-first delivery."
version: 1.0.0.0
---

# STX-001 -- Natural-language improve with CLEAR and export

Turn 1 names the job in plain words with no command token, no leading slash and no dollar-prefixed flag. The semantic route binds a text-family intent, Standard energy runs and the CLEAR gate guards a `.md` export.

---

## 1. OVERVIEW

The user supplies a rough prompt and asks for a better one in natural language. The router scores `prompt` on a word boundary, binds the text lane and proceeds. At most one consolidated question is allowed before delivery, and the reply leads with the saved path.

### Why this matters

This is the delivery shape most users see first: path-first reply, compact score, short summary and never a full prompt pasted into chat. A runtime that skips the gate or shows output before saving breaks the export protocol.

---

## 2. SCENARIO CONTRACT

- Objective: Verify the natural-language improve flow delivers a CLEAR-gated markdown export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and the saved file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery, and a further question the rules allow on Turn 2 is logged as a follow-up finding. The runtime improves at Standard energy, applies CLEAR with its 40 of 50 pass threshold and dimension floors, saves `export/[###] - enhanced-*.md` before responding and replies path-first with a compact score and a two to three sentence summary without pasting the full prompt. Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it
- Desired user-visible outcome: One path-first reply whose saved file reads back as a better version of the supplied prompt
- Pass/fail: PASS if the export exists, the CLEAR gate ran and the chat shape holds. FAIL if output appears before saving, the reply does not lead with the saved path, the full prompt is pasted, the score is absent or requirements were invented

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | Bind the text lane, either deliver through a verified `.md` export or ask at most one consolidated question | No more than one question and no file before it is answered | Response transcript and `export/` listing |
| 2 | `For a general audience blog post, markdown is fine.` | When Turn 1 asked, complete the enhancement, save the export and reply path-first. When Turn 1 already delivered, Turn 1 stays the graded delivery, and this turn may save a revised export under the next number or acknowledge the added context without a new file | Coffee subject and general-audience intent retained | Response, score line, export excerpt |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same session`
4. `filesystem: read the saved .md export -> operator: grade gate, chat shape and readback`

### Expected

Step 1 fixes the baseline. Step 2 binds the text lane and either delivers or asks once. Step 3 completes delivery when Turn 1 asked. Step 4 proves the saved file exists and reads back as the enhanced prompt. A Turn 2 reply that follows a Turn 1 delivery is checked only for the blocking defects the root playbook lists.

### Evidence

Turn transcripts, the CLEAR score line with gate status, `export/` listings before and after, a file excerpt showing the single-line header plus prompt body and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export, a reported CLEAR result and the path-first compact reply shape
- **Fail**: Output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, missing score, invented requirements or a path that does not match disk
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the export-first sequence in `AGENTS.md` section 2 against the observed ordering
2. Re-check the CLEAR thresholds and floors in `references/patterns-evaluation.md` when the score is missing or off
3. Compare the export body with the supplied prompt to catch scope expansion

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| STX-001 | Natural-language improve with CLEAR and export | Verify plain-word improve delivers a gated markdown export | `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read saved export` | Step 1: baseline known. Step 2: text lane bound. Step 3: delivery complete when Turn 1 asked. Step 4: file verified | Transcripts, CLEAR line, export listings, file excerpt | PASS if export, gate and chat shape all hold. FAIL on pre-save output, a reply that does not lead with the path, pasted prompt, missing score or invented scope | 1. Check export-first ordering.<br>2. Check CLEAR thresholds.<br>3. Check export against supplied prompt. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming and chat response shape |
| [`SKILL.md`](../../SKILL.md) | Semantic routing, Standard energy and CLEAR summary |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR rubric, floors and repair rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown export file rules |

---

## 5. SOURCE METADATA

- Group: Skill text modes
- Playbook ID: STX-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-text-modes/improve-flow-clear-export.md`
