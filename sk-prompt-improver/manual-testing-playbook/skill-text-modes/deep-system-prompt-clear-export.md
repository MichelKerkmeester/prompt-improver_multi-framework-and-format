---
title: "STX-002 -- Deep mode system prompt with CLEAR and export"
description: "Validates the $deep lane on a fact-dense system prompt: Deep energy, the CLEAR gate, a markdown export and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# STX-002 -- Deep mode system prompt with CLEAR and export

`$deep` binds the Deep lane outright, so Deep energy runs with all five perspectives and CLEAR guards a `.md` export. The request is dense with numbers, categories and hard limits, which makes it the text-mode case where a dropped fact or an added output is easiest to see.

---

## 1. OVERVIEW

The user wants a system prompt for a helpdesk triage bot and supplies the categories, the SLA tiers, the escalation triggers, two prohibitions, the output destination and the weak prompt it replaces. The runtime improves that into one system prompt, scores it with CLEAR and saves it before replying. Turn 2 adds a language rule, which is a revision of the delivered prompt.

### Why this matters

Deep energy invites elaboration. The test is whether that elaboration stays inside what the user asked for: every supplied fact survives, nothing the user did not ask for is added, and the revision lands as a new file rather than an edit to the delivered one.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$deep` delivers a CLEAR-gated markdown export that keeps every supplied fact, then saves the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Can you turn this into a proper system prompt? Our helpdesk triage bot reads support emails for our project management SaaS, tags the category, sets priority by our SLA tiers, escalates data loss, security and multi-user outages to the on-call engineer, never promises refunds or dates and writes a Zendesk internal note. Right now the prompt is just one line.`
- Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: `SKILL.md` line 383 asks only when essential context is missing, while `references/interactive-mode.md` line 656 draws a Question step for `$deep` and line 215 routes `$deep` straight to processing. Command flow allows at most one interaction (`SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). The Deep lane binds with Deep energy and CLEAR (`SKILL.md` lines 79 and 349), all five perspectives run (`references/depth-framework.md` lines 59-63), and CLEAR passes at 40 of 50 with floors Correctness 7, Logic 7, Expression 10, Arrangement 7 and Reusability 3 (`SKILL.md` lines 444-445). The format defaults to Markdown (`SKILL.md` line 408), the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), the file opens with the single-line `Mode: $deep | Complexity: [level] | Framework: [Framework]` header followed only by the prompt (`SKILL.md` lines 558-559) and the reply leads with the saved path, reports the CLEAR score and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: a B2B project management SaaS, incoming support emails as input, exactly the five categories billing, bug, how-to, account access and feature request, the tiers Enterprise 1 hour, Business 4 hours and Starter 24 hours as first-response targets, escalation straight to the on-call engineer on data loss, a security issue or an outage affecting more than one user, no promised refunds or delivery dates and a Zendesk internal note as the output. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved file reads back as a full triage system prompt with every supplied fact intact, then a second export carrying the language rule
- Pass/fail: PASS if the Turn 1 delivery is a verified `.md` export with the header, a CLEAR result and every supplied fact intact, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if output appears before saving, the reply does not lead with the saved path, the full prompt is pasted, the score is absent, a fact is dropped or altered, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a customer-facing reply draft, a sixth category or a routing target other than the on-call engineer are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."` | Bind Deep, either deliver through a verified `.md` export or ask at most one consolidated question | No more than one question and no file before it is answered | Response transcript and `export/` listing |
| 2 | `Customers also write in Dutch. Keep the internal note in English, but quote the customer's key sentence in their own language.` | When Turn 1 asked, complete the enhancement with the language rule included, save the export and reply path-first, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: save a new export under the next number that carries every Turn 1 fact plus the language rule, and leave the delivered export unchanged | Every Turn 1 fact retained, Dutch input accepted, internal note in English and the key sentence quoted in the customer's language | Response, score line, both export excerpts and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum the Turn 1 file -> operator: grade gate, facts, scope, chat shape and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Deep and either delivers or asks once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the graded file carries the header and every supplied fact with nothing added, and, when Turn 1 delivered, that Turn 2 saved a new file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the CLEAR score line with gate status, `export/` listings before and after each turn, a fact checklist against the graded file, excerpts of every export showing the single-line header plus prompt body, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export with the header, a reported CLEAR result, every supplied fact intact, no scope expansion, the path-first reply and a Turn 2 revision saved as a new export
- **Fail**: Output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, missing score, a dropped or altered fact, scope expansion, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Deep binding and energy in `SKILL.md` lines 79, 349 and 375 when the lane or perspective count is off
2. Re-check the CLEAR threshold and floors in `SKILL.md` lines 444-445 and `references/patterns-evaluation.md` lines 461-469 when the score is missing or off
3. Check the revision rule in `SKILL.md` lines 421-422 and `AGENTS.md` line 70 when Turn 2 edited the delivered file or saved nothing

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| STX-002 | Deep mode system prompt with CLEAR and export | Verify `$deep` delivers a gated markdown export with every supplied fact and saves the revision as a new export | `$deep I need a system prompt for our helpdesk triage bot. We are a B2B SaaS (a project management tool). It reads incoming support emails and should tag the category (billing, bug, how-to, account access, feature request), set priority by our SLA tiers (Enterprise gets a first response within 1 hour, Business within 4 hours, Starter within 24 hours) and escalate straight to the on-call engineer when an email mentions data loss, a security issue or an outage affecting more than one user. It must never promise refunds or delivery dates. Its output goes into Zendesk as an internal note. Our current prompt is just "You are a helpful support assistant, triage tickets."` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Read exports, re-checksum` | Step 1: baseline known. Step 2: Deep bound, delivery or one question. Step 3: first delivery fixed. Step 4: facts intact, revision in a new file | Transcripts, CLEAR line, export listings, fact checklist, excerpts, checksums | PASS if export, gate, facts, scope and revision all hold. FAIL on pre-save output, a reply that does not lead with the path, pasted prompt, missing score, a lost fact, scope expansion or an in-place edit | 1. Check Deep binding.<br>2. Check CLEAR thresholds.<br>3. Check revision rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Deep binding, interaction limits, CLEAR summary, header and revision rule |
| [`depth-framework.md`](../../references/depth-framework.md) | Deep energy and the five-perspective requirement |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$deep` state route and conversation flow |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR rubric, floors and repair rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown export file rules |

---

## 5. SOURCE METADATA

- Group: Skill text modes
- Playbook ID: STX-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-text-modes/deep-system-prompt-clear-export.md`
