---
title: "PTX-004 -- Refine mode on an existing prompt with CLEAR and Canvas"
description: "Validates the $refine lane in the Project on a self-contradicting prompt: Standard energy, the CLEAR gate, conflicts resolved toward the user's complaint, placeholders kept and a Turn 2 revision rendered as a new block."
version: 1.0.0.0
---

# PTX-004 -- Refine mode on an existing prompt with CLEAR and Canvas

`$refine` binds the Refine lane outright in the Project router, so Standard energy runs and CLEAR guards the Deliverable Block. The supplied prompt contradicts itself twice, and the user has already said which way it fails, so the refinement has a direction to follow rather than a gap to fill.

---

## 1. OVERVIEW

The user pastes a webshop product-description prompt that produces copy that is too salesy and too long. The prompt asks for enthusiasm and understatement at once, and for about 300 words that are also short enough for mobile. A good refinement resolves both conflicts toward the complaint, keeps the template placeholders and the call to action, and invents no audience. Turn 2 narrows the call to action, which is a revision of the delivered prompt.

### Why this matters

Refinement is where a runtime either repairs the prompt the user has or rewrites it into a different one. The placeholders, the call to action and the stated complaint are the fixed points a grader can check.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$refine` delivers a CLEAR-gated Deliverable Block that resolves the supplied prompt's conflicts toward the user's complaint and keeps its placeholders, then renders the Turn 2 revision as a new block in the Project runtime
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. With no Canvas panel in the session, the reply renders the Deliverable Block as one fenced block at the start of the reply, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence, or at the single-line header when no fence opens it, and ends after the attestation footer, whether that footer sits inside the fence or on the line directly below it
- Real user request: `The prompt we use for webshop product descriptions keeps giving us copy that is too salesy and too long. Can you fix it? It asks for enthusiasm and lots of adjectives but also for a professional, understated tone, around 300 words but short enough for mobile, the materials, a call to action and "everyone" as the audience.`
- Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: the kernel checklist at `Custom Instructions.md` line 398 gathers missing essentials with one question, while `Prompt Improver - Interactive Mode - v0.700.md` line 204 routes `$refine` to the refinement focus question (lines 283-286). Command flow allows at most one interaction (same file, line 405). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 413). The Refine lane binds with Standard energy and CLEAR (`Custom Instructions.md` line 49), Standard runs at least three perspectives (`Prompt Improver - DEPTH Thinking Framework - v0.200.md` line 65), and CLEAR passes at 40 of 50 with its floors, where Correctness scores the absence of contradictions (`Prompt Improver - Patterns and Evaluation - v0.212.md` lines 214, 302 and 447). The format defaults to Markdown (`Prompt Improver - Format Guide Markdown - v0.141.md` line 438). The Deliverable Block comes before any commentary and holds only the single-line `Mode: $refine | Complexity: [level] | Framework: [Framework]` header, the prompt and the attestation footer ending `execution = did not occur | save = did not occur` (`Custom Instructions.md` lines 319-320, 372 and 377). After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].md`, the CLEAR score with gate status and a short summary, and does not paste the prompt again (lines 341 and 384-387). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The refined prompt keeps `{product_name}` and `{materials}` verbatim, keeps a call to action and keeps the materials mention. It resolves the tone conflict toward professional and understated and the length conflict toward shorter copy, since the user's complaint is too salesy and too long (`Custom Instructions.md` line 308). It does not replace "everyone" with an invented audience segment (line 335). A new length figure is a default filling a gap and is expected as an `[Assumes: ...]` note (`Prompt Improver - Interactive Mode - v0.700.md` line 502); its presence is recorded and does not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 291). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One Artifact-first reply whose block reads back as the user's prompt repaired, not replaced, and whose chat claims no file was written, then a second block with a one-sentence call to action
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block with header, prompt and attestation before any commentary, a CLEAR result, both placeholders verbatim, the call to action kept, both conflicts resolved toward the complaint and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if commentary precedes the block, the header or attestation is missing, the prompt is pasted again, the score is absent, a placeholder is renamed or dropped, the call to action is dropped, the refined prompt still asks for enthusiasm with lots of adjectives or still targets around 300 words, an audience is invented, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: an SEO keyword block or a headline field are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."` | Bind Refine at Standard energy, either deliver through a Deliverable Block or ask at most one consolidated question | No more than one question and no block before it is answered | Response transcript and Artifact panel state |
| 2 | `Keep the call to action, but make it one short sentence.` | When Turn 1 asked, complete the refinement with a one-sentence call to action, render the block and report the export-equivalent path, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries the Turn 1 refinement with the call to action limited to one short sentence | Placeholders, materials mention and resolved tone and length retained, call to action kept as one short sentence | Response, score line, both block excerpts |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered -> user: submit Turn 2 in the same conversation`
4. `artifact: read every Deliverable Block -> operator: grade gate, placeholders, conflict resolution, scope, chat shape, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Refine and either delivers or asks once. Step 3 records the first delivery. Step 4 proves the graded block keeps both placeholders and the call to action with both conflicts resolved toward the complaint, and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the CLEAR score line with gate status, the Artifact panel state, a checklist of placeholders, call to action, tone and length against the graded block, excerpts of every block showing the single-line header, prompt body and attestation footer, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A Deliverable Block before commentary with header and attestation, a reported CLEAR result, both placeholders verbatim, the call to action kept, both conflicts resolved toward the complaint, no invented audience, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: Commentary before the block, a missing header or attestation, the prompt pasted again in chat, missing score, a renamed or dropped placeholder, a dropped call to action, an unresolved conflict, an invented audience, scope expansion, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the Delivery Protocol and No Canvas panel rule in `Custom Instructions.md` lines 367-390 against the observed ordering
2. Re-check CLEAR Correctness in `Prompt Improver - Patterns and Evaluation - v0.212.md` line 214 and the floors at line 447 when a conflict survived or the score is off
3. Check intent preservation and the invention ban in `Custom Instructions.md` lines 308 and 335, and the delivery override in line 291 when Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PTX-004 | Refine mode on an existing prompt with CLEAR and Canvas | Verify `$refine` repairs the supplied prompt toward the user's complaint, keeps its placeholders and renders the revision as a new block | `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Read every block` | Step 1: packaging fixed. Step 2: Refine bound, delivery or one question. Step 3: first delivery fixed. Step 4: placeholders kept, conflicts resolved, revision in a new block | Transcripts, CLEAR line, panel state, checklist, block excerpts | PASS if block, attestation, gate, placeholders, conflict resolution and revision all hold. FAIL on commentary before the block, pasted prompt, missing score, a lost placeholder, an unresolved conflict, an invented audience, a claimed save or a patch in place of a block | 1. Check delivery ordering.<br>2. Check CLEAR Correctness.<br>3. Check intent, invention and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Refine binding, intent and invention rules, delivery override, Delivery Protocol and No Canvas panel rule |
| [DEPTH knowledge](<../../../claude project/knowledge/Prompt Improver - DEPTH Thinking Framework - v0.200.md>) | Standard energy and the perspective minimum |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode - v0.700.md>) | `$refine` route, the refinement focus question, interaction limits and the assumption format |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation - v0.212.md>) | CLEAR rubric, Correctness criteria and floors |
| [Format Guide Markdown knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide Markdown - v0.141.md>) | Markdown default and deliverable rules |

---

## 5. SOURCE METADATA

- Group: Project text modes
- Playbook ID: PTX-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-text-modes/refine-existing-prompt-canvas.md`
