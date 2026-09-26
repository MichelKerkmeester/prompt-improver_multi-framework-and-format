Saved: `export/001 - enhanced-aml-alert-narrative-prompt.md`

CLEAR 44/50 | Gate: passed | Framework: TIDD-EC | Energy: Deep (5 perspectives applied) | Format: Markdown

Rebuilt for Mistral Large as a TIDD-EC prompt: Task/Instructions drive the fixed five-section narrative (Trigger, Customer Profile, Observed Pattern, Expected Activity, Open Questions) with per-transaction citation and dual-currency formatting; Do's/Don'ts lock in the no-conclusion/no-recommendation constraint and the exact structuring rule (3+ cash deposits of EUR 9,000–9,999 within 10 days); Examples include your auditor-approved sentence plus correctly-applied and correctly-withheld structuring cases, joint-account/missing-KYC/mid-window-closure handling, and an anti-pattern to avoid.

`[Assumes: alert package (rule, 90-day transactions, KYC, prior alerts) is supplied as data immediately after this prompt each run]` `[Assumes: EUR conversion uses an FX rate supplied with the data; if absent, the model states this rather than estimating]` `[Assumes: rolling 10-day window is inclusive of first and last qualifying deposit dates]`