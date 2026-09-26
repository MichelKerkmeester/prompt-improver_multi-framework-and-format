---
title: "PCR-003 -- Vibe mode EVOKE gate and follow-up in the Project"
description: "Validates the $vibe lane in the Project: Creative energy, grounding-first VIBE, the component library question, EVOKE scoring, a Deliverable Block with every supplied fact, the share-back invitation and the Turn 2 path."
version: 1.0.0.0
---

# PCR-003 -- Vibe mode EVOKE gate and follow-up in the Project

`$vibe` binds the Visual lane at Creative energy in the Project router, grounds the subject first and scores with EVOKE at 40 of 50, never CLEAR or VISUAL. The Visual lane is the one creative lane with a mandatory question of its own, the component library choice, so Turn 1 is expected to ask before the brief is written.

---

## 1. OVERVIEW

The user asks for a v0 dashboard concept for a bakery owner and supplies the subject, the person, the moment, the device, the three things she checks and the feel she wants. That already covers the three grounding anchors. The Project asks its one question, which carries the component library choice, then builds a creative brief, scores it with EVOKE and renders it as a Deliverable Block. Turn 2 adds a fourth thing she checks.

### Why this matters

A visual brief fails quietly in two ways: it drifts into the generic default the user explicitly rejected, or it quietly picks a component library nobody chose. Both are visible in the block, and so is every fact the owner's morning routine depends on.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$vibe` delivers an EVOKE-scored Deliverable Block that keeps every supplied fact, injects no unchosen component library and carries the creative follow-up in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `Can you write me a v0 prompt for a dashboard concept? The owner of a small bakery chain checks daily sales, low stock and tomorrow's pre-orders for her 3 shops on an iPad at 6am before they open. It should feel warm and calm, not like a SaaS analytics tool.`
- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 is expected to ask one consolidated question that includes the component library choice: `Prompt Improver - Interactive Mode - v0.700.md` lines 205, 298 and 643 put the library question first for `$vibe`, and `Prompt Improver - Visual Mode - v0.301.md` lines 584 and 831 mark it mandatory. A Turn 1 that delivers without asking is graded as the delivery and the skipped library question is recorded as a follow-up finding, because the kernel checklist at `Custom Instructions.md` line 398 asks only for missing essentials. Command flow allows at most one interaction, the format or library question (`Prompt Improver - Interactive Mode - v0.700.md` line 405). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 413). When Turn 1 asked, Turn 2 answers no part of the question, so the interaction is spent and Turn 2 delivers with smart defaults and the unanswered choice flagged as an assumption (same file, line 413); a second question fails. The Visual lane binds with Creative energy and EVOKE (`Custom Instructions.md` line 52), EVOKE passes at 40 of 50 after a grounding pre-check on subject, audience, single job and anti-default (`Prompt Improver - Patterns and Evaluation - v0.212.md` line 302, `Prompt Improver - Visual Mode - v0.301.md` lines 60 and 347-354), and CLEAR or VISUAL on a visual UI prompt is the wrong scorer (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306 and 308). The format defaults to Markdown (`Prompt Improver - Format Guide Markdown - v0.141.md` line 438). The Deliverable Block comes before any commentary and holds only a single-line `Mode: $vibe` header carrying complexity and framework, the brief and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the EVOKE score with gate status and a short summary, does not paste the brief again and closes by inviting the user to share the generated result (lines 323, 341 and 384-388). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The brief carries every supplied fact: a dashboard concept, v0 as the target, named in the header or the body, the owner of a small bakery chain, daily sales, stock running low and tomorrow's pre-orders, her 3 shops, an iPad at 6am before the shops open, and a warm, calm feel that is not like a SaaS analytics tool. A component library instruction appears only when the user selected one (`Prompt Improver - Visual Mode - v0.301.md` lines 599-600). The UX-floor constraints that `Prompt Improver - Visual Mode - v0.301.md` lines 948-959 inject into every brief without a user request (responsive layout, visible focus, reduced motion and WCAG AA contrast) are recorded and do not decide the verdict, whether present or absent. Whether the brief names the median default it steers away from (line 352), and its word count against the 100 to 300 words set for v0 (lines 61 and 753-756), are recorded and do not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply carrying the EVOKE score and the share-back invitation with no file claimed, whose brief keeps the owner's morning, her three checks and the feel she asked for
- Pass/fail: PASS if the graded delivery is a Deliverable Block with header and attestation before any commentary, an EVOKE result, every supplied fact, no unchosen component library, the share-back invitation and no save claimed, and, when Turn 1 delivered, the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if CLEAR or VISUAL scored instead, the invitation is missing, a supplied fact is dropped or altered, a component library the user did not choose is written into the brief, commentary precedes the block, the header or attestation is missing, the brief is pasted again, a second question follows the first, a save is claimed or a revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a staff rota panel, a customer loyalty module or extra pages are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | Bind Visual at Creative energy and ask one consolidated question that includes the component library choice, or deliver through a Deliverable Block with the EVOKE score and share-back invite | No more than one question and no block before it is answered | Response transcript and Artifact panel state |
| 2 | `She also wants to see yesterday's waste per shop.` | When Turn 1 asked, deliver now: render the block with yesterday's waste per shop included and the unanswered library choice flagged as an assumption with no library injected, and reply with the EVOKE score and follow-up invite. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 fact plus yesterday's waste per shop | Every Turn 1 fact retained and yesterday's waste per shop added | Response, score line, block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked, and whether the question carried the library choice, or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade scorer, facts, library injection, follow-up, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Visual and normally asks one question carrying the library choice. Step 3 records which path Turn 1 took. Step 4 proves the graded block carries header, attestation and every supplied fact with no unchosen library, that the chat scored EVOKE and invited share-back, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, whether the Turn 1 question carried the library choice, the EVOKE score line with gate status, the Artifact panel state, a fact checklist against the graded block, any library instruction in the brief, whether the brief names a default it steers away from, its word count, the share-back sentence in chat, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, an EVOKE result, every supplied fact, no unchosen component library, the share-back invitation, no save claimed and, when Turn 1 delivered, a Turn 2 revision rendered as a new block
- **Fail**: The wrong scorer, a missing invitation, a dropped or altered fact, an unchosen component library in the brief, scope expansion, commentary before the block, a missing header or attestation, the brief pasted again in chat, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Visual binding in `Custom Instructions.md` line 52 and the scorer bans in `Prompt Improver - Patterns and Evaluation - v0.212.md` lines 306-308 when the scorer or energy is off
2. Re-check grounding, the EVOKE pre-check and the library question in `Prompt Improver - Visual Mode - v0.301.md` lines 65-86, 347-354 and 829-831 when the brief or the question is off
3. Check the follow-up rule in `Custom Instructions.md` lines 323 and 388, the Delivery Protocol in lines 367-390 and the delivery override in line 291 when the invite, the ordering or the Turn 2 block is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PCR-003 | Vibe mode EVOKE gate and follow-up in the Project | Verify the visual UI lane asks its library question, scores EVOKE, keeps every supplied fact and invites share-back | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Record path, submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Visual bound, library question or delivery. Step 3: path recorded. Step 4: EVOKE, facts, no unchosen library, invite | Transcripts, EVOKE line, panel state, fact checklist, library note, invite | PASS if block, attestation, EVOKE, facts, library rule and invite all hold. FAIL on wrong scorer, missing invite, a lost fact, an unchosen library, a second question, a claimed save or a patch in place of a block | 1. Check lane and scorer bans.<br>2. Check grounding, EVOKE and library rules.<br>3. Check follow-up, ordering and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Visual binding, follow-up rule, delivery override and the Delivery Protocol |
| [Visual Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Visual Mode - v0.301.md>) | Grounding, EVOKE pre-check, avoid-list, library question and v0 notes |
| [Visual Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Visual Mode Library - v0.110.md>) | Visual UI vocabulary and platform templates |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$vibe` route, library question, conversation flow and interaction limits |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | EVOKE threshold and scorer bans |

---

## 5. SOURCE METADATA

- Group: Project creative modes
- Playbook ID: PCR-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-creative-modes/vibe-mode-evoke-canvas.md`
