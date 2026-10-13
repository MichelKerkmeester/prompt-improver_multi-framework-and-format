# Complexity recount C (new rubric)

## Note on method

I read only the Complexity Rubric section of `sk-prompt-improver/references/depth-framework.md` and the 24 inputs, and scored each request as the user wrote it. Outputs and Inputs describe what the target model does with the finished prompt, so a negative prompt, CFG and steps or the prompt's own framework blocks count as nothing, and a generated image or video counts as one output. Facts written into the request count as context, not inputs, except in SFW-015 where the user states board positions that contradict each other. A required field counts as one constraint each, a layout or order rule counts as a constraint rather than a section, and a rule that applies only when a threshold, route or state holds counts once as a conditional. The wording that left me guessing most is the line between "one output with distinct sections" and "three or more outputs": a user who says "one draft in three layers" (SFW-003), "a plan that needs" a checklist, hypercare plan and rollback path (SFW-018) or "a flow with five screens" (SFW-024) can be read either way. A second guess was whether a field required only "for each open item" is a scoped constraint or a conditional rule, and whether three files from one repository (SFW-008) are several inputs or three kinds of source.

## Scores

| ID | Outputs | Inputs | Rules | Audience | Stakes | Rating | Band | Borderline |
|---|---|---|---|---|---|---|---|---|
| SFW-001 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Rules 2 if "just facts" counts apart from "no blame language" (5) |
| SFW-002 | 0 | 2 | 2 | 1 | 2 | 8 | High | Outputs 1 if the receipt request and return note count as separate messages (9), Audience 0 (7) |
| SFW-003 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | Outputs 2 if the three layers are outputs (10, capped), Stakes 1 (9) |
| SFW-004 | 0 | 1 | 1 | 1 | 2 | 6 | Medium | Stakes 1 if naming a pupil is not read as exposed personal data (5), Inputs 2 (7) |
| SFW-005 | 2 | 0 | 1 | 2 | 1 | 7 | High | Audience 1 if all staff is one audience (6), Inputs 1 if "the policy text" is an input (8) |
| SFW-006 | 2 | 0 | 2 | 2 | 2 | 9 | Complex | Stakes 1 (8) |
| SFW-007 | 0 | 0 | 1 | 1 | 1 | 4 | Low | Stakes 2 if a wrong credit-note booking counts as a wrong payment (5) |
| SFW-008 | 1 | 1 | 2 | 1 | 1 | 7 | High | Rules 1 if "in one afternoon" is a goal, not a limit (6), Inputs 2 if README, Makefile and CI config are three kinds (8) |
| SFW-009 | 1 | 2 | 2 | 2 | 2 | 10 | Complex | Outputs 2 changes nothing (capped) |
| SFW-010 | 0 | 0 | 1 | 1 | 2 | 5 | Medium | None material |
| SFW-011 | 0 | 1 | 1 | 0 | 2 | 5 | Medium | Outputs 1 if flag and rewrite are distinct sections (6) |
| SFW-012 | 0 | 2 | 2 | 1 | 2 | 8 | High | Audience 2 if auditors are a second reader (9) |
| SFW-013 | 0 | 0 | 1 | 0 | 0 | 2 | Low | Stakes 1 for the launch pricing (3), Outputs 1 (3) |
| SFW-014 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Outputs 0 if the reasoning step is process, not a section (4) |
| SFW-015 | 1 | 2 | 2 | 0 | 1 | 7 | High | Rules 1 if "skeptical" is persona, not a constraint (6), Audience 1 for the board (8) |
| SFW-016 | 1 | 0 | 2 | 1 | 1 | 6 | Medium | Rules 1 if the two targets count once (5) |
| SFW-017 | 1 | 0 | 2 | 1 | 1 | 6 | Medium | Audience 0 (5), Stakes 2 for lost mail (7) |
| SFW-018 | 1 | 0 | 2 | 0 | 1 | 5 | Medium | Outputs 2 (6), Audience 1 (6), Stakes 2 (6) |
| SFW-019 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None material |
| SFW-020 | 0 | 0 | 2 | 0 | 0 | 3 | Low | Outputs 1 if the separate negative prompt counts (4) |
| SFW-021 | 0 | 0 | 2 | 0 | 0 | 3 | Low | None material |
| SFW-022 | 0 | 0 | 2 | 0 | 0 | 3 | Low | Outputs 1 if native audio is a second output (4) |
| SFW-023 | 0 | 0 | 2 | 1 | 0 | 4 | Low | Outputs 1 if the reject state is a distinct section (5) |
| SFW-024 | 2 | 0 | 2 | 2 | 1 | 8 | High | Outputs 1 if five screens are one flow with sections (7), Stakes 2 for an insurance claim (9) |

## SFW-001

- Outputs 0: one shift summary, and "group exceptions by type" is a layout rule
- Inputs 0: one input, the pasted exception log
- Rules 1: counted group by type, flag anything still open, dock door per open item, pallet ID per open item, under 200 words, no blame language and just facts (6 constraints)
- Audience 1: "the night lead reads the summary at the 22:00 handover"
- Stakes 1: a missed open item costs the next shift time
- Borderline: counting "just facts" apart from "no blame language" gives 7 constraints, Rules 2, rating 5

## SFW-002

- Outputs 0: one per-line recommendation set, no named sections
- Inputs 2: claim lines, receipts as text and the employee's grade, and receipts can contradict claim lines
- Rules 2: conditionals counted are the four class routes (approval, receipt request, controller, back to employee with clause), "any line above EUR 750 goes to the controller" and the grade-based hotel limit (6 conditionals), constraints counted are recommend only, never mark as paid and always quote the receipt line
- Audience 1: the finance team and controller who act on the recommendation
- Stakes 2: a wrong approval is a wrong payment
- Borderline: the receipt request and the return note could be separate messages, Outputs 1, rating 9

## SFW-003

- Outputs 1: "one blameless draft in three layers", named sections doing different jobs
- Inputs 2: PagerDuty timeline, Slack export and deploy log, three kinds that can contradict
- Rules 2: conditionals counted are "flags any gap over 10 minutes" and root cause only where the logs support it, else hypothesis, constraints counted are blameless, normalise to UTC, action item owner from the responders list, due week, customer names become account IDs and a five-sentence exec brief
- Audience 2: engineers, support leads and the exec team
- Stakes 2: customer names must become account IDs, so an error exposes customer data
- Borderline: the layers could be three outputs (no change, capped), Stakes 1 if customer names are not read as personal data, rating 9

## SFW-004

- Outputs 0: one newsletter, "event dates go in a list at the top" is a layout rule
- Inputs 1: headteacher's bullet notes, event dates and timetable changes to combine
- Rules 1: counted B1-level language, short paragraphs, warm but not chatty, dates list at the top, under 350 words and never name individual pupils (6 constraints)
- Audience 1: parents on phones, many with Dutch as a second language
- Stakes 2: naming a pupil in a newsletter to all parents exposes a child's personal data
- Borderline: Stakes 1 gives 5, Inputs 2 if the three pastes are three kinds gives 7

## SFW-005

- Outputs 2: announcement of about 300 words, a six-question FAQ and a two-line Slack teaser
- Inputs 0: the policy facts are written into the request
- Rules 1: counted about 300 words, six questions, two lines, direct and reassuring, never corporate spin and no promise beyond the policy text (6 constraints)
- Audience 2: 420 staff "from warehouse crew to engineers" across two offices, several reading levels at once
- Stakes 1: a wrong promise costs trust
- Borderline: Audience 1 if all staff is one audience, rating 6

## SFW-006

- Outputs 2: SMS, email and phone script, each in Dutch and English
- Inputs 0: one input, the pasted incident facts
- Rules 2: constraints counted are SMS max 300 characters, B1-level language, what we know, what we do not know yet, when the next update comes, never guess a cause, always the direct clinic number and formal but empathetic (8), conditional counted is "never mentions data exposure unless the facts say so"
- Audience 2: patients from teenagers to people in their 80s, front-desk staff, two languages
- Stakes 2: a wrong data-exposure statement is a privacy harm for patients
- Borderline: Stakes 1, rating 8

## SFW-007

- Outputs 0: one step-by-step procedure
- Inputs 0: one transcript
- Rules 1: constraints counted are one action per step, the screen or field, what the clerk should see, field names exactly as spoken and no chit-chat (5), conditional counted is second approver for credit notes above EUR 5,000
- Audience 1: new accounts-payable clerks
- Stakes 1: a wrong step costs rework
- Borderline: Stakes 2 if a missed approval marking is read as a wrong payment, rating 5

## SFW-008

- Outputs 1: one guide with named sections doing different jobs, macOS and Ubuntu paths, prerequisites list and troubleshooting section
- Inputs 1: README, Makefile and CI config to combine
- Rules 2: counted fresh laptop to green run in one afternoon, separate macOS and Ubuntu paths, exact versions from the files, a verification check after every stage, troubleshooting only from stated errors, commands verbatim and secrets located but never shown (7 constraints)
- Audience 1: "a new backend engineer"
- Stakes 1: secrets handled with care score 1 on their own
- Borderline: Rules 1 if "one afternoon" is a goal, rating 6, Inputs 2 if the three files are three kinds, rating 8

## SFW-009

- Outputs 1: one work instruction in two language versions
- Inputs 2: call transcript, current checklist and carrier dangerous-goods rules, and the user expects conflicts
- Rules 2: conditionals counted are list the conflict where transcript and checklist disagree, and UN3480 goes to the DG officer before booking, constraints counted are split by role, trigger, system, document produced, hand-off and same step numbers in both languages
- Audience 2: broker, planner and warehouse roles in Dutch and English
- Stakes 2: lithium-battery dangerous goods are a safety and legal risk
- Borderline: Outputs 2 changes nothing, capped at 10

## SFW-010

- Outputs 0: one intake note
- Inputs 0: one web-form inquiry
- Rules 1: constraints counted are client type, issue, every date, other party's name, never give legal advice and never estimate chances (6), conditional counted is flag any dismissal older than two months
- Audience 1: the lawyer doing the free 20-minute call
- Stakes 2: a missed deadline flag is a missed legal duty, and the prompt must refuse to estimate chances
- Borderline: none that moves the band

## SFW-011

- Outputs 0: one list of flags, each with the same fields
- Inputs 1: the listing text and the approved list of 38 claims, two sources
- Rules 1: counted flag every unlisted claim, exact sentence, rule broken, compliant rewrite keeping product facts, never touch compliant text and never judge whether the product works (6 constraints)
- Audience 0: no reader named
- Stakes 2: unauthorised health claims are a legal risk, and the prompt must refuse to judge efficacy
- Borderline: Outputs 1 if flag and rewrite are distinct sections, rating 6

## SFW-012

- Outputs 0: one narrative, "our fixed order" is an order rule
- Inputs 2: alert rule, 90 days of transactions, KYC profile and prior alerts
- Rules 2: conditionals counted are the structuring threshold, joint accounts, missing KYC fields and accounts closed mid-window, constraints counted are fixed order, cite a transaction ID, never conclude laundering, never recommend filing or closing and original currency with EUR in brackets
- Audience 1: the analyst
- Stakes 2: a laundering conclusion is a judgment the prompt must refuse, with legal and financial stakes
- Borderline: Audience 2 if auditors are a second reader, rating 9

## SFW-013

- Outputs 0: one answer with three routes of the same shape
- Inputs 0: the start-up facts are context
- Rules 1: counted three clearly different routes, one-line pitch, café type, a cheap test within a month and frank and practical with no buzzwords (5 constraints)
- Audience 0: the user as sparring partner, baristas are the subject not the reader
- Stakes 0: brainstorm ideas are easy to correct
- Borderline: Stakes 1 for the 15% price premium, rating 3

## SFW-014

- Outputs 1: a named reasoning part on early-tenure leavers and four experiments, doing different jobs
- Inputs 0: the exit-interview findings are written in as context
- Rules 2: counted four distinct experiments, EUR 120,000 yearly budget, hypothesis, pilot depot, metric, 10-week read-out, main schedule risk and challenge the pay assumption (8 constraints)
- Audience 0: the user
- Stakes 1: a budget scores 1 on its own
- Borderline: Outputs 0 if the reasoning is process, rating 4

## SFW-015

- Outputs 1: the deciding insight, the sharp question, three scenarios and the thin-data statement as named sections
- Inputs 2: the user states contradicting positions, CEO for Germany, CFO for Benelux first and sales on on-premise hosting
- Rules 2: counted skeptical, three named scenarios, assumptions per scenario, cheapest test before Q2, kill signal, say where data is too thin and exploration not a plan (7 constraints)
- Audience 0: the user, the board is described but not named as reader
- Stakes 1: a strategy call on EUR 7.8M ARR costs time and trust
- Borderline: Rules 1 if "skeptical" is persona, rating 6, Audience 1 for the board, rating 8

## SFW-016

- Outputs 1: run-of-show and a prep checklist for the trainers
- Inputs 0: the workshop facts are context
- Rules 2: counted agenda 09:30 to 16:00, two hands-on leave-module sessions, lunch, closing Q&A, a short checklist, session rating of at least 8 and at least 10 pilot sign-ups (7 constraints)
- Audience 1: the two trainers
- Stakes 1: a sales-style target scores 1 on its own
- Borderline: Rules 1 if the two targets count once, rating 5

## SFW-017

- Outputs 1: one plan with phases and a risk table
- Inputs 0: the scope facts are context
- Rules 2: counted weekends only, customer-service mailbox offline at most two hours, phone-only field staff, entry and exit criteria, rollback per phase, a staff communication moment per phase, zero lost mail, under 5% tickets and within six weekends (9 constraints)
- Audience 1: the IT team running the migration
- Stakes 1: a bad cutover costs time and trust
- Borderline: Audience 0 gives 5, Stakes 2 if lost mail is read as data loss gives 7

## SFW-018

- Outputs 1: one plan with named sections, workstreams, dependencies, go or no-go checklist, hypercare plan and rollback path
- Inputs 0: the site facts are context
- Rules 2: conditional counted is Tilburg only after four weeks above 99.5% pick accuracy, constraints counted are no go-live between 15 November and 10 January, Liège first, four named workstreams, dependencies, rollback within 12 hours, training in two languages and no missed carrier cut-off
- Audience 0: no reader named
- Stakes 1: a failed go-live costs time and trust
- Borderline: Outputs 2, Audience 1 or Stakes 2 each give 6

## SFW-019

- Outputs 0: one image
- Inputs 0: none
- Rules 2: counted one rider, gravel dyke path, golden hour, low angle, toward camera, Oosterschelde behind, photorealistic catalogue look, warm light with long shadows, 21:9, left third empty, olive jersey, no logos, no text and no other people
- Audience 0: general homepage visitors
- Stakes 0: an image is easy to regenerate
- Borderline: none

## SFW-020

- Outputs 0: one image, the negative prompt and CFG and steps belong to the prompt itself
- Inputs 0: none
- Rules 2: counted 2:3 portrait, 1960s screen-print style, four named colours, three depth layers, top quarter empty, no lettering, paper grain, ink misregistration and children not photoreal
- Audience 0: general poster readers
- Stakes 0: easy to regenerate
- Borderline: Outputs 1 if the separate negative prompt counts, rating 4

## SFW-021

- Outputs 0: one video
- Inputs 0: one input, the still image
- Rules 2: counted 10 seconds, 9:16, bowl rises and widens, slip spiral, drifting dust, slow push-in from waist height, close-up at 8 seconds then hold, warm natural light, shallow depth of field, face out of frame and clutter soft
- Audience 0: general Reels viewers
- Stakes 0: easy to regenerate
- Borderline: none

## SFW-022

- Outputs 0: one video with its audio track
- Inputs 0: none
- Rules 2: counted one continuous 10-second shot, 16:9, glide at about three metres, trolley trains in two directions, three workers on tugs, rise at 4 seconds, settle on the clock at 8 seconds, named sounds, no music, no voices, blue to gold light and workers small and anonymous
- Audience 0: general film viewers
- Stakes 0: easy to regenerate
- Borderline: Outputs 1 if native audio is a second output, rating 4

## SFW-023

- Outputs 0: one screen concept
- Inputs 0: none
- Rules 2: conditional counted is a reject asks for one damage photo, constraints counted are 24-inch touchscreen, about 20 seconds per item, order photo next to the item, return reason, a big tap target per grade, four grades, not a spreadsheet or dark developer tool, calm tactile and fast and shadcn/ui components
- Audience 1: an inspector in cotton gloves grading 300 items a shift
- Stakes 0: a screen concept is easy to revise
- Borderline: Outputs 1 if the reject state is a distinct section, rating 5

## SFW-024

- Outputs 2: five named screens doing different jobs, in Dutch and English
- Inputs 0: none
- Rules 2: conditional counted is a draft survives a lost signal, constraints counted are under five minutes, five screens, station prefilled from location, police report number or add later, back links without losing input, steady and never cheerful or gamified, no generic fintech gradient and no component library
- Audience 2: an upset commuter on her phone, served in Dutch and English at once
- Stakes 1: a broken claim flow costs time and trust
- Borderline: Outputs 1 if the flow is one output with sections, rating 7, Stakes 2 if a lost claim is a financial harm, rating 9
