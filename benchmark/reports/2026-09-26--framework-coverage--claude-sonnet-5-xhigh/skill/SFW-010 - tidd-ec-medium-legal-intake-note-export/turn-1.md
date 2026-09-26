**Saved:** `export/001 - enhanced-employment-law-intake-prompt.md`
**CLEAR: 44/50** | Gate: passed | Framework: TIDD-EC | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimization)

Summary: Restructured the intake prompt into TIDD-EC (Task, Instructions, Do's, Don'ts, Examples, Context) as requested, since precision-critical/compliance tasks fit that framework best. The Instructions section makes the client-type/issue/date/other-party extraction and the dismissal-deadline logic explicit and conditional, Do's/Don'ts hard-lock the no-advice/no-odds rule, and Examples include your original good note plus a "not-stated" edge case and an anti-pattern showing exactly what crosses the line.

`[Assumes: "today" for the two-month dismissal check is the date the note is generated, not the form-submission date — flag this with the firm if the intake pipeline timestamps differently.]`