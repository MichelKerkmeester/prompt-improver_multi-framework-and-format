# Blind recount of the 24 framework-coverage inputs

## Note on method

I read only the `### Complexity Rubric` section of the DEPTH Thinking Framework knowledge file and the 24 inputs. Every point rests on something the request states. Outputs and Inputs describe what the target model hands back and receives, so for image and video requests the output is one image or one clip, and a negative prompt or suggested settings are parts of the prompt, not outputs. The leading `$` commands, the named framework and the request for no questions are not counted. I also left out "keep the full scope", "keep every rule" and "keep every beat", because they instruct the prompt writer and set no limit on the target output. Facts written into the request are context, except in SFW-015, where the user states board positions that contradict each other. A required field repeated per item (per step, per flag, per experiment) counts once. A rule that applies only when something holds counts once as a conditional and never also as a constraint. Wording that still left me guessing: whether several inputs are "different kinds" when the user names them but does not say where they come from (SFW-002, SFW-004, SFW-008), whether per-channel or per-screen parts of one deliverable are sections or separate outputs (SFW-003, SFW-018, SFW-024), whether "one specific audience with stated needs" covers a user who is the only reader, and where "an error costs time or trust" ends for a design concept.

## Scores

| ID | Outputs | Inputs | Rules | Audience | Stakes | Rating | Band | Borderline |
|---|---|---|---|---|---|---|---|---|
| SFW-001 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Audience could be 0 (rating 3) |
| SFW-002 | 0 | 1 | 2 | 1 | 2 | 7 | High | Inputs could be 2 (rating 8), Audience could be 0 (rating 6) |
| SFW-003 | 1 | 2 | 2 | 2 | 1 | 9 | Complex | Outputs could be 2, Stakes could be 2 (rating 10 either way) |
| SFW-004 | 0 | 1 | 1 | 1 | 2 | 6 | Medium | Stakes could be 1 (rating 5), Inputs could be 2 (rating 7) |
| SFW-005 | 2 | 0 | 1 | 1 | 1 | 6 | Medium | Audience could be 2 (rating 7), Inputs could be 1 (rating 7) |
| SFW-006 | 2 | 0 | 2 | 2 | 2 | 9 | Complex | Stakes could be 1 (rating 8) |
| SFW-007 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Stakes could be 2 (rating 5) |
| SFW-008 | 1 | 1 | 2 | 1 | 1 | 7 | High | Rules could be 1 (rating 6), Inputs could be 2 (rating 8) |
| SFW-009 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | Outputs could be 2 (still 10 after the cap) |
| SFW-010 | 0 | 0 | 1 | 1 | 2 | 5 | Medium | None |
| SFW-011 | 0 | 1 | 1 | 0 | 2 | 5 | Medium | Rules could be 2 (rating 6) |
| SFW-012 | 0 | 2 | 2 | 1 | 2 | 8 | High | None |
| SFW-013 | 0 | 0 | 1 | 0 | 0 | 2 | Low | Outputs could be 1 (rating 3) |
| SFW-014 | 0 | 0 | 2 | 0 | 1 | 4 | Low | Outputs could be 1 (rating 5) |
| SFW-015 | 1 | 2 | 2 | 0 | 1 | 7 | High | Audience could be 1 (rating 8) |
| SFW-016 | 1 | 0 | 1 | 1 | 1 | 5 | Medium | Rules could be 2 (rating 6), Audience could be 0 (rating 4) |
| SFW-017 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Audience could be 1 (rating 6) |
| SFW-018 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Outputs could be 2 (rating 6) |
| SFW-019 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None |
| SFW-020 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None |
| SFW-021 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None |
| SFW-022 | 0 | 0 | 2 | 0 | 0 | 3 | Low | Outputs could be 1 if the native audio counts as a second output (rating 4) |
| SFW-023 | 0 | 0 | 2 | 1 | 0 | 4 | Low | Outputs could be 1, Stakes could be 1 (rating 5 either way) |
| SFW-024 | 2 | 0 | 2 | 2 | 1 | 8 | High | Outputs could be 1 (rating 7), Stakes could be 0 (rating 7) |

## Reasons per ID

### SFW-001

- Outputs 0: one handover summary. Grouping by type is an ordering rule, not a section
- Inputs 0: one input, the pasted exception log
- Rules 1: group by type, flag anything still open, under 200 words, no blame language (one limit with "just facts"), and one conditional, dock door and pallet ID for each open item
- Audience 1: the night lead reading at the 22:00 handover
- Stakes 1: a wrong or missed exception costs the next shift time and trust
- Borderline: Audience could be 0 if a named reader at handover is not "stated needs"

### SFW-002

- Outputs 0: one per-line classification with a recommended action per line
- Inputs 1: claim lines, receipts as text and the employee's grade, several inputs to combine. All arrive from the expense tool, so I did not treat them as three kinds
- Rules 2: constraints are the four classes, recommend only and never mark paid, quote the receipt line relied on. Conditionals are within policy gives approval, missing receipt gives a receipt request, over limit goes to the controller, non-business cost goes back with the policy clause, any line above EUR 750 goes to the controller, hotel limits EUR 180 or EUR 240 by grade
- Audience 1: the finance team and the finance controller
- Stakes 2: a wrong class or missed limit is a wrong payment
- Borderline: Inputs could be 2 if claim lines, receipts and grade count as three kinds of source, Audience could be 0 since the output goes to a tool

### SFW-003

- Outputs 1: one blameless draft in three named layers that do different jobs
- Inputs 2: PagerDuty timeline, Slack export and deploy log, three kinds of source, and timestamps arrive in two time zones
- Rules 2: constraints are blameless, five-sentence exec brief, normalise to UTC, action items need an owner from the responders list, a due week, customer names become account IDs. Conditionals are flag any gap over 10 minutes, and state a root cause only when the logs support it, otherwise label it a hypothesis
- Audience 2: engineers, support leads and the exec team served at once
- Stakes 1: a wrong root cause or timeline costs trust
- Borderline: Outputs could be 2 if the three layers count as three outputs, Stakes could be 2 if customer names are personal data

### SFW-004

- Outputs 0: one newsletter. Dates at the top is a layout rule
- Inputs 1: headteacher's bullet notes, upcoming event dates and timetable changes to combine
- Rules 1: B1-level language, short paragraphs, warm but not chatty, event dates in a list at the top, under 350 words, never name individual pupils (six constraints)
- Audience 1: parents on phones, many with Dutch as a second language
- Stakes 2: naming a pupil exposes a child's personal data
- Borderline: Stakes could be 1 if naming a pupil in a school newsletter is read as a trust cost, Inputs could be 2 if the three pastes are three kinds of source

### SFW-005

- Outputs 2: announcement, six-question FAQ and Slack teaser
- Inputs 0: the policy facts are written into the request
- Rules 1: about 300 words, six questions, two lines, direct and reassuring never corporate spin, never promise beyond the policy text (five constraints)
- Audience 1: 420 staff in Utrecht and Ghent
- Stakes 1: a wrong policy detail costs trust and HR time
- Borderline: Audience could be 2 if "from warehouse crew to engineers" counts as several reading levels, Inputs could be 1 if "the policy text" is a pasted input

### SFW-006

- Outputs 2: SMS, email and phone script, each in Dutch and English
- Inputs 0: one input, the pasted incident facts
- Rules 2: constraints are SMS max 300 characters, B1 language, says what we know, what we do not know yet, when the next update comes, never guess at a cause, always give the clinic phone number, formal but empathetic. Conditionals are the SMS only for patients with appointments in the next 48 hours, and mention data exposure only when the facts say so
- Audience 2: patients from teenagers to people in their 80s, front-desk staff, Dutch and English
- Stakes 2: a wrong statement about data exposure is a privacy and legal harm for health patients
- Borderline: Stakes could be 1 if an outage message is read as a trust cost only

### SFW-007

- Outputs 0: one step-by-step procedure
- Inputs 0: one transcript
- Rules 1: constraints are one action per step, the screen or field, what the clerk sees afterwards, field names exactly as spoken, leave out chit-chat. One conditional, mark steps needing a second approver for credit notes above EUR 5,000
- Audience 1: new accounts-payable clerks
- Stakes 1: a wrong step costs clerks time and rework
- Borderline: Stakes could be 2 if a missed approver mark counts as a wrong payment

### SFW-008

- Outputs 1: one guide with named sections, macOS and Ubuntu paths, a prerequisites list and a troubleshooting section
- Inputs 1: README, Makefile and CI config from one monorepo, several inputs to combine
- Rules 2: fresh laptop to a green test run in one afternoon, exact versions taken from the files, a verification check after every stage, troubleshooting only from errors the inputs mention, commands copied verbatim, say where to fetch secrets, never show a secret value (seven constraints)
- Audience 1: a new backend engineer
- Stakes 1: the rubric scores a secret to handle with care at 1
- Borderline: Rules could be 1 if the two secrets limits are one phrase, Inputs could be 2 if three file types count as three kinds

### SFW-009

- Outputs 1: one work instruction in two language versions
- Inputs 2: transcript, checklist and carrier dangerous-goods rules, and the user states they can disagree
- Rules 2: constraints are steps split by role, each step's trigger, system, document and hand-off, same step numbers in both languages. Conditionals are list the conflict where transcript and checklist disagree, and UN3480 shipments go to the DG officer before a slot is booked
- Audience 2: broker, planner and warehouse roles in Dutch and English
- Stakes 2: lithium battery dangerous goods, a safety and legal harm
- Borderline: Outputs could be 2, which leaves the rating at 10 after the cap

### SFW-010

- Outputs 0: one intake note
- Inputs 0: one web-form inquiry
- Rules 1: constraints are client type, issue, every date, the other party's name, never give legal advice or estimate chances. One conditional, flag a dismissal older than two months
- Audience 1: the lawyer doing the free 20-minute call and the conflict check
- Stakes 2: a missed deadline flag is a missed legal duty, and the prompt must refuse to give legal advice
- Borderline: none

### SFW-011

- Outputs 0: one list of flags
- Inputs 1: the listing and the approved list of 38 claims, two inputs of different kinds
- Rules 1: constraints are the exact sentence, the rule broken from three classes, a compliant rewrite that keeps the product facts, never touch compliant text, never judge whether the product works. One conditional, flag a claim only when it is not on the list
- Audience 0: no reader is stated
- Stakes 2: EU health-claim compliance is legal, and the prompt must refuse the efficacy judgment
- Borderline: Rules could be 2 if "keeps the product facts" and the rewrite count separately and the flag rule is read as a plain constraint

### SFW-012

- Outputs 0: one case narrative. The fixed order is a constraint
- Inputs 2: the fired rule, 90 days of transactions, the KYC profile and prior alerts, four kinds of source
- Rules 2: constraints are the fixed five-part order, cite a transaction ID per claim, never conclude laundering, never recommend filing or closing, original currency with EUR in brackets. Conditionals are the structuring flag at three or more deposits of EUR 9,000 to 9,999 within 10 days, joint accounts, missing KYC fields and accounts closed mid-window
- Audience 1: the analyst, with auditors as a stated reviewer
- Stakes 2: AML is legal and financial, and the prompt must refuse the laundering conclusion
- Borderline: none

### SFW-013

- Outputs 0: one set of three routes
- Inputs 0: facts are in the request
- Rules 1: three clearly different routes, a one-line pitch, the café type it wins, a cheap test within a month, weigh foam stability, taste and price per cup, frank and practical with no buzzwords (six constraints)
- Audience 0: the user as sole reader
- Stakes 0: marketing ideas are easy to correct
- Borderline: Outputs could be 1 if the barista analysis and the routes are distinct sections

### SFW-014

- Outputs 0: one set of four experiments
- Inputs 0: the turnover and exit-interview facts are written into the request
- Rules 2: four distinct experiments, fit EUR 120,000 a year, hypothesis, pilot depot, metric, 10-week read-out, main risk to the schedule, challenge the pay assumption (eight constraints)
- Audience 0: the user as sole reader
- Stakes 1: the rubric scores a budget at 1
- Borderline: Outputs could be 1 if the reasoning about early leavers and the challenge are distinct sections

### SFW-015

- Outputs 1: one analysis with named parts, the deciding insight, the sharp question, three scenarios and the data-gap statement
- Inputs 2: the user states contradicting positions from the CEO, CFO and sales
- Rules 2: skeptical stance, three named scenarios, the assumptions each depends on, the cheapest test before Q2, the kill signal, say where data is too thin, exploration not a plan (seven constraints)
- Audience 0: no reader beyond the user is stated
- Stakes 1: a strategy call with budget weight costs time and trust
- Borderline: Audience could be 1 if the split board is read as the audience

### SFW-016

- Outputs 1: the run-of-show and a prep checklist for the trainers
- Inputs 0: facts are in the request
- Rules 1: 09:30 to 16:00, two hands-on sessions on the leave module, lunch, a closing Q&A, a short checklist, keep the targets in view (six constraints)
- Audience 1: the two trainers who use the checklist
- Stakes 1: the rubric scores a sales target at 1
- Borderline: Rules could be 2 if the two targets count separately, Audience could be 0 if the user is the only reader

### SFW-017

- Outputs 1: one plan with named parts, phases, rollback steps, communication moments and a risk table
- Inputs 0: facts are in the request
- Rules 2: weekend cutover only, customer-service mailbox offline at most two hours, 80 phone-only field staff, entry and exit criteria, a rollback step per phase, a communication moment per phase, zero lost mail, under 5% tickets, done within six weekends
- Audience 0: the IT team is the reader, with no stated needs
- Stakes 1: lost mail or downtime costs time and trust
- Borderline: Audience could be 1 if the IT team counts as a specific audience

### SFW-018

- Outputs 1: one plan with named parts, workstreams, dependencies, a go or no-go checklist, a hypercare plan and a rollback path
- Inputs 0: facts are in the request
- Rules 2: constraints are no go-live between 15 November and 10 January, Liège first, the four named workstreams, training in two languages, rollback within 12 hours, no missed carrier cut-off in two weeks. One conditional, Tilburg follows only after four weeks above 99.5% pick accuracy (seven items)
- Audience 0: no reader is stated
- Stakes 1: a missed cut-off costs time and trust
- Borderline: Outputs could be 2 if the checklist, hypercare plan and rollback path are separate outputs

### SFW-019

- Outputs 0: one image
- Inputs 0: none
- Rules 2: one rider, gravel dyke path, golden hour, low angle, toward the camera, Oosterschelde behind, photorealistic catalogue look, warm light with long shadows, 21:9, left third empty, olive jersey, no logos, no text, no other people
- Audience 0: general
- Stakes 0: easy to regenerate
- Borderline: none

### SFW-020

- Outputs 0: one poster image. The negative prompt and the CFG and steps suggestion are parts of the prompt
- Inputs 0: none
- Rules 2: 2:3 portrait, 1960s screen-print style, four named colours, three depth layers with named content, top quarter empty, no lettering, paper grain, ink misregistration, children aged 8 to 10 and not photoreal
- Audience 0: general
- Stakes 0: easy to regenerate
- Borderline: none

### SFW-021

- Outputs 0: one clip
- Inputs 0: one input, the still image
- Rules 2: 10 seconds, 9:16, bowl rises and widens, slip flicks, dust drifts, slow push-in from waist height, close-up of the thumbs at 8 seconds then hold, calm and tactile, warm natural light, shallow depth of field, face out of frame, clutter soft
- Audience 0: general
- Stakes 0: easy to regenerate
- Borderline: none

### SFW-022

- Outputs 0: one clip with native audio
- Inputs 0: none
- Rules 2: one continuous shot, 10 seconds, 16:9, glide at about three metres, trolley trains in two directions, three workers on tugs, rise at 4 seconds, settle on the clock at 8 seconds, hum, wheels and chime, no music, no voices, blue to gold light, workers small and anonymous
- Audience 0: general
- Stakes 0: easy to regenerate
- Borderline: Outputs could be 1 if the audio track counts as a second output

### SFW-023

- Outputs 0: one screen concept
- Inputs 0: none
- Rules 2: constraints are about 20 seconds per item, grades A, B, C or reject, 24-inch touchscreen, cotton gloves, order photo next to the item, the return reason, a big tap target per grade, not a spreadsheet or dark developer tool, calm tactile and fast, shadcn/ui. One conditional, a reject asks for one damage photo
- Audience 1: the inspector, with stated needs
- Stakes 0: a screen concept is easy to correct
- Borderline: Outputs could be 1 if the reject state is a distinct section, Stakes could be 1 if a grading slip at 300 items a shift counts

### SFW-024

- Outputs 2: five named screens, in Dutch and English
- Inputs 0: none
- Rules 2: constraints are under five minutes, station prefilled from location, photos and frame number, police report number or add it later, a live claim tracker, back links without losing input, steady and competent never cheerful or gamified, no generic fintech gradient, no component library. One conditional, a draft survives a lost signal
- Audience 2: an upset commuter short on time, served in two languages
- Stakes 1: an incomplete theft claim costs the user time and trust
- Borderline: Outputs could be 1 if five screens are sections of one flow, Stakes could be 0 for a design brief
