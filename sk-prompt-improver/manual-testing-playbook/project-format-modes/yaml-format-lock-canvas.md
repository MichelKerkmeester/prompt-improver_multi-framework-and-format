---
title: "PFM-002 -- Independent $yaml format lock with Text mode in the Project"
description: "Validates that $yaml locks the format axis while $text wins the mode axis in the Project, producing a YAML Deliverable Block with every requested field, the overhead report and a Turn 2 revision rendered as a new block."
version: 1.1.1.0
---

# PFM-002 -- Independent $yaml format lock with Text mode in the Project

`$text` and `$yaml` live on different axes in the Project router. The mode command binds the Text lane and the format command locks the prompt payload to YAML, so the Deliverable Block carries a payload that parses and fields that are exactly the ones the user listed.

---

## 1. OVERVIEW

The user wants a data-extraction prompt for supplier invoices and names every field, the null rule and the downstream consumer. The Text lane runs at Standard energy with CLEAR while the YAML lock shapes the payload. The fence holds the payload alone, so the format lock covers everything inside it. Turn 2 adds a VAT breakdown, which is a revision of the delivered prompt.

### Why this matters

A field list is the easiest place for a runtime to be helpful in the wrong way. Every field the user named must survive, no field the user did not name may appear, and the null rule must stay a rule rather than a suggestion.

---

## 2. SCENARIO CONTRACT

- Objective: Verify `$yaml` locks format independently while `$text` binds the mode in the Project runtime, delivering a YAML Deliverable Block with exactly the requested fields, then rendering the Turn 2 revision as a new block
- Preconditions: PID-001 passed and a claude.ai Project is configured with `Custom Instructions.md` pasted and the system's knowledge documents attached. The reply renders the Deliverable Block as one bare code fence at the start of the reply, holding only the prompt, with no preamble. Commentary is any text before the block, including a heading, a bold label or an environment note. The block starts at its opening fence and ends at its closing fence, and it holds the prompt alone, with no `Mode:` header, divider or footer inside it
- Real user request: `I need a prompt, in YAML, that pulls data out of supplier invoices from pasted PDF text: supplier name, invoice number, invoice and due dates, currency, subtotal, VAT amount, total and the line items with description, quantity and unit price. Missing fields must be null, never guessed, because it feeds our accounting import.`
- Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`
- Expected execution process: Start a fresh conversation in the configured Project, submit Turn 1, submit Turn 2 in the same conversation whatever Turn 1 did and then inspect every Deliverable Block and the chat report
- Expected signals: The first reply that delivers is the graded delivery. When neither reply delivers, the scenario fails for missing delivery. Turn 1 delivers with no question first: the request names its mode and carries enough to default the rest, so a Turn 1 question is a failure, and every default appears as a numbered open item after the fence (`Custom Instructions.md` section 6). A question covers every missing essential in one message; asking two things in that one message is correct, and splitting them across messages is the failure (same file, line 395). Mode and format are independent axes (`Custom Instructions.md` lines 43 and 73): the Text lane binds with Standard energy and CLEAR (line 47) and the format locks to YAML (line 56), so a Turn 1 question asking which mode to use means the format token stole the mode axis. CLEAR passes at 40 of 50 with its floors (`Prompt Improver - Patterns and Evaluation.md` lines 302 and 447). The reply opens with one bare code fence, no language tag, holding only a prompt payload that parses as valid YAML; the single-line `Mode:` header follows the fence in chat, and the format lock covers everything inside the fence (`Custom Instructions.md` section 6). The payload carries no Markdown such as `**`, `###` or a code fence (`Prompt Improver - Format Guide YAML.md` lines 133 and 451); the fence markers themselves are not part of the payload. The chat header after the fence may be labelled `$yaml` or `$text`; both pass and only a missing header fails; the label used is recorded. After the block the chat reports the export-equivalent path `export/[###] - enhanced-[description].yaml`, the CLEAR result, roughly three to seven percent token overhead and a short summary, and does not paste the prompt again (`Custom Instructions.md` lines 159, 178 and 232-434). A guessed number in place of `[###]` is recorded and does not decide the run, unless the reply presents it as a saved file. The enhanced prompt carries every supplied fact: supplier invoices as the source, PDF text pasted in as the input, exactly the fields supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount and total, line items with description, quantity and unit price, null for any missing field with no guessing, and the accounting import as the consumer. Scope test: a default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect (`Custom Instructions.md` line 18). Revision: a revision the user asks for after a delivery is a new deliverable under the next number. It renders a new Deliverable Block under the next export-equivalent name, since naming stays identical to CLI delivery (`Custom Instructions.md` line 128). The two to three sentence summary is advisory under the root's Defect severity section: a summary outside the band is recorded and never decides a verdict
- Desired user-visible outcome: One fence-first reply whose fenced payload parses cleanly with exactly the requested fields and whose chat claims no file was written, then a second block that adds the VAT breakdown
- Pass/fail: PASS if the Turn 1 delivery is a Deliverable Block as a bare fence before any commentary, with the header in chat after it whose payload parses as YAML with every requested field and the null rule, with a CLEAR result, the overhead note and no save claimed, and the Turn 2 revision is a new Deliverable Block under the next export-equivalent name. FAIL if commentary precedes the block, the chat header is missing or anything besides the prompt sits in the fence, the payload is Markdown or invalid YAML, the mode axis was stolen, the overhead or score is missing, a requested field or the null rule is dropped, a save is claimed or the revision arrives as a partial patch or as chat text instead of a new block. A default fills a gap in what the user asked for. An output, field or section the user did not ask for is scope expansion, even when the reply flags it, and scope expansion inside the enhanced prompt is a blocking defect: a supplier VAT number, an IBAN, a purchase order number or, before Turn 2 asks for it, a per-rate VAT breakdown are examples

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.` | Bind Text, lock YAML, deliver through the bare-fence Deliverable Block in Turn 1 with no question, listing every default as an open item | Format locked to YAML regardless of any question, no question about the mode | Response transcript and the opening fence |
| 2 | `Some invoices carry two VAT rates. Add a VAT breakdown with rate and amount per rate.` | Treat this as a revision: render a new Deliverable Block under the next export-equivalent name that carries every Turn 1 field and rule plus a VAT breakdown with rate and amount per rate | YAML lock retained, every Turn 1 field and the null rule kept, VAT amount kept and the per-rate breakdown added | Response, score line, parse results for both blocks |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.`

### Commands

1. `project: configure the Project with Custom Instructions pasted and the knowledge documents attached`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `operator: record that Turn 1 delivered with no question first -> user: submit Turn 2 in the same conversation`
4. `artifact: parse the YAML payload inside every Deliverable Block -> operator: grade format lock, syntax, fields, overhead report, no-save report and revision`

### Expected

Step 1 fixes the packaging under test. Step 2 binds Text and locks YAML, delivering with no question first. Step 3 records the first delivery. Step 4 proves the chat header follows the fence, the payload inside the fence parses as YAML, the field list matches the request exactly and, when Turn 1 delivered, that Turn 2 rendered a complete new block rather than a patch.

### Evidence

Turn transcripts, the CLEAR score line, the opening fence, the header label used, a parse check on the payload inside each Deliverable Block, a field checklist against the graded block, the token-overhead note in chat, the export-equivalent path lines and the verdict.

### Pass / fail

- **Pass**: A bare-fence Deliverable Block before commentary, with the `Mode:` header in chat after it, whose payload parses as valid YAML with exactly the requested fields and the null rule, a reported CLEAR result, the overhead note, no save claimed and a Turn 2 revision rendered as a new block
- **Fail**: Commentary before the block, a missing chat header, anything besides the prompt in the fence, a Markdown payload, invalid YAML syntax, format competing with mode, missing overhead report or score, a dropped field or null rule, scope expansion, a second question after the first, any claim that a file was written or a revision that is not a new block
- **Skip**: only when a named runtime or environment blocker prevents opening the configured Project session

### Failure triage

1. Check the independent format axis in `Custom Instructions.md` lines 43 and 73 when the format or mode was lost
2. Re-check the YAML rules in `Prompt Improver - Format Guide YAML.md` lines 110-148 and 442-454 when the payload fails to parse, and the Delivery Protocol in `Custom Instructions.md` lines 204-437 when the chat header, the fence contents or the ordering is off
3. Check the token-overhead rule in `Custom Instructions.md` lines 159 and 234 and the delivery override in line 128 when the overhead is missing or Turn 2 did not render a new block

| Feature ID | Feature Name | Scenario Name / Objective | Exact Prompt | Exact Command Sequence | Expected Signals | Evidence | Pass/Fail Criteria | Failure Triage |
|---|---|---|---|---|---|---|---|---|
| PFM-002 | Independent $yaml format lock with Text mode in the Project | Verify format axis locks YAML while Text binds mode, with exactly the requested fields and the revision rendered as a new block | `$text $yaml Build me a prompt for extracting data from supplier invoices (the PDF text is pasted in). Fields we need: supplier name, invoice number, invoice date, due date, currency, subtotal, VAT amount, total, and line items with description, quantity and unit price. If a field is missing it must be null, never a guess. The result feeds our accounting import.` | 1. `Configure Project` -> 2. `Submit Turn 1 fresh` -> 3. `Submit Turn 2` -> 4. `Check header, parse payloads` | Step 1: packaging fixed. Step 2: Text bound, YAML locked. Step 3: first delivery fixed. Step 4: chat header, prompt-only fence, valid YAML payload, exact fields, revision in a new block | Transcripts, CLEAR line, fence state, parse results, field checklist, overhead note | PASS if the chat header, a prompt-only fence and payload are valid, the fields match, and the lock, overhead and revision hold. FAIL on wrong format, missing chat header, anything besides the prompt in the fence, invalid YAML, a lost or added field, missing overhead, a claimed save or a patch in place of a block | 1. Check format axis rule.<br>2. Check YAML format guide.<br>3. Check overhead rule and revision naming. |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, defect severity and root summary |
| [Custom Instructions](<../../../claude project/Custom Instructions.md>) | Independent format axis, Text binding, overhead rule, delivery override and the Delivery Protocol |
| [Interactive Mode knowledge](<../../../claude project/knowledge/Prompt Improver - Interactive Mode.md>) | `$text` and format command routes and interaction limits |
| [Format Guide YAML knowledge](<../../../claude project/knowledge/Prompt Improver - Format Guide YAML.md>) | YAML syntax, header and delivery rules |
| [Patterns and Evaluation knowledge](<../../../claude project/knowledge/Prompt Improver - Patterns and Evaluation.md>) | CLEAR gate for the Text lane |

---

## 5. SOURCE METADATA

- Group: Project format modes
- Playbook ID: PFM-002
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-format-modes/yaml-format-lock-canvas.md`
