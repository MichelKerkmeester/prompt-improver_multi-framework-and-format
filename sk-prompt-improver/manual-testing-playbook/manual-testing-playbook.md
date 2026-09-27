---
title: "Prompt Improver: Manual Testing Playbook"
description: "Operator-facing directory, execution policy and release-readiness guide for the two-runtime Prompt Improver scenario inventory."
version: 1.5.0.0
---

# Prompt Improver: Manual Testing Playbook

This package turns the Prompt Improver contract into seventy-eight reproducible conversations split into two runtime sets. The skill set runs the system from `AGENTS.md` with `sk-prompt-improver/` loaded and proves export-first file delivery. The project set runs the same system from `claude project/Custom Instructions.md` with the knowledge documents attached and proves Canvas Artifact delivery with no file claim. The root owns shared policy and indexing. Each linked scenario file owns one synchronized Turn 1 prompt, either a conversation chain of up to two user turns or a single prompt with no chain, one nine-field execution table and current source anchors.

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are recorded into `benchmark/reports/<dated-run-label>/`. Skill-set outcomes are persisted by the canonical scenario-persistence wrapper named in the skill's result persistence contract. Project-set outcomes are recorded by the operator in the same run folder. `skill-benchmark-report.md` and any `results.md` or `report.md` output stay renderer-owned and are never hand-authored.

---

## 1. OVERVIEW

The playbook holds seventy-eight operator scenarios in two runtime sets across fourteen category folders. No alternate or supplemental scenario files are part of the package.

### Coverage map

| Set | Category | IDs | Count | Primary surface |
|---|---|---|---:|---|
| Skill | Skill identity | `SID-001` | 1 | `AGENTS.md` identity string and export-first file delivery |
| Skill | Skill interactive routing | `SIR-001..SIR-002` | 2 | Command-conflict and no-signal question flow |
| Skill | Skill text modes | `STX-001..STX-005` | 5 | Natural improve, `$deep`, `$short`, `$refine` and `$raw` lanes, CLEAR gate or no scorer, markdown export and revision |
| Skill | Skill format modes | `SFM-001..SFM-003` | 3 | Independent `$json`, `$yaml` and `$markdown` axis, valid locked-format export |
| Skill | Skill creative modes | `SCR-001..SCR-003` | 3 | `$image` FRAME, `$video` MOTION and `$vibe` VIBE, VISUAL and EVOKE gates, share-back invite |
| Skill | Skill safety boundaries | `SSB-001` | 1 | Reframe once, then persistent refusal |
| Skill | Skill framework coverage | `SFW-001..SFW-024` | 24 | One named framework per prompt at the Low, Medium, High or Complex tier: RCAF, COSTAR, CIDI, TIDD-EC, CRISPE, CRAFT, FRAME, MOTION, VIBE and VIBE-MP, single-turn export |
| Project | Project identity | `PID-001` | 1 | `Custom Instructions` identity string and Canvas Artifact delivery |
| Project | Project interactive routing | `PIR-001..PIR-002` | 2 | Command-conflict and no-signal question flow |
| Project | Project text modes | `PTX-001..PTX-005` | 5 | Natural improve, `$deep`, `$short`, `$refine` and `$raw` lanes, CLEAR gate or no scorer, Canvas Artifact and revision |
| Project | Project format modes | `PFM-001..PFM-003` | 3 | Independent `$json`, `$yaml` and `$markdown` axis, locked-format Deliverable Block |
| Project | Project creative modes | `PCR-001..PCR-003` | 3 | `$image` FRAME, `$video` MOTION and `$vibe` VIBE, VISUAL and EVOKE gates, share-back invite |
| Project | Project safety boundaries | `PSB-001` | 1 | Reframe once, then persistent refusal |
| Project | Project framework coverage | `PFW-001..PFW-024` | 24 | The `SFW` prompts, character for character, single-turn Deliverable Block |

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

### Framework coverage

Forty-eight scenarios test whether the system writes a prompt that visibly uses one framework from its own library, at the complexity the rubric gives its input. Each of the twenty-four `SFW` skill scenarios has a `PFW` Project twin with the same prompt, character for character. Every prompt names its framework, carries every essential and asks the runtime not to ask, so these scenarios have a single prompt and no conversation chain: the one reply is the graded delivery, and a question instead of a delivery fails for missing delivery.

A framework scenario passes only when all of these hold: the delivery exists in its runtime's form, the header names the framework and a complexity inside the tier, the body is visibly organised by the framework's named elements, the routed scorer passes its gate, a JSON or YAML payload parses, every supplied fact is kept and the scope test holds. VIBE and VIBE-MP carry their elements labelled or as prose, since `references/visual-mode.md` line 62 asks a Visual prompt to flow as natural prose: a prose passage the operator can map to one element counts as that element.

| Tier | Complexity band | Header complexity that passes |
|---|---|---|
| Low | 1 to 4 | The label `Low`, or 1 to 4 |
| Medium | 5 to 6 | The label `Medium`, or 5 or 6 |
| High | 7 to 8 | The label `High`, or 7 or 8 |
| Complex | 9 to 10 | The label `Complex`, or 9 or 10, or another label above High such as `Very High`; a bare `High` label fails |

The bands are the skill's own, from the Complexity Rubric in `references/depth-framework.md` lines 147-165 and its Project twin in `Prompt Improver - DEPTH Thinking Framework - v0.200.md` lines 134-152.

RCAF, COSTAR, CIDI, TIDD-EC, CRISPE and CRAFT each run at Medium, High and Complex. The creative scenarios sit where the rubric places their input, because one image, clip or screen scores low on most of its dimensions: FRAME at Low and Medium, MOTION at Low twice, VIBE at Medium and VIBE-MP at High. Where the library ranks the named framework outside the tier, the prompt makes the user's case for it: a fit note from the runtime is recorded and never decides the verdict, while a delivery built on another framework fails.

### No-feature-catalog exception

This skill has no canonical feature catalog. Scenario files link directly to current skill, reference, asset, Custom Instructions and knowledge sources. Section 22 is the source cross-reference.

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
- A missing `---` divider between the header and the prompt, which the six format-lock scenarios test directly
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
| 6 | `SFW-001..SFW-024`, `PFW-001..PFW-024` | Fresh session per ID, single-turn framework deliveries with separate export baselines and separate Project conversations |

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

Desired user-visible outcome: One path-first reply whose saved `.json` file carries the required header, the `---` divider and a payload below it that parses cleanly.

#### Test execution

> **Feature File:** [SFM-001](skill-format-modes/json-format-lock-export.md)

### SFM-002 | Independent $yaml format lock with Text mode

#### Description

Verify format axis locks YAML while Text binds mode.

#### Scenario contract

Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`

Desired user-visible outcome: One path-first reply whose saved `.yaml` file carries the header, the `---` divider and a parsing payload with exactly the requested fields, then a second `.yaml` export that adds the VAT breakdown.

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

## 19. SKILL FRAMEWORK COVERAGE (`SFW-001..SFW-024`)

### SFW-001 | RCAF at Medium complexity for a warehouse shift handover

#### Description

Verify `$text` delivers a Medium-tier RCAF prompt in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$text $markdown Improve this prompt we use in ChatGPT at our Rotterdam warehouse: "Summarise today's exceptions for the next shift." Every evening the day shift lead pastes the exception log (damaged pallets, short picks, late trucks, scanner faults), and the night lead reads the summary at the 22:00 handover. It should group exceptions by type, flag anything still open, give the dock door and pallet ID for each open item and stay under 200 words. No blame language, just facts. Structure it with RCAF. No questions, use your judgment on anything I left open.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming RCAF at Medium complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-001](skill-framework-coverage/rcaf-medium-warehouse-handover-export.md)

### SFW-002 | RCAF at High complexity for an expense claim review

#### Description

Verify `$improve` delivers a High-tier RCAF prompt in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$improve $json Our finance team calls this prompt through the Claude API from our expense tool: "Check this expense claim and say if it is fine." Make it much stronger. The model gets the claim lines, the receipts as text and the employee's grade. It sorts each line into within policy, missing receipt, over limit or not a business cost. Within policy gets a recommended approval, a missing receipt gets a receipt request, over limit goes to the finance controller, and a non-business cost goes back to the employee with the policy clause. Any line above EUR 750 goes to the controller whatever its class. Hotel limits are EUR 180 a night for grades 1 to 5 and EUR 240 above. It only recommends, never marks anything as paid, and always quotes the receipt line it relies on. Our prompt registry stores only the four RCAF keys, so keep it RCAF even for a prompt this size, and keep every rule rather than streamlining. No questions, use your judgment on the rest.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming RCAF at High complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, its payload parsing as JSON.

#### Test execution

> **Feature File:** [SFW-002](skill-framework-coverage/rcaf-high-expense-claim-review-export.md)

### SFW-003 | RCAF at Complex complexity for an incident postmortem

#### Description

Verify `$deep` delivers a Complex-tier RCAF prompt in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$deep $markdown I want a serious upgrade of our postmortem prompt, currently just "Write a postmortem from these notes." We give Claude a PagerDuty timeline, a Slack incident-channel export and the deploy log for one SEV1 or SEV2 incident. It must produce one blameless draft in three layers: a technical timeline for engineers, an impact summary for support leads and a five-sentence brief for the exec team. Timestamps arrive in both UTC and Amsterdam time, so it normalises everything to UTC and flags any gap over 10 minutes. It may only state a root cause the logs support and labels everything else as a hypothesis. Action items need an owner from the responders list and a due week. Customer names become account IDs. Our SRE prompt catalogue lints for the four RCAF sections, so use RCAF, layered per audience, not another framework. Keep everything, no streamlining, and skip the questions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming RCAF at Complex complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-003](skill-framework-coverage/rcaf-complex-incident-postmortem-export.md)

### SFW-004 | COSTAR at Medium complexity for a school parent newsletter

#### Description

Verify `$improve` delivers a Medium-tier COSTAR prompt in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$improve $markdown Please improve the prompt our primary school office uses in ChatGPT for the monthly parent newsletter: "Write a newsletter for parents about this month." The office pastes in the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes. Parents read it on their phones, and many speak Dutch as a second language, so it needs plain B1-level language, short paragraphs and a warm but not chatty tone. Event dates go in a list at the top. Keep it under 350 words and never name individual pupils. Use COSTAR for the structure. Don't ask me anything, just make sensible calls where I left gaps.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming COSTAR at Medium complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-004](skill-framework-coverage/costar-medium-school-newsletter-export.md)

### SFW-005 | COSTAR at High complexity for a hybrid-work announcement

#### Description

Verify `$text` delivers a High-tier COSTAR prompt in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$text $yaml We need a prompt for our HR assistant, GPT-4.1 on our intranet, that drafts the announcement of our new hybrid-work policy. Audience: 420 staff across the Utrecht and Ghent offices, from warehouse crew to engineers. From 1 March everyone is in the office on Tuesday and Thursday, team leads can grant two exceptions per person per quarter, and the travel allowance moves from per kilometre to a flat EUR 60 a month. The draft needs an announcement of about 300 words, a six-question FAQ and a two-line Slack teaser. Tone: direct and reassuring, never corporate spin, and it must not promise anything beyond the policy text. Build it with COSTAR and keep all three outputs. No questions please, fill gaps sensibly.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.yaml` file opens with a header naming COSTAR at High complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept, its payload parsing as YAML.

#### Test execution

> **Feature File:** [SFW-005](skill-framework-coverage/costar-high-hybrid-work-announcement-export.md)

### SFW-006 | COSTAR at Complex complexity for clinic outage messages

#### Description

Verify `$deep` delivers a Complex-tier COSTAR prompt in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$deep $markdown Rebuild our outage-communication prompt for Gemini 2.5 Pro; right now it is "Write a message to patients about the outage." We run 14 physiotherapy clinics. When our booking platform fails, the prompt takes the incident facts we paste and drafts three messages: an SMS to patients with appointments in the next 48 hours (max 300 characters), an email to all active patients and a phone script for front-desk staff. Each message in Dutch and English. Patients range from teenage athletes to people in their 80s, so plain B1-level language. Every message says what we know, what we do not know yet and when the next update comes. It never guesses at a cause, never mentions data exposure unless the facts say so, and always gives the direct clinic phone number. Formal but empathetic. Structure it with COSTAR, with an Audience and Response block per channel. Keep the full scope and don't ask me questions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming COSTAR at Complex complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-006](skill-framework-coverage/costar-complex-clinic-outage-messages-export.md)

### SFW-007 | CIDI at Medium complexity for a credit-note procedure

#### Description

Verify `$improve` delivers a Medium-tier CIDI prompt in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$improve $yaml Improve our SOP-writing prompt for Claude: "Turn this into a how-to for the team." We paste a transcript of a senior clerk narrating a screen recording, and Claude writes a step-by-step procedure for new accounts-payable clerks on booking a supplier credit note against an open invoice. Each step needs one action, the screen or field it happens in and what the clerk should see afterwards. Steps that need a second approver, for credit notes above EUR 5,000, must be marked. Keep the clerk's field names exactly as spoken and leave out the chit-chat. The result goes into Confluence. Use CIDI. No questions, just use your judgment.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.yaml` file opens with a header naming CIDI at Medium complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as YAML.

#### Test execution

> **Feature File:** [SFW-007](skill-framework-coverage/cidi-medium-credit-note-procedure-export.md)

### SFW-008 | CIDI at High complexity for a developer setup guide

#### Description

Verify `$improve` delivers a High-tier CIDI prompt in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$improve $markdown Improve this onboarding prompt our platform team runs with Claude in Cursor: "Write a setup guide for new devs from this README." The input is our monorepo README, the Makefile and the CI config. The guide must take a new backend engineer from a fresh laptop to a green local test run in one afternoon. It needs separate paths for macOS and Ubuntu, a prerequisites list with exact versions taken from the files, a verification check after every stage and a troubleshooting section built only from errors the CI config or README mention. Commands are copied verbatim from the input, never invented. Secrets live in 1Password, so the guide says where to fetch them but never shows a value. Lay it out with CIDI and keep the whole scope. No questions, fill any gaps sensibly.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CIDI at High complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-008](skill-framework-coverage/cidi-high-developer-setup-guide-export.md)

### SFW-009 | CIDI at Complex complexity for a customs work instruction

#### Description

Verify `$deep` delivers a Complex-tier CIDI prompt in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$deep $json Our freight-forwarding team needs a far better prompt for work instructions; today it is "Document this process." GPT-4.1 gets three inputs: a call transcript with a senior customs broker, our current checklist and the carrier's dangerous-goods rules. It must write the work instruction for clearing inbound sea containers carrying lithium batteries at the port of Rotterdam. Steps are split by role (broker, planner, warehouse), and each has its trigger, the system it happens in, the document it produces and the hand-off. Where the transcript and the checklist disagree, it lists the conflict instead of choosing. Any shipment declared under UN3480 goes to the DG officer before the planner books a slot. Dutch and English versions with the same step numbers. The result feeds our knowledge-base importer, which maps CIDI sections to fields, so it has to be CIDI. Keep the full scope and don't ask questions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming CIDI at Complex complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as JSON.

#### Test execution

> **Feature File:** [SFW-009](skill-framework-coverage/cidi-complex-lithium-customs-instruction-export.md)

### SFW-010 | TIDD-EC at Medium complexity for a legal intake note

#### Description

Verify `$improve` delivers a Medium-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$improve $markdown Tighten this intake prompt for our employment-law firm: "Read the web form and summarise the case." Claude reads each web-form inquiry and writes an intake note for the lawyer who does the free 20-minute call. The note needs the client type (employee or employer), the issue (dismissal, contract, discrimination or pay), every date mentioned and the other party's name for our conflict check. It must never give legal advice or estimate chances, and it flags any dismissal older than two months, because the deadline may have passed. One good note: "Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag." Structure it with TIDD-EC. No questions, use your judgment on the rest.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming TIDD-EC at Medium complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-010](skill-framework-coverage/tidd-ec-medium-legal-intake-note-export.md)

### SFW-011 | TIDD-EC at High complexity for a health-claims checker

#### Description

Verify `$improve` delivers a High-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$improve $json Improve the compliance prompt behind the listing checker for our supplement brand's marketplace listings. Current version: "Check if this product text is OK." GPT-4.1 receives the title, description and bullet points of one listing, plus our approved list of 38 EU-authorised health claims with each call. It flags every health claim that is not on the list, and for each flag returns the exact sentence, the rule it breaks (unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts. It must not touch text that is already compliant and must not judge whether the product works. Worked example: "Boosts your immune system" is unauthorised, while "Vitamin C contributes to the normal function of the immune system" is approved. Use TIDD-EC and keep the full scope. No questions, decide the open points yourself.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.json` file opens with a header naming TIDD-EC at High complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept, its payload parsing as JSON.

#### Test execution

> **Feature File:** [SFW-011](skill-framework-coverage/tidd-ec-high-health-claims-checker-export.md)

### SFW-012 | TIDD-EC at Complex complexity for an AML alert narrative

#### Description

Verify `$deep` delivers a Complex-tier TIDD-EC prompt in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$deep $markdown Rebuild our AML alert-narrative prompt for Mistral Large; today it is just "Explain why this alert fired." The model gets one transaction-monitoring alert: the rule that fired, 90 days of transactions, the KYC profile and prior alerts. It writes the analyst's case narrative in our fixed order: trigger, customer profile, observed pattern, expected activity, open questions. Every claim cites a transaction ID. It never concludes that the customer is laundering money and never recommends filing or closing, which stays the analyst's call. Amounts keep their original currency with the EUR equivalent in brackets. It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days, and it handles joint accounts, missing KYC fields and accounts closed mid-window. Auditors liked this sentence: "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month." Use TIDD-EC, keep the full scope and don't ask me anything.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming TIDD-EC at Complex complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-012](skill-framework-coverage/tidd-ec-complex-aml-alert-narrative-export.md)

### SFW-013 | CRISPE at Medium complexity for oat milk positioning

#### Description

Verify `$improve` delivers a Medium-tier CRISPE prompt in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRISPE at Medium complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-013](skill-framework-coverage/crispe-medium-oat-milk-positioning-export.md)

### SFW-014 | CRISPE at High complexity for driver retention experiments

#### Description

Verify `$improve` delivers a High-tier CRISPE prompt in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$improve $yaml Improve this: "How do we keep our drivers?" We run 210 parcel-delivery drivers from four depots around Antwerp, and 38% left in the last 12 months, mostly within their first 90 days. Exit interviews point at route density, the 06:00 start and pay per stop. I want ChatGPT to act as a workforce strategist with last-mile experience, reason about why early-tenure drivers leave, then propose four distinct retention experiments that fit a EUR 120,000 yearly budget. Each experiment needs the hypothesis, the depot to pilot it in, the metric, a 10-week read-out point and the main risk to the delivery schedule. It should challenge our assumption that pay is the main lever. Build it with CRISPE and keep the full scope. No questions, fill in the gaps yourself.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.yaml` file opens with a header naming CRISPE at High complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, its payload parsing as YAML.

#### Test execution

> **Feature File:** [SFW-014](skill-framework-coverage/crispe-high-driver-retention-experiments-export.md)

### SFW-015 | CRISPE at Complex complexity for market expansion scenarios

#### Description

Verify `$deep` delivers a Complex-tier CRISPE prompt in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$deep $markdown Upgrade my strategy prompt, currently "Should we expand to Germany?" We sell site-diary software to construction firms: 640 customers in the Netherlands and Belgium, EUR 7.8M ARR and 4% monthly churn among firms under 20 staff. The board is split: the CEO wants Germany in 2027, the CFO wants to deepen in the Benelux mid-market first, and sales says German customers will need on-premise hosting. I want Gemini 2.5 Pro to act as a skeptical B2B SaaS strategist, surface the insight that decides this, state the question sharply, then run three scenario experiments (Germany first, Benelux first, a staged hybrid) with the assumptions each depends on, the cheapest test of them before Q2 and the signal that would kill it. It must say where our data is too thin to decide. I want exploration, not a plan, so structure it with CRISPE. Keep the full scope and don't ask questions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRISPE at Complex complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-015](skill-framework-coverage/crispe-complex-market-expansion-scenarios-export.md)

### SFW-016 | CRAFT at Medium complexity for a customer workshop plan

#### Description

Verify `$improve` delivers a Medium-tier CRAFT prompt in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$improve $markdown Improve this planning prompt: "Help me plan our customer workshop." We are a payroll software company hosting a one-day workshop in Utrecht on 12 November for 25 HR managers from existing customers, and I use ChatGPT to draft the run-of-show. It should cover the agenda from 09:30 to 16:00, two hands-on sessions on our new leave module, lunch and a closing Q&A, plus a short prep checklist for our two trainers. We judge success by an average session rating of at least 8 out of 10 and at least 10 sign-ups for the module pilot, so the prompt must keep those targets in view. Use CRAFT, since the Target part matters to us. No questions, use your judgment where I was vague.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRAFT at Medium complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-016](skill-framework-coverage/craft-medium-customer-workshop-plan-export.md)

### SFW-017 | CRAFT at High complexity for a mailbox migration plan

#### Description

Verify `$improve` delivers a High-tier CRAFT prompt in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$improve $markdown Our IT team asks Microsoft Copilot for migration plans with one line: "Plan the email migration." Turn it into a real prompt. Scope: move 1,150 user mailboxes and 60 shared mailboxes from an on-premise Exchange 2016 server to Microsoft 365 for a housing association with offices in Zwolle and Deventer. Cutover happens only at weekends, the customer-service mailbox may be offline for at most two hours, and 80 field staff use phones only. The plan needs phases with entry and exit criteria, a rollback step per phase, a staff communication moment before each phase and a risk table. Targets: zero lost mail, under 5% of users raising a ticket in the first week and done within six weekends. Structure it with CRAFT and keep the full scope. No questions, fill the gaps with sensible assumptions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRAFT at High complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-017](skill-framework-coverage/craft-high-mailbox-migration-plan-export.md)

### SFW-018 | CRAFT at Complex complexity for a WMS go-live plan

#### Description

Verify `$deep` delivers a Complex-tier CRAFT prompt in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`

Desired user-visible outcome: One path-first reply carrying a passing CLEAR result, whose saved `.md` file opens with a header naming CRAFT at Complex complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept.

#### Test execution

> **Feature File:** [SFW-018](skill-framework-coverage/craft-complex-wms-go-live-plan-export.md)

### SFW-019 | FRAME at Low complexity for a gravel cycling hero image

#### Description

Verify `$image` delivers a Low-tier FRAME prompt in one turn with every FRAME element labelled.

#### Scenario contract

Prompt: `$image $markdown Midjourney v6.1 prompt for the homepage hero of our Zeeland gravel-cycling tours: one rider on a gravel dyke path at golden hour, shot from a low angle, riding toward the camera with the Oosterschelde behind. Photorealistic, like an outdoor-apparel catalogue photo, warm light with long shadows. It is a 21:9 banner, so the left third stays calm and empty for our headline. The rider wears an olive jersey, and there are no visible logos, no text in the image and no other people. Organise it by FRAME so I can tweak each part, and keep every detail. No questions, pick sensible parameters yourself.`

Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.md` file opens with a header naming FRAME at Low complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-019](skill-framework-coverage/frame-low-gravel-cycling-hero-export.md)

### SFW-020 | FRAME at Medium complexity for a library science poster

#### Description

Verify `$image` delivers a Medium-tier FRAME prompt in one turn with every FRAME element labelled.

#### Scenario contract

Prompt: `$image $markdown We make event posters with Stable Diffusion XL in ComfyUI, which has a separate negative prompt field. I need a prompt for this year's Night of Science at the Leiden city library: a 2:3 portrait poster in a flat 1960s screen-print style, limited to four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper). Three depth layers: two children at a brass telescope in the foreground, the library's brick facade with lit windows in the middle, and Orion rising over the rooftops behind. The top quarter stays empty sky for the title we add later, so no lettering anywhere. Visible paper grain and slight ink misregistration. The children look about 8 to 10 and are not photoreal. Use weights where they help, give me the negative prompt separately and suggest CFG and steps. Build it with FRAME, keep all of it, no questions.`

Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.md` file opens with a header naming FRAME at Medium complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-020](skill-framework-coverage/frame-medium-library-science-poster-export.md)

### SFW-021 | MOTION at Low complexity for a potter wheel reel

#### Description

Verify `$video` delivers a Low-tier MOTION prompt in one turn with every MOTION element labelled.

#### Scenario contract

Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`

Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.md` file opens with a header naming MOTION at Low complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-021](skill-framework-coverage/motion-low-potter-wheel-reel-export.md)

### SFW-022 | MOTION at Low complexity for a flower auction opening shot

#### Description

Verify `$video` delivers a Low-tier MOTION prompt in one turn with every MOTION element labelled.

#### Scenario contract

Prompt: `$video $yaml Kling 2.6 prompt with native audio for the opening shot of a brand film about a flower auction near Aalsmeer. One continuous 10-second shot, 16:9, text-to-video. At dawn the camera glides forward about three metres above a hall full of trolley trains loaded with red and yellow tulips, the trains snaking past each other in two directions while three workers on electric tugs steer them. At 4 seconds the camera rises slowly to reveal the whole hall, and at 8 seconds it settles facing the big auction clock as its hand starts to sweep. Audio: electric hum, trolley wheels on concrete and a distant chime at the end, with no music and no voices. Cool blue daylight from the roof windows warms to gold by the end. The workers stay small and anonymous. Use MOTION, keep every beat and don't ask me questions.`

Desired user-visible outcome: One path-first reply carrying a passing VISUAL result, whose saved `.yaml` file opens with a header naming MOTION at Low complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-022](skill-framework-coverage/motion-low-flower-auction-opening-export.md)

### SFW-023 | VIBE at Medium complexity for a returns inspection screen

#### Description

Verify `$vibe` delivers a Medium-tier VIBE prompt in one turn with every VIBE element present, labelled or as prose.

#### Scenario contract

Prompt: `$vibe $markdown Screen concept for v0: the returns-inspection station in our fashion e-commerce warehouse. An inspector stands at a bench in cotton gloves, scans a returned item and has about 20 seconds to grade it A, B, C or reject on a 24-inch touchscreen. She needs the original order photo next to the item, the customer's return reason and a big tap target for each grade, and a reject asks for one damage photo. After 300 items a shift it must not feel like a spreadsheet or a dark developer tool: calm, tactile and fast. Use shadcn/ui components, so there is nothing to ask me. Shape the brief with VIBE and keep every state I described.`

Desired user-visible outcome: One path-first reply carrying a passing EVOKE result, whose saved `.md` file opens with a header naming VIBE at Medium complexity and reads back as a VIBE prompt with every element present, labelled or as prose, and every supplied fact kept, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-023](skill-framework-coverage/vibe-medium-returns-inspection-screen-export.md)

### SFW-024 | VIBE-MP at High complexity for an e-bike theft claim flow

#### Description

Verify `$vibe` delivers a High-tier VIBE-MP prompt in one turn with every VIBE-MP element present, labelled or as prose.

#### Scenario contract

Prompt: `$vibe $markdown MagicPath brief for the claim flow in our e-bike insurance app. The user is a commuter who has just found her e-bike stolen from a station bike rack, on her phone, upset and short on time. Single job: file a complete theft claim in under five minutes. The multi-page flow has five screens: what happened; where and when, with the station prefilled from her location; photos and frame number; the police report number or a clear way to add it later; and a confirmation with a live claim tracker. Every screen links back to the previous one without losing input, and a draft survives a lost signal. It should feel steady and competent, never cheerful or gamified, and nothing like a generic fintech gradient. Dutch and English. No component library, let MagicPath choose. Shape it with VIBE-MP and keep all five screens. No questions please.`

Desired user-visible outcome: One path-first reply carrying a passing EVOKE result, whose saved `.md` file opens with a header naming VIBE-MP at High complexity and reads back as a VIBE-MP prompt with every element present, labelled or as prose, and every supplied fact kept, closing on the share-back invitation.

#### Test execution

> **Feature File:** [SFW-024](skill-framework-coverage/vibe-mp-high-ebike-theft-claim-flow-export.md)

---

## 20. PROJECT FRAMEWORK COVERAGE (`PFW-001..PFW-024`)

### PFW-001 | RCAF at Medium complexity for a warehouse shift handover in the Project

#### Description

Verify `$text` renders a Medium-tier RCAF Deliverable Block in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$text $markdown Improve this prompt we use in ChatGPT at our Rotterdam warehouse: "Summarise today's exceptions for the next shift." Every evening the day shift lead pastes the exception log (damaged pallets, short picks, late trucks, scanner faults), and the night lead reads the summary at the 22:00 handover. It should group exceptions by type, flag anything still open, give the dock door and pallet ID for each open item and stay under 200 words. No blame language, just facts. Structure it with RCAF. No questions, use your judgment on anything I left open.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming RCAF at Medium complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-001](project-framework-coverage/rcaf-medium-warehouse-handover-canvas.md)

### PFW-002 | RCAF at High complexity for an expense claim review in the Project

#### Description

Verify `$improve` renders a High-tier RCAF Deliverable Block in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$improve $json Our finance team calls this prompt through the Claude API from our expense tool: "Check this expense claim and say if it is fine." Make it much stronger. The model gets the claim lines, the receipts as text and the employee's grade. It sorts each line into within policy, missing receipt, over limit or not a business cost. Within policy gets a recommended approval, a missing receipt gets a receipt request, over limit goes to the finance controller, and a non-business cost goes back to the employee with the policy clause. Any line above EUR 750 goes to the controller whatever its class. Hotel limits are EUR 180 a night for grades 1 to 5 and EUR 240 above. It only recommends, never marks anything as paid, and always quotes the receipt line it relies on. Our prompt registry stores only the four RCAF keys, so keep it RCAF even for a prompt this size, and keep every rule rather than streamlining. No questions, use your judgment on the rest.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming RCAF at High complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, its payload parsing as JSON, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-002](project-framework-coverage/rcaf-high-expense-claim-review-canvas.md)

### PFW-003 | RCAF at Complex complexity for an incident postmortem in the Project

#### Description

Verify `$deep` renders a Complex-tier RCAF Deliverable Block in one turn with every RCAF element labelled.

#### Scenario contract

Prompt: `$deep $markdown I want a serious upgrade of our postmortem prompt, currently just "Write a postmortem from these notes." We give Claude a PagerDuty timeline, a Slack incident-channel export and the deploy log for one SEV1 or SEV2 incident. It must produce one blameless draft in three layers: a technical timeline for engineers, an impact summary for support leads and a five-sentence brief for the exec team. Timestamps arrive in both UTC and Amsterdam time, so it normalises everything to UTC and flags any gap over 10 minutes. It may only state a root cause the logs support and labels everything else as a hypothesis. Action items need an owner from the responders list and a due week. Customer names become account IDs. Our SRE prompt catalogue lints for the four RCAF sections, so use RCAF, layered per audience, not another framework. Keep everything, no streamlining, and skip the questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming RCAF at Complex complexity and reads back as a RCAF prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-003](project-framework-coverage/rcaf-complex-incident-postmortem-canvas.md)

### PFW-004 | COSTAR at Medium complexity for a school parent newsletter in the Project

#### Description

Verify `$improve` renders a Medium-tier COSTAR Deliverable Block in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$improve $markdown Please improve the prompt our primary school office uses in ChatGPT for the monthly parent newsletter: "Write a newsletter for parents about this month." The office pastes in the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes. Parents read it on their phones, and many speak Dutch as a second language, so it needs plain B1-level language, short paragraphs and a warm but not chatty tone. Event dates go in a list at the top. Keep it under 350 words and never name individual pupils. Use COSTAR for the structure. Don't ask me anything, just make sensible calls where I left gaps.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming COSTAR at Medium complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-004](project-framework-coverage/costar-medium-school-newsletter-canvas.md)

### PFW-005 | COSTAR at High complexity for a hybrid-work announcement in the Project

#### Description

Verify `$text` renders a High-tier COSTAR Deliverable Block in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$text $yaml We need a prompt for our HR assistant, GPT-4.1 on our intranet, that drafts the announcement of our new hybrid-work policy. Audience: 420 staff across the Utrecht and Ghent offices, from warehouse crew to engineers. From 1 March everyone is in the office on Tuesday and Thursday, team leads can grant two exceptions per person per quarter, and the travel allowance moves from per kilometre to a flat EUR 60 a month. The draft needs an announcement of about 300 words, a six-question FAQ and a two-line Slack teaser. Tone: direct and reassuring, never corporate spin, and it must not promise anything beyond the policy text. Build it with COSTAR and keep all three outputs. No questions please, fill gaps sensibly.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming COSTAR at High complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-005](project-framework-coverage/costar-high-hybrid-work-announcement-canvas.md)

### PFW-006 | COSTAR at Complex complexity for clinic outage messages in the Project

#### Description

Verify `$deep` renders a Complex-tier COSTAR Deliverable Block in one turn with every COSTAR element labelled.

#### Scenario contract

Prompt: `$deep $markdown Rebuild our outage-communication prompt for Gemini 2.5 Pro; right now it is "Write a message to patients about the outage." We run 14 physiotherapy clinics. When our booking platform fails, the prompt takes the incident facts we paste and drafts three messages: an SMS to patients with appointments in the next 48 hours (max 300 characters), an email to all active patients and a phone script for front-desk staff. Each message in Dutch and English. Patients range from teenage athletes to people in their 80s, so plain B1-level language. Every message says what we know, what we do not know yet and when the next update comes. It never guesses at a cause, never mentions data exposure unless the facts say so, and always gives the direct clinic phone number. Formal but empathetic. Structure it with COSTAR, with an Audience and Response block per channel. Keep the full scope and don't ask me questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming COSTAR at Complex complexity and reads back as a COSTAR prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-006](project-framework-coverage/costar-complex-clinic-outage-messages-canvas.md)

### PFW-007 | CIDI at Medium complexity for a credit-note procedure in the Project

#### Description

Verify `$improve` renders a Medium-tier CIDI Deliverable Block in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$improve $yaml Improve our SOP-writing prompt for Claude: "Turn this into a how-to for the team." We paste a transcript of a senior clerk narrating a screen recording, and Claude writes a step-by-step procedure for new accounts-payable clerks on booking a supplier credit note against an open invoice. Each step needs one action, the screen or field it happens in and what the clerk should see afterwards. Steps that need a second approver, for credit notes above EUR 5,000, must be marked. Keep the clerk's field names exactly as spoken and leave out the chit-chat. The result goes into Confluence. Use CIDI. No questions, just use your judgment.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CIDI at Medium complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-007](project-framework-coverage/cidi-medium-credit-note-procedure-canvas.md)

### PFW-008 | CIDI at High complexity for a developer setup guide in the Project

#### Description

Verify `$improve` renders a High-tier CIDI Deliverable Block in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$improve $markdown Improve this onboarding prompt our platform team runs with Claude in Cursor: "Write a setup guide for new devs from this README." The input is our monorepo README, the Makefile and the CI config. The guide must take a new backend engineer from a fresh laptop to a green local test run in one afternoon. It needs separate paths for macOS and Ubuntu, a prerequisites list with exact versions taken from the files, a verification check after every stage and a troubleshooting section built only from errors the CI config or README mention. Commands are copied verbatim from the input, never invented. Secrets live in 1Password, so the guide says where to fetch them but never shows a value. Lay it out with CIDI and keep the whole scope. No questions, fill any gaps sensibly.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CIDI at High complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-008](project-framework-coverage/cidi-high-developer-setup-guide-canvas.md)

### PFW-009 | CIDI at Complex complexity for a customs work instruction in the Project

#### Description

Verify `$deep` renders a Complex-tier CIDI Deliverable Block in one turn with every CIDI element labelled.

#### Scenario contract

Prompt: `$deep $json Our freight-forwarding team needs a far better prompt for work instructions; today it is "Document this process." GPT-4.1 gets three inputs: a call transcript with a senior customs broker, our current checklist and the carrier's dangerous-goods rules. It must write the work instruction for clearing inbound sea containers carrying lithium batteries at the port of Rotterdam. Steps are split by role (broker, planner, warehouse), and each has its trigger, the system it happens in, the document it produces and the hand-off. Where the transcript and the checklist disagree, it lists the conflict instead of choosing. Any shipment declared under UN3480 goes to the DG officer before the planner books a slot. Dutch and English versions with the same step numbers. The result feeds our knowledge-base importer, which maps CIDI sections to fields, so it has to be CIDI. Keep the full scope and don't ask questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CIDI at Complex complexity and reads back as a CIDI prompt with every element labelled and every supplied fact kept, its payload parsing as JSON, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-009](project-framework-coverage/cidi-complex-lithium-customs-instruction-canvas.md)

### PFW-010 | TIDD-EC at Medium complexity for a legal intake note in the Project

#### Description

Verify `$improve` renders a Medium-tier TIDD-EC Deliverable Block in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$improve $markdown Tighten this intake prompt for our employment-law firm: "Read the web form and summarise the case." Claude reads each web-form inquiry and writes an intake note for the lawyer who does the free 20-minute call. The note needs the client type (employee or employer), the issue (dismissal, contract, discrimination or pay), every date mentioned and the other party's name for our conflict check. It must never give legal advice or estimate chances, and it flags any dismissal older than two months, because the deadline may have passed. One good note: "Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag." Structure it with TIDD-EC. No questions, use your judgment on the rest.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming TIDD-EC at Medium complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-010](project-framework-coverage/tidd-ec-medium-legal-intake-note-canvas.md)

### PFW-011 | TIDD-EC at High complexity for a health-claims checker in the Project

#### Description

Verify `$improve` renders a High-tier TIDD-EC Deliverable Block in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$improve $json Improve the compliance prompt behind the listing checker for our supplement brand's marketplace listings. Current version: "Check if this product text is OK." GPT-4.1 receives the title, description and bullet points of one listing, plus our approved list of 38 EU-authorised health claims with each call. It flags every health claim that is not on the list, and for each flag returns the exact sentence, the rule it breaks (unauthorised claim, disease claim or dosage promise) and a compliant rewrite that keeps the product facts. It must not touch text that is already compliant and must not judge whether the product works. Worked example: "Boosts your immune system" is unauthorised, while "Vitamin C contributes to the normal function of the immune system" is approved. Use TIDD-EC and keep the full scope. No questions, decide the open points yourself.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming TIDD-EC at High complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept, its payload parsing as JSON, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-011](project-framework-coverage/tidd-ec-high-health-claims-checker-canvas.md)

### PFW-012 | TIDD-EC at Complex complexity for an AML alert narrative in the Project

#### Description

Verify `$deep` renders a Complex-tier TIDD-EC Deliverable Block in one turn with every TIDD-EC element labelled.

#### Scenario contract

Prompt: `$deep $markdown Rebuild our AML alert-narrative prompt for Mistral Large; today it is just "Explain why this alert fired." The model gets one transaction-monitoring alert: the rule that fired, 90 days of transactions, the KYC profile and prior alerts. It writes the analyst's case narrative in our fixed order: trigger, customer profile, observed pattern, expected activity, open questions. Every claim cites a transaction ID. It never concludes that the customer is laundering money and never recommends filing or closing, which stays the analyst's call. Amounts keep their original currency with the EUR equivalent in brackets. It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days, and it handles joint accounts, missing KYC fields and accounts closed mid-window. Auditors liked this sentence: "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month." Use TIDD-EC, keep the full scope and don't ask me anything.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming TIDD-EC at Complex complexity and reads back as a TIDD-EC prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-012](project-framework-coverage/tidd-ec-complex-aml-alert-narrative-canvas.md)

### PFW-013 | CRISPE at Medium complexity for oat milk positioning in the Project

#### Description

Verify `$improve` renders a Medium-tier CRISPE Deliverable Block in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$improve $markdown Make this prompt stronger: "Give me marketing ideas for our oat milk." We are a small Ghent start-up launching an oat barista milk for independent cafés in Belgium, priced 15% above the market leader. I use Claude as a sparring partner. It should act as a B2B food-and-beverage strategist, think about what baristas care about (foam stability, taste with espresso, price per cup), then give three clearly different positioning routes, each with a one-line pitch, the type of café it wins and a cheap way to test it within a month. Frank and practical, no buzzwords. Structure it with CRISPE. No questions, use your judgment.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRISPE at Medium complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-013](project-framework-coverage/crispe-medium-oat-milk-positioning-canvas.md)

### PFW-014 | CRISPE at High complexity for driver retention experiments in the Project

#### Description

Verify `$improve` renders a High-tier CRISPE Deliverable Block in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$improve $yaml Improve this: "How do we keep our drivers?" We run 210 parcel-delivery drivers from four depots around Antwerp, and 38% left in the last 12 months, mostly within their first 90 days. Exit interviews point at route density, the 06:00 start and pay per stop. I want ChatGPT to act as a workforce strategist with last-mile experience, reason about why early-tenure drivers leave, then propose four distinct retention experiments that fit a EUR 120,000 yearly budget. Each experiment needs the hypothesis, the depot to pilot it in, the metric, a 10-week read-out point and the main risk to the delivery schedule. It should challenge our assumption that pay is the main lever. Build it with CRISPE and keep the full scope. No questions, fill in the gaps yourself.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRISPE at High complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-014](project-framework-coverage/crispe-high-driver-retention-experiments-canvas.md)

### PFW-015 | CRISPE at Complex complexity for market expansion scenarios in the Project

#### Description

Verify `$deep` renders a Complex-tier CRISPE Deliverable Block in one turn with every CRISPE element labelled.

#### Scenario contract

Prompt: `$deep $markdown Upgrade my strategy prompt, currently "Should we expand to Germany?" We sell site-diary software to construction firms: 640 customers in the Netherlands and Belgium, EUR 7.8M ARR and 4% monthly churn among firms under 20 staff. The board is split: the CEO wants Germany in 2027, the CFO wants to deepen in the Benelux mid-market first, and sales says German customers will need on-premise hosting. I want Gemini 2.5 Pro to act as a skeptical B2B SaaS strategist, surface the insight that decides this, state the question sharply, then run three scenario experiments (Germany first, Benelux first, a staged hybrid) with the assumptions each depends on, the cheapest test of them before Q2 and the signal that would kill it. It must say where our data is too thin to decide. I want exploration, not a plan, so structure it with CRISPE. Keep the full scope and don't ask questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRISPE at Complex complexity and reads back as a CRISPE prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-015](project-framework-coverage/crispe-complex-market-expansion-scenarios-canvas.md)

### PFW-016 | CRAFT at Medium complexity for a customer workshop plan in the Project

#### Description

Verify `$improve` renders a Medium-tier CRAFT Deliverable Block in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$improve $markdown Improve this planning prompt: "Help me plan our customer workshop." We are a payroll software company hosting a one-day workshop in Utrecht on 12 November for 25 HR managers from existing customers, and I use ChatGPT to draft the run-of-show. It should cover the agenda from 09:30 to 16:00, two hands-on sessions on our new leave module, lunch and a closing Q&A, plus a short prep checklist for our two trainers. We judge success by an average session rating of at least 8 out of 10 and at least 10 sign-ups for the module pilot, so the prompt must keep those targets in view. Use CRAFT, since the Target part matters to us. No questions, use your judgment where I was vague.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRAFT at Medium complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-016](project-framework-coverage/craft-medium-customer-workshop-plan-canvas.md)

### PFW-017 | CRAFT at High complexity for a mailbox migration plan in the Project

#### Description

Verify `$improve` renders a High-tier CRAFT Deliverable Block in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$improve $markdown Our IT team asks Microsoft Copilot for migration plans with one line: "Plan the email migration." Turn it into a real prompt. Scope: move 1,150 user mailboxes and 60 shared mailboxes from an on-premise Exchange 2016 server to Microsoft 365 for a housing association with offices in Zwolle and Deventer. Cutover happens only at weekends, the customer-service mailbox may be offline for at most two hours, and 80 field staff use phones only. The plan needs phases with entry and exit criteria, a rollback step per phase, a staff communication moment before each phase and a risk table. Targets: zero lost mail, under 5% of users raising a ticket in the first week and done within six weekends. Structure it with CRAFT and keep the full scope. No questions, fill the gaps with sensible assumptions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRAFT at High complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-017](project-framework-coverage/craft-high-mailbox-migration-plan-canvas.md)

### PFW-018 | CRAFT at Complex complexity for a WMS go-live plan in the Project

#### Description

Verify `$deep` renders a Complex-tier CRAFT Deliverable Block in one turn with every CRAFT element labelled.

#### Scenario contract

Prompt: `$deep $markdown I need a prompt that makes Claude produce the go-live plan for our new warehouse management system; today we just ask "Make a go-live plan." Facts: two distribution centres, Tilburg with 38,000 order lines a day and Liège with 12,000, one WMS vendor, and integrations with our SAP ERP and three carriers. Go-live cannot fall between 15 November and 10 January, Liège goes first as the pilot, and Tilburg may only follow after four weeks of pick accuracy above 99.5% in Liège. The plan needs workstreams (data migration, integrations, training for 260 pickers in two languages, cutover), the dependencies between them, a go or no-go checklist, a hypercare plan and a rollback path that restores the old system within 12 hours. Success means no missed carrier cut-off in the first two weeks. Use CRAFT and keep every part. Don't ask me questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming CRAFT at Complex complexity and reads back as a CRAFT prompt with every element labelled and every supplied fact kept, with a passing CLEAR result in chat and no file claimed.

#### Test execution

> **Feature File:** [PFW-018](project-framework-coverage/craft-complex-wms-go-live-plan-canvas.md)

### PFW-019 | FRAME at Low complexity for a gravel cycling hero image in the Project

#### Description

Verify `$image` renders a Low-tier FRAME Deliverable Block in one turn with every FRAME element labelled.

#### Scenario contract

Prompt: `$image $markdown Midjourney v6.1 prompt for the homepage hero of our Zeeland gravel-cycling tours: one rider on a gravel dyke path at golden hour, shot from a low angle, riding toward the camera with the Oosterschelde behind. Photorealistic, like an outdoor-apparel catalogue photo, warm light with long shadows. It is a 21:9 banner, so the left third stays calm and empty for our headline. The rider wears an olive jersey, and there are no visible logos, no text in the image and no other people. Organise it by FRAME so I can tweak each part, and keep every detail. No questions, pick sensible parameters yourself.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming FRAME at Low complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-019](project-framework-coverage/frame-low-gravel-cycling-hero-canvas.md)

### PFW-020 | FRAME at Medium complexity for a library science poster in the Project

#### Description

Verify `$image` renders a Medium-tier FRAME Deliverable Block in one turn with every FRAME element labelled.

#### Scenario contract

Prompt: `$image $markdown We make event posters with Stable Diffusion XL in ComfyUI, which has a separate negative prompt field. I need a prompt for this year's Night of Science at the Leiden city library: a 2:3 portrait poster in a flat 1960s screen-print style, limited to four colours (#1B2A49 navy, #F2C14E mustard, #E4572E vermilion, #F4F1E8 paper). Three depth layers: two children at a brass telescope in the foreground, the library's brick facade with lit windows in the middle, and Orion rising over the rooftops behind. The top quarter stays empty sky for the title we add later, so no lettering anywhere. Visible paper grain and slight ink misregistration. The children look about 8 to 10 and are not photoreal. Use weights where they help, give me the negative prompt separately and suggest CFG and steps. Build it with FRAME, keep all of it, no questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming FRAME at Medium complexity and reads back as a FRAME prompt with every element labelled and every supplied fact kept, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-020](project-framework-coverage/frame-medium-library-science-poster-canvas.md)

### PFW-021 | MOTION at Low complexity for a potter wheel reel in the Project

#### Description

Verify `$video` renders a Low-tier MOTION Deliverable Block in one turn with every MOTION element labelled.

#### Scenario contract

Prompt: `$video $markdown Runway Gen-4 prompt, image-to-video from our still of a potter's hands at a spinning wheel in a sunlit studio. 10 seconds, 9:16 for Reels. The wet clay bowl rises and widens under her hands, a thin spiral of slip flicks off the rim, and dust drifts through the window light. Camera: a slow push-in from waist height that reaches a close-up of her thumbs smoothing the rim at 8 seconds, then holds. Calm and tactile, warm natural light, shallow depth of field. Her face stays out of frame and the studio clutter stays soft in the background. Structure it with MOTION so each part is easy to adjust, keeping every beat. No questions, choose sensible settings.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming MOTION at Low complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-021](project-framework-coverage/motion-low-potter-wheel-reel-canvas.md)

### PFW-022 | MOTION at Low complexity for a flower auction opening shot in the Project

#### Description

Verify `$video` renders a Low-tier MOTION Deliverable Block in one turn with every MOTION element labelled.

#### Scenario contract

Prompt: `$video $yaml Kling 2.6 prompt with native audio for the opening shot of a brand film about a flower auction near Aalsmeer. One continuous 10-second shot, 16:9, text-to-video. At dawn the camera glides forward about three metres above a hall full of trolley trains loaded with red and yellow tulips, the trains snaking past each other in two directions while three workers on electric tugs steer them. At 4 seconds the camera rises slowly to reveal the whole hall, and at 8 seconds it settles facing the big auction clock as its hand starts to sweep. Audio: electric hum, trolley wheels on concrete and a distant chime at the end, with no music and no voices. Cool blue daylight from the roof windows warms to gold by the end. The workers stay small and anonymous. Use MOTION, keep every beat and don't ask me questions.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming MOTION at Low complexity and reads back as a MOTION prompt with every element labelled and every supplied fact kept, its payload parsing as YAML, with a passing VISUAL result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-022](project-framework-coverage/motion-low-flower-auction-opening-canvas.md)

### PFW-023 | VIBE at Medium complexity for a returns inspection screen in the Project

#### Description

Verify `$vibe` renders a Medium-tier VIBE Deliverable Block in one turn with every VIBE element present, labelled or as prose.

#### Scenario contract

Prompt: `$vibe $markdown Screen concept for v0: the returns-inspection station in our fashion e-commerce warehouse. An inspector stands at a bench in cotton gloves, scans a returned item and has about 20 seconds to grade it A, B, C or reject on a 24-inch touchscreen. She needs the original order photo next to the item, the customer's return reason and a big tap target for each grade, and a reject asks for one damage photo. After 300 items a shift it must not feel like a spreadsheet or a dark developer tool: calm, tactile and fast. Use shadcn/ui components, so there is nothing to ask me. Shape the brief with VIBE and keep every state I described.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming VIBE at Medium complexity and reads back as a VIBE prompt with every element present, labelled or as prose, and every supplied fact kept, with a passing EVOKE result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-023](project-framework-coverage/vibe-medium-returns-inspection-screen-canvas.md)

### PFW-024 | VIBE-MP at High complexity for an e-bike theft claim flow in the Project

#### Description

Verify `$vibe` renders a High-tier VIBE-MP Deliverable Block in one turn with every VIBE-MP element present, labelled or as prose.

#### Scenario contract

Prompt: `$vibe $markdown MagicPath brief for the claim flow in our e-bike insurance app. The user is a commuter who has just found her e-bike stolen from a station bike rack, on her phone, upset and short on time. Single job: file a complete theft claim in under five minutes. The multi-page flow has five screens: what happened; where and when, with the station prefilled from her location; photos and frame number; the police report number or a clear way to add it later; and a confirmation with a live claim tracker. Every screen links back to the previous one without losing input, and a draft survives a lost signal. It should feel steady and competent, never cheerful or gamified, and nothing like a generic fintech gradient. Dutch and English. No component library, let MagicPath choose. Shape it with VIBE-MP and keep all five screens. No questions please.`

Desired user-visible outcome: One Artifact-first reply whose Deliverable Block opens with a header naming VIBE-MP at High complexity and reads back as a VIBE-MP prompt with every element present, labelled or as prose, and every supplied fact kept, with a passing EVOKE result in chat and no file claimed, closing on the share-back invitation.

#### Test execution

> **Feature File:** [PFW-024](project-framework-coverage/vibe-mp-high-ebike-theft-claim-flow-canvas.md)

---

## 21. AUTOMATED VALIDATION CROSS-REFERENCE

| Check | Coverage | Playbook overlap |
|---|---|---|
| [Router oracle and fixtures](../../benchmark/router/) | Command, semantic and fallback lane decisions | `SIR-001`, `SIR-002`, `PIR-001`, `PIR-002` |
| [Parity benchmark](../../benchmark/parity/) | Skill and Project behavior comparison | All seventy-eight scenarios |
| Operator-contract validator | Package structure, prompts, tables, turns and links | All seventy-eight scenarios and this root |
| Shared document validator | Markdown structure of root and scenario files | All package Markdown |
| Real manual execution | Runtime behavior, deliveries and side effects | `SID-001..SSB-001`, `PID-001..PSB-001`, `SFW-001..SFW-024`, `PFW-001..PFW-024` |

---

## 22. SOURCE CROSS-REFERENCE INDEX

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
| SFW-001 | RCAF at Medium complexity for a warehouse shift handover | Skill framework coverage | [SFW-001](skill-framework-coverage/rcaf-medium-warehouse-handover-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-002 | RCAF at High complexity for an expense claim review | Skill framework coverage | [SFW-002](skill-framework-coverage/rcaf-high-expense-claim-review-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-003 | RCAF at Complex complexity for an incident postmortem | Skill framework coverage | [SFW-003](skill-framework-coverage/rcaf-complex-incident-postmortem-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-004 | COSTAR at Medium complexity for a school parent newsletter | Skill framework coverage | [SFW-004](skill-framework-coverage/costar-medium-school-newsletter-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-005 | COSTAR at High complexity for a hybrid-work announcement | Skill framework coverage | [SFW-005](skill-framework-coverage/costar-high-hybrid-work-announcement-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-006 | COSTAR at Complex complexity for clinic outage messages | Skill framework coverage | [SFW-006](skill-framework-coverage/costar-complex-clinic-outage-messages-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-007 | CIDI at Medium complexity for a credit-note procedure | Skill framework coverage | [SFW-007](skill-framework-coverage/cidi-medium-credit-note-procedure-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-008 | CIDI at High complexity for a developer setup guide | Skill framework coverage | [SFW-008](skill-framework-coverage/cidi-high-developer-setup-guide-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-009 | CIDI at Complex complexity for a customs work instruction | Skill framework coverage | [SFW-009](skill-framework-coverage/cidi-complex-lithium-customs-instruction-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-010 | TIDD-EC at Medium complexity for a legal intake note | Skill framework coverage | [SFW-010](skill-framework-coverage/tidd-ec-medium-legal-intake-note-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-011 | TIDD-EC at High complexity for a health-claims checker | Skill framework coverage | [SFW-011](skill-framework-coverage/tidd-ec-high-health-claims-checker-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-012 | TIDD-EC at Complex complexity for an AML alert narrative | Skill framework coverage | [SFW-012](skill-framework-coverage/tidd-ec-complex-aml-alert-narrative-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-013 | CRISPE at Medium complexity for oat milk positioning | Skill framework coverage | [SFW-013](skill-framework-coverage/crispe-medium-oat-milk-positioning-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-014 | CRISPE at High complexity for driver retention experiments | Skill framework coverage | [SFW-014](skill-framework-coverage/crispe-high-driver-retention-experiments-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-015 | CRISPE at Complex complexity for market expansion scenarios | Skill framework coverage | [SFW-015](skill-framework-coverage/crispe-complex-market-expansion-scenarios-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-016 | CRAFT at Medium complexity for a customer workshop plan | Skill framework coverage | [SFW-016](skill-framework-coverage/craft-medium-customer-workshop-plan-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-017 | CRAFT at High complexity for a mailbox migration plan | Skill framework coverage | [SFW-017](skill-framework-coverage/craft-high-mailbox-migration-plan-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-018 | CRAFT at Complex complexity for a WMS go-live plan | Skill framework coverage | [SFW-018](skill-framework-coverage/craft-complex-wms-go-live-plan-export.md) | [`framework-pattern-library.md`](../assets/framework-pattern-library.md) |
| SFW-019 | FRAME at Low complexity for a gravel cycling hero image | Skill framework coverage | [SFW-019](skill-framework-coverage/frame-low-gravel-cycling-hero-export.md) | [`image-mode.md`](../references/image-mode.md) |
| SFW-020 | FRAME at Medium complexity for a library science poster | Skill framework coverage | [SFW-020](skill-framework-coverage/frame-medium-library-science-poster-export.md) | [`image-mode.md`](../references/image-mode.md) |
| SFW-021 | MOTION at Low complexity for a potter wheel reel | Skill framework coverage | [SFW-021](skill-framework-coverage/motion-low-potter-wheel-reel-export.md) | [`video-mode.md`](../references/video-mode.md) |
| SFW-022 | MOTION at Low complexity for a flower auction opening shot | Skill framework coverage | [SFW-022](skill-framework-coverage/motion-low-flower-auction-opening-export.md) | [`video-mode.md`](../references/video-mode.md) |
| SFW-023 | VIBE at Medium complexity for a returns inspection screen | Skill framework coverage | [SFW-023](skill-framework-coverage/vibe-medium-returns-inspection-screen-export.md) | [`visual-mode.md`](../references/visual-mode.md) |
| SFW-024 | VIBE-MP at High complexity for an e-bike theft claim flow | Skill framework coverage | [SFW-024](skill-framework-coverage/vibe-mp-high-ebike-theft-claim-flow-export.md) | [`visual-mode.md`](../references/visual-mode.md) |
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
| PFW-001 | RCAF at Medium complexity for a warehouse shift handover in the Project | Project framework coverage | [PFW-001](project-framework-coverage/rcaf-medium-warehouse-handover-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-002 | RCAF at High complexity for an expense claim review in the Project | Project framework coverage | [PFW-002](project-framework-coverage/rcaf-high-expense-claim-review-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-003 | RCAF at Complex complexity for an incident postmortem in the Project | Project framework coverage | [PFW-003](project-framework-coverage/rcaf-complex-incident-postmortem-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-004 | COSTAR at Medium complexity for a school parent newsletter in the Project | Project framework coverage | [PFW-004](project-framework-coverage/costar-medium-school-newsletter-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-005 | COSTAR at High complexity for a hybrid-work announcement in the Project | Project framework coverage | [PFW-005](project-framework-coverage/costar-high-hybrid-work-announcement-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-006 | COSTAR at Complex complexity for clinic outage messages in the Project | Project framework coverage | [PFW-006](project-framework-coverage/costar-complex-clinic-outage-messages-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-007 | CIDI at Medium complexity for a credit-note procedure in the Project | Project framework coverage | [PFW-007](project-framework-coverage/cidi-medium-credit-note-procedure-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-008 | CIDI at High complexity for a developer setup guide in the Project | Project framework coverage | [PFW-008](project-framework-coverage/cidi-high-developer-setup-guide-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-009 | CIDI at Complex complexity for a customs work instruction in the Project | Project framework coverage | [PFW-009](project-framework-coverage/cidi-complex-lithium-customs-instruction-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-010 | TIDD-EC at Medium complexity for a legal intake note in the Project | Project framework coverage | [PFW-010](project-framework-coverage/tidd-ec-medium-legal-intake-note-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-011 | TIDD-EC at High complexity for a health-claims checker in the Project | Project framework coverage | [PFW-011](project-framework-coverage/tidd-ec-high-health-claims-checker-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-012 | TIDD-EC at Complex complexity for an AML alert narrative in the Project | Project framework coverage | [PFW-012](project-framework-coverage/tidd-ec-complex-aml-alert-narrative-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-013 | CRISPE at Medium complexity for oat milk positioning in the Project | Project framework coverage | [PFW-013](project-framework-coverage/crispe-medium-oat-milk-positioning-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-014 | CRISPE at High complexity for driver retention experiments in the Project | Project framework coverage | [PFW-014](project-framework-coverage/crispe-high-driver-retention-experiments-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-015 | CRISPE at Complex complexity for market expansion scenarios in the Project | Project framework coverage | [PFW-015](project-framework-coverage/crispe-complex-market-expansion-scenarios-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-016 | CRAFT at Medium complexity for a customer workshop plan in the Project | Project framework coverage | [PFW-016](project-framework-coverage/craft-medium-customer-workshop-plan-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-017 | CRAFT at High complexity for a mailbox migration plan in the Project | Project framework coverage | [PFW-017](project-framework-coverage/craft-high-mailbox-migration-plan-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-018 | CRAFT at Complex complexity for a WMS go-live plan in the Project | Project framework coverage | [PFW-018](project-framework-coverage/craft-complex-wms-go-live-plan-canvas.md) | [Framework Pattern Library knowledge](<../../claude project/knowledge/Prompt Improver - Assets - Framework Pattern Library - v0.100.md>) |
| PFW-019 | FRAME at Low complexity for a gravel cycling hero image in the Project | Project framework coverage | [PFW-019](project-framework-coverage/frame-low-gravel-cycling-hero-canvas.md) | [Image Mode knowledge](<../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) |
| PFW-020 | FRAME at Medium complexity for a library science poster in the Project | Project framework coverage | [PFW-020](project-framework-coverage/frame-medium-library-science-poster-canvas.md) | [Image Mode knowledge](<../../claude project/knowledge/Prompt Improver - Image Mode - v0.123.md>) |
| PFW-021 | MOTION at Low complexity for a potter wheel reel in the Project | Project framework coverage | [PFW-021](project-framework-coverage/motion-low-potter-wheel-reel-canvas.md) | [Video Mode knowledge](<../../claude project/knowledge/Prompt Improver - Video Mode - v0.123.md>) |
| PFW-022 | MOTION at Low complexity for a flower auction opening shot in the Project | Project framework coverage | [PFW-022](project-framework-coverage/motion-low-flower-auction-opening-canvas.md) | [Video Mode knowledge](<../../claude project/knowledge/Prompt Improver - Video Mode - v0.123.md>) |
| PFW-023 | VIBE at Medium complexity for a returns inspection screen in the Project | Project framework coverage | [PFW-023](project-framework-coverage/vibe-medium-returns-inspection-screen-canvas.md) | [Visual Mode knowledge](<../../claude project/knowledge/Prompt Improver - Visual Mode - v0.301.md>) |
| PFW-024 | VIBE-MP at High complexity for an e-bike theft claim flow in the Project | Project framework coverage | [PFW-024](project-framework-coverage/vibe-mp-high-ebike-theft-claim-flow-canvas.md) | [Visual Mode knowledge](<../../claude project/knowledge/Prompt Improver - Visual Mode - v0.301.md>) |
