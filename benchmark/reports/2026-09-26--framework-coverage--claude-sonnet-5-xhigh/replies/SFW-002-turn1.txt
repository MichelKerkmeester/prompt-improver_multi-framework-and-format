JSON body validates successfully. The file is exported and confirmed.

**Saved:** `export/001 - enhanced-expense-claim-triage-prompt.json`
CLEAR Score: 46/50 | Gate: passed (floors met: C9, L9, E12, A9, R3)

The prompt is built RCAF (single object: role, context, action, format — matching your registry's 4-key constraint) with every rule preserved rather than streamlined: the four-way classification, the EUR 750 controller override applying regardless of class, grade-based hotel nightly limits (180/240), the recommend-only constraint, and the mandatory receipt-line quote (or explicit "no match found") on every line. `[Assumes: grade boundary is inclusive at grade 5 for the EUR 180 tier, and hotel lines carry enough data to derive a per-night rate — both flagged for finance to confirm]`.

Share the next prompt whenever you want another one improved.