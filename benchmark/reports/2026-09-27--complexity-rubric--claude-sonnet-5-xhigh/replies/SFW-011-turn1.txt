JSON body validated successfully.

Saved: `export/001 - enhanced-supplement-listing-compliance-checker.json`
CLEAR 45/50 | Gate: passed (floors met: C9, L9, E13, A9, R5)

Built with TIDD-EC (Task, Instructions, Do's, Don'ts, Examples, Context) — the framework you named and the one this compliance-critical, precision task calls for. It locks the checker to your three rule categories (unauthorised claim, disease claim, dosage promise), keeps the "don't touch compliant text" and "don't judge efficacy" boundaries explicit, and adds a `flags` output schema plus two illustrative examples (disease claim, dosage promise) beyond your immune-system worked example so the model has a demonstrated pattern for every category. `[Assumes: output returns only a `flags` array — compliant sentences produce no entry at all; the immune-system example's distinction between "boosts" and "contributes to the normal function of" was generalized into a broader/vaguer-restatement-is-non-compliant rule]`.

Complexity: High (8/10) — driven by the 4 input sources (title, description, bullets, 38-item claims list), the 3-way rule classification, and legal/regulatory stakes.