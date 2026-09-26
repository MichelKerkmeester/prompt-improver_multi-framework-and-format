---
title: "STX-003 -- Short mode quick enhancement with CLEAR and export"
description: "Validates the $short lane on a one-line request: Quick energy, the CLEAR gate, a markdown export with every supplied fact and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# STX-003 -- Short mode quick enhancement with CLEAR and export

`$short` binds the Short lane outright, so Quick energy runs a lean D, P, H pass and CLEAR still guards the `.md` export. The request is one casual line with a name, a date and a tone, and nothing else to lean on.

---

## 1. OVERVIEW

The user wants a prompt for a LinkedIn post announcing a new head of design. Quick energy trims the thinking, not the gate: CLEAR still scores the result and the export-first sequence still holds. Turn 2 adds where the new hire comes from, which is a revision of the delivered prompt.

### Why this matters

A thin request tempts the runtime to fill the gaps with invented biography. The facts the user gave are few, so each one is easy to check, and anything the prompt says about the hire beyond them is an invention.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$short` delivers a CLEAR-gated markdown export at Quick energy that keeps every supplied fact and invents none, then saves the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Quick one: I need a prompt for a LinkedIn post saying we hired Priya Nair as our new head of design. She starts on October 14. Warm, please, not corporate.`
- Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: `SKILL.md` line 383 asks only when essential context is missing, while `references/interactive-mode.md` line 216 routes `$short` to the format selection question (Template 4, line 152). Command flow allows at most one interaction (`SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). The Short lane binds with Quick energy and CLEAR (`SKILL.md` lines 78 and 348), Quick runs D, P and H with one or two perspectives (`references/depth-framework.md` lines 49-53), and CLEAR still passes at 40 of 50 with its floors (`SKILL.md` lines 444-445). The format defaults to Markdown (`SKILL.md` line 408), the runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 40), the file opens with the single-line `Mode: $short | Complexity: [level] | Framework: [Framework]` header followed only by the prompt (`SKILL.md` lines 558-559) and the reply leads with the saved path, reports the CLEAR score and does not paste the prompt (`AGENTS.md` lines 61-64). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: a LinkedIn post, announcing a new head of design, the name Priya Nair, the start date Oct 14 and a warm, not corporate tone. It adds no biography the user did not give: no previous employer before Turn 2 supplies one, no invented achievement or background and no year or weekday attached to Oct 14 (`SKILL.md` line 512). Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved file reads back as a lean LinkedIn post prompt with the name, date and tone intact, then a second export that adds Spotify
- Pass/fail: PASS if the Turn 1 delivery is a verified `.md` export with the header, a CLEAR result, every supplied fact intact and nothing invented, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if output appears before saving, the reply does not lead with the saved path, the full prompt is pasted, the score is absent, the name or date is altered, a fact about Priya Nair is invented, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a second post variant or an image brief are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate` | Bind Short at Quick energy, either deliver through a verified `.md` export or ask at most one consolidated question | No more than one question and no file before it is answered | Response transcript and `export/` listing |
| 2 | `Mention that she joins us from Spotify.` | When Turn 1 asked, complete the enhancement with Spotify included, save the export and reply path-first, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: save a new export under the next number that carries every Turn 1 fact plus Spotify, and leave the delivered export unchanged | Name, date and tone retained and Spotify added as her previous employer | Response, score line, both export excerpts and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum the Turn 1 file -> operator: grade gate, facts, invention, chat shape and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Short and either delivers or asks once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the graded file carries the header, the name, the date and the tone with no invented biography, and, when Turn 1 delivered, that Turn 2 saved a new file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the CLEAR score line with gate status, `export/` listings before and after each turn, a fact checklist against the graded file, excerpts of every export showing the single-line header plus prompt body, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export with the header, a reported CLEAR result, every supplied fact intact, nothing invented, the path-first reply and a Turn 2 revision saved as a new export
- **Fail**: Output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, missing score, an altered name or date, invented biography, scope expansion, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Short binding and Quick energy in `SKILL.md` lines 78, 348 and 373 when the lane or energy is off
2. Re-check the CLEAR threshold and floors in `SKILL.md` lines 444-445 and `references/patterns-evaluation.md` lines 461-469 when the score is missing or off
3. Check the invention ban in `SKILL.md` line 512 and the revision rule in lines 421-422 when facts were added or Turn 2 edited the delivered file

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| STX-003 | Short mode quick enhancement with CLEAR and export | Verify `$short` delivers a gated markdown export with every supplied fact and nothing invented, and saves the revision as a new export | `$short linkedin post announcing we hired a new head of design, Priya Nair, she starts Oct 14, keep it warm not corporate` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Read exports, re-checksum` | Step 1: baseline known. Step 2: Short bound at Quick energy, delivery or one question. Step 3: first delivery fixed. Step 4: facts intact, revision in a new file | Transcripts, CLEAR line, export listings, fact checklist, excerpts, checksums | PASS if export, gate, facts and revision all hold. FAIL on pre-save output, a reply that does not lead with the path, pasted prompt, missing score, an altered fact, invented biography or an in-place edit | 1. Check Short binding.<br>2. Check CLEAR thresholds.<br>3. Check invention ban and revision rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, naming, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Short binding, interaction limits, CLEAR summary, header, invention ban and revision rule |
| [`depth-framework.md`](../../references/depth-framework.md) | Quick energy phases and perspectives |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$short` state route and the format selection template |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR rubric, floors and repair rules |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown export file rules |

---

## 5. SOURCE METADATA

- Group: Skill text modes
- Playbook ID: STX-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-text-modes/short-quick-enhancement-export.md`
