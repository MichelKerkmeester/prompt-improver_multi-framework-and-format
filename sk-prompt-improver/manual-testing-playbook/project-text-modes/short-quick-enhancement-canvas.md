---
title: "PTX-003 -- Short mode quick enhancement with CLEAR and Canvas"
description: "Validates the $short lane in the Project on a one-line request: Quick energy, the CLEAR gate, a Deliverable Block with every supplied fact and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PTX-003 -- Short mode quick enhancement with CLEAR and Canvas

`$short` binds the Short lane outright in the Project router, so Quick energy runs a lean D, P, H pass and CLEAR still guards the Deliverable Block. The request is one casual line with a name, a date and a tone, and nothing else to lean on.

---

## 1. OVERVIEW

The user wants a prompt for a LinkedIn post announcing a new head of design. Quick energy trims the thinking, not the gate: CLEAR still scores the result and the block still comes before any commentary. Turn 2 adds where the new hire comes from, which is a revision of the delivered prompt.

### Why this matters

A thin request tempts the runtime to fill the gaps with invented biography. The facts the user gave are few, so each one is easy to check, and anything the prompt says about the hire beyond them is an invention.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$short` delivers a CLEAR-gated Deliverable Block at Quick energy that keeps every supplied fact and invents none, then renders the Turn 2 revision as a new block in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Quick one: I need a prompt for a LinkedIn post saying we hired Priya Nair as our new head of design. She starts on October 14. Warm, please, not corporate.`
- Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: the kernel checklist at `Custom Instructions.md` line 398 gathers missing essentials with one question, while `Prompt Improver - Interactive Mode - v0.700.md` line 202 routes `$short` to the format selection question (Template 4, line 138). Command flow allows at most one interaction (same file, line 405). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 413). The Short lane binds with Quick energy and CLEAR (`Custom Instructions.md` line 50), Quick runs D, P and H with one or two perspectives (`Prompt Improver - DEPTH Thinking Framework - v0.200.md` line 64), and CLEAR still passes at 40 of 50 with its floors (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447). The format defaults to Markdown (`Prompt Improver - Format Guide Markdown - v0.141.md` line 438). The Deliverable Block comes before any commentary and holds only the single-line `Mode: $short | Complexity: [level] | Framework: [Framework]` header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR score with gate status and a short summary, and does not paste the prompt again (lines 341 and 384-387). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: a LinkedIn post, announcing a new head of design, the name Priya Nair, the start date Oct 14 and a warm, not corporate tone. It adds no biography the user did not give: no previous employer before Turn 2 supplies one, no invented achievement or background and no year or weekday attached to Oct 14 (`Custom Instructions.md` line 335). Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose block reads back as a lean LinkedIn post prompt with the name, date and tone intact and whose chat claims no file was written, then a second block that adds Spotify
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block with header, prompt and attestation before any commentary, a CLEAR result, every supplied fact intact, nothing invented and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if commentary precedes the block, the header or attestation is missing, the prompt is pasted again, the score is absent, the name or date is altered, a fact about Priya Nair is invented, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a second post variant or an image brief are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate` | Bind Short at Quick energy, either deliver through a Deliverable Block or ask at most one consolidated question | No more than one question and no block before it is answered | Response transcript and Artifact panel state |
| 2 | `Mention that she joins us from Spotify.` | When Turn 1 asked, complete the enhancement with Spotify included, render the block and report the export-equivalent path, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 fact plus Spotify | Name, date and tone retained and Spotify added as her previous employer | Response, score line, both block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade gate, facts, invention, chat shape, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Short and either delivers or asks once. Step 3 records the first delivery. Step 4 proves the graded block carries header, attestation, the name, the date and the tone with no invented biography, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the Artifact panel state, a fact checklist against the graded block, excerpts of every block showing the single-line header, prompt body and attestation footer, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a reported CLEAR result, every supplied fact intact, nothing invented, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: Commentary before the block, a missing header or attestation, the prompt pasted again in chat, missing score, an altered name or date, invented biography, scope expansion, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 against the observed ordering
2. Re-check the CLEAR threshold and floors in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447 when the score is missing or off
3. Check the invention ban in `Custom Instructions.md` line 335 and the delivery override in line 291 when facts were added or Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-003 | Short mode quick enhancement with CLEAR and Canvas | Verify `$short` delivers a gated Deliverable Block with every supplied fact and nothing invented, and renders the revision as a new block | `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Short bound at Quick energy, delivery or one question. Step 3: first delivery fixed. Step 4: facts intact, revision in a new block | Transcripts, CLEAR line, panel state, fact checklist, block excerpts | PASS if block, attestation, gate, facts and revision all hold. FAIL on commentary before the block, pasted prompt, missing score, an altered fact, invented biography, a claimed save or a patch in place of a block | 1. Check delivery ordering.<br>2. Check CLEAR thresholds.<br>3. Check invention ban and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Short binding, invention ban, delivery override, Delivery Protocol and No Canvas panel rule |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Quick energy phases and perspectives |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$short` route, the format selection template and interaction limits |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR rubric, floors and repair rules |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown default and deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/short-quick-enhancement-canvas.md`
