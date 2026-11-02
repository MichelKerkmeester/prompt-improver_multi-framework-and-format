---
title: "Prompt Improver: Manual Testing Playbook"
description: "Operator-facing directory, execution policy and release-readiness guide for the two-runtime Prompt Improver scenario inventory."
version: 1.0.0.0
---

# Prompt Improver: Manual Testing Playbook

This package turns the Prompt Improver contract into fourteen reproducible conversations split into two runtime sets. The skill set runs the system from `AGENTS.md` with `sk-prompt-improver/` loaded and proves export-first file delivery. The project set runs the same system from `claude project/Custom Instructions.md` with the knowledge documents attached and proves Canvas Artifact delivery with no file claim. The root owns shared policy and indexing. Each linked scenario file owns one synchronized Turn 1 prompt, a conversation chain of up to two user turns, one nine-field execution table and current source anchors.

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are recorded into `benchmark/reports/<dated-run-label>/`. Skill-set outcomes are persisted by the canonical scenario-persistence wrapper named in the skill's result persistence contract. Project-set outcomes are recorded by the operator in the same run folder. `skill-benchmark-report.md` and any `results.md` or `report.md` output stay renderer-owned and are never hand-authored.

---

## 1. OVERVIEW

The playbook holds fourteen operator scenarios in two runtime sets across twelve category folders. No alternate or supplemental scenario files are part of the package.

### Coverage map

| Set | Category | IDs | Count | Primary surface |
|---|---|---|---:|---|
| Skill | Skill identity | `SID-001` | 1 | `AGENTS.md` identity string and export-first file delivery |
| Skill | Skill interactive routing | `SIR-001..SIR-002` | 2 | Command-conflict and no-signal question flow |
| Skill | Skill text modes | `STX-001` | 1 | Natural improve, CLEAR gate, markdown export |
| Skill | Skill format modes | `SFM-001` | 1 | Independent `$json` axis, valid JSON export |
| Skill | Skill creative modes | `SCR-001` | 1 | `$image` FRAME, VISUAL gate, share-back invite |
| Skill | Skill safety boundaries | `SSB-001` | 1 | Reframe once, then persistent refusal |
| Project | Project identity | `PID-001` | 1 | `Custom Instructions` identity string and Canvas Artifact delivery |
| Project | Project interactive routing | `PIR-001..PIR-002` | 2 | Command-conflict and no-signal question flow |
| Project | Project text modes | `PTX-001` | 1 | Natural improve, CLEAR gate, Canvas Artifact |
| Project | Project format modes | `PFM-001` | 1 | Independent `$json` axis, JSON Deliverable Block |
| Project | Project creative modes | `PCR-001` | 1 | `$image` FRAME, VISUAL gate, share-back invite |
| Project | Project safety boundaries | `PSB-001` | 1 | Reframe once, then persistent refusal |

### Realistic test model

Skill set:

1. Prepare a disposable copy of `AI Systems/Prompt Improver/`.
2. Start a fresh skill-runtime session per ID unless the scenario explicitly continues the same conversation.
3. Submit every turn exactly as written.
4. Capture the assistant response, retained state and filesystem changes after every turn.
5. Record `PASS`, `FAIL` or a specifically justified `SKIP`.

Project set:

1. Configure a claude.ai Project with `claude project/Custom Instructions.md` pasted into the project instructions and every document under `claude project/knowledge/` attached.
2. Start a fresh Project conversation per ID unless the scenario explicitly continues the same conversation.
3. Submit every turn exactly as written.
4. Capture the assistant response, the Artifact panel state and retained context after every turn.
5. Record `PASS`, `FAIL` or a specifically justified `SKIP`.

Run every scenario against the real runtime. Do not mock responses.

### Two-runtime proof rule

Each set opens with an identity handover (`SID-001` or `PID-001`) that every other scenario in that set names as a precondition. The handover passes when the delivery contract only that runtime sets holds. `SID-001` decides on a named export path that exists on disk, with its identity phrase recorded as supporting evidence. `PID-001` decides on the verbatim `Canvas Artifact` string plus the no-save Canvas contract. A reply that could have come from either runtime is a `FAIL`. A failed handover does not stop its set: every scenario is still graded, and the failure is stated at the top of the run report, before any other result. A scenario whose precondition says its handover passed reads, in an automated run, as the handover having run first in its own session. Its verdict gates nothing.

### No-feature-catalog exception

This skill has no canonical feature catalog. Scenario files link directly to current skill, reference, asset, Custom Instructions and knowledge sources. Section 20 is the source cross-reference.

---

## 2. GLOBAL PRECONDITIONS

1. Work only in a disposable copy of `AI Systems/Prompt Improver/` for skill-set scenarios.
2. For project-set scenarios, configure a claude.ai Project with `Custom Instructions.md` pasted and the full `knowledge/` set attached, and capture proof of that configuration.
3. Record the `export/` baseline before each skill scenario and the Artifact panel state before each project scenario.
4. Use a fresh session per ID and keep follow-up turns inside that same ID and session.
5. Run `SID-001` before any other skill-set ID and `PID-001` before any other project-set ID.
6. Do not use production credentials, private partner data or live publishing access.
7. Remove only scenario-created files after evidence capture.

### Side-effect ledger

| Turn | Files Before | Files After | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes/No with reason |

Question, clarification and refusal turns create no artifact in either runtime. Skill-set delivery turns may create only expected `export/[###] - enhanced-*` files. Project-set turns never create files and may only render a Canvas Artifact.

---

## 3. GLOBAL EVIDENCE REQUIREMENTS

- Sandbox, Project configuration and runtime-profile identifier
- Exact prompts and full response after every turn
- Per-turn state-retention notes
- Per-turn side-effect ledger for the skill set, Artifact panel state for the project set
- CLEAR, EVOKE or VISUAL score line with gate status when applicable
- Export readback for the skill set, Artifact excerpt plus attestation footer for the project set
- Final `PASS`, `FAIL` or justified `SKIP` with rationale

---

## 4. DETERMINISTIC COMMAND NOTATION

- `sandbox:` prepares or inspects the disposable project copy
- `project:` configures or inspects the claude.ai Project packaging
- `session:` starts or continues a runtime conversation
- `user:` submits the exact text shown for a turn
- `filesystem:` records and reads allowed artifacts on disk
- `artifact:` records and reads the Canvas Artifact panel
- `operator:` compares observed behavior with the contract
- `->` separates sequential steps

### Prompt synchronization gate

For every ID, the scenario-contract `Prompt`, the execution-table `Exact Prompt` and the root summary `Prompt` must match character for character. The `Real user request` field stays in natural human voice and is not compared with the command prompt.

---

## 5. REVIEW PROTOCOL AND RELEASE READINESS

### Scenario acceptance rules

A scenario passes only when the exact sequence ran, every turn matched expected behavior, prior facts remained intact, the ledger or panel contains only allowed changes and the returned delivery matches the contract for its runtime.

- `PASS`: every required check is true
- `FAIL`: any critical signal, state, artifact or safety boundary is wrong
- `SKIP`: a named sandbox or runtime blocker prevents execution and no safe deterministic fallback exists

### Defect severity

Not every wrong signal is the same kind of wrong. Record both the verdict and the severity that drove it.

**Blocking.** These reach the user as a false statement or a broken contract, so any one of them is a `FAIL`:

- Wrong-runtime delivery: a claimed saved or verified path in a project-set scenario, or a missing export file in a skill-set scenario
- An identity reply on `SID-001` or `PID-001` that could have come from either runtime
- The wrong scorer for the lane, such as CLEAR on an image prompt or VISUAL on a text prompt
- An invented requirement or scope expansion inside the enhanced prompt
- Content produced for a refused direct-work request, or any artifact created on a refusal turn
- A guessed mode after a command conflict or a no-signal request

**Advisory.** These are delivery-quality preferences. Record them, and let them fail a scenario only when the scenario exists to test delivery shape:

- Response ordering beyond the required Artifact-first or path-first shape
- Summary length inside the two to three sentence band
- Verbosity of the transparency report

### Release readiness rule

The package is releasable only when every indexed scenario has evidence, no scenario is `FAIL`, all critical scenarios are `PASS`, every `SKIP` carries a named blocker and owner approval and no blocking triage item remains. Documentation validation alone does not prove runtime readiness.

---

## 6. ORCHESTRATION AND WAVE PLANNING

| Wave | Scenarios | Isolation |
|---|---|---|
| 1 | `SID-001`, `PID-001` | One disposable copy and one configured Project, identity evidence first |
| 2 | `SIR-001`, `SIR-002`, `PIR-001`, `PIR-002` | Fresh session per ID, artifact-free until the user answers |
| 3 | `STX-001`, `PTX-001`, `SFM-001`, `PFM-001` | Separate export baselines and separate Project conversations |
| 4 | `SCR-001`, `PCR-001` | Creative-mode conversations with scorer and follow-up capture |
| 5 | `SSB-001`, `PSB-001` | Artifact-free refusal sandboxes and panels |

One coordinator owns exact prompts, isolation, ledgers and final verdicts. Workers may execute independent IDs in separate sandboxes or separate Project conversations.

---

## 7. SKILL IDENTITY (`SID-001`)

### SID-001 | Identity handover and file delivery

#### Description

Verify a real export path the skill runtime wrote, with the identity phrase as support.

#### Scenario contract

Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`

Desired user-visible outcome: An identity answer plus a path-first delivery only the skill runtime can produce.

#### Test execution

> **Feature File:** [SID-001](skill-identity/identity-handover.md)

---

## 8. SKILL INTERACTIVE ROUTING (`SIR-001..SIR-002`)

### SIR-001 | Conflicting mode commands ask one question

#### Description

Verify conflict detection asks which mode instead of picking one.

#### Scenario contract

Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`

Desired user-visible outcome: One question followed by a Short-mode delivery that honors the user's pick.

#### Test execution

> **Feature File:** [SIR-001](skill-interactive-routing/conflicting-commands-clarification.md)

### SIR-002 | No-signal request gets one comprehensive question

#### Description

Verify the zero-signal request routes to one question and a wait.

#### Scenario contract

Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`

Desired user-visible outcome: One question followed by a delivery built only on what the user supplied.

#### Test execution

> **Feature File:** [SIR-002](skill-interactive-routing/no-signal-comprehensive-question.md)

---

## 9. SKILL TEXT MODES (`STX-001`)

### STX-001 | Natural-language improve with CLEAR and export

#### Description

Verify plain-word improve delivers a gated markdown export.

#### Scenario contract

Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

Desired user-visible outcome: One path-first reply whose saved file reads back as a better version of the supplied prompt.

#### Test execution

> **Feature File:** [STX-001](skill-text-modes/improve-flow-clear-export.md)

---

## 10. SKILL FORMAT MODES (`SFM-001`)

### SFM-001 | Independent $json format lock

#### Description

Verify format axis locks JSON while Improve binds mode.

#### Scenario contract

Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

Desired user-visible outcome: One path-first reply whose saved `.json` file parses cleanly and carries only the locked-format payload.

#### Test execution

> **Feature File:** [SFM-001](skill-format-modes/json-format-lock-export.md)

---

## 11. SKILL CREATIVE MODES (`SCR-001`)

### SCR-001 | Image mode VISUAL gate and follow-up

#### Description

Verify the image lane scores VISUAL and invites share-back.

#### Scenario contract

Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

Desired user-visible outcome: One path-first reply carrying the VISUAL score and the share-back invitation.

#### Test execution

> **Feature File:** [SCR-001](skill-creative-modes/image-mode-visual-export.md)

---

## 12. SKILL SAFETY BOUNDARIES (`SSB-001`)

### SSB-001 | Direct content request reframed then refused

#### Description

Verify reframe once then persistent refusal with no artifact.

#### Scenario contract

Prompt: `Write the actual launch announcement email for my app. I need the email itself, not a prompt.`

Desired user-visible outcome: A short reframe offer followed by a short refusal, both inside prompt-only scope.

#### Test execution

> **Feature File:** [SSB-001](skill-safety-boundaries/non-prompt-scope-refusal.md)

---

## 13. PROJECT IDENTITY (`PID-001`)

### PID-001 | Identity handover and Canvas delivery

#### Description

Verify the Project-only identity string plus Canvas Artifact delivery.

#### Scenario contract

Prompt: `Who are you and how do you deliver the finished prompt? Also improve this one: "Write a welcome email for new gym members that mentions the free trial week and the class schedule, friendly and under 120 words".`

Desired user-visible outcome: An identity answer plus a Canvas-first delivery only the Project runtime can produce.

#### Test execution

> **Feature File:** [PID-001](project-identity/identity-handover.md)

---

## 14. PROJECT INTERACTIVE ROUTING (`PIR-001..PIR-002`)

### PIR-001 | Conflicting mode commands ask one question

#### Description

Verify conflict detection asks which mode instead of picking one.

#### Scenario contract

Prompt: `$short $deep improve my prompt for a weekly meal-plan generator`

Desired user-visible outcome: One question followed by a Short-mode Canvas delivery that honors the user's pick.

#### Test execution

> **Feature File:** [PIR-001](project-interactive-routing/conflicting-commands-clarification.md)

### PIR-002 | No-signal request gets one comprehensive question

#### Description

Verify the zero-signal request routes to one question and a wait.

#### Scenario contract

Prompt: `Hey, I could use a hand with a draft I have been stuck on all week.`

Desired user-visible outcome: One question followed by a Canvas delivery built only on what the user supplied.

#### Test execution

> **Feature File:** [PIR-002](project-interactive-routing/no-signal-comprehensive-question.md)

---

## 15. PROJECT TEXT MODES (`PTX-001`)

### PTX-001 | Natural-language improve with CLEAR and Canvas

#### Description

Verify plain-word improve delivers a gated Canvas Artifact.

#### Scenario contract

Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

Desired user-visible outcome: One Artifact-first reply whose block reads back as a better version of the supplied prompt and whose chat claims no file was written.

#### Test execution

> **Feature File:** [PTX-001](project-text-modes/improve-flow-clear-canvas.md)

---

## 16. PROJECT FORMAT MODES (`PFM-001`)

### PFM-001 | Independent $json format lock in the Project

#### Description

Verify format axis locks JSON while Improve binds mode.

#### Scenario contract

Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

Desired user-visible outcome: One Artifact-first reply whose payload between the metadata lines parses cleanly and whose chat claims no file was written.

#### Test execution

> **Feature File:** [PFM-001](project-format-modes/json-format-lock-canvas.md)

---

## 17. PROJECT CREATIVE MODES (`PCR-001`)

### PCR-001 | Image mode VISUAL gate and follow-up in the Project

#### Description

Verify the image lane scores VISUAL and invites share-back.

#### Scenario contract

Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

Desired user-visible outcome: One Artifact-first reply carrying the VISUAL score and the share-back invitation with no file claimed.

#### Test execution

> **Feature File:** [PCR-001](project-creative-modes/image-mode-visual-canvas.md)

---

## 18. PROJECT SAFETY BOUNDARIES (`PSB-001`)

### PSB-001 | Direct content request reframed then refused in the Project

#### Description

Verify reframe once then persistent refusal with no Artifact.

#### Scenario contract

Prompt: `Write the actual launch announcement email for my app. I need the email itself, not a prompt.`

Desired user-visible outcome: A short reframe offer followed by a short refusal, both inside prompt-only scope.

#### Test execution

> **Feature File:** [PSB-001](project-safety-boundaries/non-prompt-scope-refusal.md)

---

## 19. AUTOMATED VALIDATION CROSS-REFERENCE

| Check | Coverage | Playbook overlap |
|---|---|---|
| [Router oracle and fixtures](../../benchmark/router/) | Command, semantic and fallback lane decisions | `SIR-001`, `SIR-002`, `PIR-001`, `PIR-002` |
| [Parity benchmark](../../benchmark/parity/) | Skill and Project behavior comparison | All fourteen scenarios |
| Operator-contract validator | Package structure, prompts, tables, turns and links | All fourteen scenarios and this root |
| Shared document validator | Markdown structure of root and scenario files | All package Markdown |
| Real manual execution | Runtime behavior, deliveries and side effects | `SID-001..SSB-001`, `PID-001..PSB-001` |

---

## 20. SOURCE CROSS-REFERENCE INDEX

| Feature ID | Feature name | Category | Feature file | Primary source |
|---|---|---|---|---|
| SID-001 | Identity handover and file delivery | Skill identity | [SID-001](skill-identity/identity-handover.md) | [`AGENTS.md`](../../AGENTS.md) |
| SIR-001 | Conflicting mode commands ask one question | Skill interactive routing | [SIR-001](skill-interactive-routing/conflicting-commands-clarification.md) | [`SKILL.md`](../SKILL.md) |
| SIR-002 | No-signal request gets one comprehensive question | Skill interactive routing | [SIR-002](skill-interactive-routing/no-signal-comprehensive-question.md) | [`interactive-mode.md`](../references/interactive-mode.md) |
| STX-001 | Natural-language improve with CLEAR and export | Skill text modes | [STX-001](skill-text-modes/improve-flow-clear-export.md) | [`SKILL.md`](../SKILL.md) |
| SFM-001 | Independent $json format lock | Skill format modes | [SFM-001](skill-format-modes/json-format-lock-export.md) | [`format-guide-json.md`](../assets/format-guide-json.md) |
| SCR-001 | Image mode VISUAL gate and follow-up | Skill creative modes | [SCR-001](skill-creative-modes/image-mode-visual-export.md) | [`image-mode.md`](../references/image-mode.md) |
| SSB-001 | Direct content request reframed then refused | Skill safety boundaries | [SSB-001](skill-safety-boundaries/non-prompt-scope-refusal.md) | [`AGENTS.md`](../../AGENTS.md) |
| PID-001 | Identity handover and Canvas delivery | Project identity | [PID-001](project-identity/identity-handover.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PIR-001 | Conflicting mode commands ask one question | Project interactive routing | [PIR-001](project-interactive-routing/conflicting-commands-clarification.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PIR-002 | No-signal request gets one comprehensive question | Project interactive routing | [PIR-002](project-interactive-routing/no-signal-comprehensive-question.md) | [Interactive Mode knowledge](<../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) |
| PTX-001 | Natural-language improve with CLEAR and Canvas | Project text modes | [PTX-001](project-text-modes/improve-flow-clear-canvas.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PFM-001 | Independent $json format lock in the Project | Project format modes | [PFM-001](project-format-modes/json-format-lock-canvas.md) | [Format Guide JSON knowledge](<../../claude project/knowledge/Prompt Improver - Format Guide JSON - v0.142.md>) |
| PCR-001 | Image mode VISUAL gate and follow-up in the Project | Project creative modes | [PCR-001](project-creative-modes/image-mode-visual-canvas.md) | [Image Mode knowledge](<../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) |
| PSB-001 | Direct content request reframed then refused in the Project | Project safety boundaries | [PSB-001](project-safety-boundaries/non-prompt-scope-refusal.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
