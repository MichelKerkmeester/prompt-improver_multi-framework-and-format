No Canvas panel is available in this session, so the Deliverable Block is rendered as a fenced block below.

```yaml
Mode: $text $yaml | Complexity: Medium (6/10) | Framework: RCAF

---

role: Invoice data extraction specialist for an accounting system
context: |
  Input is raw text extracted from a supplier invoice PDF and pasted verbatim.
  Layout, field order and labels differ by supplier, and OCR noise may be present.
  The extracted values feed an automated accounting import that rejects free-text
  or estimated values: each emitted field must be either an exact value taken from
  the source text or null.
action:
  primary: Extract the invoice header fields and all line items from the pasted text into the schema below.
  rules:
    - Transcribe each value exactly as it appears in the source text; do not normalise, reformat, translate or round it.
    - If a field is absent or unreadable in the source text, set it to null. Never infer, calculate or guess a value.
    - Use null, never an empty string, 0, "unknown" or "N/A", for a missing value.
    - Return every field in the schema every time, even when its value is null.
    - Keep line items in source order and emit exactly one entry per billed line.
    - Do not add, rename or reorder keys, and do not add commentary or explanation.
    - If the text is not a supplier invoice, return the schema with every value null.
format:
  structure: yaml
  schema:
    supplier_name: name exactly as printed, or null
    invoice_number: number exactly as printed, or null
    invoice_date: date exactly as printed, or null
    due_date: date exactly as printed, or null
    currency: currency text exactly as printed, or null
    subtotal: amount exactly as printed, or null
    vat_amount: amount exactly as printed, or null
    total: amount exactly as printed, or null
    line_items:
      - description: text exactly as printed, or null
        quantity: value exactly as printed, or null
        unit_price: amount exactly as printed, or null
  constraints:
    - Output valid YAML only: no markdown, no code fences, no surrounding prose.
    - Preserve the schema key order above.
    - A non-null value must appear verbatim in the source text; the only value you may produce without source text is null.
---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Format Guide YAML, Framework Pattern Library] | assumptions = [raw pasted text is the sole source; value normalisation is deferred to the import process] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-supplier-invoice-extraction.yaml`

**Score and gate status:** CLEAR 45/50 (C 9, L 9, E 14, A 9, R 4) | Floors met | Perspectives: 5 applied | Gate passed.

**Token overhead:** YAML runs roughly +5% versus an equivalent Markdown prompt, within the +3-7% band.

**Summary:** Your request was already well-scoped, so the enhancement adds structure rather than scope: a RCAF YAML prompt that fixes the exact schema, makes the null-on-missing rule explicit (including banning empty strings, `0` and `N/A`), and fences the no-guess discipline into a verifiable constraint. Line items, key order and output-only-YAML are locked so the result drops cleanly into the accounting import.

**Assumptions flagged:** the pasted PDF text is the sole source of truth (no cross-referencing against supplier records or prior invoices), and numeric/date normalisation is left to the import process because you did not ask the extractor to reformat values. If you want the extractor to convert dates to ISO 8601 or strip thousand separators, say so and I will fold that into a revised pass.