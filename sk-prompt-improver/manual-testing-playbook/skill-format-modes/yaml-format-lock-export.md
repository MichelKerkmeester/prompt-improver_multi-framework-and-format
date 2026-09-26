---
title: "SFM-002 -- Independent $yaml format lock with Text mode"
description: "Validates that $yaml locks the format axis while $text wins the mode axis, producing a valid YAML export with every requested field, the overhead report and a Turn 2 revision saved under the next number."
version: 1.0.0.0
---

# SFM-002 -- Independent $yaml format lock with Text mode

`$text` and `$yaml` live on different axes. The mode command binds the Text lane and the format command locks the output to YAML, so the export is a `.yaml` file whose payload parses and whose fields are exactly the ones the user listed.

---

## 1. OVERVIEW

The user wants a data-extraction prompt for supplier invoices and names every field, the null rule and the downstream consumer. The Text lane runs at Standard energy with CLEAR while the YAML lock shapes the file: a single-line `Mode:` header, a payload below it that parses as YAML and no Markdown inside. Turn 2 adds a VAT breakdown, which is a revision of the delivered prompt.

### Why this matters

A field list is the easiest place for a runtime to be helpful in the wrong way. Every field the user named must survive, no field the user did not name may appear, and the null rule must stay a rule rather than a suggestion.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$yaml` locks format independently while `$text` binds the mode, delivering a valid YAML export with exactly the requested fields, then saving the Turn 2 revision as a new export
- Preconditions: SID-001 passed, a disposable copy of `AI Systems/Prompt Improver/` is prepared and the `export/` baseline is recorded
- Real user request: `I need a prompt, in YAML, that pulls data out of supplier invoices from pasted PDF text: supplier name, invoice number, invoice and due dates, currency, subtotal, VAT amount, total and the line items with description, quantity and unit price. Missing fields must be null, never guessed, because it feeds our accounting import.`
- Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`
- Expected execution process: Start a fresh session in the disposable copy, submit Turn 1, submit Turn 2 in the same session whatever Turn 1 did and then inspect both replies and every saved `.yaml` file
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 either delivers or asks at most one consolidated question, and both paths are correct: `SKILL.md` line 383 asks only when essential context is missing, while `references/interactive-mode.md` lines 222-223 route `$text` and a format command to the comprehensive question. Command flow allows at most one interaction (`SKILL.md` line 402). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (`SKILL.md` lines 397-398). Mode and format are independent axes (`SKILL.md` lines 71 and 99): the Text lane binds with Standard energy and CLEAR (lines 75 and 345) and the format locks to YAML (line 84), so a Turn 1 question asking which mode to use means the format token stole the mode axis. CLEAR passes at 40 of 50 with its floors (lines 444-445). The runtime saves `export/[###] - enhanced-[description].yaml` before replying (`AGENTS.md` lines 34 and 49), the file opens with a single-line `Mode:` header carrying complexity and framework (`SKILL.md` lines 558-559), the payload below the header parses as valid YAML (lines 410 and 497) and the file carries no Markdown such as `**`, `###` or a code fence (`assets/format-guide-yaml.md` lines 133-141 and 451). The YAML format guide writes the header as `Mode: $yaml` (line 128) while `SKILL.md` asks for the mode with its `$` prefix (line 559), so a header labelled `$yaml` or `$text` both pass and only a missing header fails; the label used is recorded. A header written as a YAML comment, `# Mode: ...`, also counts as the single-line header and is not Markdown: the literal `Mode: $yaml | ...` line does not parse as YAML, so the comment form lets the whole file parse. Either form passes, and the form used is recorded. The reply leads with the path, reports the CLEAR result and reports roughly three to seven percent token overhead (`SKILL.md` lines 410 and 501), and does not paste the prompt (`AGENTS.md` line 64). The enhanced prompt carries every supplied fact: supplier invoices as the source, PDF text pasted in as the input, exactly the fields supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount and total, line items with description, quantity and unit price, null for any missing field with no guessing, and the accounting import as the consumer. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`SKILL.md` lines 46 to 47 and 511). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It saves as a new `export/[###]` file and never edits the delivered export in place (`SKILL.md` lines 421 to 422, `AGENTS.md` line 70). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One path-first reply whose saved `.yaml` file carries the header and a parsing payload with exactly the requested fields, then a second `.yaml` export that adds the VAT breakdown
- Pass/fail: PASS if the Turn 1 delivery is a `.yaml` export with the single-line header, a payload that parses, every requested field, the null rule, a CLEAR result and the overhead note, and the Turn 2 revision is a new export under the next number while the delivered export stays unchanged. FAIL if the file is not `.yaml`, the header is missing, the payload does not parse, Markdown appears in the file, the mode axis was stolen, the overhead or score is missing, a requested field or the null rule is dropped, the delivered export is edited in place or the revision saves no new file. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a supplier VAT number, an IBAN, a purchase order number or, before Turn 2 asks for it, a per-rate VAT breakdown are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.` | Bind Text, lock YAML, either deliver through a verified `.yaml` export or ask at most one consolidated question | Format locked to YAML regardless of any question, no question about the mode | Response transcript and `export/` listing |
| 2 | `Some invoices carry two VAT rates. Add a VAT breakdown with rate and amount per rate.` | When Turn 1 asked, complete the enhancement with the VAT breakdown included, save the `.yaml` export and reply path-first, flagging any unanswered essential as an assumption. When Turn 1 delivered, treat this as a revision: save a new `.yaml` export under the next number that carries every Turn 1 field and rule plus a VAT breakdown with rate and amount per rate, and leave the delivered export unchanged | YAML lock retained, every Turn 1 field and the null rule kept, VAT amount kept and the per-rate breakdown added | Response, score line, parse results for both exports and a byte comparison of the Turn 1 export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`

### Commands

1. `sandbox: copy "AI Systems/Prompt Improver/" and record the export/ baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record whether Turn 1 asked or delivered, and checksum any saved export -> user: submit Turn 2 in the same session`
4. `filesystem: check the single-line Mode: header and parse the payload below it in every .yaml export, re-checksum the Turn 1 file -> operator: grade format lock, syntax, fields, overhead report and revision`

### Expected

Step 1 fixes the baseline. Step 2 binds Text and locks YAML, delivering or asking once. Step 3 records the first delivery and fixes its checksum. Step 4 proves the header exists, the payload below it parses as YAML, the field list matches the request exactly and, when Turn 1 delivered, that Turn 2 saved a new `.yaml` file under the next number while the first file stayed byte-identical.

### Evidence

Turn transcripts, the CLEAR score line, `export/` listings before and after each turn, the header label used, a parse check on the payload below each `.yaml` header, a field checklist against the graded file, the token-overhead note in chat, the Turn 1 checksum before and after Turn 2 and the verdict.

### Pass / fail

- **Pass**: A `.yaml` export with the required header and a payload that parses, exactly the requested fields and the null rule, a reported CLEAR result, the overhead note, the path-first reply and a Turn 2 revision saved as a new `.yaml` export
- **Fail**: A non-YAML file, a missing header, invalid YAML payload syntax, Markdown inside the file, format competing with mode, missing overhead report or score, a dropped field or null rule, scope expansion, a second question after the first, an edited Turn 1 export or a revision with no new file
- **Skip**: only when a named sandbox blocker prevents creating the disposable copy or the session

### Failure triage

1. Check the independent format axis in `SKILL.md` lines 71 and 99 when the format or mode was lost
2. Re-check the YAML rules in `assets/format-guide-yaml.md` lines 124-156 and 442-476 when the file fails to parse or carries Markdown
3. Check the token-overhead rule in `SKILL.md` lines 410 and 501 and the revision rule in lines 421-422

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| SFM-002 | Independent $yaml format lock with Text mode | Verify format axis locks YAML while Text binds mode, with exactly the requested fields and the revision saved as a new export | `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.` | 1. `Record export baseline` -> 2. `Submit Turn 1 fresh` -> 3. `Checksum export, submit Turn 2` -> 4. `Check header, parse payloads, re-checksum` | Step 1: baseline known. Step 2: Text bound, YAML locked. Step 3: first delivery fixed. Step 4: header, valid YAML payload, exact fields, revision in a new file | Transcripts, CLEAR line, export listings, parse results, field checklist, overhead note, checksums | PASS if the .yaml header and payload are valid, the fields match, and the lock, overhead and revision hold. FAIL on wrong format, missing header, invalid YAML, a lost or added field, missing overhead or an in-place edit | 1. Check format axis rule.<br>2. Check YAML format guide.<br>3. Check overhead and revision rules. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Export protocol, `.yaml` naming and the in-place edit prohibition |
| [`SKILL.md`](../../SKILL.md) | Independent format axis, Text binding, overhead rule, header and revision rule |
| [`interactive-mode.md`](../../references/interactive-mode.md) | `$text` and format command state routes |
| [`format-guide-yaml.md`](../../assets/format-guide-yaml.md) | YAML file syntax, header and delivery rules |
| [`patterns-evaluation.md`](../../references/patterns-evaluation.md) | CLEAR gate for the Text lane |

---

## 5. SOURCE METADATA

- Group: Skill format modes
- Playbook ID: SFM-002
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-format-modes/yaml-format-lock-export.md`
