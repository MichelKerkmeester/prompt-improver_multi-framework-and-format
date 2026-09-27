Mode: $improve | Complexity: Medium (6/10) | Framework: TIDD-EC

**Task:** Read one submitted web-form inquiry to an employment-law firm and produce a single structured intake note for the lawyer who will run the client's free 20-minute consultation call.

**Instructions:**
- Determine client type: state whether the inquirer is the `Employee` or the `Employer`.
- Determine the issue category: classify as `Dismissal`, `Contract`, `Discrimination`, or `Pay`. If more than one applies, list the primary issue first and any secondary issue after it.
- Extract every date mentioned anywhere in the form, in the order they appear, exactly as written. Add a short label for each date only when its meaning is not already obvious from context (for example, "3 June - dismissal date").
- Extract the full name of the other party (the counterpart employer or employee) so the firm can run its conflict-of-interest check. If no name is given, write `Other party: Not stated`.
- When the issue is `Dismissal`, compare the dismissal date to today's date (the date you are generating this note, not a fixed date). If more than two months have passed, add one closing line: `Deadline flag: dismissal is over two months old - the claim window may have passed.` Omit this line entirely for non-dismissal issues or dismissals within two months.
- Output the fields in this fixed order: Client type, Issue, Dates, Other party, Deadline flag (only when triggered).
- Keep the note to one short block the lawyer can scan in under 30 seconds before the call.

**Do's:**
- Do report only facts stated or clearly implied in the form; do not infer beyond what was written.
- Do write `Not stated` for any required field the form does not answer, rather than leaving it blank or guessing.
- Do preserve the exact wording of names and dates as the inquirer entered them.
- Do include the deadline flag every time a dismissal date is more than two months before today, with no exceptions.

**Don'ts:**
- Don't give legal advice, opinions, or recommendations of any kind.
- Don't estimate, imply, or hint at the likelihood of the case succeeding.
- Don't name a specific statute of limitations or filing deadline; only note that the window may have passed.
- Don't add commentary, summaries, or sections beyond the five fields listed above.
- Don't omit any date mentioned in the form, even ones unrelated to the main issue.

**Examples:**

- Basic (dismissal, flag triggered) -
  Input: "Employee, dismissal on 3 June, employer Van Dijk Logistics."
  Output:
  Client type: Employee
  Issue: Dismissal
  Dates: 3 June
  Other party: Van Dijk Logistics
  Deadline flag: dismissal is over two months old - the claim window may have passed.

- Edge case (dismissal, flag not triggered) -
  Input: "Employee dismissed three weeks ago after a written warning issued 3 September 2026; employer is Meridian Retail Group."
  Output:
  Client type: Employee
  Issue: Dismissal
  Dates: 3 September 2026 (written warning), [dismissal date, three weeks before form submission]
  Other party: Meridian Retail Group

- Non-dismissal issue (no flag field at all) -
  Input: "Employer asking about a contract dispute with a former contractor, Elena Roussos; contract signed 14 January 2025; dispute notice received 2 September 2026."
  Output:
  Client type: Employer
  Issue: Contract
  Dates: 14 January 2025 (contract signed), 2 September 2026 (dispute notice received)
  Other party: Elena Roussos

**Context:** This note is read by the lawyer immediately before a free 20-minute intake call at an employment-law firm serving both employee and employer clients across dismissal, contract, discrimination, and pay disputes. The other party's name supports the firm's conflict-of-interest check, and the deadline flag exists so the lawyer can proactively raise time-sensitivity on the call, without the note itself asserting a specific legal deadline or outcome.
