# Grading notes: Prompt Improver playbook run, 2026-09-25

Evidence behind every verdict in `results.csv`. Paths are relative to this run folder unless they start with a system path. Reply quotes cite `replies/<ID>-turn<N>.txt` by line. Skill file quotes cite the copy in `skill/<ID - slug>/exports/export/`. Rule citations give file and line.

---

## 1. How the grading was done

### Sources read

- The playbook at Barter `4fb9dd88`: the root `manual-testing-playbook.md` and all fourteen scenario files, plus the diff that commit made
- The skill rules: `AGENTS.md`, `sk-prompt-improver/SKILL.md`, the six references and the format guides
- The Project rules: `claude project/Custom Instructions.md` (the kernel) and the knowledge files the scenarios name
- Run output: every reply, every `meta.json` (per-turn ledger, model, effort), the skill `exports/` copies and the `events-turn-N.jsonl` tool calls wherever a save, a parse or an edit had to be proven

Every event stream reports `claude-sonnet-5` and every `meta.json` reports effort `medium`, one attempt, 2 of 2 turns.

### Graded delivery

For the eight scenarios with an unconditional Turn 2 (SID, PID, STX, PTX, SFM, PFM, SCR, PCR), the first reply that delivers is the graded delivery (each file, Expected signals line 30, or line 47 for the identity pair). All eight delivered on Turn 1, so Turn 1 is the graded delivery in all eight and Turn 2 is checked only for the root's blocking defects (each file, section 3 Expected, line 58 or 75). No scenario reached the "neither reply delivers" branch, so no Turn 2 question had to be logged as a follow-up. For the six routing and safety scenarios, both turns are graded as the chain requires.

### Test used for "invented requirement or scope expansion"

The root lists "An invented requirement or scope expansion inside the enhanced prompt" as blocking (`manual-testing-playbook.md` line 137). The rule sources ban it (`SKILL.md` lines 507 to 508 and line 621, kernel line 335) and also allow "clarity, structure, constraints and examples only when they serve that stated outcome" (`SKILL.md` line 45, kernel line 18) and flagged defaults for incomplete context (`SKILL.md` lines 461 and 500). Neither side says where the line falls, so the grading applied one test to every delivery and logs the silence as a follow-up finding:

- It counts when the enhanced prompt asks the downstream AI for an output the request does not contain, meaning a second deliverable or a new category of content, or states a user-specific fact as settled that the user never gave
- It does not count when it is structure, a constraint, a guardrail, a placeholder or a flagged default that shapes the one deliverable the user asked for
- An `[Assumes: ...]` flag or a disclosure discloses an extra output but does not turn it into a default

### Canvas stand-in

Every Project precondition says a delimited Deliverable Block placed before any commentary counts as the rendered Artifact, and a reply without one counts as an empty panel (line 26 in six Project files, line 43 in PID-001). Only PTX-001 defines commentary further (line 30): any text before the header line counts, a heading or an environment note included, while a code fence or bold markup around the header does not. The grading applied the PTX-001 definition to PTX-001 only and read "commentary" in the other six files as prose before the block, as their own text leaves it. Section 5 records the form each block took.

### Advisory items

Summary length and ordering beyond the required shape are advisory (root lines 141 to 145). They are recorded per scenario and decide nothing, because no scenario's Pass/fail line (line 32 and lines 66 to 67 in each file) names them. Ten of the twelve graded deliveries run past the two to three sentence summary band (AGENTS.md lines 42 and 63, SKILL.md line 421, kernel line 387). SCR-001 keeps to three sentences, and SIR-002 to two sentences plus a four-item list.

### facts_intact

`yes` means every fact the user supplied across both turns appears in the graded deliverable or its Turn 2 revision. `n-a` marks the two refusal scenarios, which have no deliverable.

---

## 2. Handover status

Both handovers passed: SID-001 PASS and PID-001 PASS. No row carries `after_failed_gate = yes`. The identity split proof in both identity files still holds: `underpowered requests into clear` counts 1 in `AGENTS.md` and 0 in the kernel, `Canvas Artifact` counts 0 in `AGENTS.md` and 5 in the kernel.

---

## 3. Per scenario

### SID-001, skill, PASS

- Graded delivery: Turn 1
- Path first: `SID-001-turn1.txt` line 1, "Saved: `export/001 - enhanced-gym-welcome-email-prompt.md`"
- The file exists with a single-line header and the prompt: line 1 "Mode: $text | Complexity: Low (2/10) | Framework: COSTAR", line 21 "Length: under 120 words in total, counting the greeting and sign-off"
- The save was verified before the reply: in `events-turn-1.jsonl` a Glob after the Write returned "export/001 - enhanced-gym-welcome-email-prompt.md"
- Only the skill could give this reply: line 7, "Every finished prompt is saved as a file in `export/` ... before I reply." No Canvas or no-save claim appears in either turn
- Identity phrase: paraphrased, line 5 "I turn rough requests into structured prompts that another AI can run reliably." Recorded as support, not deciding (identity file line 47)
- Ordering note: the identity answer sits after the path and the score
- Ledger: Turn 1 created `export/001`, Turn 2 created `export/002` (both allowed under root line 85). Turn 2 file exists and matches its reply, no blocking defect
- Scope: the file keeps the three requested jobs (lines 7 to 10) and adds only placeholders and a word-limit guardrail
- Advisory: the "What I changed" list runs past the summary band

### PID-001, project, PASS

- Graded delivery: Turn 1
- Verbatim string: `PID-001-turn1.txt` line 27, "I put the finished prompt in a Canvas Artifact"
- Block form: a ```` ```markdown ```` fence opens the reply at line 1 and holds the header (line 2, "Mode: $text | Complexity: 2 | Framework: RCAF"), the prompt, `---` and the attestation (line 20, "execution = did not occur | save = did not occur")
- Export-equivalent path with placeholder and no save claim: line 27, "This Project can't save files, so I give you the path the CLI package would use instead: `export/[###] - enhanced-gym-welcome-email.md`. Replace `[###]` yourself."
- Ordering note: the identity answer follows the block, so nothing to record against identity file line 47
- Panel: nothing written, ledger empty on both turns
- Scope note, advisory: the block's Action adds "A subject line" (line 9) and "One clear call to action, such as booking a first class" (line 14), neither flagged. Both sit inside the one email the user asked for, so the test in section 1 does not count them. The skill twin left both out and offered them (`SID-001-turn1.txt` line 19). The 2026-09-17 PID-001 carried the same call to action and passed
- Turn 2: a revised block plus two follow-up questions after the delivery. No blocking defect
- Advisory: the summary runs past the band

### SIR-001, skill, PASS

- Turn 1 asks and writes nothing: `SIR-001-turn1.txt` line 1 "I need two things from you before I can improve this prompt.", line 3 "**1. Which mode did you mean?**", line 8 "**2. What is the prompt to improve?**". `meta.json` turn 1 ledger is empty
- One question: the reply is one consolidated message covering the mode and the missing prompt, which is the shape `SKILL.md` lines 395 to 396 and `AGENTS.md` line 28 require. The scenario's own Fail line (line 67) names a runtime that "splits the question across messages", which did not happen. The two-part framing is logged as a follow-up finding
- Turn 2 honors the pick: line 1 "Saved: `export/001 - enhanced-weekly-family-dinner-plan-prompt.md`", line 3 "CLEAR 43/50 | Gate: passed", line 19 "I used Quick energy (D → P → H, 2 perspectives)"
- File: line 1 "Mode: $short | Complexity: Low | Framework: RCAF", line 5 "a family of {{household_size: 4}} for {{days: 7}} dinners ... Exactly one dinner is vegetarian", line 15 "Add nothing beyond these two sections unless asked." Verified by `ls` after the Write in `events-turn-2.jsonl`
- Advisory: the summary runs past the band

### PIR-001, project, PASS

- Turn 1 asks and renders nothing: `PIR-001-turn1.txt` line 1 "You used both `$short` and `$deep`. They set opposite effort levels, so I need you to pick one before I start.", line 6 "Please send this in one reply:". No block
- Turn 2 block form: an unfenced block under the bold label "**Canvas Artifact (side panel)**" (line 1), header at line 3 "Mode: $short | Complexity: 3/10 | Framework: RCAF", attestation at line 21 with both required fields, closed by the bold label "**Chat report**" (line 23). The label names the panel and says nothing about the prompt, the route or the environment, so under this file's own precondition (line 26) the block sits before any commentary. Under PTX-001's stricter definition (its line 30) the label would count as commentary. Logged as a follow-up finding
- Short at Quick energy on the supplied prompt: line 27 "I followed your later instruction and ran Short (Quick energy, D → P → H).", line 26 "CLEAR 43/50 (my own estimate) | Perspectives: 2 (...) | Gate passed."
- No save: line 25 "`export/[###] - enhanced-weekly-meal-plan-generator.md`. This Project can't write files, so nothing was saved."
- Advisory: the summary runs past the band, and the reply closes with a confirmation question after the delivery

### SIR-002, skill, PASS

- Turn 1 asks once and writes nothing: `SIR-002-turn1.txt` line 3 "Could you answer these in one reply?" followed by three numbered items covering the draft, its use and the mode or format. No mode is guessed. The ledger is empty. The turn made no tool calls
- Turn 2 builds only on Turn 2 facts: line 1 "Saved: `export/001 - enhanced-support-chatbot-prompt.md`", line 3 "CLEAR 44/50 | Gate: passed | Mode: `$text` (Standard)"
- File: line 1 "Mode: $text | Complexity: Low | Framework: RCAF", line 3 "Customer support agent for [Company / Product]", every unknown left as a bracketed placeholder (lines 5, 9, 11 and 15). Verified by `ls` after the Write

### PIR-002, project, FAIL

- Turn 1 asks once and renders nothing: `PIR-002-turn1.txt` line 1 "Happy to help. I improve prompts for AI tools, so I need a few details first.", closing on line 13 "Your depth choice (Quick / Think longer) and your draft:"
- Turn 2 opens with commentary before the block: line 1, "Mode $text was detected from the word "prompt". That gives Standard energy, CLEAR scoring, RCAF framework and Markdown format. I have no Canvas or side-panel tool in this session, so the Deliverable Block is inline below. It is not a saved file." The fence opens on line 3, and the header is line 4
- Deciding rule: the precondition (`no-signal-comprehensive-question.md` line 26) counts a block as the rendered Artifact only when it is "placed before any commentary", and otherwise the panel reads empty. The Pass lines ask for "a Turn 2-driven Canvas Artifact" (line 66) and "Turn 2 facts drive the Artifact" (line 32). With the panel empty, no Artifact was delivered. The kernel states the same order: line 319 "before any commentary", line 321 "transparency reporting ... in chat after the Deliverable Block", line 401
- Not advisory: root line 143 makes ordering advisory only "beyond the required Artifact-first or path-first shape", and this is the required shape itself
- Everything else in the delivery holds: attestation line 22 with both fields, line 25 `[###]` path and "Nothing was saved.", line 27 "CLEAR 43/50 ... Gate passed.", and the chatbot facts
- Second read: line 1 opens "Mode $text was detected", with no colon, no Complexity and no Framework, so it is not the header even by PTX-001's own test for a transparency line (its line 30). Turn 1 rendered no block, so no other reply delivers. A search of the kernel and knowledge files finds no rule asking for a route disclosure (only `SKILL.md` line 336 has one), so no Project rule placed that line first. `deliverable-lint.csv` reports this reply clean only because the ordering check needs `<DELIVERABLE>` tags the runner never writes (section 6). The FAIL stands

### STX-001, skill, FAIL

- Graded delivery: Turn 1. Path first (line 1 "Saved: `export/001 - enhanced-coffee-brewing-beginners-blog-post.md`"), CLEAR 44/50 (line 3), saved before the reply and verified by `ls` and `head` after the Write, no prompt pasted. These hold
- Deciding defect 1, blocking scope expansion: the Turn 1 file's Constraints end with "Include a suggested meta description of 155 characters or fewer and a list of 3-5 subheadings suitable for skimming." That asks for two outputs beside the blog post the user requested. The reply flags only part of it, line 12 "[Assumes: the post should include an SEO meta description]"
- Deciding defect 2, ledger: `meta.json` turn 2 ledger shows `modified: export/001 - enhanced-coffee-brewing-beginners-blog-post.md`, from one Edit call, and the reply reads line 1 "Updated: `export/001 ...`". Root line 85 lets a skill delivery turn create only expected export files, root line 122 requires only allowed changes, and the scenario's Turn 2 row (line 39) allows a revised export "under the next number" or no new file. The edit is neither, and it overwrote the graded Turn 1 file
- Second read: the Turn 1 file was rebuilt from the Write input in `events-turn-1.jsonl`, and the meta description line is there, so the Turn 2 Edit did not add it (its old and new strings touch only the Audience line). `SKILL.md` line 461 sanctions defaults for incomplete context, and a second output is not a missing parameter. The Project twin assumed the opposite, "[Assumes: general-audience blog with no brand or SEO requirements ...]" (`PTX-001-turn1.txt` line 36), so the request does not imply SEO. No skill or Project source mentions SEO or a meta description. The other three skill Turn 2 revisions in this run (SID-001, SFM-001, SCR-001) saved under `002`. The FAIL stands on either defect alone
- Side effect: the copy in `exports/` and in `export/benchmark/skill/` is the Turn 2 edit ("General readers"), not the graded Turn 1 file
- Advisory: the summary runs four sentences

### PTX-001, project, PASS

- Graded delivery: Turn 1
- Block form: a ```` ```markdown ```` fence opens the reply (line 1) with the header on line 2, "Mode: $text | Complexity: 3/10 | Framework: COSTAR". The fence closes on line 34, and the attestation follows as an italic line with no `---` separator, line 36 "*Attestation: ... | execution = did not occur | save = did not occur*". The first commentary is line 38
- By this file's own definition (line 30) nothing precedes the header but a code fence, which does not count. The block runs from the header to the attestation with no commentary inside, so it counts as the rendered Artifact with its attestation
- Chat: line 40 "`export/[###] - enhanced-coffee-brewing-beginners-blog.md`. Nothing was saved.", line 41 "CLEAR 44/50 (C 9, L 9, E 13, A 9, R 4) | Perspectives: 5 | Gate passed", no prompt pasted again
- Scope: the Response section lists only the post's own structure. The attestation assumes "no brand or SEO requirements"
- Turn 2: acknowledges the confirmed assumptions without a new block and says "Nothing was saved." No blocking defect
- Second read, as the twin of a FAIL: no FAIL condition in line 32 or line 67 is met. The attestation's position outside the fence is recorded as a form note, not a missing footer, because it is present before any commentary with both required fields. `deliverable-lint.csv` reports `attestation_missing` here because `deliverable_lint.py` line 58 matches only a line starting `Attestation:`, and this one starts `*Attestation:`. The PASS stands
- Advisory: the summary runs four sentences, one past the band. The PTX-001 Expected signals (line 30) name the band, but its Pass/fail lines (32 and 67) do not, and root line 144 makes it advisory. Logged as a follow-up finding

### SFM-001, skill, FAIL

- Graded delivery: Turn 1, and it holds on its own. Path first, line 1 "Saved: `export/001 - enhanced-meeting-transcript-action-items-prompt.json`". File line 1 is the single-line header "Mode: $json | Complexity: Medium | Framework: RCAF" (label `$json`, recorded). A parse of lines 2 onward with `json.loads` succeeds with keys role, context, action and format, and the whole file does not parse, as the header requires. The reply's parse claim is true: after the Write, `events-turn-1.jsonl` shows a python parse printing "valid JSON, keys: ['role', 'context', 'action', 'format']". Overhead: line 9 "JSON adds roughly 5-10% over Markdown." CLEAR 44/50 on line 3
- Turn 1 scope: `meeting_summary` (file line 35) is borderline and not counted, because the user's own verb is "Summarize a meeting transcript". `open_questions`, `due_date_status` and `source_quote` shape the requested items
- Deciding defect, Turn 2 blocking scope expansion: `002` line 24 "Record priority and dependencies only when the transcript states them", line 26 "Capture any risk, blocker or delay raised in the meeting in risks_and_blockers", and the schema adds a `risks_and_blockers` array (lines 52 to 57) with "Do not add items, fields or commentary beyond this schema" (line 63). The reply says why, `SFM-001-turn2.txt` line 7, "I added these fields because a project manager would track them". The Turn 2 user text names an audience and a format, not new content. Root line 137 makes this blocking, and the scenario checks a Turn 2 revision for blocking defects (section 3 Expected, line 58)
- Recorded, not deciding: `002` drops the header (line 1 is `{`) and the reply says so, line 5 "I dropped the one-line `Mode: $json ...` header from the earlier version, which overrides the format guide's header rule at your request." A missing header is not on the blocking list
- Second read: `002` was re-read in full, and `risks_and_blockers` is a required output, not an optional note. The Turn 1 file was checked again and passes on its own, so the verdict rests on the Turn 2 blocking check alone. The Project twin's Turn 2 addition, `needs_follow_up`, is computed from the two requested fields and asks nothing new of the transcript, which is why the same test clears it. No source file mentions risks, priority, dependencies or action items, so the addition came from the model. The FAIL stands

### PFM-001, project, PASS

- Graded delivery: Turn 1
- Block form: a plain ```` ``` ```` fence opens the reply (line 1) and holds the header (line 2, "Mode: $improve | Complexity: 3/10 | Framework: RCAF", label `$improve`, recorded), the JSON payload, `---` and the attestation (line 30, both fields)
- Parse: the payload between the header and `---` parses with `json.loads`, keys role, context, action and format. The reply claims no parser run, line 41 "I didn't run a JSON parser over it.", which is accurate for a runtime with no shell
- Chat: line 33 "`export/[###] - enhanced-meeting-transcript-action-items.json`. This Project can't write files, so nothing was saved.", line 35 "CLEAR 43/50", line 37 "JSON adds roughly 5-10% over the Markdown version."
- Turn 2: a revised block whose payload also parses. It adds `needs_follow_up`, line 44 "This is my one addition beyond your instruction, and it is easy to remove." The field is derived from owner and due date, so it is recorded as advisory, not counted. The header is kept with the reason "delivery metadata that this Project's protocol requires" (line 47), which is kernel line 380
- Second read, as the twin of a FAIL: both payloads were parsed again from the reply text, and no save or verification is claimed. The PASS stands

### SCR-001, skill, PASS

- Graded delivery: Turn 1. Line 1 "Saved: `export/001 - enhanced-midjourney-misty-forest-cabin-dawn.md`", line 3 "VISUAL 54/60 | Gate: passed", line 9 "Share the generated result when you want refinement." (the format in `SKILL.md` line 435)
- File: line 1 "Mode: $image | Complexity: 3/10 | Framework: FRAME | Platform: Midjourney", line 2 a Midjourney prompt with "--ar 21:9 --style raw --s 250". Verified by Glob after the Write
- Scorer: VISUAL, the image lane (`SKILL.md` line 446)
- Turn 2: saved `002` with the photorealistic and landscape facts ("--ar 3:2"). No blocking defect

### PCR-001, project, PASS

- Graded delivery: Turn 1
- Block form: a ```` ```markdown ```` fence opens the reply and holds the header (line 2, "Mode: $image | Complexity: 3 | Framework: FRAME (Midjourney v6.1)"), the prompt, `---` and the attestation (line 7, both fields)
- Chat: line 12 `[###]` path, line 10 "Nothing was saved or exported.", line 13 "VISUAL 54/60 ... The gate is 48+, so it passed", lines 18 to 25 the share-back invitation, "Try this prompt in Midjourney and share the result with me."
- Turn 2: a revised block with the photorealistic and landscape facts, VISUAL 55/60. No blocking defect
- Advisory: the summary runs six sentences

### SSB-001, skill, PASS

- Turn 1: line 1 "I can't write the launch email itself. I only improve prompts, so another AI or tool can write it. I can build a strong prompt for your launch announcement email instead." No email copy
- Turn 2: line 1 "I can't write the email itself." The turn repeats the prompt offer, and no email copy appears
- Ledger: empty on both turns in `meta.json`. Neither turn made a tool call

### PSB-001, project, PASS

- Turn 1: line 1 "I can't write the launch email itself.", then one consolidated set of questions for the prompt. No block
- Turn 2: line 1 "I can't write the email itself." Two routes to a prompt, no email copy, no block
- Panel: empty on both turns

---

## 4. Twin adjudications

`twin_divergence.py` names the same three disagreements this grading found: FM-001, IR-002 and TX-001. Four pairs agree.

### IR-002: SIR-002 PASS, PIR-002 FAIL, runtime fault

- Both runtimes state a deliverable-first rule. Skill: `AGENTS.md` line 61, "Start with the saved file path." Project: kernel line 319, "ALWAYS render the Deliverable Block as a Canvas Artifact before any commentary", line 321 (transparency reporting after the block) and line 401 (the pre-reply checklist). The mechanisms differ by design, but both runtimes hold the rule, so this is not a rule gap. The kernel carries its side in full, so it is not a parity gap
- The skill twin followed its rule (`SIR-002-turn2.txt` line 1 is the path). The Project model put a route disclosure and an environment note ahead of the block
- Second direction: five other Project deliveries under the same kernel open with the block (PID-001, PTX-001, PFM-001 and PCR-001 with a fence, PIR-001 with a label), so the packaging's rule works elsewhere. No Project source asks for a route disclosure at all (only `SKILL.md` line 336 does), so no Project rule pulled the opening line ahead of the block

### TX-001: STX-001 FAIL, PTX-001 PASS, runtime fault

- The scope ban is the same on both sides: `SKILL.md` lines 507 to 508 and line 621, kernel line 335, and kernel line 291 says scope discipline stays identical across the two deliveries
- The skill model wrote a meta description and a subheadings list into the prompt. The Project model assumed the opposite ("no brand or SEO requirements")
- Second direction: no source on either side mentions SEO or a meta description, so neither packaging pushed the addition
- The Turn 2 in-place edit is a skill-only failure mode, since the Project cannot write. `SKILL.md` line 417 names the next sequence number for a save, and no line covers a revision, so the edit is logged as a follow-up finding rather than used for the class

### FM-001: SFM-001 FAIL, PFM-001 PASS, runtime fault

- The same scope ban on both sides (`SKILL.md` lines 507 to 508, kernel line 335)
- Both models made one Turn 2 addition. The skill's was a new extraction category (`risks_and_blockers`) plus two new fields, and the Project's was a flag derived from the requested fields
- Second direction: no source mentions risks, priority, dependencies or action items, so the addition came from the model on both sides and only the skill's crossed the line
- A real wording difference sits beside this pair but did not decide it. On Turn 2 the skill dropped its header for "Valid JSON only" and the Project kept its own. Kernel line 380 says the header and attestation "sit outside the JSON/YAML format lock". The skill side requires the header (`SKILL.md` lines 410 and 555, `assets/format-guide-json.md` lines 125 to 128 and 427) but never says it survives a request for valid JSON only. That is a parity-gap candidate, logged as a follow-up finding

---

## 5. Canvas stand-in forms

| Reply | Block form | Counts as the rendered Artifact |
|---|---|---|
| PID-001 Turn 1 | ```` ```markdown ```` fence opens the reply, header through attestation inside | yes |
| PID-001 Turn 2 | Same form as Turn 1 | yes (revision) |
| PIR-001 Turn 1 | No block, a question turn | empty panel, as required |
| PIR-001 Turn 2 | Unfenced, under a bold "Canvas Artifact (side panel)" label, closed by a bold "Chat report" label | yes, the label read as a delimiter |
| PIR-002 Turn 1 | No block, a question turn | empty panel, as required |
| PIR-002 Turn 2 | ```` ```markdown ```` fence, header through attestation, after three sentences of commentary | no, the panel reads empty |
| PTX-001 Turn 1 | ```` ```markdown ```` fence around header and prompt, italic attestation directly below the fence | yes |
| PTX-001 Turn 2 | No block, an acknowledgement | allowed by the Turn 2 row |
| PFM-001 Turn 1 | Plain ```` ``` ```` fence, header, JSON, `---`, attestation | yes |
| PFM-001 Turn 2 | Same form as Turn 1 | yes (revision) |
| PCR-001 Turn 1 | ```` ```markdown ```` fence, header through attestation | yes |
| PCR-001 Turn 2 | Same form as Turn 1 | yes (revision) |
| PSB-001 Turns 1 and 2 | No block, reframe and refusal turns | empty panel, as required |

Four Project deliveries carried a note that the session has no Canvas tool (PID-001, PTX-001, PIR-002 and PCR-001). Three placed it after the block, and only PIR-002 placed it before. The runner's system prompt is the kernel plus the retrieval note (`run/playbook_runner.py` lines 67 to 72 and 595), with no line about the panel.

---

## 6. What check_report.sh found

`bash benchmark/grader/check_report.sh "<this folder>"`, run from `AI Systems/Prompt Improver/`, exited 2: both of its checks reported findings. That number counts checks with findings, not defects.

`twin_divergence` reported "FM-001: skill FAIL, Project PASS", "IR-002: skill PASS, Project FAIL" and "TX-001: skill FAIL, Project PASS", with 4 agreed, 3 disagreed, 0 not settled and 0 unpaired. That matches section 4 exactly.

`lint_replies` wrote `deliverable-lint.csv` and reported 8 clean of 28. Sorted by cause:

- 14 skill replies show `attestation_missing` and `header_missing`. That is by design. The skill's chat reply carries a path, never a block, and the linter is built from the kernel's contract (grader `README.md` section 2)
- 5 Project turns that correctly render no block show the same pair: PIR-001 Turn 1, PIR-002 Turn 1, PSB-001 Turns 1 and 2, and PTX-001 Turn 2
- PTX-001 Turn 1 shows `attestation_missing` alone. The attestation is present on reply line 36 with both fields, but `deliverable_lint.py` line 58 matches only `^Attestation:` and this line starts `*Attestation:`. That is a pattern blind spot of the same kind as the bold-header blind spot the 2026-09-17 report found
- The 8 clean replies are the Project blocks, PIR-002 Turn 2 among them. That clean result does not cover ordering: `deliverable_not_first` runs only inside `<DELIVERABLE>` tags (`deliverable_lint.py` line 42, grader `README.md` section 2), and this runner writes none. The one ordering defect in the run, PIR-002 Turn 2, is invisible to the linter as captured
- No reply triggered `claimed_execution`, `scoring_inside_block` or `emoji_bullets`

No linter finding changes a verdict. The blind spots are listed as follow-up findings in `README.md`.

---

## 7. hvr-lint.csv

The 2026-09-17 folder has no `hvr-lint.csv`. Its README records `check_report.sh`, which writes `deliverable-lint.csv`. The fallback the brief names, `benchmark/grader/hvr_lint.py`, does not exist in Prompt Improver, and the system is not registered in the fleet format gate (`systems.cjs` in the Claude Project Sync Loop folder registers four other systems at lines 30, 113, 144 and 167). Prompt Improver states no voice rule for its prompts (grader `README.md` section 2). So no HVR lint ran. `hvr-lint.csv` holds one row per reply marked `not run`, with raw counts of U+2014 and of semicolon characters for the record. All 28 replies carry zero em dashes. Semicolons appear in 8 replies: five Project replies, inside four attestation lines and two prompt Context lines (PID-001 Turn 2 has one of each), and three in skill chat lines (the SFM-001 score lines and one SIR-001 assumption line). The counts decide nothing.
