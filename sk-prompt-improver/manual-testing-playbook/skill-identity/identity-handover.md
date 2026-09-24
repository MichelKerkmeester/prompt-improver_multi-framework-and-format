---
title: "SID-001 -- Identity handover and file delivery"
description: "Validates that the skill runtime delivers through a real export file it wrote and supports the split with its AGENTS.md identity phrase."
version: 1.0.0.0
---

# SID-001 -- Identity handover and file delivery

This scenario proves which packaging answered: the skill runtime must deliver through a file it actually wrote, with an identity phrase from `AGENTS.md` recorded as support.

---

## 1. OVERVIEW

The skill runtime and the Claude Project share almost every rule, so most replies look alike. The deciding evidence is a delivery contract only the skill sets: a named path under `export/` that exists on disk. The phrase `underpowered requests into clear` lives in `AGENTS.md` and nowhere in `claude project/Custom Instructions.md`, and it is recorded as supporting evidence when the reply carries it.

### Why this matters

A reply that could have come from either runtime proves nothing about which packaging loaded. Every other skill-set scenario names this handover as a precondition, so a weak identity check contaminates all downstream evidence.

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

- Objective: Verify the reply names a real export path the skill runtime wrote, with the identity phrase recorded as supporting evidence
- Preconditions: Global preconditions hold, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, allow one conditional follow-up and then inspect the reply and `export/`
- Expected signals: The reply names a saved path matching `export/[###] - enhanced-*.md` and that file exists with a single-line header plus the enhanced prompt. The reply never mentions a Canvas Artifact and never claims no file was written. `underpowered requests into clear` is recorded as supporting evidence when the reply carries it, and a paraphrase is recorded without failing the run
- Desired user-visible outcome: An identity answer plus a path-first delivery only the skill runtime can produce
- Pass/fail: PASS if the named path exists on disk with valid content and the reply carries no Project-only delivery claim. FAIL if the path does not exist, the reply claims no file was written, or the reply could have come from either runtime. A paraphrased identity phrase is supporting evidence, not a deciding failure

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | Answer with the AGENTS.md identity phrasing, then either deliver through a verified export or ask at most one consolidated question | No file exists before any needed answer, and the identity phrase is recorded for support | Response transcript and `export/` listing |
| 2, only when Turn 1 asked a question | `For new member onboarding in our gym app.` | Deliver the enhanced prompt, save the next `export/` file and reply path-first | Named file exists and matches the reply | Export excerpt and side-effect ledger |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record the identity phrase and check any single allowed question -> user: submit conditional Turn 2 when asked`
4. `filesystem: read the named export path -> operator: confirm the file exists and matches the reply`

### Expected

Step 1 fixes the side-effect baseline. Step 2 returns the identity answer plus delivery or one allowed question. Step 3 completes the delivery. Step 4 proves the named file exists on disk, which is the deciding signal.

### Evidence

Turn transcripts, the identity line or its paraphrase, `export/` listings before and after, an excerpt of the saved file showing header and prompt body and the verdict.

### Pass / fail

- **Pass**: The named export path exists with valid content and no Project-only delivery claim appears, with any identity phrase recorded as support
- **Fail**: The named path is absent, the reply claims no file was written or the reply could have come from either runtime
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Record the runtime's role wording and compare it with `AGENTS.md` and `claude project/Custom Instructions.md`
2. Re-check the export protocol in `AGENTS.md` section 2 and the delivery rules in `SKILL.md` when the path is missing
3. Treat a Canvas or no-save claim as the wrong packaging and re-check the session bootstrap

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SID-001 | Identity handover and file delivery | Verify a real export path with the identity phrase as support | `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Record identity phrase, allow one question` -> 4. `Read named export` | Step 1: baseline known. Step 2: identity phrase recorded. Step 3: delivery or one question. Step 4: file exists | Transcripts, identity phrase, export listings, file excerpt | PASS if the real path exists and no Project-only claim appears. FAIL on a missing file, a no-save claim or an either-runtime reply | 1. Compare quoted role with both identity files.<br>2. Re-check export protocol.<br>3. Re-check session bootstrap. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Skill runtime identity file and export protocol |
| [`SKILL.md`](../../SKILL.md) | Routing, scoring gates and export-first delivery |
| [`interactive-mode.md`](../../references/interactive-mode.md) | One-question flow and wait rules |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | The other runtime identity file used to prove the split |

---

## 5. SOURCE METADATA

- Group: Skill identity
- Playbook ID: SID-001
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-identity/identity-handover.md`
