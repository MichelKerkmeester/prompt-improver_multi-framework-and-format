File verified: `export/001 - enhanced-employment-law-intake-prompt.md`

CLEAR: 42/50 (C:8 L:8 E:12 A:9 R:5) | Gate: passed | Complexity: Medium (6/10) | Framework: TIDD-EC | Perspectives: 3 (Prompt Engineering, AI Interpretation, End-User/Lawyer Experience)

The prompt structures the intake task with Task, Instructions, Do's, Don'ts, Examples (basic, edge case with no flag, non-dismissal case), and Context — preserving your exact field order, the two-month dismissal flag logic, and hard bans on legal advice or chance estimates.

**[Assumes:]**
- "Today" is the date the AI processes the form (dynamic), not a fixed calendar date, so the two-month check stays accurate on reuse.
- The deadline flag line is included only when triggered (matching your one given example), not shown as "N/A" otherwise.
- No specific statute-of-limitations figure is asserted, since jurisdiction wasn't stated — the note only flags proactively, per your "never estimate chances" constraint.