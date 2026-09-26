---
title: "STX-005 -- Raw mode cleanup without scoring and export"
description: "Validates the $raw lane: no DEPTH, no question and no scorer, an immediate markdown export with every supplied constraint, and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# STX-005 -- Raw mode cleanup without scoring and export

`$raw` binds Raw mode outright: no DEPTH phases, no clarifying question and no scorer. The export-first sequence still holds, so Turn 1 must save a cleaned prompt and reply with its path, with nothing asked first and no score reported.

---

## 1. OVERVIEW

The user dictates a rough instruction for ChatGPT and asks for it cleaned up. Raw mode is the one lane that allows zero interactions and runs no gate, which makes it the lane where a runtime that asks anyway, or scores anyway, is plainly visible. Turn 2 adds a closing item, which is a revision of the delivered prompt.

### Why this matters

Raw is an explicit request to skip the machinery. A question or a score on this lane means the command did not bind, and a cleanup that adds sections turns a passthrough into an enhancement the user did not ask for.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$raw` saves a cleaned markdown export immediately, with no question, no DEPTH and no score, keeps every supplied constraint, then saves the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Just tidy this up so I can paste it into ChatGPT, no questions: summarise the attached quarterly sales report for the exec team in bullet points, highlight regions that missed target, don't make up numbers and keep it to one page.`
- Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session and then inspect both replies and every saved file
- Expected signals: Turn 1 is the graded delivery and must deliver: Raw mode allows zero interactions (`SKILL.md` line 403), bypasses the question and the wait (line 384) and skips questions and validation (`AGENTS.md` line 181), so any Turn 1 question is a failure. Raw runs no DEPTH and no scorer (`SKILL.md` lines 74, 344 and 372; `references/interactive-mode.md` lines 307 and 655), so the reply reports no CLEAR, EVOKE or VISUAL score and no gate status; a score line on a Raw delivery is the wrong scorer for the lane, whose scorer is none (`SKILL.md` line 190). The export-first sequence still applies to every enhanced prompt (`AGENTS.md` line 34): the runtime saves `export/[###] - enhanced-[description].md` before replying, the file opens with a single-line `Mode:` header followed only by the prompt (`SKILL.md` lines 558-559) and the reply leads with the saved path and does not paste the prompt (`AGENTS.md` lines 61 and 64). The header's framework value is recorded and not graded, since Raw uses no framework (`SKILL.md` line 344). Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The cleaned prompt carries every supplied constraint: ChatGPT as the target, named in the header or the body, a summary of the attached quarterly sales report, the exec team as the audience, bullet points, highlighted regions that missed target, no invented numbers and a one-page maximum. It adds no section the user did not ask for, and before Turn 2 it does not ask for the worst-selling products. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band, or none, is recorded and never decides a verdict. On Turn 2, whether the reply carries a score line is recorded and not graded, because no source says a follow-up without a command keeps the Raw binding
- Desired user-visible outcome: One immediate path-first reply with no score, whose saved file reads back as the user's instruction cleaned up, then a second export that ends with the three worst-selling products
- Pass/fail: PASS if Turn 1 saves a verified `.md` export with the header and every supplied constraint, asks nothing and reports no score, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if Turn 1 asks a question, reports a score or gate status, shows output before saving, does not lead with the saved path, pastes the full prompt, drops or alters a constraint, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a recommendations section, a chart request or a forecast are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page` | Bind Raw, ask nothing, run no scorer, save a verified `.md` export and reply path-first | No question, no score line, one new export | Response transcript and `export/` listing |
| 2 | `Also ask it to end with the three products that sold worst.` | Treat this as a revision: save a new export under the next number that carries every Turn 1 constraint and ends with the three worst-selling products, and leave the delivered export unchanged | Every Turn 1 constraint retained and the closing item added | Response, both export excerpts and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: confirm Turn 1 asked nothing and reported no score, and checksum the saved export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum the Turn 1 file -> operator: grade Raw binding, constraints, scope, chat shape and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Raw and saves an export with no question and no score. Step 3 fixes the checksum of the first delivery. Step 4 proves the graded file carries the header and every supplied constraint with nothing added, and that Turn 2 saved a new file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, `export/` listings before and after each turn, a constraint checklist against the graded file, excerpts of every export showing the single-line header plus prompt body, the Turn 1 checksum before and after Turn 2, a note of any score line on either turn and the verdict.

### Pass / fail

- **Pass**: An immediate verified `.md` export with the header, no question, no score, every supplied constraint intact, no scope expansion, the path-first reply and a Turn 2 revision saved as a new export
- **Fail**: A Turn 1 question, a score or gate status on the Raw delivery, output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, a dropped or altered constraint, scope expansion, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the Raw binding in `SKILL.md` lines 74, 344 and 403 and the escalation note in `AGENTS.md` line 181 when Turn 1 asked or scored
2. Check the export-first sequence in `AGENTS.md` lines 34-42 when no file was saved before the reply
3. Check the revision rule in `SKILL.md` lines 421-422 and `AGENTS.md` line 70 when Turn 2 edited the delivered file or saved nothing

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| STX-005 | Raw mode cleanup without scoring and export | Verify `$raw` saves a cleaned export at once with no question and no score, and saves the revision as a new export | `$raw clean this up so I can paste it into ChatGPT: summarise the attached quarterly sales report for the exec team, bullet points, highlight regions that missed target, dont make up numbers, max 1 page` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Read exports, re-checksum` | Step 1: baseline known. Step 2: Raw bound, no question, no score, export saved. Step 3: first delivery fixed. Step 4: constraints intact, revision in a new file | Transcripts, export listings, constraint checklist, excerpts, checksums | PASS if export, Raw binding, constraints and revision all hold. FAIL on a question, a score line, pre-save output, a reply that does not lead with the path, a lost constraint, scope expansion or an in-place edit | 1. Check Raw binding.<br>2. Check export-first sequence.<br>3. Check revision rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, Raw escalation note, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Raw binding, zero interactions, no scorer, header and revision rule |
| [`depth-framework.md`](../../references/depth-framework.md) | Raw energy with no phases and no perspectives |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$raw` command detection and the Raw conversation flow |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown export file rules |

---

## 5. SOURCE METADATA

- Group: Skill text modes
- Playbook ID: STX-005
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-text-modes/raw-cleanup-no-scoring-export.md`
