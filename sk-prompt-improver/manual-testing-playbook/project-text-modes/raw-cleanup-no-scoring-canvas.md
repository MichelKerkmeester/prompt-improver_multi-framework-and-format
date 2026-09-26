---
title: "PTX-005 -- Raw mode cleanup without scoring and Canvas"
description: "Validates the $raw lane in the Project: no DEPTH, no question and no scorer, an immediate Deliverable Block with every supplied constraint, and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PTX-005 -- Raw mode cleanup without scoring and Canvas

`$raw` binds Raw mode outright in the Project router: no DEPTH phases, no clarifying question and no scorer. The Deliverable Block protocol still holds, so Turn 1 must render the cleaned prompt with its header and attestation, with nothing asked first and no score reported.

---

## 1. OVERVIEW

The user dictates a rough instruction for ChatGPT and asks for it cleaned up. Raw mode is the one lane that allows zero interactions and runs no gate, which makes it the lane where a runtime that asks anyway, or scores anyway, is plainly visible. Turn 2 adds a closing item, which is a revision of the delivered prompt.

### Why this matters

Raw is an explicit request to skip the machinery. A question or a score on this lane means the command did not bind, and a cleanup that adds sections turns a passthrough into an enhancement the user did not ask for.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$raw` renders a cleaned Deliverable Block immediately, with no question, no DEPTH and no score, keeps every supplied constraint, then renders the Turn 2 revision as a new block in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Just tidy this up so I can paste it into ChatGPT, no questions: summarise the attached quarterly sales report for the exec team in bullet points, highlight regions that missed target, don't make up numbers and keep it to one page.`
- Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation and then inspect every Deliverable Block and the chat report
- Expected signals: Turn 1 is the graded delivery and must deliver: Raw mode allows zero interactions (`Prompt Improver - Interactive Mode - v0.700.md` line 406) and bypasses the question (`Custom Instructions.md` line 398), so any Turn 1 question is a failure. Raw runs no DEPTH and no scorer (`Custom Instructions.md` line 46; `Prompt Improver - Interactive Mode - v0.700.md` lines 293, 623 and 641; `Prompt Improver - DEPTH Thinking Framework - v0.200.md` line 63), so the chat reports no CLEAR, EVOKE or VISUAL score and no gate status; a score line on a Raw delivery is the wrong scorer for the lane, whose scorer is none. The Deliverable Block comes before any commentary and holds only a single-line `Mode:` header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). The header's framework value is recorded and not graded, since Raw uses no framework. After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md` and does not paste the prompt again (lines 341 and 384). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The cleaned prompt carries every supplied constraint: ChatGPT as the target, named in the header or the body, a summary of the attached quarterly sales report, the exec team as the audience, bullet points, highlighted regions that missed target, no invented numbers and a one-page maximum. It adds no section the user did not ask for, and before Turn 2 it does not ask for the worst-selling products. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band, or none, is recorded and never decides a verdict. On Turn 2, whether the reply carries a score line is recorded and not graded, because no source says a follow-up without a command keeps the Raw binding
- Desired user-visible outcome: One immediate Artifact-first reply with no score, whose block reads back as the user's instruction cleaned up and whose chat claims no file was written, then a second block that ends with the three worst-selling products
- Pass/fail: PASS if Turn 1 renders a Deliverable Block with header, prompt and attestation before any commentary, carries every supplied constraint, asks nothing, reports no score and claims no save, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if Turn 1 asks a question, reports a score or gate status, puts commentary before the block, omits the header or attestation, pastes the prompt again, drops or alters a constraint, claims a save or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a recommendations section, a chart request or a forecast are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page` | Bind Raw, ask nothing, run no scorer, render the Deliverable Block and report the export-equivalent path | No question, no score line, one block | Response transcript and Artifact panel state |
| 2 | `Also ask it to end with the three products that sold worst.` | Treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 constraint and ends with the three worst-selling products | Every Turn 1 constraint retained and the closing item added | Response, both block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm Turn 1 asked nothing and reported no score -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade Raw binding, constraints, scope, chat shape, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Raw and renders a block with no question and no score. Step 3 records the first delivery. Step 4 proves the graded block carries header, attestation and every supplied constraint with nothing added, and that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the Artifact panel state, a constraint checklist against the graded block, excerpts of every block showing the single-line header, prompt body and attestation footer, the export-equivalent path lines, a note of any score line on either turn and the verdict.

### Pass / fail

- **Pass**: An immediate Deliverable Block before commentary with header and attestation, no question, no score, every supplied constraint intact, no scope expansion, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: A Turn 1 question, a score or gate status on the Raw delivery, commentary before the block, a missing header or attestation, the prompt pasted again in chat, a dropped or altered constraint, scope expansion, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Raw binding in `Custom Instructions.md` line 46 and the interaction limits in `Prompt Improver - Interactive Mode - v0.700.md` lines 404-406 when Turn 1 asked or scored
2. Check the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 against the observed ordering
3. Check the delivery override in `Custom Instructions.md` line 291, which keeps naming identical to CLI delivery, when Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-005 | Raw mode cleanup without scoring and Canvas | Verify `$raw` renders a cleaned block at once with no question and no score, and renders the revision as a new block | `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Raw bound, no question, no score, block rendered. Step 3: first delivery fixed. Step 4: constraints intact, revision in a new block | Transcripts, panel state, constraint checklist, block excerpts | PASS if block, attestation, Raw binding, constraints and revision all hold. FAIL on a question, a score line, commentary before the block, a lost constraint, scope expansion, a claimed save or a patch in place of a block | 1. Check Raw binding.<br>2. Check delivery ordering.<br>3. Check revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Raw binding, delivery override, Delivery Protocol and No Canvas panel rule |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Raw energy with no phases and no perspectives |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$raw` command detection, zero interactions and the Raw conversation flow |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown default and deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-005
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/raw-cleanup-no-scoring-canvas.md`
