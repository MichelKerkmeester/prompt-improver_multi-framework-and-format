Mode: $improve | Complexity: 6/10 | Framework: TIDD-EC

**Task:** Read one client inquiry submitted through the firm's employment-law web form and produce a single structured intake note for the lawyer running that client's free 20-minute consultation call.

**Instructions:**
1. Determine client type: `Employee` or `Employer`. Use only what the inquiry states; do not infer beyond it.
2. Determine the issue category: `Dismissal`, `Contract`, `Discrimination`, or `Pay`. Choose the single closest match; if a second category also applies, name it in parentheses after the primary one.
3. Extract every date mentioned anywhere in the inquiry, in the order they appear, using the client's own wording (e.g., "3 June", "15/08/2025").
4. Extract the full name of the other party (the opposing employer, employee, or company) exactly as written, for the firm's conflict check.
5. If the issue category is `Dismissal`, compare the dismissal date to today's date. If more than two months have elapsed, append a deadline flag noting the statutory claim window may have passed. Skip this step for every other issue category.
6. Assemble the note as one comma-separated line, in this fixed order: client type, issue, date(s), other party, deadline flag (only when triggered).
7. If a required field (client type, issue, a date, or other party name) is missing or unclear, write that field as "not stated" instead of guessing or omitting it.

**Do's:**
- Do use the client's own wording for names and dates.
- Do list every date found, even when there are several.
- Do keep the note to short factual phrases, not full sentences.
- Do write "not stated" for any missing required field rather than leaving a gap.

**Don'ts:**
- Don't give legal advice, opinions on the merits, or interpretation of the law.
- Don't estimate or imply the likelihood of winning the case.
- Don't add recommendations, next steps, or case strategy.
- Don't drop or soften the deadline flag when a dismissal is older than two months.

**Examples:**
- Employee inquiry: dismissed 3 June, employer named Van Dijk Logistics, no other dates, more than two months have passed since 3 June. Note: `Employee, dismissal, 3 June, employer Van Dijk Logistics, deadline flag.`
- Employer inquiry: pay dispute with employee Sara de Groot, contract dated 1 January, dispute started 15 August. Note: `Employer, pay, dates 1 January and 15 August, other party Sara de Groot.`
- Anti-pattern (never produce this): `Employee, dismissal, 3 June, employer Van Dijk Logistics, deadline flag — strong case, likely to win.` This adds a legal opinion and a win estimate, which stay prohibited no matter how confident the inquiry reads.

**Context:** This note is the only material the lawyer sees before the free 20-minute call, so it must be fast to scan, legally neutral, and complete enough to run a conflict-of-interest check on the other party. The firm has not yet been retained, so anything resembling legal advice or a merit assessment is out of scope. Treat "today" as the date the note is generated, not the date the client submitted the form, when checking the two-month dismissal window.
