```markdown
Mode: $improve | Complexity: 4/10 | Framework: TIDD-EC

**Task:** Read one employment-law web-form inquiry and produce a single compact intake note for the lawyer running the free 20-minute consultation call, so they can triage the client and run a conflict check before the call starts.

**Instructions:**
1. Determine client type: `Employee` or `Employer`. If not determinable from the text, write `Client type not stated`.
2. Determine the issue category: `Dismissal`, `Contract`, `Discrimination`, or `Pay`. If more than one applies, list the primary category first and any secondary category after it.
3. Extract every date mentioned in the inquiry, in the format the client used. If no date is mentioned, write `No date stated`.
4. Extract the name of the other party (the counterpart individual or organisation) for the conflict-of-interest check. If not named, write `Other party not stated`.
5. If the issue category is `Dismissal` and a dismissal date is present, compare it to today's date. If the dismissal date is more than two months before today, append `deadline flag` to the note, because the claim window may have passed. If the issue is not `Dismissal`, or the dismissal date is missing, omit the flag rather than guessing.
6. Assemble the note as a single comma-separated line, in this field order: client type, issue (with date if central to the issue), other party, deadline flag (only if triggered by Step 5).

**Do's:**
- Do use only facts stated in the web-form text.
- Do write `not stated` for any missing field instead of inferring or guessing it.
- Do keep the note to one line, scannable in under 10 seconds before the call.
- Do apply the deadline flag every time Step 5's condition is met, even if the client shows no urgency.

**Don'ts:**
- Don't give legal advice, procedural guidance, or next-step recommendations.
- Don't estimate, imply, or hint at the odds of winning or the strength of the case.
- Don't invent dates, names, or facts absent from the submitted form.
- Don't add commentary, opinions, or reassurance beyond the six fields above.

**Examples:**
- Input: "I'm an employee, dismissed on 3 June by Van Dijk Logistics, can I sue?" → Output: `Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag.`
- Input: "We're the employer, dispute over a contract clause signed 12 January 2026 with our former contractor, Meridian Consulting." → Output: `Employer, contract dated 12 January 2026, other party Meridian Consulting.` (No flag: only dismissal triggers it.)
- Edge case, missing detail: "My manager told me my role's cut. I think it's discrimination." → Output: `Employee, discrimination, no date stated, other party not stated.`
- Anti-pattern, never produce this: `Employee, dismissal 3 June, employer Van Dijk Logistics — strong case, good odds of winning.` The odds judgment violates the never-advise constraint; stop at the facts and the flag.

**Context:** This note supports a free 20-minute intake call at an employment-law firm. The lawyer reads it in the seconds before picking up the call, so it must be scannable, not exhaustive. The other party's name exists solely to run a conflict-of-interest check, not for the note's narrative. The two-month deadline flag exists because dismissal-related claims can carry short statutory limitation windows, and the firm needs an early warning before the client's window may have closed. The note is a triage artifact, not a case assessment; legal merit and advice are strictly out of scope at this stage.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = two-month threshold measured from today's date to the stated dismissal date; "other party" means the counterpart in the dispute (employer name if client is employee, and vice versa); date format mirrors the client's own wording rather than normalizing to ISO | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-employment-intake-note.md`

**Score and gate status:** CLEAR 44/50 (C 9, L 9, E 13, A 9, R 4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed

**Summary:** TIDD-EC was the right fit here since this is a quality-critical, compliance-sensitive intake task — the Do's/Don'ts split gives a hard boundary against legal advice or odds-estimation, and the anti-pattern example makes that boundary concrete rather than abstract. The Instructions turn your five requirements (client type, issue, dates, party name, deadline flag) into a deterministic six-step build so the AI never has to guess when data is missing.

Two assumptions are flagged in the attestation: the two-month clock runs from today against the stated dismissal date, and "other party" is read as the dispute counterpart for conflict-check purposes. Flag if either should work differently.