---
title: "STX-004 -- Refine mode on an existing prompt with CLEAR and export"
description: "Validates the $refine lane on a self-contradicting prompt: Standard energy, the CLEAR gate, conflicts resolved toward the user's complaint, placeholders kept and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# STX-004 -- Refine mode on an existing prompt with CLEAR and export

`$refine` binds the Refine lane outright, so Standard energy runs and CLEAR guards the `.md` export. The supplied prompt contradicts itself twice, and the user has already said which way it fails, so the refinement has a direction to follow rather than a gap to fill.

---

## 1. OVERVIEW

The user pastes a webshop product-description prompt that produces copy that is too salesy and too long. The prompt asks for enthusiasm and understatement at once, and for about 300 words that are also short enough for mobile. A good refinement resolves both conflicts toward the complaint, keeps the template placeholders and the call to action, and invents no audience. Turn 2 narrows the call to action, which is a revision of the delivered prompt.

### Why this matters

Refinement is where a runtime either repairs the prompt the user has or rewrites it into a different one. The placeholders, the call to action and the stated complaint are the fixed points a grader can check.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$refine` delivers a CLEAR-gated markdown export that resolves the supplied prompt's conflicts toward the user's complaint and keeps its placeholders, then saves the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `The prompt we use for webshop product descriptions keeps giving us copy that is too salesy and too long. Can you fix it? It asks for enthusiasm and lots of adjectives but also for a professional, understated tone, around 300 words but short enough for mobile, the materials, a call to action and "everyone" as the audience.`
- Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: `SKILL.md` line 383 asks only when essential context is missing, while `references/interactive-mode.md` line 218 routes `$refine` to the refinement focus question (line 311). Command flow allows at most one interaction (`SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). The Refine lane binds with Standard energy and CLEAR (`SKILL.md` lines 77 and 347), Standard runs at least three perspectives (`references/depth-framework.md` lines 54-58), and CLEAR passes at 40 of 50 with its floors, where Correctness scores the absence of contradictions (`SKILL.md` lines 444-445, `references/patterns-evaluation.md` line 228). The format defaults to Markdown (`SKILL.md` line 408), the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), the file opens with the single-line `Mode: $refine | Complexity: [level] | Framework: [Framework]` header followed only by the prompt (`SKILL.md` lines 558-559) and the reply leads with the saved path, reports the CLEAR score and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The refined prompt keeps `{product_name}` and `{materials}` verbatim, keeps a call to action and keeps the materials mention. It resolves the tone conflict toward professional and understated and the length conflict toward shorter copy, since the user's complaint is too salesy and too long (`SKILL.md` line 478). It does not replace "everyone" with an invented audience segment (`SKILL.md` line 512). A new length figure is a default filling a gap and is expected as an `[Assumes: ...]` note (`SKILL.md` line 504); its presence is recorded and does not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved file reads back as the user's prompt repaired, not replaced, then a second export with a one-sentence call to action
- Pass/fail: PASS if the Turn 1 delivery is a verified `.md` export with the header, a CLEAR result, both placeholders verbatim, the call to action kept and both conflicts resolved toward the complaint, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if output appears before saving, the reply does not lead with the saved path, the full prompt is pasted, the score is absent, a placeholder is renamed or dropped, the call to action is dropped, the refined prompt still asks for enthusiasm with lots of adjectives or still targets around 300 words, an audience is invented, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: an SEO keyword block or a headline field are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."` | Bind Refine at Standard energy, either deliver through a verified `.md` export or ask at most one consolidated question | No more than one question and no file before it is answered | Response transcript and `export/` listing |
| 2 | `Keep the call to action, but make it one short sentence.` | When Turn 1 asked, complete the refinement with a one-sentence call to action, save the export and reply path-first, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: save a new export under the next number that carries the Turn 1 refinement with the call to action limited to one short sentence, and leave the delivered export unchanged | Placeholders, materials mention and resolved tone and length retained, call to action kept as one short sentence | Response, score line, both export excerpts and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum the Turn 1 file -> operator: grade gate, placeholders, conflict resolution, scope, chat shape and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Refine and either delivers or asks once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the graded file keeps both placeholders and the call to action with both conflicts resolved toward the complaint, and, when Turn 1 delivered, that Turn 2 saved a new file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the CLEAR score line with gate status, `export/` listings before and after each turn, a checklist of placeholders, call to action, tone and length against the graded file, excerpts of every export showing the single-line header plus prompt body, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export with the header, a reported CLEAR result, both placeholders verbatim, the call to action kept, both conflicts resolved toward the complaint, no invented audience, the path-first reply and a Turn 2 revision saved as a new export
- **Fail**: Output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, missing score, a renamed or dropped placeholder, a dropped call to action, an unresolved conflict, an invented audience, scope expansion, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Refine binding in `SKILL.md` lines 77 and 347 when the lane or energy is off
2. Re-check CLEAR Correctness in `references/patterns-evaluation.md` line 228 and the floors in `SKILL.md` lines 444-445 when a conflict survived or the score is off
3. Check intent preservation and the invention ban in `SKILL.md` lines 478 and 512, and the revision rule in lines 421-422

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| STX-004 | Refine mode on an existing prompt with CLEAR and export | Verify `$refine` repairs the supplied prompt toward the user's complaint, keeps its placeholders and saves the revision as a new export | `$refine Our webshop product-description prompt keeps producing copy that is too salesy and too long. Here it is: "You are an expert copywriter. Write a product description for {product_name}. Be enthusiastic and exciting!! Use lots of adjectives. Keep it professional and understated. Mention the materials: {materials}. Length: around 300 words but short enough to read on mobile. Include a call to action. Target audience: everyone."` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Read exports, re-checksum` | Step 1: baseline known. Step 2: Refine bound, delivery or one question. Step 3: first delivery fixed. Step 4: placeholders kept, conflicts resolved, revision in a new file | Transcripts, CLEAR line, export listings, checklist, excerpts, checksums | PASS if export, gate, placeholders, conflict resolution and revision all hold. FAIL on pre-save output, a reply that does not lead with the path, pasted prompt, missing score, a lost placeholder, an unresolved conflict, an invented audience or an in-place edit | 1. Check Refine binding.<br>2. Check CLEAR Correctness.<br>3. Check intent, invention and revision rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Refine binding, interaction limits, CLEAR summary, header, intent, invention and revision rules |
| [`depth-framework.md`](../../references/depth-framework.md) | Standard energy and the perspective minimum |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$refine` state route and the refinement focus question |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR rubric, Correctness criteria and floors |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown export file rules |

---

## 5. SOURCE METADATA

- Group: Skill text modes
- Playbook ID: STX-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-text-modes/refine-existing-prompt-export.md`
