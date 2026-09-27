# Complexity rubric recount: 24 framework-coverage inputs

## 1. OVERVIEW

One rater scored the 24 framework-coverage inputs with the Complexity Rubric in `sk-prompt-improver/references/depth-framework.md` lines 147-165. The rater read only the rubric and the inputs, never a scenario tier, a target or a deliverable, and wrote the reasons below so any reader can recount a score. The text is the rater's own, with numbered headings added for this folder.

### How the rubric was applied

I scored each request only from what the user wrote, and I ignored the leading `$` commands, the named framework, "keep the full scope" and "no questions". Outputs and Inputs describe the task the user wants the target model to do, not the prompt Prompt Improver writes. The rubric does not say this outright, and it matters for every request. Four wording gaps affected more than one request. First, "one output with distinct sections" does not say whether per-item fields or a layout rule count as sections. I scored Outputs 1 only when the user names parts that do different jobs, and I counted layout rules under Rules so nothing is counted twice. Second, the rubric does not say how finely to split constraints. I counted one constraint per stated limit and per required field, and kept a compound phrase such as "warm but not chatty" as one. Several requests sit at six or seven, so this choice moves Rules between 1 and 2. A conditional rule is counted once, as a conditional, not also as a constraint. Third, "kinds of source" does not say whether facts written inside the request count as inputs. I counted only material the model receives, with one exception, SFW-015, where the user states three positions that contradict each other. Fourth, Stakes names legal, financial, health, safety and privacy but not security, and "financial" does not say whether any budget counts. I gave 2 only where an error would itself cause a legal, payment, health, safety or privacy harm, or where the user bans a judgment. Stated secrets handling and business budgets got 1, and each is marked borderline.

---

## 2. SCORES

| ID | Outputs | Inputs | Rules | Audience | Stakes | Rating | Band | Borderline |
|---|---|---|---|---|---|---|---|---|
| SFW-001 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Outputs 1 (5), Rules 2 (5) |
| SFW-002 | 0 | 2 | 2 | 1 | 2 | 8 | High | Outputs 1 (9), Inputs 1 (7) |
| SFW-003 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | Outputs 2 (still 10, capped), Stakes 1 (9) |
| SFW-004 | 0 | 2 | 1 | 1 | 2 | 7 | High | Inputs 1 (6), Rules 2 (8), Stakes 1 (6) |
| SFW-005 | 2 | 0 | 1 | 2 | 1 | 7 | High | Rules 2 (8), Audience 1 (6), Stakes 2 (8) |
| SFW-006 | 2 | 0 | 2 | 2 | 2 | 9 | Complex | none |
| SFW-007 | 0 | 0 | 1 | 1 | 2 | 5 | Medium | Stakes 1 (4) |
| SFW-008 | 1 | 2 | 2 | 1 | 1 | 8 | High | Rules 1 (7), Stakes 2 (9) |
| SFW-009 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | none |
| SFW-010 | 0 | 0 | 1 | 1 | 2 | 5 | Medium | Rules 2 (6) |
| SFW-011 | 0 | 1 | 2 | 0 | 2 | 6 | Medium | Inputs 2 (7), Rules 1 (5) |
| SFW-012 | 1 | 2 | 2 | 1 | 2 | 9 | Complex | Audience 2 (10) |
| SFW-013 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Outputs 2 (6), Rules 1 (4) |
| SFW-014 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Outputs 2 (6), Stakes 2 (6) |
| SFW-015 | 1 | 2 | 2 | 0 | 1 | 7 | High | Inputs 0 (5), Stakes 2 (8) |
| SFW-016 | 1 | 0 | 1 | 1 | 1 | 5 | Medium | Rules 2 (6) |
| SFW-017 | 1 | 0 | 2 | 1 | 1 | 6 | Medium | Audience 2 (7), Stakes 2 (7) |
| SFW-018 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Audience 1 (6), Stakes 2 (6) |
| SFW-019 | 0 | 0 | 2 | 0 | 0 | 3 | Low | none |
| SFW-020 | 2 | 0 | 2 | 0 | 0 | 5 | Medium | Outputs 1 (4) |
| SFW-021 | 0 | 0 | 2 | 0 | 0 | 3 | Low | none |
| SFW-022 | 0 | 0 | 2 | 0 | 0 | 3 | Low | none |
| SFW-023 | 1 | 0 | 2 | 1 | 0 | 5 | Medium | Outputs 0 (4) |
| SFW-024 | 2 | 0 | 2 | 2 | 1 | 8 | High | Audience 1 (7), Stakes 2 (9) |

The number in brackets in the Borderline column is the rating if that one dimension took the alternative value.

---

## 3. REASONS PER INPUT

### SFW-001

- Outputs 0: one handover summary with one job. "Group exceptions by type" is a layout rule, counted under Rules
- Inputs 0: one input, "the exception log"
- Rules 1: six constraints. Group by type, flag anything still open, dock door for each open item, pallet ID for each open item, under 200 words, "no blame language, just facts" (read as one limit)
- Audience 1: "the night lead reads the summary at the 22:00 handover"
- Stakes 1: a missed open item costs the next shift time
- Borderline: Outputs 1 if grouping by type counts as sections. Rules 2 if "just facts" is split from "no blame language" (seven constraints), or if "for each open item" is read as a second conditional next to "flag anything still open"

### SFW-002

- Outputs 0: one classification of the claim lines. Class, action and quoted receipt line are fields per line, not sections
- Inputs 2: three kinds of source, "the claim lines, the receipts as text and the employee's grade"
- Rules 2: conditional rules: within policy to approval, missing receipt to receipt request, over limit to controller, non-business cost back to employee with the clause, any line above EUR 750 to the controller, hotel limit EUR 180 for grades 1 to 5 and EUR 240 above. Constraints: four fixed classes, recommend only, never mark as paid, always quote the receipt line
- Audience 1: "our finance team", with a stated need for the quoted receipt line
- Stakes 2: financial (expense payments), and a judgment it must not make, "never marks anything as paid"
- Borderline: Outputs 1 if the per-line fields count as sections. Inputs 1 if the employee's grade is a field rather than a source

### SFW-003

- Outputs 1: "one blameless draft in three layers", so one output with distinct sections, plus action items
- Inputs 2: three kinds of source, "a PagerDuty timeline, a Slack incident-channel export and the deploy log", and the two time zones show they can disagree
- Rules 2: conditional rules: flag any gap over 10 minutes, state a root cause only where the logs support it and label everything else a hypothesis. Constraints: blameless, five-sentence exec brief, normalise to UTC, owner from the responders list, due week, customer names become account IDs, SEV1 or SEV2 only
- Audience 2: "engineers", "support leads" and "the exec team"
- Stakes 2: privacy, "customer names become account IDs", and a root-cause judgment it must not make without log support
- Borderline: Outputs 2 if the three layers count as three outputs (no change, capped at 10). Stakes 1 if the name rule reads as house style for an internal draft

### SFW-004

- Outputs 0: one newsletter with one job. "Event dates go in a list at the top" is a layout rule, counted under Rules
- Inputs 2: three kinds of source, "the headteacher's bullet notes, the dates of upcoming events and any lunch or bus timetable changes"
- Rules 1: six constraints. Plain B1-level language, short paragraphs, "warm but not chatty", event dates in a list at the top, under 350 words, never name individual pupils
- Audience 1: parents on phones, "many speak Dutch as a second language"
- Stakes 2: privacy of children, "never name individual pupils"
- Borderline: Inputs 1 if the three are one pasted batch of school news. Rules 2 if "warm" and "not chatty" are two limits. Stakes 1 if the name ban reads as a style rule

### SFW-005

- Outputs 2: three outputs on different channels, "an announcement of about 300 words, a six-question FAQ and a two-line Slack teaser"
- Inputs 0: one source, the policy text given in the request
- Rules 1: six constraints. About 300 words, six FAQ questions, two-line teaser, "direct and reassuring", "never corporate spin", "must not promise anything beyond the policy text". The policy facts are content, not limits
- Audience 2: "420 staff across the Utrecht and Ghent offices, from warehouse crew to engineers", mixed reading levels served at once
- Stakes 1: an overpromise costs trust with staff
- Borderline: Rules 2 if "direct" and "reassuring" are split. Audience 1 if all staff are one audience. Stakes 2 if a promise beyond the policy text is read as a legal or employment risk

### SFW-006

- Outputs 2: SMS, email and phone script, "each message in Dutch and English"
- Inputs 0: one input, "the incident facts we paste"
- Rules 2: conditional rules: SMS only to patients with appointments in the next 48 hours, never mention data exposure unless the facts say so. Constraints: SMS max 300 characters, B1-level language, what we know, what we do not know yet, when the next update comes, never guess a cause, always give the clinic phone number, "formal but empathetic"
- Audience 2: patients "from teenage athletes to people in their 80s", front-desk staff, two languages
- Stakes 2: health (physiotherapy patients) and privacy ("data exposure")
- Borderline: none

### SFW-007

- Outputs 0: one step-by-step procedure
- Inputs 0: one input, "a transcript of a senior clerk narrating a screen recording"
- Rules 1: one conditional rule, mark steps that need a second approver "for credit notes above EUR 5,000". Constraints: one action per step, the screen or field, what the clerk should see afterwards, field names exactly as spoken, leave out the chit-chat (five)
- Audience 1: "new accounts-payable clerks", with stated needs per step
- Stakes 2: financial, booking supplier credit notes with an approval control above EUR 5,000
- Borderline: Stakes 1 if a wrong SOP step is read as a correctable process error rather than a financial one

### SFW-008

- Outputs 1: one guide with distinct sections, macOS and Ubuntu paths, prerequisites list, troubleshooting section
- Inputs 2: three kinds of source, "our monorepo README, the Makefile and the CI config"
- Rules 2: seven constraints. Fresh laptop to green test run in one afternoon, separate macOS and Ubuntu paths, prerequisites with exact versions from the files, a verification check after every stage, troubleshooting only from errors the files mention, commands copied verbatim and never invented, say where to fetch secrets but never show a value
- Audience 1: "a new backend engineer"
- Stakes 1: a wrong step costs a new hire time. Secrets handling is security, which the rubric does not list
- Borderline: Rules 1 if "in one afternoon" is a goal rather than a limit (six). Stakes 2 if secret exposure is read as privacy

### SFW-009

- Outputs 1: two language versions, "Dutch and English versions", which is "two outputs"
- Inputs 2: three kinds of source that can contradict, "a call transcript", "our current checklist" and "the carrier's dangerous-goods rules", with "where the transcript and the checklist disagree"
- Rules 2: conditional rules: list a conflict instead of choosing, any UN3480 shipment goes to the DG officer before the planner books a slot. Constraints: split by role, trigger, system, document, hand-off per step, same step numbers in both languages
- Audience 2: broker, planner and warehouse roles, in two languages
- Stakes 2: safety and legal, lithium batteries under dangerous-goods and customs rules
- Borderline: none

### SFW-010

- Outputs 0: one intake note
- Inputs 0: one input, "each web-form inquiry"
- Rules 1: one conditional rule, flag any dismissal older than two months. Constraints: client type, issue from four classes, every date, the other party's name, never give legal advice, never estimate chances (six)
- Audience 1: "the lawyer who does the free 20-minute call"
- Stakes 2: legal, a possibly missed deadline, and judgments it must refuse, "never give legal advice or estimate chances"
- Borderline: Rules 2 if the conditional is also counted as a constraint (seven)

### SFW-011

- Outputs 0: one list of flags. Sentence, rule and rewrite are fields per flag
- Inputs 1: two inputs to combine, the listing (title, description, bullets) and "our approved list of 38 EU-authorised health claims"
- Rules 2: seven constraints. Flag every claim not on the list, return the exact sentence, the rule it breaks from three classes, a compliant rewrite, the rewrite keeps the product facts, do not touch compliant text, do not judge whether the product works
- Audience 0: no reader stated, the output feeds "the listing checker"
- Stakes 2: legal (EU health-claim rules) and a judgment it must refuse, "must not judge whether the product works"
- Borderline: Inputs 2 if title, description and bullets count as separate kinds of source. Rules 1 if the rewrite and "keeps the product facts" are one limit

### SFW-012

- Outputs 1: one narrative with five named sections, "trigger, customer profile, observed pattern, expected activity, open questions"
- Inputs 2: four kinds of source, "the rule that fired, 90 days of transactions, the KYC profile and prior alerts"
- Rules 2: conditional rules: flag structuring at three or more cash deposits between EUR 9,000 and 9,999 within 10 days, handle joint accounts, missing KYC fields, accounts closed mid-window. Constraints: fixed order, cite a transaction ID per claim, never conclude laundering, never recommend filing or closing, original currency with EUR in brackets
- Audience 1: "the analyst"
- Stakes 2: legal and financial (AML), and a judgment it must refuse, "stays the analyst's call"
- Borderline: Audience 2 if "Auditors liked this sentence" makes auditors a second reader

### SFW-013

- Outputs 1: one answer with three distinct routes
- Inputs 0: no input, the context is stated in the request
- Rules 2: seven constraints. Three routes, clearly different, a one-line pitch each, the café type it wins, a cheap test within a month, "frank and practical", "no buzzwords"
- Audience 0: the user as the reader, "I use Claude as a sparring partner". Baristas are the market, not the reader
- Stakes 1: a weak positioning costs a launch time, "priced 15% above the market leader"
- Borderline: Outputs 2 if the three routes count as three outputs. Rules 1 if "three clearly different" is one limit (six)

### SFW-014

- Outputs 1: one answer with distinct parts, the reasoning, four experiments and the challenge to the pay assumption
- Inputs 0: no input. The exit-interview findings are summarised in the request
- Rules 2: nine constraints. Reason about early-tenure leavers, four distinct experiments, within EUR 120,000 a year, hypothesis, pilot depot, metric, 10-week read-out, main risk to the delivery schedule, challenge the pay assumption
- Audience 0: the user's team as the reader, no specific reader stated
- Stakes 1: a poor experiment costs time and budget
- Borderline: Outputs 2 if the four experiments count as four outputs. Stakes 2 if the EUR 120,000 budget counts as financial stakes

### SFW-015

- Outputs 1: one answer with distinct parts, the insight, the question, three scenarios and where the data is too thin
- Inputs 2: sources that contradict each other, "the CEO wants Germany in 2027, the CFO wants to deepen in the Benelux", "sales says German customers will need on-premise hosting"
- Rules 2: nine constraints. Skeptical stance, surface the deciding insight, state the question sharply, three named scenarios, the assumptions each depends on, the cheapest test before Q2, the kill signal, say where the data is too thin, "exploration, not a plan"
- Audience 0: no reader stated
- Stakes 1: a wrong steer costs time in a split board decision
- Borderline: Inputs 0 if positions written into the request are not inputs, as I read them elsewhere. Stakes 2 if an expansion call on EUR 7.8M ARR counts as financial stakes

### SFW-016

- Outputs 1: two outputs, "the run-of-show" and "a short prep checklist for our two trainers"
- Inputs 0: no input
- Rules 1: six constraints. Agenda from 09:30 to 16:00, two hands-on sessions on the leave module, lunch, a closing Q&A, a short checklist, keep the two targets in view
- Audience 1: "our two trainers", named readers of the checklist
- Stakes 1: a poor plan costs trust with 25 existing customers
- Borderline: Rules 2 if the rating target and the sign-up target are two constraints (seven)

### SFW-017

- Outputs 1: one plan with distinct sections, phases, rollback, communication moments and "a risk table"
- Inputs 0: no input, the scope is stated in the request
- Rules 2: ten constraints. Weekend cutover only, customer-service mailbox offline at most two hours, account for 80 phone-only field staff, entry and exit criteria per phase, a rollback step per phase, a staff communication moment before each phase, a risk table, zero lost mail, under 5% tickets in week one, done within six weekends
- Audience 1: "our IT team"
- Stakes 1: downtime and tickets cost time and trust
- Borderline: Audience 2 if the staff communication moments make staff a second audience. Stakes 2 if lost mail is read as a privacy or records risk

### SFW-018

- Outputs 1: one plan with distinct sections, workstreams, dependencies, go or no-go checklist, hypercare plan, rollback path
- Inputs 0: no input, the facts are stated in the request
- Rules 2: conditional rule, Tilburg only after four weeks of pick accuracy above 99.5% in Liège. Constraints: no go-live from 15 November to 10 January, Liège first, four named workstreams, dependencies, checklist, hypercare, rollback within 12 hours, training in two languages, no missed carrier cut-off in two weeks
- Audience 0: no reader stated. The 260 pickers are a workstream, not a reader
- Stakes 1: a failed go-live costs time and trust with carriers
- Borderline: Audience 1 if the plan's owners are read as a specific audience. Stakes 2 if missed carrier cut-offs count as financial stakes

### SFW-019

- Outputs 0: one image prompt
- Inputs 0: no input
- Rules 2: fourteen constraints. One rider, gravel dyke path, golden hour, low angle, riding toward the camera, Oosterschelde behind, photorealistic catalogue style, warm light with long shadows, 21:9, left third calm and empty, olive jersey, no visible logos, no text, no other people
- Audience 0: no reader with stated needs
- Stakes 0: an image is easy to regenerate
- Borderline: none

### SFW-020

- Outputs 2: three outputs, the prompt, "the negative prompt separately" and "suggest CFG and steps"
- Inputs 0: no input
- Rules 2: more than seven constraints. 2:3 portrait, 1960s screen-print style, four named colours, three depth layers with named content, top quarter empty sky, no lettering, paper grain, slight misregistration, children about 8 to 10 and not photoreal
- Audience 0: no reader with stated needs
- Stakes 0: a poster draft is easy to regenerate
- Borderline: Outputs 1 if the CFG and steps suggestion is not a separate output

### SFW-021

- Outputs 0: one video prompt
- Inputs 0: one input, "our still of a potter's hands"
- Rules 2: more than seven constraints. 10 seconds, 9:16, bowl rises and widens, spiral of slip, dust in window light, slow push-in from waist height, close-up at 8 seconds then hold, calm and tactile, warm natural light, shallow depth of field, face out of frame, clutter soft
- Audience 0: no reader with stated needs
- Stakes 0: a clip is easy to regenerate
- Borderline: none

### SFW-022

- Outputs 0: one continuous shot with native audio
- Inputs 0: no input, text-to-video
- Rules 2: more than seven constraints. One continuous shot, 10 seconds, 16:9, glide at three metres, trolley trains in two directions, three workers on tugs, rise at 4 seconds, settle on the clock at 8 seconds, named sounds, no music, no voices, blue to gold light, workers small and anonymous
- Audience 0: no reader with stated needs
- Stakes 0: a clip is easy to regenerate. "Small and anonymous" is a framing choice for generated people
- Borderline: none

### SFW-023

- Outputs 1: one screen with distinct states, grading and the reject damage-photo step, "keep every state I described"
- Inputs 0: no input. The order photo and return reason are screen content, not task inputs
- Rules 2: one conditional rule, "a reject asks for one damage photo". Constraints: 20 seconds per item, 24-inch touchscreen, cotton gloves, order photo next to the item, the return reason, a big tap target for each of four grades, not a spreadsheet or dark developer tool, "calm, tactile and fast", shadcn/ui
- Audience 1: the inspector, with stated needs, "about 20 seconds", "300 items a shift"
- Stakes 0: a screen concept is easy to correct
- Borderline: Outputs 0 if the states are parts of one screen with one job

### SFW-024

- Outputs 2: five screens in "Dutch and English"
- Inputs 0: no input
- Rules 2: conditional rules: police report number "or a clear way to add it later", "a draft survives a lost signal". Constraints: under five minutes, five named screens, station prefilled, photos and frame number, confirmation with a live tracker, back link without losing input, "steady and competent, never cheerful or gamified", no fintech gradient, no component library
- Audience 2: one stressed commuter served in two languages, "Dutch and English"
- Stakes 1: lost input costs an upset user time and trust
- Borderline: Audience 1 if two languages for one user read as one audience. Stakes 2 if an insurance claim counts as financial stakes
