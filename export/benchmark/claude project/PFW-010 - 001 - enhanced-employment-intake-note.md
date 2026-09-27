Mode: $improve | Complexity: High (7/10) | Framework: TIDD-EC

**Task:** Read one employment-law web-form inquiry and produce a short intake note that prepares the lawyer for the client's free 20-minute call.

**Context:** Barter, an employment-law firm. The note is read internally by the lawyer immediately before the call; it is never shown to the client. The other party's name is used separately for the firm's conflict-of-interest check.

**Instructions:**
1. Identify client type as exactly one of: Employee or Employer. If the form does not make this clear, write "Client type: unclear" instead of guessing.
2. Identify the core issue and classify it as exactly one of: Dismissal, Contract, Discrimination, Pay. If the form describes more than one, name the primary issue and note the secondary one in parentheses.
3. Extract every date mentioned in the inquiry. Label each with what it refers to (e.g., dismissal date, contract start, last payment date). If no date is given, write "no dates given."
4. Extract the other party's name (the counterpart employer or employee) verbatim as written, for the conflict check. If none is given, write "other party: not provided."
5. If the issue is Dismissal, compare the dismissal date to today's date. If more than two months have passed, append a deadline flag noting the statutory claim window may have passed. Do not add this flag for any other issue type, and do not add it if the dismissal date is unclear or missing.
6. Write the note as a single comma-separated line, in this field order: client type, issue, date(s), other party, deadline flag (only if triggered).

**Do's:**
- Keep the note to one line — it is a pre-call briefing, not a case file.
- Preserve names and dates exactly as written in the form, including spelling.
- Write "not provided" or "unclear" for any missing or ambiguous required field rather than inferring it.

**Don'ts:**
- Never give legal advice, an opinion on the merits, or a recommended next legal step.
- Never estimate the client's chances of success or the strength of the claim.
- Never omit the deadline flag when a dismissal date is more than two months old.
- Never add case law, a file number, or commentary the form did not supply.

**Examples:**
- Input: former employee's form describing dismissal on 3 June, naming employer "Van Dijk Logistics."
  Output: `Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag.`
- Input: employer HR contact's form describing a pay dispute, no dates, no counterpart name given.
  Output: `Employer, pay, no dates given, other party: not provided.`

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = [web form is a single structured submission, not multi-page] · [two-month threshold is measured dismissal-date-to-review-date] · [note is internal-only, never client-facing] | format = Markdown | execution = did not occur | save = did not occur
