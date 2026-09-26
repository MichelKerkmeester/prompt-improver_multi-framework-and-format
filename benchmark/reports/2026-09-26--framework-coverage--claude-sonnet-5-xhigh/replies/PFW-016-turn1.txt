Two conflicting mode/format signals aren't present here, so no clarification is needed — `$improve` and `$markdown` both parsed cleanly. Building the CRAFT prompt now (no Canvas panel is available in this terminal session, so the Deliverable Block below stands as the equivalent).

```
Mode: $improve | Complexity: 6 (Medium-High) | Framework: CRAFT

**Context:** Our payroll software company is hosting a one-day, in-person customer workshop in Utrecht on 12 November for 25 HR managers from existing customer accounts. These attendees already use our core platform; the workshop's centerpiece is hands-on training on our new leave module ahead of its pilot. The day runs 09:30-16:00 (6.5 hours), delivered by two internal trainers. This run-of-show is a working production document for those trainers, not attendee-facing marketing copy.

**Role:** Corporate workshop designer and B2B customer-education facilitator, experienced in structuring hands-on software training days for HR/payroll audiences and in designing sessions that convert product exposure into pilot adoption.

**Action:**
1. Build a minute-level run-of-show spanning 09:30-16:00 that includes, in this order: an opening/welcome, two hands-on sessions on the new leave module, lunch, and a closing Q&A. [Assumes: no other fixed content was specified — size the two hands-on blocks and any connective segments (breaks, transitions) so the full 6.5 hours reads as a professional, well-paced day; adjust freely if real timings differ.]
2. Because success is judged by average session rating, give each hands-on session a distinct, stated learning objective plus real practice time (not just a demo), and build in a lightweight rating capture immediately after each session — not only at day's end — so a weak session can still be reinforced live in the closing Q&A.
3. Because success also depends on pilot sign-ups, embed one clear, low-friction call-to-action for the leave-module pilot inside each hands-on session, and repeat a final ask during the closing Q&A, rather than relying on a single end-of-day pitch.
4. Note explicitly in the run-of-show where the two trainers hand off to each other, and flag any point where the design has to trade off session depth against time available for the pilot pitch.
5. Draft a short pre-workshop prep checklist (max 10 items) for the two trainers covering: materials/demo environment readiness, role split for each agenda segment, and a final day-before logistics check.

**Format:** Deliver two Markdown artifacts:
1. A time-blocked agenda table with columns: Start, End, Duration, Segment, Trainer(s), Objective/Outcome, Materials Needed — covering the full 09:30-16:00 window.
2. A short prep checklist, grouped under "Materials," "Session Roles," and "Day-Before Check," one actionable item per line.
No narrative explanation outside these two artifacts.

**Target:** The agenda and checklist must be designed to demonstrably support two measurable outcomes: an average per-session rating of at least 8/10 across the two hands-on sessions, and at least 10 sign-ups for the leave-module pilot by the end of the workshop. Wherever a design choice serves one target at the expense of the other, flag the trade-off inline in the agenda.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = session/break durations not specified so sized to fill 6.5 hours, single in-person event, both trainers split delivery, sign-up mechanism left to downstream AI/user to define | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-customer-workshop-runofshow.md`
**Score and gate status:** CLEAR 43/50 (C9·L8·E13·A9·R4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed
**Assumptions flagged:** exact durations for the two hands-on blocks and breaks (sized to fill 09:30-16:00), single in-person format, both trainers splitting delivery, sign-up capture mechanism left open for you to specify.

This CRAFT version keeps your 09:30-16:00 structure and required segments intact but makes the two success metrics (8/10 rating, 10+ sign-ups) active design constraints baked into the sessions and Q&A, not an afterthought — and separates the agenda from the trainer checklist as requested. Let me know if the session lengths or trainer split should be locked to specific numbers rather than left to the downstream AI's judgment.