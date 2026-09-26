---
title: "PTX-002 -- Deep mode system prompt with CLEAR and Canvas"
description: "Validates the $deep lane in the Project on a fact-dense system prompt: Deep energy, the CLEAR gate, a Deliverable Block with attestation and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PTX-002 -- Deep mode system prompt with CLEAR and Canvas

`$deep` binds the Deep lane outright in the Project router, so Deep energy runs with all five perspectives and CLEAR guards a Deliverable Block rendered as a Canvas Artifact. The request is dense with numbers, categories and hard limits, which makes a dropped fact or an added output easy to see.

---

## 1. OVERVIEW

The user wants a system prompt for a helpdesk triage bot and supplies the categories, the SLA tiers, the escalation triggers, two prohibitions, the output destination and the weak prompt it replaces. The Project improves that into one system prompt, scores it with CLEAR and renders it as a Deliverable Block before any commentary. Turn 2 adds a language rule, which is a revision of the delivered prompt.

### Why this matters

Deep energy invites elaboration, and a Project cannot write files, so the only proof of delivery is the block itself. The test is whether every supplied fact survives, nothing unasked is added, no save is claimed and the revision arrives as a new block.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a CLEAR-gated Deliverable Block that keeps every supplied fact, then renders the Turn 2 revision as a new block in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Can you turn this into a proper system prompt? Our helpdesk triage bot reads support emails for our project management SaaS, tags the category, sets priority by our SLA tiers, escalates data loss, security and multi-user outages to the on-call engineer, never promises refunds or dates and writes a Zendesk internal note. Right now the prompt is just one line.`
- Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: the kernel checklist at `Custom Instructions.md` line 398 gathers missing essentials with one question, while `Prompt Improver - Interactive Mode - v0.700.md` line 642 draws a Question step for `$deep` and line 201 routes `$deep` straight to processing. Command flow allows at most one interaction (same file, line 405). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 413). The Deep lane binds with Deep energy and CLEAR (`Custom Instructions.md` line 51) with all five perspectives (`Prompt Improver - DEPTH Thinking Framework - v0.200.md` line 66), and CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447). The format defaults to Markdown (`Prompt Improver - Format Guide Markdown - v0.141.md` line 438). The Deliverable Block comes before any commentary and holds only the single-line `Mode: $deep | Complexity: [level] | Framework: [Framework]` header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR score with gate status and a short summary, and does not paste the prompt again (lines 341 and 384-387). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: a B2B project management SaaS, incoming support emails as input, exactly the five categories billing, bug, how-to, account access and feature request, the tiers Enterprise 1 hour, Business 4 hours and Starter 24 hours as first-response targets, escalation straight to the on-call engineer on data loss, a security issue or an outage affecting more than one user, no promised refunds or delivery dates and a Zendesk internal note as the output. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose block reads back as a full triage system prompt with every supplied fact intact and whose chat claims no file was written, then a second block carrying the language rule
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block with header, prompt and attestation before any commentary, a CLEAR result, every supplied fact intact and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if commentary precedes the block, the header or attestation is missing, the prompt is pasted again, the score is absent, a fact is dropped or altered, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a customer-facing reply draft, a sixth category or a routing target other than the on-call engineer are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."` | Bind Deep, either deliver through a Deliverable Block or ask at most one consolidated question | No more than one question and no block before it is answered | Response transcript and Artifact panel state |
| 2 | `Customers also write in Dutch. Keep the internal note in English, but quote the customer's key sentence in their own language.` | When Turn 1 asked, complete the enhancement with the language rule included, render the block and report the export-equivalent path, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 fact plus the language rule | Every Turn 1 fact retained, Dutch input accepted, internal note in English and the key sentence quoted in the customer's language | Response, score line, both block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade gate, facts, scope, chat shape, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Deep and either delivers or asks once. Step 3 records the first delivery. Step 4 proves the graded block carries header, attestation and every supplied fact with nothing added, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the Artifact panel state, a fact checklist against the graded block, excerpts of every block showing the single-line header, prompt body and attestation footer, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a reported CLEAR result, every supplied fact intact, no scope expansion, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: Commentary before the block, a missing header or attestation, the prompt pasted again in chat, missing score, a dropped or altered fact, scope expansion, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 against the observed ordering
2. Re-check the CLEAR threshold and floors in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447 when the score is missing or off
3. Check the delivery override in `Custom Instructions.md` line 291, which keeps naming identical to CLI delivery, when Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-002 | Deep mode system prompt with CLEAR and Canvas | Verify `$deep` delivers a gated Deliverable Block with every supplied fact and renders the revision as a new block | `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Deep bound, delivery or one question. Step 3: first delivery fixed. Step 4: facts intact, revision in a new block | Transcripts, CLEAR line, panel state, fact checklist, block excerpts | PASS if block, attestation, gate, facts, scope and revision all hold. FAIL on commentary before the block, pasted prompt, missing score, a lost fact, scope expansion, a claimed save or a patch in place of a block | 1. Check delivery ordering.<br>2. Check CLEAR thresholds.<br>3. Check revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Deep binding, scope rule, delivery override, Delivery Protocol and No Canvas panel rule |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Deep energy and the five-perspective requirement |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$deep` route, interaction limits and the one-question rule |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR rubric, floors and repair rules |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown default and deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/deep-system-prompt-clear-canvas.md`
