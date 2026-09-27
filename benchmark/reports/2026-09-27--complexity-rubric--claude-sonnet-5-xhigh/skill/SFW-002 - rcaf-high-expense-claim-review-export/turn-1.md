JSON validated (top-level keys are exactly `role`, `context`, `action`, `format`) and the file is saved.

**Saved:** `export/001 - enhanced-expense-claim-review-prompt.json`
CLEAR 44/50 | Gate: passed | Complexity: Complex (9/10) | Framework: RCAF

Summary: The four-key RCAF structure now encodes every rule the finance team listed — the four-way classification, grade-tiered hotel limits (€180/€240), the blanket €750 controller override that preserves the original classification, the recommend-only/no-payment constraint, and mandatory verbatim receipt quoting — nested inside `context`, `action`, and `format` so the registry's four-key limit is respected without dropping anything. `[Assumes: the reviewer has access to the organization's expense-policy clauses to cite on not_business_cost lines, and to the standing per-category limits for any non-hotel expense type, since only the hotel figures were given.]`