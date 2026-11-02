# Grading 3: SFW-013 to SFW-018 and PFW-013 to PFW-018

Run: `benchmark/reports/2026-09-27--complexity-rubric--claude-sonnet-5-xhigh`, graded against the playbook as it stood at run time (the scratchpad copy of `manual-testing-playbook/`). Every item below was checked against the reply, the deliverable and, for SFW, the sandbox `exports/` copy and `meta.json`. The structure review was used as a list of leads only.

Readings applied to all twelve, stated once:

- Judgment call on the target model and the replaced one-liner in each fact list: none of the twelve prompts names its target model (Claude, ChatGPT, Gemini 2.5 Pro, Microsoft Copilot) or quotes the old one-liner in the body. I read those two items as kept when the deliverable is the replacement for that one-liner written for that target, since a prompt does not normally name the model it is pasted into. No verdict turns on this reading
- Judgment call on facts: narrowing or recasting a stated number, constraint or preference counts as altered. A default that fills a gap the user left (a placeholder name, "in-person", "internal trainers") counts as kept
- Every SFW sandbox export under `RUN/skill/<ID> - <slug>/exports/export/` is byte-identical to its copy in `export/benchmark/skill/` (checked with `cmp`), and each `meta.json` records exactly one created file, `turns_run` 1 and `turns_declared` 1, with the Write call before the final reply
- Every reply reports a CLEAR result with `passed`, and no reply is a best-effort note below the gate, so `after_failed_gate` is `no` throughout

```csv
id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note
SFW-013,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Header complexity High (7/10) sits above the Medium tier and the prompt adds a trade-off or risk per route and a café-type justification the user did not ask for, with the cheap test narrowed to close to zero budget"
PFW-013,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Header complexity High (7/10) sits above the Medium tier and the 15% list-price premium is recast as 15% more per cup, with an added requirement that each test isolate the positioning story"
SFW-014,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Tier, elements, gate and YAML parse hold but the prompt adds a risk-containment plan, a go or no-go criterion and a depot justification per experiment and narrows the pay assumption to pay per stop"
PFW-014,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Tier, block order, elements, gate and YAML parse hold but the prompt adds a one-depot-per-experiment rule and a conditional extra signal for a next cycle and alters route density to route density perceived as unmanageable"
SFW-015,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Header complexity High (8/10) sits below the Complex tier, the CFO route is tied to small-firm churn and the prompt adds evidence-to-close-each-gap and weakest-board-position outputs"
PFW-015,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Tier and block order hold but the churn fact is recast as concentrated in small firms, an unsupplied hosting fact is added and invented example gaps such as GoBD, CAC and TAM seed the prompt"
SFW-016,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Header complexity High (7/10) sits above the Medium tier and the prompt adds a welcome block, learning objectives, facilitation notes, per-session feedback capture and fixed table columns the user did not ask for"
PFW-016,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Commentary about mode detection and the missing Canvas panel precedes the block, the header complexity High (7/10) sits above the Medium tier, the pilot target gains an end-of-day deadline and unasked segments and checklist items are added"
SFW-017,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"The reply opens with File verified and saved instead of the path, the ticket target is rebased on 1,210 users and narrowed to migration-related tickets and the prompt adds an executive summary, sub-plans, a traceability section and a GDPR note"
PFW-017,project,claude-sonnet-5-xhigh,FAIL,1,1,no,no,"Tier and block order hold but phone-only field staff become phone or tablet users and the prompt adds a scope summary, per-phase execution summaries, a reconciliation check and a ticket monitoring and escalation step"
SFW-018,skill,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Header complexity High (7/10) sits below the Complex tier and the rollback section gains per-step time estimates the user did not ask for"
PFW-018,project,claude-sonnet-5-xhigh,FAIL,1,1,no,yes,"Header complexity High (8/10) sits below the Complex tier and the prompt adds an executive overview, per-workstream milestones, hypercare exit criteria and a named audience"
```

---

### SFW-013, skill, FAIL

Tier sentence: Medium, the label `Medium` or 5 or 6. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRISPE`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, `export/001 - enhanced-oat-milk-positioning-prompt.md`, the sandbox copy matches the deliverable, and the reply's first line is "Saved: `export/001 - enhanced-oat-milk-positioning-prompt.md`". The file holds only the header and the prompt, and the reply does not paste it
- Header names CRISPE inside the Medium tier: FAILS. CRISPE is named, but "High (7/10)" is the High tier
- Body organised by Capacity, Insight, Statement, Personality and Experiment, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 45/50 | Gate: passed"
- Every supplied fact kept: FAILS (judgment call). "a cheap way to test it within a month" became "one cheap way to test it within a month using close to zero budget", which narrows the user's constraint. Ghent, 15% above the market leader, the three barista concerns, three routes and their three fields, the persona, the sparring-partner framing and the frank, no-buzzwords style are all kept
- Scope test: FAILS. Personality adds "name the real trade-off or risk in each route", an output per route the user did not ask for. Experiment adds "(and why that type over another)" to the café-type field and a one-line assumption note. The Experiment element also says "give exactly three things", so the extra risk item contradicts its own element
- Recorded, not deciding: the summary is one long sentence plus an assumption tag, inside or near the advisory band

### PFW-013, project, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. The reply opens with a ```` ```markdown ```` fence, the attestation ending `execution = did not occur | save = did not occur` sits inside the fence, and the chat gives an "Export-equivalent path" with no save claim. The prompt is not pasted again. The block is byte-identical to the deliverable file once the fence lines are removed
- Header names CRISPE inside the Medium tier: FAILS. "High (7/10)"
- Body organised by the five CRISPE elements, each labelled: holds. All five are bold labels. The three route fields sit in Statement and Experiment holds the test design, which still reads as the Experiment element
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | ... | Gate passed"
- Every supplied fact kept: FAILS. The input prices the milk "15% above the market leader", a list-price premium, and Insight keeps that. Experiment then asks whether a barista would "accept paying 15% more per cup", which contradicts Insight's own point that per-cup cost can make the gap "disappear or explode". "a cheap way to test it" became "using only resources a small startup already has", and "the type of café it wins" became "the specific type of café or barista it wins"
- Scope test: FAILS (judgment call). Experiment adds a requirement that each test isolate the positioning story from milk performance ("A test that only proves the milk performs is not enough"). The user asked for a cheap one-month test, not a test design rule. I read this as an added requirement rather than a default
- Recorded, not deciding: the summary is three sentences plus a closing line, and it claims "No new sections or requirements were added"

### SFW-014, skill, FAIL

Tier sentence: High, the label `High` or 7 or 8. Header as written: `Mode: $yaml | Complexity: High (7/10) | Framework: CRISPE`

- Verified `.yaml` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "**Saved:** `export/001 - enhanced-driver-retention-strategy-prompt.yaml`". The prompt is not pasted
- Header names CRISPE inside the High tier: holds. "High (7/10)", mode label `$yaml`, which the scenario allows
- Body organised by the five CRISPE elements, each labelled: holds. Top-level keys `capacity`, `insight`, `statement`, `personality`, `experiment`
- CLEAR passes its gate: holds, with an arithmetic error recorded. The reply gives "C9/L9/E13/A9/R6 → total 46" and itself notes "Reusability 6/5 capped→5". Capped, the total is 45, still above 40, and every floor is met
- Payload below the header parses as YAML: holds. `yaml.safe_load` on the file minus its header line returns the five keys
- Every supplied fact kept: FAILS (judgment call). The input's assumption is "that pay is the main lever". `insight.standing_assumption_to_test` rewrites it as "Leadership currently treats pay per stop as the primary retention lever", and `experiment.pay_lever_guardrail` tests only pay per stop. Personality keeps "pay is the main lever", so the challenge survives, but the fact under challenge is narrowed from pay to one pay component
- Scope test: FAILS. `delivery_schedule_risk` adds "and how that risk is contained", a mitigation output per experiment. `readout_point` adds "what result counts as a go or no-go signal". `pilot_depot` adds "and why that depot is the right test site". `pay_lever_guardrail` adds a conditional explanation output. `reasoning_task` adds five causes the exit interviews never named (onboarding quality, schedule predictability, physical demands, manager relationship, route unfamiliarity)
- Recorded, not deciding: the reply gives no token-overhead figure, which the Expected signals mention but the Pass/fail line does not list. Depot A to D placeholders are a gap fill

### PFW-014, project, FAIL

Tier sentence: High. Header as written: `Mode: $yaml | Complexity: High (7/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds (judgment call on the block boundary). The reply opens on the header line with no preamble, so the block starts there under the stand-in rule. The YAML payload is fenced, then comes a `---` line and the attestation. The attestation is not inside the fence or on the line directly below it, but the `---` separator is the kernel's own template (`Custom Instructions.md` Delivery Protocol), no commentary precedes the block, and nothing sits between the fence and the attestation except that separator. I read the block as header through attestation. No save is claimed, and the prompt is not pasted again
- Header names CRISPE inside the High tier: holds. "High (7/10)"
- Body organised by the five CRISPE elements, each labelled: holds. Five top-level keys
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9/L9/E13/A9/R4) | Perspectives: 5 | Gate passed"
- Payload between the metadata lines parses as YAML: holds. `yaml.safe_load` returns the five keys. The token overhead line reports "+3-7%"
- Every supplied fact kept: FAILS. "route density" became "Route density perceived as unmanageable". `assumption_on_the_table` adds "this has not been tested against route density or shift start time", a claim the user did not make. Pay as the main lever, the 210 drivers, four depots, 38%, the 90 days, the budget and the five fields are kept
- Scope test: FAILS. `depot_allocation` adds "Assign each experiment to a different one of the four Antwerp depots", a constraint the user did not set. `condition_pay_not_primary` adds a new output, "name one additional low-cost signal worth testing in the following 10-week cycle". `required_output` adds a three-way causal verdict (primary, secondary, downstream symptom)
- Recorded, not deciding: the summary is three sentences

### SFW-015, skill, FAIL

Tier sentence: Complex, the label `Complex` or 9 or 10, or a label above High. A bare `High` fails. Header as written: `Mode: $deep | Complexity: High (8/10) | Framework: CRISPE`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line "File verified: **`export/001 - enhanced-germany-expansion-strategy-prompt.md`**" names the path. The prompt is not pasted
- Header names CRISPE inside the Complex tier: FAILS. "High (8/10)" is the High tier
- Body organised by the five CRISPE elements, each labelled: holds. "Capacity & Role", which the scenario allows for Capacity, then Insight, Statement, Personality and Experiment as bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | Gate: passed"
- Every supplied fact kept: FAILS. The CFO's route, "deepen in the Benelux mid-market first", became "deepen the Benelux mid-market as the CFO proposes, directly addressing the 4% monthly churn among sub-20-staff firms", tying the mid-market route to the small-firm segment the user never linked it to. Insight also adds that hosting cost and build timeline "are unknown"
- Scope test: FAILS. Statement adds "explain why it outweighs the other points of disagreement" and "state what evidence would resolve it" for every data gap. Personality adds an output, naming "which board position looks weakest given the data". None of these was asked for. The three named scenarios, their assumptions, tests and kill signals, the data-too-thin warning and "not a plan" are all present
- Recorded, not deciding: the "Q2" reading as Q2 2027 is flagged inline as an assumption. The summary runs four sentences and the reply closes with an offer of other variants

### PFW-015, project, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: Complex (9/10) | Framework: CRISPE`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRISPE inside the Complex tier: holds. "Complex (9/10)"
- Body organised by the five CRISPE elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 | ... | Gate passed"
- Every supplied fact kept: FAILS. "4% monthly churn among firms under 20 staff" became "4% monthly churn concentrated in firms under 20 staff", which changes a segment rate into a claim about where overall churn sits. Insight adds an unsupplied fact about on-premise hosting, "a delivery model this business has not had to support at scale in NL/BE", right after telling the model to use "nothing you have to invent". The product, site-diary software for construction firms, appears only as "site-diary/construction-tech economics" in Capacity (recorded as kept)
- Scope test: FAILS (judgment call). The data-gap section is requested, but it is pre-seeded with invented gaps the input never raised: "German win rate, CAC, and sales-cycle length", "remaining Benelux mid-market TAM" and "German procurement or regulatory requirements such as GoBD or data-residency rules". The scenario says what goes inside an element "still has to come from the request", so I read these as invented requirements rather than illustrations
- Recorded, not deciding: the summary is two long sentences

### SFW-016, skill, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "**Saved:** `export/001 - enhanced-customer-workshop-planning-prompt.md`". The prompt is not pasted
- Header names CRAFT inside the Medium tier: FAILS. "High (7/10)"
- Body organised by Context, Role, Action, Format and Target, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR: 44/50 | Gate: passed"
- Every supplied fact kept: holds. Utrecht, 12 November, 25 HR managers from existing customers, 09:30 to 16:00, two hands-on sessions on the leave module, lunch, closing Q&A, the prep checklist for two trainers, and both targets ("at least 8/10" and "at least 10 sign-ups for the leave module pilot") are present. "in-person" and "internal trainers" are gap fills
- Scope test: FAILS. Action adds "an opening welcome/intro", "its own learning objective and activity" per session, "a one-line facilitation note" per session, "a quick feedback capture point after each hands-on session" and a "pilot sign-up call-to-action". Format fixes table columns and checklist groups the user did not specify. Each is an output or field the user did not ask for
- Recorded, not deciding: the summary is one sentence plus an assumption tag and a share-back line

### PFW-016, project, FAIL

Tier sentence: Medium. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Deliverable Block first, with no commentary before it: FAILS. The reply opens with a mode-detection paragraph ("Mode: $improve, format locked to $markdown by explicit command...") and an environment note ("This session has no Canvas panel available, so the Deliverable Block is rendered as a single fenced block below"). The scenario names a heading, a bold label or an environment note before the block as commentary. The header, attestation and no-save claim inside the block hold, and the prompt is not pasted again
- Header names CRAFT inside the Medium tier: FAILS. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (...) | Gate passed"
- Every supplied fact kept: FAILS. "at least 10 sign-ups for the module pilot" became "at least 10 attendee sign-ups for the leave module pilot by the end of the day", which adds a deadline. The year "[2026]" is a flagged placeholder
- Scope test: FAILS. Action adds "Add any short transition or break segments", a "weight session time toward guided hands-on practice" rule and checklist items for "demo environment/login access", "timing cues" and "how to make the pilot sign-up ask". Target adds "Mark on the run-of-show exactly where feedback is captured", although the user never asked for feedback capture
- Recorded, not deciding: the summary is two sentences

### SFW-017, skill, FAIL

Tier sentence: High. Header as written: `Mode: $improve | Complexity: High (8/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: FAILS on path-first. The export exists (`meta.json` lists one created file, and the sandbox copy matches), but the reply's first line is "File verified and saved.", which names no path. The path comes on line 3. The scenario defines path-first as "the first line of the reply names the saved `export/` path". The prompt is not pasted
- Header names CRAFT inside the High tier: holds. "High (8/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR: 46/50 | Gate: passed"
- Every supplied fact kept: FAILS. "under 5% of users raising a ticket in the first week" became "fewer than 5% of the 1,210 users logging a migration-related support ticket in the first week after their cutover". That counts the 60 shared mailboxes as users, filters by migration-related tickets and moves the window per batch. Context also adds "past Microsoft's extended support since October 2025" and GDPR/AVG obligations, neither supplied
- Scope test: FAILS. Format adds an executive summary of about 150 words, a weekend-by-weekend batching table with fixed columns, a customer-service sub-plan with "a go/no-go checkpoint partway through the 2-hour window", a mobile-only sub-plan and a "Success-target traceability section". The risk table adds an end-of-support row
- Recorded, not deciding: the summary is two sentences plus an assumption tag

### PFW-017, project, FAIL

Tier sentence: High. Header as written: `Mode: $improve | Complexity: High (7/10) | Framework: CRAFT`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRAFT inside the High tier: holds. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9 / L9 / E13 / A9 / R4, all floors met) | ... | Gate passed"
- Every supplied fact kept: FAILS. "80 field staff use phones only" became "their mail access depends entirely on phone/tablet mail-app reconfiguration", which adds tablets. The customer-service mailbox becomes "mission-critical", which the input never said. The ticket target keeps the 1,150-user denominator, and the other counts, offices and targets are kept
- Scope test: FAILS. Format adds a "Scope summary" section, an "Execution Summary" per phase and a "Success-metrics tracking section". Exit criteria add "a mail-integrity or item-count reconciliation check". Action adds "a first-week post-migration monitoring step" with escalation triggers, and asks the model to "state the technique used" for the customer-service ceiling
- Recorded, not deciding: the reply reports four perspectives for an Improve lane at Standard energy. The summary is two sentences and claims "without adding unrequested scope"

### SFW-018, skill, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: High (7/10) | Framework: CRAFT`

- Verified `.md` export saved before a path-first reply: holds. `meta.json` lists one created file, the sandbox copy matches, and the first line is "Saved: `export/001 - enhanced-warehouse-go-live-plan-prompt.md`". The prompt is not pasted
- Header names CRAFT inside the Complex tier: FAILS. "High (7/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 45/50 | Gate: passed"
- Every supplied fact kept: holds (judgment call). Tilburg 38,000 and Liège 12,000 lines a day, one vendor, SAP ERP and three carriers, the 15 November to 10 January blackout, Liège first, the 99.5% gate, the four workstreams, 260 pickers in two languages, dependencies, the checklist, hypercare, the 12-hour rollback and the cut-off target are all present. "four weeks" is written "four consecutive weeks", which I read as the same meaning
- Scope test: FAILS (judgment call). Format adds "time estimates summing to 12 hours or less" on each rollback step, a field the user did not ask for. The placeholders [Company], [WMS vendor] and [Carrier 1] to [Carrier 3] are gap fills. Sign-off criteria, monitoring cadence and trigger conditions sit inside requested parts and are recorded, not counted
- Recorded, not deciding: the summary is one sentence plus an assumption tag

### PFW-018, project, FAIL

Tier sentence: Complex. Header as written: `Mode: $deep | Complexity: High (8/10) | Framework: CRAFT`

- Deliverable Block first, with header, prompt and attestation, and no save claimed: holds. A ```` ```markdown ```` fence opens the reply, the attestation sits inside it, and no save is claimed. The prompt is not pasted again
- Header names CRAFT inside the Complex tier: FAILS. "High (8/10)"
- Body organised by the five CRAFT elements, each labelled: holds. All five are bold labels
- CLEAR passes its gate: holds. "CLEAR 44/50 (C9, L9, E13, A9, R4) | ... | Gate passed"
- Every supplied fact kept: holds. Every site figure, the vendor, the integrations, the blackout, the Liège-first sequence, the "above 99.5% for four consecutive weeks" gate, the 260 pickers in two languages, the 12-hour rollback and the cut-off target are kept. Measuring the 12 hours "of a rollback decision" and the cut-off target per site are flagged assumptions
- Scope test: FAILS. Format adds an "Executive overview" section. Action adds milestones and "explicit Liège vs. Tilburg variants" per workstream and hypercare "exit criteria". Target adds a named "Primary audience". Context adds a meta paragraph about the old one-line request and the claim that Tilburg "cannot inherit Liège's risk tolerance"
- Recorded, not deciding: the summary is two sentences and claims "Nothing was added beyond what makes those requested elements executable"

---

## Twin agreement

- SFW-013 and PFW-013 agree, both FAIL. Both put the header at High (7/10) on a Medium scenario and both alter the test constraint. PFW-013 also recasts the 15% premium as a per-cup figure, and SFW-013 adds a risk item per route
- SFW-014 and PFW-014 agree, both FAIL. Both hit the High tier, parse as YAML and pass CLEAR, and both fail only on facts and scope. SFW-014 narrows pay to pay per stop and adds containment, go or no-go and depot-justification fields. PFW-014 keeps pay as stated but alters route density and adds a depot rule and a next-cycle signal
- SFW-015 and PFW-015 agree, both FAIL, for partly different reasons. PFW-015 reaches the Complex tier at 9/10 and SFW-015 does not at 8/10. Both change a fact and both add unasked content, the weakest board position and evidence per gap in SFW-015, invented example gaps in PFW-015
- SFW-016 and PFW-016 agree, both FAIL. Both are High (7/10) on a Medium scenario and both add unasked agenda segments and fields. PFW-016 also puts commentary before the block and adds an end-of-day deadline to the pilot target, while SFW-016 keeps every fact
- SFW-017 and PFW-017 agree, both FAIL. Both reach the High tier and both fail on facts and scope. SFW-017 alone also fails path-first ("File verified and saved." on line 1) and rebases the ticket target on 1,210 users, while PFW-017 keeps 1,150 but adds tablets
- SFW-018 and PFW-018 agree, both FAIL. Both are High on a Complex scenario and both keep every fact. Both carry additions, per-step rollback time estimates in SFW-018 and a larger set (executive overview, milestones, hypercare exit criteria, named audience) in PFW-018
