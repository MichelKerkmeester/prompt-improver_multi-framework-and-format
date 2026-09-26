---
title: "SFM-003 -- Independent $markdown format lock with Improve mode"
description: "Validates that the long-form $markdown token locks the format axis while $improve wins the mode axis, producing a markdown export with every requested check and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# SFM-003 -- Independent $markdown format lock with Improve mode

`$improve` and `$markdown` live on different axes. Markdown is already the default format, so this scenario proves that an explicit long-form `$markdown` token still binds as a format lock and never competes with `$improve` for the mode.

---

## 1. OVERVIEW

The user's engineering team reviews pull requests with a one-line AI prompt and wants it to check three named things in a senior reviewer's voice. `$improve` binds the Improve lane at Standard energy with CLEAR, and `$markdown` locks the file to Markdown and loads the Markdown format guide. Turn 2 adds a fourth check, which is a revision of the delivered prompt.

### Why this matters

A format token that matches the default is easy to treat as noise, or worse, as the mode. The export must still honor the lock, carry the Improve mode in its header and keep the review scope to exactly what the team named.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$markdown` locks format independently while `$improve` binds the mode, delivering a CLEAR-gated markdown export with exactly the requested checks, then saving the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `Our engineers use "Review this code and tell me what's wrong." as the AI code review prompt on pull requests. Please improve it, in Markdown: it should check for security issues, missing tests and unclear naming, and explain the why like a senior reviewer. The diff gets pasted in below the prompt.`
- Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved `.md` file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: `SKILL.md` line 383 asks only when essential context is missing, while `references/interactive-mode.md` line 217 routes `$improve` to the format selection question and line 223 routes a format command to the comprehensive question. Command flow allows at most one interaction (`SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). Mode and format are independent axes (`SKILL.md` lines 71 and 99): the Improve lane binds with Standard energy and CLEAR (lines 76 and 346) and the explicit `$markdown` token locks the format to Markdown (line 85) and loads the Markdown format guide (line 335), so a Turn 1 question asking which mode to use means the format token stole the mode axis. A Turn 1 question asking which format to use is recorded as a follow-up finding and does not decide the verdict, because `references/interactive-mode.md` line 217 still routes `$improve` to format selection while `SKILL.md` line 71 gives the format axis to the format command. CLEAR passes at 40 of 50 with its floors (lines 444-445). The runtime saves `export/[###] - enhanced-[description].md` before replying (`AGENTS.md` lines 34 and 47), the file opens with the single-line `Mode: $improve | Complexity: [level] | Framework: [Framework]` header followed only by the prompt (`SKILL.md` lines 558-559, `assets/format-guide-markdown.md` lines 118-124), and the reply leads with the path, reports the CLEAR result and does not paste the prompt (`AGENTS.md` lines 61-64). A header labelled `$markdown` is recorded as a follow-up finding, since the Markdown guide names the mode in that slot. Path-first means the first line of the reply names the saved `export/` path, and a `Saved:` label or bold markup on that line does not change it. The enhanced prompt carries every supplied fact: AI code review on pull requests for an engineering team, the three checks security issues, missing tests and unclear naming, comments in a senior reviewer's voice that explain why and not just what, and the diff pasted below the prompt as the input. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved `.md` file reads back as a senior-reviewer code review prompt scoped to the three named checks, then a second export that adds TODO flagging
- Pass/fail: PASS if the Turn 1 delivery is a verified `.md` export with the header, a CLEAR result and exactly the three requested checks with the reviewer voice and diff input kept, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if the file is not `.md`, the header is missing, the mode or format axis was lost, the score is missing, a requested check or the reviewer voice is dropped, output appears before saving, the reply does not lead with the saved path, the full prompt is pasted, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a performance review, an approve or reject verdict, severity scores or, before Turn 2 asks for it, TODO flagging are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.` | Bind Improve, lock Markdown, either deliver through a verified `.md` export or ask at most one consolidated question | Format locked to Markdown regardless of any question, no question about the mode | Response transcript and `export/` listing |
| 2 | `Also have it flag any TODO comments left in the diff.` | When Turn 1 asked, complete the enhancement with TODO flagging included, save the `.md` export and reply path-first, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: save a new `.md` export under the next number that carries the three Turn 1 checks, the reviewer voice and the diff input plus TODO flagging, and leave the delivered export unchanged | Markdown lock retained, three checks, reviewer voice and diff input kept and TODO flagging added | Response, score line, both export excerpts and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: read every saved .md export and re-checksum the Turn 1 file -> operator: grade format lock, header, checks, scope, chat shape and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Improve and locks Markdown, delivering or asking once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the graded file is Markdown with the Improve header and exactly the requested checks, and, when Turn 1 delivered, that Turn 2 saved a new `.md` file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the CLEAR score line with gate status, `export/` listings before and after each turn, the header label used, a checklist of the requested checks against the graded file, excerpts of every export showing the single-line header plus prompt body, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A verified `.md` export with the Improve header, a reported CLEAR result, exactly the three requested checks with the reviewer voice and diff input, the path-first reply and a Turn 2 revision saved as a new `.md` export
- **Fail**: A non-Markdown file, a missing header, format competing with mode, missing score, a dropped check or reviewer voice, scope expansion, output shown before saving, a reply that does not lead with the saved path, full prompt pasted in chat, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the independent format axis in `SKILL.md` lines 71, 85 and 99 and the format-guide load rule in line 335 when the format or mode was lost
2. Re-check the Markdown header and file rules in `assets/format-guide-markdown.md` lines 114-133 when the header or file content is off
3. Check the revision rule in `SKILL.md` lines 421-422 and `AGENTS.md` line 70 when Turn 2 edited the delivered file or saved nothing

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFM-003 | Independent $markdown format lock with Improve mode | Verify the explicit `$markdown` token locks format while Improve binds mode, with exactly the requested checks and the revision saved as a new export | `$improve $markdown Our engineering team uses this prompt for AI code review on pull requests: "Review this code and tell me what's wrong." It needs to check for security issues, missing tests and unclear naming, and comment like a senior reviewer who explains why, not just what. We paste the diff in below the prompt.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Read exports, re-checksum` | Step 1: baseline known. Step 2: Improve bound, Markdown locked. Step 3: first delivery fixed. Step 4: Improve header, exact checks, revision in a new file | Transcripts, CLEAR line, export listings, header label, check list, excerpts, checksums | PASS if the .md export, header, gate, checks and revision all hold. FAIL on wrong format, missing header, a lost axis, missing score, a lost or added check or an in-place edit | 1. Check format axis rule.<br>2. Check Markdown format guide.<br>3. Check revision rule. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, `.md` naming, chat response shape and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Independent format axis, Improve binding, format-guide loading, header and revision rule |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$improve` and format command state routes |
| [`format-guide-markdown.md`](../../assets/format-guide-markdown.md) | Markdown header and file content rules |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR gate for the Improve lane |

---

## 5. SOURCE METADATA

- Group: Skill format modes
- Playbook ID: SFM-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-format-modes/markdown-format-lock-export.md`
