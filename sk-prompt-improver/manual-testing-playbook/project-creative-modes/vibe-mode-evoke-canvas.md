---
title: "PCR-003 -- Vibe mode EVOKE gate and follow-up in the Project"
description: "Validates the $vibe lane in the Project: Creative energy, grounding-first VIBE, the component library default as an open item, EVOKE scoring, a Deliverable Block with every supplied fact, the share-back invitation and the Turn 2 path."
version: 1.0.1.0
---

# PCR-003 -- Vibe mode EVOKE gate and follow-up in the Project

`$vibe` binds the Visual lane at Creative energy in the Project router, grounds the subject first and scores with EVOKE at 40 of 50, never CLEAR or VISUAL. The component library is the Visual lane's one creative choice, and it is never a question: Turn 1 delivers with no library and lists the choice as an open item.

---

## 1. OVERVIEW

The user asks for a v0 dashboard concept for a bakery owner and supplies the subject, the person, the moment, the device, the three things she checks and the feel she wants. That already covers the three grounding anchors. The Project builds a creative brief with no component library, scores it with EVOKE, renders it as a Deliverable Block and lists the library choice as an open item. Turn 2 adds a fourth thing she checks.

### Why this matters

A visual brief fails quietly in two ways: it drifts into the generic default the user explicitly rejected, or it quietly picks a component library nobody chose. Both are visible in the block, and so is every fact the owner's morning routine depends on.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$vibe` delivers an EVOKE-scored Deliverable Block that keeps every supplied fact, injects no unchosen component library and carries the creative follow-up in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. The reply renders the Deliverable Block as one bare code fence at the start of the reply, holding only the prompt, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it
- Real user request: `Can you write me a v0 prompt for a dashboard concept? The owner of a small bakery chain checks daily sales, low stock and tomorrow's pre-orders for her 3 shops on an iPad at 6am before they open. It should feel warm and calm, not like a SaaS analytics tool.`
- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 delivers with no question first: the component library is a soft gap, so the runtime defaults to none, writes no library into the brief and lists the library choice as a numbered open item after the fence (`Prompt Improver - Visual Mode.md` Component Library Default, `Prompt Improver - Interactive Mode.md` What Blocks And What Defaults). A Turn 1 that asks anything, a library question included, fails for a soft-gap question before the deliverable. The Visual lane binds with Creative energy and EVOKE (`Custom Instructions.md` line 52), EVOKE passes at 40 of 50 after a grounding pre-check on subject, audience, single job and anti-default (`Prompt Improver - Patterns and Evaluation.md` line 302, `Prompt Improver - Visual Mode.md` lines 60 and 347-354), and CLEAR or VISUAL on a visual UI prompt is the wrong scorer (`Prompt Improver - Patterns and Evaluation.md` lines 306 and 308). The format defaults to Markdown (`Prompt Improver - Format Guide Markdown.md` line 453). The reply opens with one bare code fence, no language tag, holding only the brief; the single-line `Mode: $vibe` header carrying complexity and framework follows the fence in chat (`Custom Instructions.md` section 6). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the EVOKE score with gate status and a short summary, does not paste the brief again and closes by inviting the user to share the generated result (lines 323, 341 and 388-392). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The brief carries every supplied fact: a dashboard concept, v0 as the target, named in the header or the body, the owner of a small bakery chain, daily sales, stock running low and tomorrow's pre-orders, her 3 shops, an iPad at 6am before the shops open, and a warm, calm feel that is not like a SaaS analytics tool. A component library instruction appears only when the user selected one (`Prompt Improver - Visual Mode.md` lines 599-600). The UX-floor constraints that `Prompt Improver - Visual Mode.md` lines 949-960 inject into every brief without a user request (responsive layout, visible focus, reduced motion and WCAG AA contrast) are recorded and do not decide the verdict, whether present or absent. Whether the brief names the median default it steers away from (line 352), and its word count against the 100 to 300 words set for v0 (lines 61 and 753-756), are recorded and do not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 128). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One fence-first reply carrying the EVOKE score and the share-back invitation with no file claimed, whose brief keeps the owner's morning, her three checks and the feel she asked for
- Pass/fail: PASS if the graded delivery is a Deliverable Block as a bare fence before any commentary, with the header in chat after it, an EVOKE result, every supplied fact, no unchosen component library, the share-back invitation and no save claimed, and, when Turn 1 delivered, the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if CLEAR or VISUAL scored instead, the invitation is missing, a supplied fact is dropped or altered, a component library the user did not choose is written into the brief, commentary precedes the block, the chat header is missing or anything besides the prompt sits in the fence, the brief is pasted again, a question comes before the deliverable, a save is claimed or a revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a staff rota panel, a customer loyalty module or extra pages are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | Bind Visual at Creative energy and deliver through a Deliverable Block with no component library, the EVOKE score, the library choice as an open item and the share-back invite | No question before the block and no library in the brief | Response transcript and the opening fence |
| 2 | `She also wants to see yesterday's waste per shop.` | Treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 fact plus yesterday's waste per shop | Every Turn 1 fact retained and yesterday's waste per shop added | Response, score line, block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 delivered with no question and listed the library choice as an open item -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade scorer, facts, library injection, follow-up, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Visual and delivers with the library choice listed as an open item. Step 3 records the Turn 1 delivery. Step 4 proves the graded block carries chat header, a prompt-only fence and every supplied fact with no unchosen library, that the chat scored EVOKE and invited share-back, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, whether Turn 1 asked anything, whether the library open item appears, the EVOKE score line with gate status, the opening fence, a fact checklist against the graded block, any library instruction in the brief, whether the brief names a default it steers away from, its word count, the share-back sentence in chat, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block as a bare fence before commentary, with the header in chat after it, an EVOKE result, every supplied fact, no unchosen component library, the share-back invitation, no save claimed and, when Turn 1 delivered, a Turn 2 revision rendered as a new block
- **Fail**: The wrong scorer, a missing invitation, a dropped or altered fact, an unchosen component library in the brief, scope expansion, commentary before the block, a tagged fence or one holding more than the prompt, a missing chat header line or open items, a soft-gap question before the deliverable, the brief pasted again in chat, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Visual binding in `Custom Instructions.md` line 52 and the scorer bans in `Prompt Improver - Patterns and Evaluation.md` lines 306-308 when the scorer or energy is off
2. Re-check grounding, the EVOKE pre-check and the library default in `Prompt Improver - Visual Mode.md` lines 65-86, 347-354 and 829-831 when the brief or the library handling is off
3. Check the follow-up rule in `Custom Instructions.md` lines 160 and 237, the Delivery Protocol in lines 204-433 and the delivery override in line 128 when the invite, the ordering or the Turn 2 block is off

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PCR-003 | Vibe mode EVOKE gate and follow-up in the Project | Verify the visual UI lane lists its library choice as an open item, scores EVOKE, keeps every supplied fact and invites share-back | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Record path, submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Visual bound, delivery with the library open item. Step 3: path recorded. Step 4: EVOKE, facts, no unchosen library, invite | Transcripts, EVOKE line, fence state, fact checklist, library note, invite | PASS if block, prompt-only fence, EVOKE, facts, library rule and invite all hold. FAIL on wrong scorer, missing invite, a lost fact, an unchosen library, a question before delivery, a claimed save or a patch in place of a block | 1. Check lane and scorer bans.<br>2. Check grounding, EVOKE and library rules.<br>3. Check follow-up, ordering and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Visual binding, follow-up rule, delivery override and the Delivery Protocol |
| [Visual Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Visual Mode.md>) | Grounding, EVOKE pre-check, avoid-list, library default and v0 notes |
| [Visual Mode Library knowledge](<../../../claude project/knowledge/Prompt Improver - Assets - Visual Mode Library.md>) | Visual UI vocabulary and platform templates |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | `$vibe` route, library default, conversation flow and interaction limits |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | EVOKE threshold and scorer bans |

---

## 5. SOURCE METADATA

- Group: Project creative modes
- Playbook ID: PCR-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-creative-modes/vibe-mode-evoke-canvas.md`
