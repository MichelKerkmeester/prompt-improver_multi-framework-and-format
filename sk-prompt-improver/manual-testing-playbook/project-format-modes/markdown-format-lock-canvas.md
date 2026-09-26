---
title: "PFM-003 -- Independent $markdown format lock with Improve mode in the Project"
description: "Validates that the long-form $markdown token locks the format axis while $improve wins the mode axis in the Project, producing a Markdown Deliverable Block with every requested check and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PFM-003 -- Independent $markdown format lock with Improve mode in the Project

`$improve` and `$markdown` live on different axes in the Project router. Markdown is already the default format, so this scenario proves that an explicit long-form `$markdown` token still binds as a format lock and never competes with `$improve` for the mode.

---

## 1. OVERVIEW

The user's engineering team reviews pull requests with a one-line AI prompt and wants it to check three named things in a senior reviewer's voice. `$improve` binds the Improve lane at Standard energy with CLEAR, and `$markdown` locks the payload of the Deliverable Block to Markdown. Turn 2 adds a fourth check, which is a revision of the delivered prompt.

### Why this matters

A format token that matches the default is easy to treat as noise, or worse, as the mode. The block must still honor the lock, carry the Improve mode in its header and keep the review scope to exactly what the team named.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$markdown` locks format independently while `$improve` binds the mode in the Project runtime, delivering a CLEAR-gated Markdown Deliverable Block with exactly the requested checks, then rendering the Turn 2 revision as a new block
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Our engineers use "Review this code and tell me what's wrong." as the AI code review prompt on pull requests. Please improve it, in Markdown: it should check for security issues, missing tests and unclear naming, and explain the why like a senior reviewer. The diff gets pasted in below the prompt.`
- Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: the kernel checklist at `Custom Instructions.md` line 398 gathers missing essentials with one question, while `Prompt Improver - Interactive Mode - v0.700.md` line 203 routes `$improve` to the format selection question and line 209 routes a format command to the comprehensive question. Command flow allows at most one interaction (same file, line 405). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 413). Mode and format are independent axes (`Custom Instructions.md` lines 43 and 71): the Improve lane binds with Standard energy and CLEAR (line 48) and the explicit `$markdown` token locks the format to Markdown (line 57), so a Turn 1 question asking which mode to use means the format token stole the mode axis. A Turn 1 question asking which format to use is recorded as a follow-up finding and does not decide the verdict, because the knowledge file's line 203 still routes `$improve` to format selection while the kernel's line 43 gives the format axis to the format command. CLEAR passes at 40 of 50 with its floors (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 302 and 447). The Deliverable Block comes before any commentary and holds only the single-line `Mode: $improve | Complexity: [level] | Framework: [Framework]` header, the Markdown prompt and the attestation footer with `format = Markdown` and ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377; `Prompt Improver - Format Guide Markdown - v0.141.md` lines 104-108 and 438). A header labelled `$markdown` is recorded as a follow-up finding, since the Markdown guide names the mode in that slot. After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR score with gate status and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 341 and 384-387). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: AI code review on pull requests for an engineering team, the three checks security issues, missing tests and unclear naming, comments in a senior reviewer's voice that explain why and not just what, and the diff pasted below the prompt as the input. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose block reads back as a senior-reviewer code review prompt scoped to the three named checks and whose chat claims no file was written, then a second block that adds TODO flagging
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block with the Improve header and attestation before any commentary, a CLEAR result, exactly the three requested checks with the reviewer voice and diff input kept and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if commentary precedes the block, the header or attestation is missing, the payload is not Markdown, the mode axis was lost, the score is missing, a requested check or the reviewer voice is dropped, the prompt is pasted again, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a performance review, an approve or reject verdict, severity scores or, before Turn 2 asks for it, TODO flagging are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.` | Bind Improve, lock Markdown, either deliver through a Deliverable Block or ask at most one consolidated question | Format locked to Markdown regardless of any question, no question about the mode | Response transcript and Artifact panel state |
| 2 | `Also have it flag any TODO comments left in the diff.` | When Turn 1 asked, complete the enhancement with TODO flagging included, render the block and report the export-equivalent path, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries the three Turn 1 checks, the reviewer voice and the diff input plus TODO flagging | Markdown lock retained, three checks, reviewer voice and diff input kept and TODO flagging added | Response, score line, both block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade format lock, header, checks, scope, chat shape, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Improve and locks Markdown, delivering or asking once. Step 3 records the first delivery. Step 4 proves the graded block carries the Improve header, a Markdown payload with exactly the requested checks and the attestation, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the Artifact panel state, the header label used, a checklist of the requested checks against the graded block, excerpts of every block showing the single-line header, prompt body and attestation footer, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with the Improve header and attestation, a reported CLEAR result, exactly the three requested checks with the reviewer voice and diff input, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: Commentary before the block, a missing header or attestation, a non-Markdown payload, format competing with mode, missing score, a dropped check or reviewer voice, scope expansion, the prompt pasted again in chat, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the independent format axis in `Custom Instructions.md` lines 43, 57 and 71 when the format or mode was lost
2. Re-check the Markdown header and deliverable rules in `Prompt Improver - Format Guide Markdown - v0.141.md` lines 100-120 and 438, and the Delivery Protocol in `Custom Instructions.md` lines 367-390 when the header, attestation or ordering is off
3. Check the delivery override in `Custom Instructions.md` line 291, which keeps naming identical to CLI delivery, when Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFM-003 | Independent $markdown format lock with Improve mode in the Project | Verify the explicit `$markdown` token locks format while Improve binds mode, with exactly the requested checks and the revision rendered as a new block | `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Improve bound, Markdown locked. Step 3: first delivery fixed. Step 4: Improve header, attestation, exact checks, revision in a new block | Transcripts, CLEAR line, panel state, header label, check list, block excerpts | PASS if block, header, attestation, gate, checks and revision all hold. FAIL on wrong format, missing header or attestation, a lost mode axis, missing score, a lost or added check, a claimed save or a patch in place of a block | 1. Check format axis rule.<br>2. Check Markdown format guide.<br>3. Check revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Independent format axis, Improve binding, delivery override and the Delivery Protocol |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$improve` and format command routes and interaction limits |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown header, default format and format lock |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR gate for the Improve lane |

---

## 5. SOURCE METADATA

- Group: Project format modes
- Playbook ID: PFM-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-format-modes/markdown-format-lock-canvas.md`
