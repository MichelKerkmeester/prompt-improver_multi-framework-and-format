```markdown
Mode: $improve | Complexity: 4/10 | Framework: TIDD-EC

**Task:** Read a single web-form inquiry submitted to the firm and produce one intake note for the lawyer conducting the free 20-minute consultation call.

**Instructions:**
1. Determine client type — `employee` or `employer` — from the inquiry. If the inquiry does not make this clear, write "client type unclear" rather than guessing.
2. Classify the core issue as exactly one of: `dismissal`, `contract`, `discrimination`, `pay`. If more than one applies, name the primary issue and add the secondary issue in parentheses.
3. Extract every date mentioned in the inquiry, in the order it appears, each labelled with what it refers to (e.g. dismissal date, contract start, last pay date) when not self-evident.
4. Extract the name(s) of the other party involved (opposing employer, employee, manager or organisation) so the firm can run its conflict-of-interest check. If no name is given, write "other party not named."
5. Because unfair-dismissal claims can become time-barred, when the issue is `dismissal`: compare the dismissal date to today's date, and if more than two months have elapsed, append a deadline flag so the lawyer can prioritise the call.
6. Compose the note as a single comma-separated line, in this order: client type, issue (with date(s)), other party, deadline flag (only when triggered).

**Do's:**
- Use the client's and other party's exact wording for names, dates and organisation names as written in the form.
- Keep the note to one line; no narrative, commentary or elaboration.
- State missing or unclear information explicitly rather than inferring it.
- Recalculate the two-month window against the actual current date each time the prompt runs.

**Don'ts:**
- Never give legal advice, opinions, or recommendations on next steps — that is the lawyer's job on the call, not this note's.
- Never estimate the merits, strength or chances of success of the case.
- Never omit the deadline flag when the two-month condition is met.
- Never invent a date, name or client type that is not present in the inquiry.

**Examples:**
- Input: "I was let go on 3 June by Van Dijk Logistics, no reason given." → Output: `Employee, dismissal on 3 June, employer Van Dijk Logistics, deadline flag.`
- Input: "Dismissed two weeks ago, no idea who to name as my old employer's HR contact." → Output: `Employee, dismissal on [date given], other party not named.` (no deadline flag — within two months)
- Input: "We're ABC Retail. Our contractor John Smith breached the contract signed 1 February; he stopped work on 15 May." → Output: `Employer, contract dispute (contract signed 1 February, work stopped 15 May), other party John Smith.`
- Input: message describes unequal treatment at work but never states whether the writer is reporting as the worker or the company → Output: `Client type unclear, discrimination, other party not named.`

**Context:** The firm offers free 20-minute intake calls for employment-law matters. Web-form inquiries arrive as free text. This note is internal, lawyer-facing prep read just before the call — it drives the conflict check (other party name) and surfaces time-sensitive dismissals, and it never substitutes for the lawyer's own legal judgment or advice to the prospective client.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = 2 flagged (see below) | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-employment-law-intake-prompt.md` (this Project cannot write files or verify a saved path — the block above is the deliverable).

**Score and gate status:** CLEAR ~44/50 (C9·L9·E13·A9·R4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed.

**Assumptions flagged:**
- "Today's date" for the two-month check means whenever the prompt is *run* against a given inquiry, not a fixed date — the note must recompute this each time.
- One web-form inquiry is processed per note; conflicting or multi-matter inquiries aren't split further.

**Summary:** Restructured your one-line brief into TIDD-EC so Claude has explicit, testable rules for client type, issue classification, date extraction, conflict-check naming and the two-month dismissal flag, plus hard Don'ts blocking legal advice or outcome predictions. Four cascading examples (your original, an in-window dismissal, a non-dismissal case, and an ambiguous edge case) show the model exactly how to handle missing or unclear input without guessing.