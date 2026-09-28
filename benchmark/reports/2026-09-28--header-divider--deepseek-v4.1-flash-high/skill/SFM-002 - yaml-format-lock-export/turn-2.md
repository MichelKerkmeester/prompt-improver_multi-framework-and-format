Saved and verified.

Saved: `export/002 - enhanced-supplier-invoice-extraction-prompt-vat-breakdown.yaml`

CLEAR 45/50 | Gate: passed | Complexity: Medium (6/10) | Framework: TIDD-EC | Format: YAML (valid, +3-7% token overhead)

Added a `vat_breakdown` list to the schema, where each entry has `rate` and `amount`, alongside the existing `vat_amount` total. The null-never-guess rule now extends to the breakdown, and I added three worked examples covering two rates printed, a single total with no separate rates (empty list), and no VAT at all (null plus empty list) so the model's behaviour is unambiguous in every case.

Note: `vat_amount` is kept as the invoice's total VAT so nothing from the original output is lost; the breakdown is purely additive. Want a variant where `vat_breakdown` is required to be `null` instead of an empty list when no rates are shown?