# Complexity rubric wording trial, 2026-09-27

## 1. OVERVIEW

The first recount, [`rubric-recount.md`](rubric-recount.md), named the rubric wording its rater had to settle alone: what makes "distinct sections", how finely a constraint is counted, what "kinds of source" are, what counts as financial stakes, and whether Outputs and Inputs describe the downstream task or the prompt being written. Those readings were written into the rubric as one sentence and five definitions, and two new blind raters, C and D, scored the 24 inputs with that wording. Neither saw a scenario tier, a deliverable or another recount.

The wording did not help readers, who already agreed. It lowered the ratings by about half a point and moved five more inputs outside their scenario tier. Its effect on the runtime was never measured, since that takes a rerun of the 48. The operator chose on 2026-09-27 to keep the rubric as it was, so the wording below never shipped. The raters' reasons per input stay in the spec packet's scratch folder, outside git.

---

## 2. THE TRIAL WORDING

The rubric's opening paragraph gained one sentence:

> Outputs and Inputs describe the work the target model will do with the prompt, never the prompt itself.

The two definitions below the table became five:

- **Output:** something the target model hands back, such as a message, a document, a table or an image. Parts of one output are distinct sections when the user names them and they do different jobs. A layout or ordering rule is a constraint, not a section
- **Input:** material the target model receives with the task, such as a log, a policy text or a transcript. Facts written into the request are context, not inputs, unless the user states positions that contradict each other. Two inputs are different kinds when they come from different places, such as a ticket export and a policy document
- **Constraint:** one stated limit the output must meet, such as a length, a required field, a banned element or a fixed order. Count one per stated limit or required field, and a phrase that states one limit, such as "warm but not chatty", counts once
- **Conditional rule:** a rule that applies only when something holds, such as a threshold, a route or an escalation. It counts once, as a conditional, never also as a constraint
- **Stakes of 2:** an error would itself cause the harm, such as a wrong payment or price, a missed legal duty, a health or safety risk or exposed personal data. A budget, a sales target or a secret to handle with care scores 1 on its own

---

## 3. RESULTS

| Measure | Current wording, raters A and B | Trial wording, raters C and D |
|---|---|---|
| Two raters within one point of each other | 24 of 24, 19 exactly | 24 of 24, 18 exactly |
| Two raters in the same band | 21 of 24 | 22 of 24 |
| Mean rating | 6.2 and 6.1 | 5.8 and 5.5 |
| Recount inside the scenario tier | 17 and 16 of 24 | 13 and 12 of 24 |
| Runtime within one point of the recount | 26 of 48, against rater A | not measured |

Scenario tiers here are the ones after the 2026-09-27 re-tier of the creative pairs. Against rater A, the trial wording moves SFW-007, SFW-012, SFW-013, SFW-020 and SFW-023 outside their tier under both new raters, and SFW-004 into it. Rater D also moves SFW-005 out.

---

## 4. SCORES

### Rater C

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

### Rater D

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
