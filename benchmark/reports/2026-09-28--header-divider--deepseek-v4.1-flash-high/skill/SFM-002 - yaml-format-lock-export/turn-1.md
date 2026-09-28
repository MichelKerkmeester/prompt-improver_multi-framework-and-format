Saved and verified.

Saved: `export/001 - enhanced-supplier-invoice-extraction-prompt.yaml`

CLEAR 45/50 | Gate: passed | Complexity: Medium (6/10) | Framework: TIDD-EC | Format: YAML (valid, +3-7% token overhead)

In short: I turned your request into a ready-to-use extraction prompt structured as valid YAML, covering exactly the nine fields you listed plus nested line items, with the "missing means null, never a guess" rule stated as a hard constraint reinforced by dos/donts and worked examples. TIDD-EC was chosen over the default RCAF because this is a precision-critical, compliance-style extraction task where explicit Do/Don't constraints and examples matter most, and the prompt frames the accounting-import stakes so the model understands why guessing is forbidden.

Note: the schema fields are exactly your request — no extra fields such as tax ID or PO number were added. Want me to also produce a variant tuned for a specific target model or one that outputs JSON instead?