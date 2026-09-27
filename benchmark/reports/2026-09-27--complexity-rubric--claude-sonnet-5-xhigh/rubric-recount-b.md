# Complexity rubric recount B: 24 framework-coverage inputs

## 1. OVERVIEW

A second rater scored the 24 framework-coverage inputs with the Complexity Rubric in `sk-prompt-improver/references/depth-framework.md` lines 147-165, apart from the first rater of [`rubric-recount.md`](rubric-recount.md). This rater also read only the rubric and the inputs, never a scenario tier, a target, a deliverable or the first recount. The text is the rater's own, with numbered headings added for this folder. The two recounts land within one point of each other on 24 of 24 inputs, 19 of them exactly, and in the same band on 21.

### How the rubric was applied

I scored each request against the `### Complexity Rubric` table as written, rating the output the user asked the target model to produce and counting only what the user stated. The leading `$` commands, the named framework, "keep the full scope" and every request for no questions were left out. A constraint was counted once per stated limit (length, count, required field, banned element, fixed order, tone), and paired tone words such as "warm but not chatty" count as one. A conditional rule was counted only where the user named a trigger (a threshold, an "unless", a "where", a route). Facts written inline in the request count as one input unless the user names separate sources or says they disagree. Wording that still left me guessing: whether Outputs means the prompt itself or what the prompt produces (I used the latter), whether per-item fields or per-step fields make "distinct sections", whether scene details in image and video prompts count as constraints, and whether security of secrets or an insurance claim falls under the Stakes list, which names privacy and financial but not security.

---

## 2. SCORES

| ID | Outputs | Inputs | Rules | Audience | Stakes | Rating | Band | Borderline |
|---|---|---|---|---|---|---|---|---|
| SFW-001 | 1 | 0 | 1 | 1 | 1 | 5 | Medium | Outputs 0 (grouping by type may not be sections), rating 4 |
| SFW-002 | 0 | 2 | 2 | 1 | 2 | 8 | High | Audience 0 (finance team named but needs not stated), rating 7 |
| SFW-003 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | Outputs 2 (three layers for three readers), rating stays 10 |
| SFW-004 | 1 | 2 | 1 | 1 | 2 | 8 | High | Inputs 1 (all pasted office notes), rating 7 |
| SFW-005 | 2 | 0 | 1 | 2 | 1 | 7 | High | Stakes 2 (promise beyond HR policy), rating 8 |
| SFW-006 | 2 | 0 | 2 | 2 | 2 | 9 | Complex | None that moves the band |
| SFW-007 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Stakes 2 (credit notes above EUR 5,000 are financial), rating 5 |
| SFW-008 | 1 | 2 | 2 | 1 | 1 | 8 | High | Stakes 2 (secrets read as privacy), rating 9 |
| SFW-009 | 2 | 2 | 2 | 2 | 2 | 10 | Complex | None, raw sum 11 capped at 10 |
| SFW-010 | 0 | 0 | 1 | 1 | 2 | 5 | Medium | Outputs 1 (five named note fields), rating 6 |
| SFW-011 | 0 | 1 | 1 | 0 | 2 | 5 | Medium | Rules 2 (if flag-per-claim counts as conditional), rating 6 |
| SFW-012 | 1 | 2 | 2 | 1 | 2 | 9 | Complex | Audience 2 (auditors as a second reader), rating 10 |
| SFW-013 | 1 | 0 | 2 | 0 | 0 | 4 | Low | Rules 1 (if "clearly different" is not a limit), rating 3 |
| SFW-014 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Inputs 1 (exit interviews as a second source), rating 6 |
| SFW-015 | 1 | 2 | 2 | 0 | 1 | 7 | High | Stakes 2 (must not decide where data is thin), rating 8 |
| SFW-016 | 1 | 0 | 1 | 1 | 1 | 5 | Medium | Rules 2 (two targets counted separately), rating 6 |
| SFW-017 | 1 | 0 | 2 | 1 | 1 | 6 | Medium | Stakes 2 (zero lost mail as data loss), rating 7 |
| SFW-018 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Audience 1 (260 pickers in two languages), rating 6 |
| SFW-019 | 0 | 0 | 2 | 0 | 0 | 3 | Low | Rules 1 (scene details not counted), rating 2 |
| SFW-020 | 2 | 0 | 2 | 0 | 0 | 5 | Medium | Outputs 1 (settings are not an output), rating 4 |
| SFW-021 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None that moves the band |
| SFW-022 | 0 | 0 | 2 | 0 | 0 | 3 | Low | Outputs 1 (audio as a separate section), rating 4 |
| SFW-023 | 1 | 0 | 2 | 1 | 0 | 5 | Medium | Outputs 0 (one screen, states not sections), rating 4 |
| SFW-024 | 2 | 0 | 2 | 2 | 1 | 8 | High | Stakes 2 (insurance claim as financial), rating 9 |

---

## 3. REASONS PER INPUT

### SFW-001

- Outputs 1: one handover summary grouped by exception type, which gives it type sections
- Inputs 0: one pasted exception log
- Rules 1: five constraints, group by type, flag anything still open, dock door and pallet ID for each open item, under 200 words, no blame language (just facts)
- Audience 1: the night lead reading at the 22:00 handover, with the open-item needs stated
- Stakes 1: a missed open item costs the next shift time
- Borderline: Outputs could be 0, giving rating 4 and band Low

### SFW-002

- Outputs 0: one per-line classification with a recommendation
- Inputs 2: claim lines, receipts as text and the employee's grade, three kinds of source, and receipts can contradict claim lines
- Rules 2: conditional rules within policy to approval, missing receipt to request, over limit to controller, non-business back to employee with clause, any line above EUR 750 to controller, hotel limit EUR 180 for grades 1 to 5 and EUR 240 above. Constraints four classes, only recommends, never marks paid, always quotes the receipt line
- Audience 1: the finance team, with recommendation and quoted evidence needs
- Stakes 2: financial, and it must refuse to mark anything as paid
- Borderline: Audience could be 0, giving rating 7

### SFW-003

- Outputs 1: one draft in three layers
- Inputs 2: PagerDuty timeline, Slack export and deploy log, three kinds, with timestamps in two zones
- Rules 2: conditional rules gap over 10 minutes flagged, root cause only where logs support it. Constraints blameless, three layers, five-sentence exec brief, normalise to UTC, action items with owner from responders list, due week, customer names become account IDs
- Audience 2: engineers, support leads and the exec team
- Stakes 2: privacy (customer names to account IDs), and it must not state an unsupported root cause
- Borderline: Outputs could be 2, rating stays 10

### SFW-004

- Outputs 1: one newsletter with an event-date list at the top and a body
- Inputs 2: headteacher's bullet notes, event dates and timetable changes, three kinds of source
- Rules 1: six constraints, B1-level language, short paragraphs, warm but not chatty, event dates listed at top, under 350 words, never name pupils
- Audience 1: parents on phones, many with Dutch as a second language
- Stakes 2: privacy of children (never name pupils)
- Borderline: Inputs could be 1, giving rating 7. Audience could be 2 if second-language readers count as a separate reading level

### SFW-005

- Outputs 2: announcement, six-question FAQ and Slack teaser
- Inputs 0: the policy facts written in the request
- Rules 1: six constraints, about 300 words, six-question FAQ, two-line teaser, direct and reassuring, no corporate spin, no promise beyond the policy text
- Audience 2: 420 staff from warehouse crew to engineers across two offices, several reading levels
- Stakes 1: a wrong promise costs trust
- Borderline: Stakes could be 2 if a promise beyond policy is read as legal, giving rating 8

### SFW-006

- Outputs 2: SMS, email and phone script, each in Dutch and English
- Inputs 0: the pasted incident facts
- Rules 2: conditional rule no data exposure unless the facts say so, SMS only to patients booked in the next 48 hours. Constraints SMS max 300 characters, B1 language, what we know, what we do not know, next update time, never guess a cause, direct clinic phone number, formal but empathetic
- Audience 2: patients from teens to 80s plus front-desk staff, in two languages
- Stakes 2: health clinics and possible data exposure
- Borderline: none that moves the band

### SFW-007

- Outputs 0: one step-by-step procedure
- Inputs 0: one transcript
- Rules 1: one conditional rule, second-approver mark for credit notes above EUR 5,000. Constraints one action per step, screen or field, expected result, field names as spoken, no chit-chat
- Audience 1: new accounts-payable clerks
- Stakes 1: a wrong step costs time
- Borderline: Stakes could be 2 (financial booking), giving rating 5 and band Medium

### SFW-008

- Outputs 1: one guide with macOS and Ubuntu paths, prerequisites and troubleshooting sections
- Inputs 2: README, Makefile and CI config, three kinds of source
- Rules 2: eight constraints, fresh laptop to green run in one afternoon, separate macOS and Ubuntu paths, exact versions from the files, verification after every stage, troubleshooting only from mentioned errors, commands verbatim, say where secrets live, never show a secret value
- Audience 1: a new backend engineer
- Stakes 1: a broken guide costs time
- Borderline: Stakes could be 2 if secret exposure counts as privacy, giving rating 9 and band Complex

### SFW-009

- Outputs 2: Dutch and English versions
- Inputs 2: transcript, checklist and carrier rules, stated to disagree
- Rules 2: conditional rules list the conflict where transcript and checklist disagree, UN3480 to the DG officer before a slot is booked. Constraints split by role, trigger, system, document, hand-off, same step numbers in both versions
- Audience 2: broker, planner and warehouse, in two languages
- Stakes 2: dangerous goods safety and customs, and it must refuse to choose between conflicting sources
- Borderline: none, raw sum 11 capped at 10

### SFW-010

- Outputs 0: one intake note
- Inputs 0: one web-form inquiry
- Rules 1: one conditional rule, flag dismissals older than two months. Constraints client type, issue class, every date, other party's name, no legal advice, no estimate of chances
- Audience 1: the lawyer doing the 20-minute call
- Stakes 2: legal, and it must refuse to give advice or estimate chances
- Borderline: Outputs could be 1 for the named fields, giving rating 6

### SFW-011

- Outputs 0: one list of flags
- Inputs 1: the listing and the 38 approved claims, combined
- Rules 1: six constraints, flag every claim not on the list, exact sentence, rule broken from three types, compliant rewrite keeping facts, leave compliant text alone, no efficacy judgment
- Audience 0: no reader stated
- Stakes 2: EU health-claim compliance, and it must refuse to judge whether the product works
- Borderline: Rules could be 2 if flagging only non-listed claims is a conditional rule, giving rating 6

### SFW-012

- Outputs 1: one narrative in five fixed sections
- Inputs 2: rule fired, 90 days of transactions, KYC profile and prior alerts
- Rules 2: conditional rules structuring flag at three or more deposits of EUR 9,000 to 9,999 in 10 days, joint accounts, missing KYC fields, accounts closed mid-window. Constraints fixed order, cite a transaction ID, no laundering conclusion, no filing or closing advice, original currency with EUR in brackets
- Audience 1: the analyst
- Stakes 2: AML legal and financial, and it must refuse the laundering and filing judgment
- Borderline: Audience could be 2 with auditors as a second reader, giving rating 10

### SFW-013

- Outputs 1: three positioning routes as sections of one answer
- Inputs 0: facts stated in the request
- Rules 2: seven constraints, three routes, clearly different, one-line pitch, café type, cheap test within a month, frank and practical, no buzzwords
- Audience 0: the user as sparring partner
- Stakes 0: marketing ideas are easy to revise
- Borderline: Rules could be 1, giving rating 3

### SFW-014

- Outputs 1: four experiments with the same five fields
- Inputs 0: facts and exit-interview findings stated in the request
- Rules 2: eight constraints, four distinct experiments, EUR 120,000 yearly budget, hypothesis, pilot depot, metric, 10-week read-out, main schedule risk, challenge the pay assumption
- Audience 0: the user
- Stakes 1: a weak experiment costs budget and time
- Borderline: Inputs could be 1, giving rating 6

### SFW-015

- Outputs 1: insight, question and three scenarios in one answer
- Inputs 2: CEO, CFO and sales positions stated to conflict
- Rules 2: eight constraints, deciding insight, sharp question, three named scenarios, assumptions each, cheapest test before Q2, kill signal, say where data is too thin, exploration not a plan
- Audience 0: no reader stated beyond the user
- Stakes 1: a strategic misread costs time and money
- Borderline: Stakes could be 2 if "say where data is too thin to decide" is a refused judgment, giving rating 8

### SFW-016

- Outputs 1: run-of-show and trainer prep checklist
- Inputs 0: facts stated in the request
- Rules 1: six constraints, 09:30 to 16:00, two hands-on sessions on the leave module, lunch, closing Q&A, checklist for two trainers, keep the rating and sign-up targets in view
- Audience 1: the two trainers running 25 HR managers through the day
- Stakes 1: a weak day costs customer trust
- Borderline: Rules could be 2 if the two targets count separately, giving rating 6

### SFW-017

- Outputs 1: one plan with phases, rollback, comms moments and a risk table
- Inputs 0: facts stated in the request
- Rules 2: ten constraints, weekend-only cutover, customer-service mailbox offline at most two hours, 80 phone-only field staff, entry and exit criteria, rollback per phase, comms before each phase, risk table, zero lost mail, under 5% tickets in week one, six weekends
- Audience 1: the IT team, with phone-only field staff as a stated need
- Stakes 1: a failed cutover costs time and trust
- Borderline: Stakes could be 2 if zero lost mail is read as data loss, giving rating 7

### SFW-018

- Outputs 1: one plan with workstreams, dependencies, checklist, hypercare and rollback
- Inputs 0: facts stated in the request
- Rules 2: one conditional rule, Tilburg only after four weeks above 99.5% pick accuracy in Liège. Constraints no go-live 15 November to 10 January, Liège first, four workstreams, training in two languages, dependencies, go or no-go checklist, hypercare, rollback within 12 hours, no missed carrier cut-off
- Audience 0: no reader stated
- Stakes 1: a missed cut-off costs time and customer trust
- Borderline: Audience could be 1, giving rating 6

### SFW-019

- Outputs 0: one image prompt
- Inputs 0: none
- Rules 2: one rider, low angle, toward camera, Oosterschelde behind, photorealistic catalogue look, warm light and long shadows, 21:9, calm left third, olive jersey, no logos, no text, no other people
- Audience 0: none stated
- Stakes 0: easy to regenerate
- Borderline: Rules could be 1 if scene details are not limits, giving rating 2

### SFW-020

- Outputs 2: positive prompt, separate negative prompt and CFG and steps suggestion
- Inputs 0: none
- Rules 2: 2:3 portrait, 1960s screen-print style, four named colours, three depth layers, empty top quarter, no lettering, paper grain, ink misregistration, children aged 8 to 10 and not photoreal
- Audience 0: none stated
- Stakes 0: easy to regenerate
- Borderline: Outputs could be 1 if settings are not an output, giving rating 4 and band Low

### SFW-021

- Outputs 0: one video prompt
- Inputs 0: one still image
- Rules 2: 10 seconds, 9:16, bowl rises and widens, slip spiral, drifting dust, slow push-in from waist height, close-up at 8 seconds then hold, warm natural light, shallow depth of field, face out of frame, clutter soft
- Audience 0: none stated
- Stakes 0: easy to regenerate
- Borderline: none that moves the band

### SFW-022

- Outputs 0: one video prompt with audio
- Inputs 0: none
- Rules 2: one continuous shot, 10 seconds, 16:9, glide at about three metres, rise at 4 seconds, settle on the clock at 8 seconds, named audio, no music, no voices, blue to gold light, workers small and anonymous
- Audience 0: none stated
- Stakes 0: easy to regenerate
- Borderline: Outputs could be 1 with audio as a section, giving rating 4

### SFW-023

- Outputs 1: one screen with the grading and reject states
- Inputs 0: none
- Rules 2: one conditional rule, a reject asks for one damage photo. Constraints about 20 seconds per item, grades A, B, C or reject, 24-inch touchscreen, order photo next to item, return reason, big tap targets, not a spreadsheet or dark developer tool, calm tactile and fast, shadcn/ui
- Audience 1: the gloved inspector doing 300 items a shift
- Stakes 0: a screen concept is easy to revise
- Borderline: Outputs could be 0, giving rating 4 and band Low

### SFW-024

- Outputs 2: Dutch and English versions of a five-screen flow
- Inputs 0: none
- Rules 2: ten constraints, under five minutes, five screens, prefilled station, photos and frame number, police report or add later, confirmation with live tracker, back links without losing input, draft survives lost signal, steady not cheerful, no generic fintech gradient
- Audience 2: an upset commuter served in two languages
- Stakes 1: a poor claim flow costs trust
- Borderline: Stakes could be 2 if the insurance claim counts as financial, giving rating 9 and band Complex
