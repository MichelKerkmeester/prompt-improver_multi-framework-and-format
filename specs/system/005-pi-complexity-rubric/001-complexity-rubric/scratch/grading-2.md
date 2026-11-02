# Grading 2: SFW-007 to SFW-012 and PFW-007 to PFW-012

Graded against the playbook as it stood at run time (the scratchpad copy of `manual-testing-playbook/`), run `2026-09-27--complexity-rubric--claude-sonnet-5-xhigh`. Each verdict applies the scenario's own Pass/fail line. The structure review was used as a lead only, and every item below was checked against the reply, the deliverable, `meta.json` and the sandbox `exports/` listing.

```csv
id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note
SFW-007,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The reply opens with a parse note, not the saved path, so the path-first item fails while header, elements, CLEAR, YAML parse, facts and scope all hold."
PFW-007,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"An environment note precedes the block, the header reads High (7/10) against the Medium tier, the YAML payload does not parse and a purpose statement plus a conditional approval marking are added outputs."
SFW-008,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The troubleshooting rule is widened from errors the CI config or README mention to failure modes drawn from all source files, which alters a supplied fact."
PFW-008,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The separate macOS and Ubuntu paths become a split only where steps differ, with identical steps stated once, which alters a supplied fact."
SFW-009,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The reply opens with a validation note instead of the saved path and the process is narrowed from containers carrying lithium batteries to containers declared under UN3480."
PFW-009,project,claude-sonnet-5-xhigh,PASS,1,1,no,yes,"Block first with header and attestation, CIDI at Complex (10/10), four labelled keys, CLEAR 44/50 passed, JSON parses, every fact kept and no scope expansion."
SFW-010,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The user's one-line example note is recast as example input and its output becomes a five-line labelled block, so the supplied example is not kept."
PFW-010,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"A lead-in sentence precedes the block, the header reads High (7/10) against the Medium tier and our employment-law firm becomes the invented name Barter."
SFW-011,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The reply opens with JSON body validated successfully instead of the saved path, so the path-first item fails while every other item holds."
PFW-011,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The approved list of 38 EU-authorised health claims becomes up to 38, which alters a supplied number."
SFW-012,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The structuring flag is replaced by a ban on the word structuring and every claim cites a transaction ID is narrowed to claims drawn from transaction data."
PFW-012,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"The prompt requires the structuring check result on every alert including not observed, an output the user did not ask for, so the scope test fails."
```

Two judgment calls apply to every pair and are read the same way on both sides:

- **Target model and replaced prompt:** each fact list names the target model and "the current one-line prompt it replaces". I read both as kept when the enhanced prompt is written for that model and replaces that prompt, even where the body never names the model or quotes the old line. A stricter reading would fail the facts item on most of the twelve, and it would not change any verdict except PFW-009, whose body names GPT-4.1 and quotes "Document this process" anyway, so it would still pass
- **Title lines:** a title on the produced document is read as a default that fills a gap in the output shape, not as a new section

---

### SFW-007, skill, FAIL

- **Verified `.yaml` export saved before a path-first reply: FAIL.** `meta.json` records `turns_run` 1, no failures and a ledger that creates `export/001 - enhanced-ap-credit-note-sop-prompt.yaml`. The sandbox `exports/export/` holds that file, byte-identical to the benchmark copy. But the reply's first line is "The YAML body (everything below the single-line header, per the format guide's own convention) parses cleanly and matches the intended CIDI structure." The path only appears on line 3 (`**Saved:** ...`). The scenario defines path-first as "the first line of the reply names the saved `export/` path"
- **Prompt pasted: no**, holds
- **Header names CIDI and a Medium complexity: PASS.** `Mode: $improve $yaml | Complexity: Medium (6/10) | Framework: CIDI`
- **Context, Instructions, Details and Input labelled: PASS.** The four top-level YAML keys are `context`, `instructions`, `details` and `input`
- **CLEAR passes its gate: PASS.** "CLEAR: 46/50 | Gate: passed (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4)", every floor met
- **Payload parses as YAML: PASS.** `yaml.safe_load` on the lines below the header returns the four keys
- **Every supplied fact kept: PASS (facts_intact yes).** Transcript input as a placeholder, new AP clerks, supplier credit note against an open invoice, one action plus screen or field plus result per step, the EUR 5,000 second-approver flag, verbatim field names, chit-chat excluded and Confluence as the destination are all present. Claude and the old one-liner fall under the shared judgment call above
- **Scope test: PASS.** The `document_shape` title line is read as a default per the shared judgment call. Nothing else unasked is added
- **Advisory, recorded:** summary of three sentences, inside the band. No token-overhead figure is reported, which the expected signals ask for but the Pass/fail line does not

### PFW-007, project, FAIL

- **Block before any commentary: FAIL.** The reply opens "No Canvas panel is available in this environment (terminal/API surface), so per protocol the Deliverable Block is rendered as a single fenced block first, with no preamble." The Canvas stand-in counts "an environment note" as commentary
- **Header, prompt and attestation present, no save claimed: PASS.** The attestation ends `execution = did not occur | save = did not occur`, and the chat gives an export-equivalent path only
- **Prompt pasted again: no**, holds
- **Header names CIDI and a Medium complexity: FAIL.** `Complexity: High (7/10)` sits outside the Medium band of 5 to 6
- **Four CIDI elements labelled: PASS.** Keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR 43/50 ... Gate passed", no sub-scores reported
- **Payload parses as YAML: FAIL.** With the header, the `---` and the attestation removed, `yaml.safe_load` raises "could not find expected ':'" at the plain list item that wraps after "completing the action: a"
- **Every supplied fact kept: PASS (facts_intact yes).** All ten listed facts are present, including the EUR 5,000 flag and Confluence
- **Scope test: FAIL.** Judgment call. The instruction "a short title, a one-line purpose statement, then the numbered steps" adds a purpose statement the user did not ask for, and "mark the approval step as conditional and instruct the clerk to confirm the value first" adds a clerk instruction the user did not ask for. The title is read as a default
- **Advisory, recorded:** summary of three sentences, token overhead "+3-7%" reported

### SFW-008, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "Saved: `export/001 - enhanced-onboarding-setup-guide-prompt.md`". The sandbox `exports/export/` holds the file and `meta.json` records it as the only creation
- **Prompt pasted: no**, holds
- **Header names CIDI and a High complexity: PASS.** `Complexity: High (8/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Bold labels Context, Instructions, Details, Input
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 | Gate: passed", no sub-scores
- **Every supplied fact kept: FAIL (facts_intact no).** The input said troubleshooting is "built only from errors the CI config or README mention". Instruction 6 reads "containing only failure modes drawn from the source files: error strings, named CI check failures, or problems the README explicitly calls out", and the source files include the Makefile, so Makefile error strings are admitted. A second, weaker point: instruction 4 allows a verify check "present in or directly derivable from the source files", which admits a command not copied verbatim
- **Scope test: PASS.** Judgment call. The "Secrets (1Password)" section in the section order holds only the 1Password handling the user asked for, so it is read as placement rather than a new output
- **Advisory, recorded:** summary of two sentences

### PFW-008, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence and the header directly inside it
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends with both "did not occur" fields, and the summary says "nothing was saved or executed"
- **Prompt pasted again: no**, holds
- **Header names CIDI and a High complexity: PASS.** `Complexity: High (8/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Bold labels Context, Instructions, Details, Input
- **CLEAR passes its gate: PASS.** "CLEAR 43/50 (C9, L8, E13, A9, R4)", every floor met
- **Every supplied fact kept: FAIL (facts_intact no).** The input asked for "separate paths for macOS and Ubuntu". Instruction 3 splits the paths only "anywhere a step differs by OS", and Details adds "If a command or step is identical on both platforms, state it once and note that it applies to both, rather than duplicating it under both OS paths". Claude in Cursor survives as "You are working inside Cursor"
- **Scope test: PASS.** Troubleshooting stays limited to the README and CI config, and nothing unasked is added
- **Advisory, recorded:** summary of two sentences

### SFW-009, skill, FAIL

- **Verified `.json` export saved before a path-first reply: FAIL.** The export exists in the sandbox and `meta.json` records it, but the first line is "JSON validated. The prompt is exported and CIDI-structured with all four required sections." The path is on line 3
- **Prompt pasted: no**, holds
- **Header names CIDI and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Top-level JSON keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR: 44/50 (C9 · L9 · E13 · A9 · R4) | Gate: passed"
- **Payload parses as JSON: PASS.** `json.loads` on the lines below the header succeeds
- **Every supplied fact kept: FAIL (facts_intact no).** The input covers "inbound sea containers carrying lithium batteries". `context.process` reads "clearing inbound sea containers declared under UN3480 (lithium batteries)", and `carrier_dg_rules` and its input slot are narrowed to "UN3480 lithium-battery shipments". That contradicts the file's own `un3480_gate`, which expects shipments outside UN3480. GPT-4.1, "Document this process", the three inputs, the role split, the four per-step fields, list-not-choose conflicts, the DG officer gate and bilingual step numbers are kept
- **Scope test: PASS.** The English section labels inside the Dutch version and the "Not specified in source" marker are flagged defaults that fill gaps, and the DG officer role comes from the input
- **Advisory, recorded:** one-sentence summary, below the band. No token-overhead figure reported

### PFW-009, project, PASS

- **Block before any commentary: PASS.** The reply opens with the fence, header on the next line
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends `execution = did not occur | save = did not occur`. The chat path is `export/[###] - ...` and not presented as saved. The benchmark copy's `NNN` file number is recorded, not decisive
- **Prompt pasted again: no**, holds
- **Header names CIDI and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (10/10) | Framework: CIDI`
- **Four CIDI elements labelled: PASS.** Top-level JSON keys `context`, `instructions`, `details`, `input`
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9·L9·E13·A9·R4, all floors met) ... Gate passed"
- **Payload parses as JSON: PASS.** `json.loads` succeeds with the header, `---` and attestation removed
- **Every supplied fact kept: PASS (facts_intact yes).** `target_model` GPT-4.1, "The current instruction is the placeholder 'Document this process'", the three inputs, "inbound sea containers carrying lithium batteries at the Port of Rotterdam", roles broker, planner and warehouse, trigger, system, document_produced and handoff per step, "do not pick a side: record the disagreement", the UN3480 DG officer step "before the planner's slot-booking step" and Dutch and English with identical step numbers are all present
- **Scope test: PASS.** Judgment call. `output_section_mapping` fills the CIDI output sections the importer requires, so it is read as a default. `step_requirements` lists three roles and `dangerous_goods_routing` then adds a DG officer step, an internal inconsistency that is recorded but drops no fact
- **Advisory, recorded:** summary of two sentences, token overhead "+5-10%" reported as the scenario expects

### SFW-010, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "File verified: `export/001 - enhanced-employment-law-intake-prompt.md`". The sandbox export exists and `meta.json` records it
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a Medium complexity: PASS.** `Complexity: Medium (6/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR: 42/50 (C:8 L:8 E:12 A:9 R:5) | Gate: passed"
- **Every supplied fact kept: FAIL (facts_intact no).** Judgment call on a clear case. The user's example note "Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag." is turned into an input line "Employee, dismissal on 3 June, employer Van Dijk Logistics." and its output is a five-line labelled block ending "Deadline flag: dismissal is over two months old - the claim window may have passed." The one-line note the user approved is no longer the target shape. The four issues, client type, every date, the other party for the conflict check, no advice and no chance estimate and the two-month flag are kept
- **Scope test: PASS.** The two added examples use invented parties (Meridian Retail Group, Elena Roussos) but illustrate only the user's own fields and rules, which the scenario allows
- **Advisory, recorded:** one-sentence summary plus assumptions, below the band

### PFW-010, project, FAIL

- **Block before any commentary: FAIL.** The reply opens "Here is the improved prompt, delivered as the Deliverable Block below." before the fence
- **Header, prompt and attestation present, no save claimed: PASS.** Attestation ends with both "did not occur" fields, and the chat claims no file
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a Medium complexity: FAIL.** `Complexity: High (7/10)` sits outside the Medium band of 5 to 6
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Context, Instructions, Do's, Don'ts, Examples
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) ... Gate passed"
- **Every supplied fact kept: FAIL (facts_intact no).** Context reads "Barter, an employment-law firm", where the input said "our employment-law firm". The name is invented. The user's example note is kept verbatim as the first example output, and the other facts are kept
- **Scope test: PASS.** The second example (pay dispute, no dates, no counterpart) illustrates the user's own fields only
- **Advisory, recorded:** summary of two sentences

### SFW-011, skill, FAIL

- **Verified `.json` export saved before a path-first reply: FAIL.** The export exists in the sandbox and `meta.json` records it, but the first line is "JSON body validated successfully." The path is on line 3
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a High complexity: PASS.** `Mode: $json | Complexity: High (8/10) | Framework: TIDD-EC`. The `$json` mode label is allowed
- **Six TIDD-EC elements labelled: PASS.** Keys `task`, `context`, `instructions`, `dos`, `donts`, `examples`. The extra top-level `output_schema` holds only the user's three per-flag fields (sentence, rule broken, rewrite), so it passes as the scenario allows
- **CLEAR passes its gate: PASS.** "CLEAR 45/50 | Gate: passed (floors met: C9, L9, E13, A9, R5)"
- **Payload parses as JSON: PASS**
- **Every supplied fact kept: PASS (facts_intact yes).** GPT-4.1, title, description and bullet points, "Exactly 38 EU-authorised health claims, supplied fresh with every call", the three rules, exact sentence and compliant rewrite, compliant text untouched, no efficacy judgment and the worked example pair are all present
- **Scope test: PASS.** Judgment call. The citation of "EU Regulation (EC) No 1924/2006" in `context.domain` is invented context but adds no output, field or section, so it is recorded and not counted. The disease-claim and dosage-promise examples illustrate the user's own categories
- **Advisory, recorded:** summary of two sentences, no token-overhead figure reported

### PFW-011, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence
- **Header, prompt and attestation present, no save claimed: PASS**
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a High complexity: PASS.** `Mode: $improve | Complexity: High (8/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Keys `task`, `instructions`, `dos`, `donts`, `examples`, `context`
- **CLEAR passes its gate: PASS.** "CLEAR 45/50 (target 40+) ... Gate passed on first pass", no sub-scores
- **Payload parses as JSON: PASS**
- **Every supplied fact kept: FAIL (facts_intact no).** The task reads "the supplied list of up to 38 EU-authorised health claims" and `input_format` reads "approved_claims: array of up to 38 strings". The input fixed the list at 38. A weaker second point, recorded as judgment: the `compliant_paraphrase_edge_case` example passes a reworded claim as compliant, which loosens "flags every health claim that is not on the list"
- **Scope test: PASS.** The `violations` wrapper carries only the user's three per-flag fields, and the non-health marketing exclusion is a default
- **Advisory, recorded:** summary of two sentences, token overhead "+5-10%" reported

### SFW-012, skill, FAIL

- **Verified `.md` export saved before a path-first reply: PASS.** First line "File saved and verified: **`export/001 - enhanced-aml-alert-narrative-prompt.md`**". The bold markup does not change path-first. The sandbox export exists and `meta.json` records it
- **Prompt pasted: no**, holds
- **Header names TIDD-EC and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 | Gate: passed", with Correctness 9, Logic 9, Expression 13, Arrangement 9 and Reusability 4, every floor met
- **Every supplied fact kept: FAIL (facts_intact no).** The input says "It flags structuring when three or more cash deposits between EUR 9,000 and 9,999 fall within 10 days". Instruction 3 says "do not attach a legal label to it", and Don'ts say "Never use conclusory AML labels such as \"structuring\"", so the prompt never flags structuring. Also "Every claim cites a transaction ID" is narrowed to "every claim drawn from the 90-day transaction data", with KYC and prior-alert claims citing other records. Mistral Large, the four inputs, the fixed section order, no laundering conclusion, no filing or closing recommendation, the currency rule, all three edge cases and the auditors' sentence verbatim are kept
- **Scope test: PASS.** The combined edge-case example covers only the three edge cases the user named, and "(EUR equivalent unavailable)" is a default
- **Advisory, recorded:** summary of two sentences

### PFW-012, project, FAIL

- **Block before any commentary: PASS.** The reply opens with the fence. The "Advisory note" comes after the block
- **Header, prompt and attestation present, no save claimed: PASS.** The advisory note says "nothing was written to disk, executed or verified on any filesystem"
- **Prompt pasted again: no**, holds
- **Header names TIDD-EC and a Complex complexity: PASS.** `Mode: $deep | Complexity: Complex (9/10) | Framework: TIDD-EC`
- **Six TIDD-EC elements labelled: PASS.** Bold labels Task, Instructions, Do's, Don'ts, Examples, Context
- **CLEAR passes its gate: PASS.** "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) ... Gate passed"
- **Every supplied fact kept: PASS (facts_intact yes).** The structuring threshold is kept and flagged as "a potential structuring pattern", and "Cite a transaction ID for every specific factual claim in any section" keeps the citation rule. Mistral Large, the fixed order, both bans, the currency rule, all three edge cases and the auditors' sentence are kept. The missing-KYC example carries no transaction ID although the Do's require one, an internal inconsistency that is recorded but drops no fact
- **Scope test: FAIL.** Judgment call. The Do's add "Report the structuring check result every time (present or not observed), regardless of which rule fired". The user asked for a flag when the threshold is met, so a "not observed" line on every alert is an output the user did not ask for. Fixing the output language as English is read as a default
- **Advisory, recorded:** summary of two sentences

---

## Twin comparison

- **SFW-007 and PFW-007: both FAIL, for different items.** The skill side fails only on path-first. The Project side fails on commentary before the block, a High (7/10) header against Medium, a YAML payload that does not parse and two added outputs. Both keep every fact
- **SFW-008 and PFW-008: both FAIL on facts, with different alterations.** The skill side widens the troubleshooting sources to include the Makefile. The Project side merges identical steps across the two OS paths. Everything else passes on both
- **SFW-009 and PFW-009: verdicts differ.** The skill side fails on path-first and on narrowing lithium-battery containers to UN3480-declared ones. The Project side keeps the process scope and delivers block first, so it passes
- **SFW-010 and PFW-010: both FAIL, for different items.** The skill side keeps delivery and tier but recasts the user's example note. The Project side keeps the example verbatim but fails on a lead-in sentence, a High (7/10) header against Medium and the invented firm name Barter
- **SFW-011 and PFW-011: both FAIL, for different items.** The skill side keeps every fact and fails only on path-first. The Project side delivers correctly and fails on "up to 38"
- **SFW-012 and PFW-012: both FAIL, for different items.** The skill side alters two facts (the structuring label is banned, the citation rule is narrowed). The Project side keeps both and fails the scope test on an always-reported structuring result
