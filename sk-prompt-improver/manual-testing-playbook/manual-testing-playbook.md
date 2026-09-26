---
title: "Prompt Improver: Manual Testing Playbook"
description: "Operator-facing directory, execution policy and release-readiness guide for the two-runtime Prompt Improver scenario inventory."
version: 1.1.0.0
---

# Prompt Improver: Manual Testing Playbook

This package turns the Prompt Improver contract into thirty reproducible conversations split into two runtime sets. The skill set runs the system from `AGENTS.md` with `sk-prompt-improver/` loaded and proves export-first file delivery. The project set runs the same system from `claude project/Custom Instructions.md` with the knowledge documents attached and proves Canvas Artifact delivery with no file claim. The root owns shared policy and indexing. Each linked scenario file owns one synchronized Turn 1 prompt, a conversation chain of up to two user turns, one nine-field execution table and current source anchors.

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are recorded into `benchmark/reports/<dated-run-label>/`. Skill-set outcomes are persisted by the canonical scenario-persistence wrapper named in the skill's result persistence contract. Project-set outcomes are recorded by the operator in the same run folder. `skill-benchmark-report.md` and any `results.md` or `report.md` output stay renderer-owned and are never hand-authored.

---

## 1. OVERVIEW

The playbook holds thirty operator scenarios in two runtime sets across twelve category folders. No alternate or supplemental scenario files are part of the package.

### Coverage map

| Set | Category | IDs | Count | Primary surface |
|---|---|---|---:|---|
| Skill | Skill identity | `SID-001` | 1 | `AGENTS.md` identity string and export-first file delivery |
| Skill | Skill interactive routing | `SIR-001..SIR-002` | 2 | Command-conflict and no-signal question flow |
| Skill | Skill text modes | `STX-001..STX-005` | 5 | Natural improve, `$deep`, `$short`, `$refine` and `$raw` lanes, CLEAR gate or no scorer, markdown export and revision |
| Skill | Skill format modes | `SFM-001..SFM-003` | 3 | Independent `$json`, `$yaml` and `$markdown` axis, valid locked-format export |
| Skill | Skill creative modes | `SCR-001..SCR-003` | 3 | `$image` FRAME, `$video` MOTION and `$vibe` VIBE, VISUAL and EVOKE gates, share-back invite |
| Skill | Skill safety boundaries | `SSB-001` | 1 | Reframe once, then persistent refusal |
| Project | Project identity | `PID-001` | 1 | `Custom Instructions` identity string and Canvas Artifact delivery |
| Project | Project interactive routing | `PIR-001..PIR-002` | 2 | Command-conflict and no-signal question flow |
| Project | Project text modes | `PTX-001..PTX-005` | 5 | Natural improve, `$deep`, `$short`, `$refine` and `$raw` lanes, CLEAR gate or no scorer, Canvas Artifact and revision |
| Project | Project format modes | `PFM-001..PFM-003` | 3 | Independent `$json`, `$yaml` and `$markdown` axis, locked-format Deliverable Block |
| Project | Project creative modes | `PCR-001..PCR-003` | 3 | `$image` FRAME, `$video` MOTION and `$vibe` VIBE, VISUAL and EVOKE gates, share-back invite |
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
| 3 | `STX-001..STX-005`, `PTX-001..PTX-005`, `SFM-001..SFM-003`, `PFM-001..PFM-003` | Separate export baselines and separate Project conversations |
| 4 | `SCR-001..SCR-003`, `PCR-001..PCR-003` | Creative-mode conversations with scorer and follow-up capture |
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

Desired user-visible outcome: One consolidated question followed by a Short-mode delivery that honors the user's pick.

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

## 9. SKILL TEXT MODES (`STX-001..STX-005`)

### STX-001 | Natural-language improve with CLEAR and export

#### Description

Verify plain-word improve delivers a gated markdown export.

#### Scenario contract

Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

Desired user-visible outcome: One path-first reply whose saved file reads back as a better version of the supplied prompt.

#### Test execution

> **Feature File:** [STX-001](skill-text-modes/improve-flow-clear-export.md)

### STX-002 | Deep mode system prompt with CLEAR and export

#### Description

Verify `$deep` keeps every supplied fact and saves the revision as a new export.

#### Scenario contract

Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`

Desired user-visible outcome: One path-first reply whose saved file reads back as a full triage system prompt with every supplied fact intact, then a second export carrying the language rule.

#### Test execution

> **Feature File:** [STX-002](skill-text-modes/deep-system-prompt-clear-export.md)

### STX-003 | Short mode quick enhancement with CLEAR and export

#### Description

Verify `$short` keeps every supplied fact at Quick energy and invents none.

#### Scenario contract

Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`

Desired user-visible outcome: One path-first reply whose saved file reads back as a lean LinkedIn post prompt with the name, date and tone intact, then a second export that adds Spotify.

#### Test execution

> **Feature File:** [STX-003](skill-text-modes/short-quick-enhancement-export.md)

### STX-004 | Refine mode on an existing prompt with CLEAR and export

#### Description

Verify `$refine` repairs the supplied prompt toward the user's complaint.

#### Scenario contract

Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`

Desired user-visible outcome: One path-first reply whose saved file reads back as the user's prompt repaired, not replaced, then a second export with a one-sentence call to action.

#### Test execution

> **Feature File:** [STX-004](skill-text-modes/refine-existing-prompt-export.md)

### STX-005 | Raw mode cleanup without scoring and export

#### Description

Verify `$raw` exports at once with no question and no score.

#### Scenario contract

Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`

Desired user-visible outcome: One immediate path-first reply with no score, whose saved file reads back as the user's instruction cleaned up, then a second export that ends with the three worst-selling products.

#### Test execution

> **Feature File:** [STX-005](skill-text-modes/raw-cleanup-no-scoring-export.md)

---

## 10. SKILL FORMAT MODES (`SFM-001..SFM-003`)

### SFM-001 | Independent $json format lock

#### Description

Verify format axis locks JSON while Improve binds mode.

#### Scenario contract

Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

Desired user-visible outcome: One path-first reply whose saved `.json` file carries the required header and a payload below it that parses cleanly.

#### Test execution

> **Feature File:** [SFM-001](skill-format-modes/json-format-lock-export.md)

### SFM-002 | Independent $yaml format lock with Text mode

#### Description

Verify format axis locks YAML while Text binds mode.

#### Scenario contract

Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`

Desired user-visible outcome: One path-first reply whose saved `.yaml` file carries the header and a parsing payload with exactly the requested fields, then a second `.yaml` export that adds the VAT breakdown.

#### Test execution

> **Feature File:** [SFM-002](skill-format-modes/yaml-format-lock-export.md)

### SFM-003 | Independent $markdown format lock with Improve mode

#### Description

Verify the explicit `$markdown` token locks format while Improve binds mode.

#### Scenario contract

Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`

Desired user-visible outcome: One path-first reply whose saved `.md` file reads back as a senior-reviewer code review prompt scoped to the three named checks, then a second export that adds TODO flagging.

#### Test execution

> **Feature File:** [SFM-003](skill-format-modes/markdown-format-lock-export.md)

---

## 11. SKILL CREATIVE MODES (`SCR-001..SCR-003`)

### SCR-001 | Image mode VISUAL gate and follow-up

#### Description

Verify the image lane scores VISUAL and invites share-back.

#### Scenario contract

Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

Desired user-visible outcome: One path-first reply carrying the VISUAL score and the share-back invitation.

#### Test execution

> **Feature File:** [SCR-001](skill-creative-modes/image-mode-visual-export.md)

### SCR-002 | Video mode VISUAL gate with YAML lock and follow-up

#### Description

Verify the video lane scores VISUAL with explicit motion in a YAML export.

#### Scenario contract

Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`

Desired user-visible outcome: One path-first reply carrying the VISUAL score, the overhead note and the share-back invitation, whose saved `.yaml` file parses and keeps every shot fact, then a second `.yaml` export at 6 seconds ending on a slow push-in.

#### Test execution

> **Feature File:** [SCR-002](skill-creative-modes/video-mode-visual-export.md)

### SCR-003 | Vibe mode EVOKE gate and follow-up

#### Description

Verify the visual UI lane asks its library question and scores EVOKE.

#### Scenario contract

Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`

Desired user-visible outcome: One path-first reply carrying the EVOKE score and the share-back invitation, whose saved brief keeps the owner's morning, her three checks and the feel she asked for.

#### Test execution

> **Feature File:** [SCR-003](skill-creative-modes/vibe-mode-evoke-export.md)

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

Desired user-visible outcome: One consolidated question followed by a Short-mode Canvas delivery that honors the user's pick.

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

## 15. PROJECT TEXT MODES (`PTX-001..PTX-005`)

### PTX-001 | Natural-language improve with CLEAR and Canvas

#### Description

Verify plain-word improve delivers a gated Canvas Artifact.

#### Scenario contract

Prompt: `Here is my rough prompt: "Write a blog post about coffee brewing for beginners." Can you make it better?`

Desired user-visible outcome: One Artifact-first reply whose block reads back as a better version of the supplied prompt and whose chat claims no file was written.

#### Test execution

> **Feature File:** [PTX-001](project-text-modes/improve-flow-clear-canvas.md)

### PTX-002 | Deep mode system prompt with CLEAR and Canvas

#### Description

Verify `$deep` keeps every supplied fact and renders the revision as a new block.

#### Scenario contract

Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`

Desired user-visible outcome: One Artifact-first reply whose block reads back as a full triage system prompt with every supplied fact intact and whose chat claims no file was written, then a second block carrying the language rule.

#### Test execution

> **Feature File:** [PTX-002](project-text-modes/deep-system-prompt-clear-canvas.md)

### PTX-003 | Short mode quick enhancement with CLEAR and Canvas

#### Description

Verify `$short` keeps every supplied fact at Quick energy and invents none.

#### Scenario contract

Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`

Desired user-visible outcome: One Artifact-first reply whose block reads back as a lean LinkedIn post prompt with the name, date and tone intact and whose chat claims no file was written, then a second block that adds Spotify.

#### Test execution

> **Feature File:** [PTX-003](project-text-modes/short-quick-enhancement-canvas.md)

### PTX-004 | Refine mode on an existing prompt with CLEAR and Canvas

#### Description

Verify `$refine` repairs the supplied prompt toward the user's complaint.

#### Scenario contract

Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`

Desired user-visible outcome: One Artifact-first reply whose block reads back as the user's prompt repaired, not replaced, and whose chat claims no file was written, then a second block with a one-sentence call to action.

#### Test execution

> **Feature File:** [PTX-004](project-text-modes/refine-existing-prompt-canvas.md)

### PTX-005 | Raw mode cleanup without scoring and Canvas

#### Description

Verify `$raw` renders a block at once with no question and no score.

#### Scenario contract

Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`

Desired user-visible outcome: One immediate Artifact-first reply with no score, whose block reads back as the user's instruction cleaned up and whose chat claims no file was written, then a second block that ends with the three worst-selling products.

#### Test execution

> **Feature File:** [PTX-005](project-text-modes/raw-cleanup-no-scoring-canvas.md)

---

## 16. PROJECT FORMAT MODES (`PFM-001..PFM-003`)

### PFM-001 | Independent $json format lock in the Project

#### Description

Verify format axis locks JSON while Improve binds mode.

#### Scenario contract

Prompt: `$improve $json Improve this and return it as JSON: "Summarize a meeting transcript into action items with owners and due dates".`

Desired user-visible outcome: One Artifact-first reply whose payload between the metadata lines parses cleanly and whose chat claims no file was written.

#### Test execution

> **Feature File:** [PFM-001](project-format-modes/json-format-lock-canvas.md)

### PFM-002 | Independent $yaml format lock with Text mode in the Project

#### Description

Verify format axis locks YAML while Text binds mode.

#### Scenario contract

Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`

Desired user-visible outcome: One Artifact-first reply whose payload between the metadata lines parses cleanly with exactly the requested fields and whose chat claims no file was written, then a second block that adds the VAT breakdown.

#### Test execution

> **Feature File:** [PFM-002](project-format-modes/yaml-format-lock-canvas.md)

### PFM-003 | Independent $markdown format lock with Improve mode in the Project

#### Description

Verify the explicit `$markdown` token locks format while Improve binds mode.

#### Scenario contract

Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`

Desired user-visible outcome: One Artifact-first reply whose block reads back as a senior-reviewer code review prompt scoped to the three named checks and whose chat claims no file was written, then a second block that adds TODO flagging.

#### Test execution

> **Feature File:** [PFM-003](project-format-modes/markdown-format-lock-canvas.md)

---

## 17. PROJECT CREATIVE MODES (`PCR-001..PCR-003`)

### PCR-001 | Image mode VISUAL gate and follow-up in the Project

#### Description

Verify the image lane scores VISUAL and invites share-back.

#### Scenario contract

Prompt: `$image Build me a Midjourney prompt for a misty forest cabin at dawn with cinematic light.`

Desired user-visible outcome: One Artifact-first reply carrying the VISUAL score and the share-back invitation with no file claimed.

#### Test execution

> **Feature File:** [PCR-001](project-creative-modes/image-mode-visual-canvas.md)

### PCR-002 | Video mode VISUAL gate with YAML lock and follow-up in the Project

#### Description

Verify the video lane scores VISUAL with explicit motion in a YAML block.

#### Scenario contract

Prompt: `$video $yaml 8 second product shot for Veo: our new matte black insulated water bottle on a wet rock beside a mountain stream, slow orbit, soft morning light, condensation drops, ending on the logo side of the bottle. No people, no text on screen.`

Desired user-visible outcome: One Artifact-first reply carrying the VISUAL score, the overhead note and the share-back invitation with no file claimed, whose YAML payload parses and keeps every shot fact, then a second block at 6 seconds ending on a slow push-in.

#### Test execution

> **Feature File:** [PCR-002](project-creative-modes/video-mode-visual-canvas.md)

### PCR-003 | Vibe mode EVOKE gate and follow-up in the Project

#### Description

Verify the visual UI lane asks its library question and scores EVOKE.

#### Scenario contract

Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`

Desired user-visible outcome: One Artifact-first reply carrying the EVOKE score and the share-back invitation with no file claimed, whose brief keeps the owner's morning, her three checks and the feel she asked for.

#### Test execution

> **Feature File:** [PCR-003](project-creative-modes/vibe-mode-evoke-canvas.md)

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
| [Parity benchmark](../../benchmark/parity/) | Skill and Project behavior comparison | All thirty scenarios |
| Operator-contract validator | Package structure, prompts, tables, turns and links | All thirty scenarios and this root |
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
| STX-002 | Deep mode system prompt with CLEAR and export | Skill text modes | [STX-002](skill-text-modes/deep-system-prompt-clear-export.md) | [`depth-framework.md`](../references/depth-framework.md) |
| STX-003 | Short mode quick enhancement with CLEAR and export | Skill text modes | [STX-003](skill-text-modes/short-quick-enhancement-export.md) | [`SKILL.md`](../SKILL.md) |
| STX-004 | Refine mode on an existing prompt with CLEAR and export | Skill text modes | [STX-004](skill-text-modes/refine-existing-prompt-export.md) | [`patterns-evaluation.md`](../references/patterns-evaluation.md) |
| STX-005 | Raw mode cleanup without scoring and export | Skill text modes | [STX-005](skill-text-modes/raw-cleanup-no-scoring-export.md) | [`SKILL.md`](../SKILL.md) |
| SFM-001 | Independent $json format lock | Skill format modes | [SFM-001](skill-format-modes/json-format-lock-export.md) | [`format-guide-json.md`](../assets/format-guide-json.md) |
| SFM-002 | Independent $yaml format lock with Text mode | Skill format modes | [SFM-002](skill-format-modes/yaml-format-lock-export.md) | [`format-guide-yaml.md`](../assets/format-guide-yaml.md) |
| SFM-003 | Independent $markdown format lock with Improve mode | Skill format modes | [SFM-003](skill-format-modes/markdown-format-lock-export.md) | [`format-guide-markdown.md`](../assets/format-guide-markdown.md) |
| SCR-001 | Image mode VISUAL gate and follow-up | Skill creative modes | [SCR-001](skill-creative-modes/image-mode-visual-export.md) | [`image-mode.md`](../references/image-mode.md) |
| SCR-002 | Video mode VISUAL gate with YAML lock and follow-up | Skill creative modes | [SCR-002](skill-creative-modes/video-mode-visual-export.md) | [`video-mode.md`](../references/video-mode.md) |
| SCR-003 | Vibe mode EVOKE gate and follow-up | Skill creative modes | [SCR-003](skill-creative-modes/vibe-mode-evoke-export.md) | [`visual-mode.md`](../references/visual-mode.md) |
| SSB-001 | Direct content request reframed then refused | Skill safety boundaries | [SSB-001](skill-safety-boundaries/non-prompt-scope-refusal.md) | [`AGENTS.md`](../../AGENTS.md) |
| PID-001 | Identity handover and Canvas delivery | Project identity | [PID-001](project-identity/identity-handover.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PIR-001 | Conflicting mode commands ask one question | Project interactive routing | [PIR-001](project-interactive-routing/conflicting-commands-clarification.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PIR-002 | No-signal request gets one comprehensive question | Project interactive routing | [PIR-002](project-interactive-routing/no-signal-comprehensive-question.md) | [Interactive Mode knowledge](<../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) |
| PTX-001 | Natural-language improve with CLEAR and Canvas | Project text modes | [PTX-001](project-text-modes/improve-flow-clear-canvas.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PTX-002 | Deep mode system prompt with CLEAR and Canvas | Project text modes | [PTX-002](project-text-modes/deep-system-prompt-clear-canvas.md) | [DEPTH knowledge](<../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) |
| PTX-003 | Short mode quick enhancement with CLEAR and Canvas | Project text modes | [PTX-003](project-text-modes/short-quick-enhancement-canvas.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PTX-004 | Refine mode on an existing prompt with CLEAR and Canvas | Project text modes | [PTX-004](project-text-modes/refine-existing-prompt-canvas.md) | [Patterns and Evaluation knowledge](<../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) |
| PTX-005 | Raw mode cleanup without scoring and Canvas | Project text modes | [PTX-005](project-text-modes/raw-cleanup-no-scoring-canvas.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
| PFM-001 | Independent $json format lock in the Project | Project format modes | [PFM-001](project-format-modes/json-format-lock-canvas.md) | [Format Guide JSON knowledge](<../../claude project/knowledge/Prompt Improver - Format Guide JSON - v0.142.md>) |
| PFM-002 | Independent $yaml format lock with Text mode in the Project | Project format modes | [PFM-002](project-format-modes/yaml-format-lock-canvas.md) | [Format Guide YAML knowledge](<../../claude project/knowledge/Prompt Improver - Format Guide YAML - v0.142.md>) |
| PFM-003 | Independent $markdown format lock with Improve mode in the Project | Project format modes | [PFM-003](project-format-modes/markdown-format-lock-canvas.md) | [Format Guide Markdown knowledge](<../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) |
| PCR-001 | Image mode VISUAL gate and follow-up in the Project | Project creative modes | [PCR-001](project-creative-modes/image-mode-visual-canvas.md) | [Image Mode knowledge](<../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) |
| PCR-002 | Video mode VISUAL gate with YAML lock and follow-up in the Project | Project creative modes | [PCR-002](project-creative-modes/video-mode-visual-canvas.md) | [Video Mode knowledge](<../../claude project/knowledge/Prompt Improver - Video Mode - v0.123.md>) |
| PCR-003 | Vibe mode EVOKE gate and follow-up in the Project | Project creative modes | [PCR-003](project-creative-modes/vibe-mode-evoke-canvas.md) | [Visual Mode knowledge](<../../claude project/knowledge/Prompt Improver - Visual Mode - v0.301.md>) |
| PSB-001 | Direct content request reframed then refused in the Project | Project safety boundaries | [PSB-001](project-safety-boundaries/non-prompt-scope-refusal.md) | [Custom Instructions](<../../claude project/Custom Instructions.md>) |
