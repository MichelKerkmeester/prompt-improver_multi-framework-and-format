---
title: "SCR-003 -- Vibe mode EVOKE gate and follow-up"
description: "Validates the $vibe lane: Creative energy, grounding-first VIBE, the component library question, EVOKE scoring, a markdown export with every supplied fact, the share-back invitation and the Turn 2 path."
version: 1.0.0.0
---

# SCR-003 -- Vibe mode EVOKE gate and follow-up

`$vibe` binds the Visual lane at Creative energy, grounds the subject first and scores with EVOKE at 40 of 50, never CLEAR or VISUAL. The Visual lane is the one creative lane with a mandatory question of its own, the component library choice, so Turn 1 is expected to ask before the brief is written.

---

## 1. OVERVIEW

The user asks for a v0 dashboard concept for a bakery owner and supplies the subject, the person, the moment, the device, the three things she checks and the feel she wants. That already covers the three grounding anchors. The runtime asks its one question, which carries the component library choice, then builds a creative brief, scores it with EVOKE and saves it. Turn 2 adds a fourth thing she checks.

### Why this matters

A visual brief fails quietly in two ways: it drifts into the generic default the user explicitly rejected, or it quietly picks a component library nobody chose. Both are visible in the saved file, and so is every fact the owner's morning routine depends on.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$vibe` delivers an EVOKE-scored markdown export that keeps every supplied fact, injects no unchosen component library and carries the creative follow-up
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Can you write me a v0 prompt for a dashboard concept? The owner of a small bakery chain checks daily sales, low stock and tomorrow's pre-orders for her 3 shops on an iPad at 6am before they open. It should feel warm and calm, not like a SaaS analytics tool.`
- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 is expected to ask one consolidated question that includes the component library choice: `references/interactive-mode.md` lines 219, 312 and 657 put the library question first for `$vibe`, and `references/visual-mode.md` lines 598 and 845 mark it mandatory. A Turn 1 that delivers without asking is graded as the delivery and the skipped library question is recorded as a follow-up finding, because `SKILL.md` line 383 asks only when essential context is missing. Command flow allows at most one interaction, the format or library question (`references/interactive-mode.md` line 419, `SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). When Turn 1 asked, Turn 2 answers no part of the question, so the interaction is spent and Turn 2 delivers with smart defaults and the unanswered choice flagged as an assumption (`SKILL.md` line 404); a second question fails. The Visual lane binds with Creative energy and EVOKE (`SKILL.md` lines 80, 350 and 376), EVOKE passes at 40 of 50 after a grounding pre-check on subject, audience, single job and anti-default (`SKILL.md` lines 446-447, `references/visual-mode.md` lines 74 and 357-368), and CLEAR or VISUAL on a visual UI prompt is the wrong scorer (`SKILL.md` lines 515 and 517). The format defaults to Markdown (`SKILL.md` line 408), the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), the file opens with a single-line `Mode: $vibe` header carrying complexity and framework followed only by the brief (`SKILL.md` lines 558-559), and the reply leads with the path, reports the EVOKE score, does not paste the brief (`AGENTS.md` lines 61-64) and closes by inviting the user to share the generated result (`SKILL.md` lines 439 and 502). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The brief carries every supplied fact: a dashboard concept, v0 as the target, named in the header or the body, the owner of a small bakery chain, daily sales, stock running low and tomorrow's pre-orders, her 3 shops, an iPad at 6am before the shops open, and a warm, calm feel that is not like a SaaS analytics tool. A component library instruction appears only when the user selected one (`references/visual-mode.md` lines 613-614). The UX-floor constraints that `references/visual-mode.md` lines 962-973 inject into every brief without a user request (responsive layout, visible focus, reduced motion and WCAG AA contrast) are recorded and do not decide the verdict, whether present or absent. Whether the brief names the median default it steers away from (`references/visual-mode.md` line 366), and its word count against the 100 to 300 words set for v0 (lines 75 and 767-770), are recorded and do not decide the verdict. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply carrying the EVOKE score and the share-back invitation, whose saved brief keeps the owner's morning, her three checks and the feel she asked for
- Pass/fail: PASS if the graded delivery is a verified `.md` export with the header, an EVOKE result, every supplied fact, no unchosen component library and the share-back invitation, and, when Turn 1 delivered, the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if CLEAR or VISUAL scored instead, the invitation is missing, a supplied fact is dropped or altered, a component library the user did not choose is written into the brief, output appears before saving, the reply does not lead with the saved path, the brief is pasted, a second question follows the first, the delivered export is edited in place or a revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a staff rota panel, a customer loyalty module or extra pages are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | Bind Visual at Creative energy and ask one consolidated question that includes the component library choice, or deliver through a verified `.md` export with the EVOKE score and share-back invite | No more than one question and no file before it is answered | Response transcript and `export/` listing |
| 2 | `She also wants to see yesterday's waste per shop.` | When Turn 1 asked, deliver now: save the export with yesterday's waste per shop included and the unanswered library choice flagged as an assumption with no library injected, and reply path-first with the EVOKE score and follow-up invite. When Turn 1 delivered, treat this as a revision: save a new export under the next number that carries every Turn 1 fact plus yesterday's waste per shop, and leave the delivered export unchanged | Every Turn 1 fact retained and yesterday's waste per shop added | Response, score line, export excerpts and, when Turn 1 delivered, a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked, and whether the question carried the library choice, or delivered and checksum the export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum any Turn 1 file -> operator: grade scorer, facts, library injection, follow-up and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Visual and normally asks one question carrying the library choice. Step 3 records which path Turn 1 took. Step 4 proves the graded file carries the header and every supplied fact with no unchosen library, that the reply scored EVOKE and invited share-back, and, when Turn 1 delivered, that Turn 2 saved a new file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, whether the Turn 1 question carried the library choice, the EVOKE score line with gate status, `export/` listings before and after each turn, a fact checklist against the graded file, any library instruction in the brief, whether the brief names a default it steers away from, its word count, the share-back sentence in chat and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export with the header, an EVOKE result, every supplied fact, no unchosen component library, the share-back invitation, the path-first reply and, when Turn 1 delivered, a Turn 2 revision saved as a new export
- **Fail**: The wrong scorer, a missing invitation, a dropped or altered fact, an unchosen component library in the brief, scope expansion, output shown before saving, a reply that does not lead with the saved path, the brief pasted in chat, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Visual binding and scorer map in `SKILL.md` lines 80, 350 and 515-517 when the scorer or energy is off
2. Re-check grounding, the EVOKE pre-check and the library question in `references/visual-mode.md` lines 79-100, 357-368 and 843-870 when the brief or the question is off
3. Check the follow-up rule in `SKILL.md` line 502 and the revision rule in lines 421-422 when the invite is absent or Turn 2 edited the delivered file

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SCR-003 | Vibe mode EVOKE gate and follow-up | Verify the visual UI lane asks its library question, scores EVOKE, keeps every supplied fact and invites share-back | `$vibe dashboard concept for v0: the owner of a small bakery chain checks daily sales, stock that is running low and tomorrow's pre-orders across her 3 shops. She uses it on an iPad at 6am before the shops open. Make it feel warm and calm, not like a SaaS analytics tool.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Record path, submit Turn 2` -> 4. `Read saved exports` | Step 1: baseline known. Step 2: Visual bound, library question or delivery. Step 3: path recorded. Step 4: EVOKE, facts, no unchosen library, invite | Transcripts, EVOKE line, export listings, fact checklist, library note, invite | PASS if export, EVOKE, facts, library rule and invite all hold. FAIL on wrong scorer, missing invite, a lost fact, an unchosen library, a second question or an in-place edit | 1. Check lane and scorer map.<br>2. Check grounding, EVOKE and library rules.<br>3. Check follow-up and revision rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Visual binding, scorer map, interaction limits, follow-up and revision rules |
| [`visual-mode.md`](../../references/visual-mode.md) | Grounding, EVOKE pre-check, avoid-list, library question and v0 notes |
| [`visual-mode-library.md`](../../assets/visual-mode-library.md) | Visual UI vocabulary and platform templates |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$vibe` state route, library question and conversation flow |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | EVOKE threshold and grounding pre-check |

---

## 5. SOURCE METADATA

- Group: Skill creative modes
- Playbook ID: SCR-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-creative-modes/vibe-mode-evoke-export.md`
