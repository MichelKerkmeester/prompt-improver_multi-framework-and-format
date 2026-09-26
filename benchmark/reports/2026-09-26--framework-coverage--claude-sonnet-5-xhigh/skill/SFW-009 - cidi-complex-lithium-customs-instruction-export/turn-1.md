JSON validated successfully — the header is clean and the body parses without errors.

**Saved:** `export/001 - enhanced-freight-dg-work-instruction-prompt.json`
**CLEAR: 44/50 | Gate: passed** (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4 — all floors cleared)

This CIDI-framed JSON prompt directs GPT-4.1 to build the bilingual Rotterdam lithium-battery (UN3480) work instruction from the transcript, checklist, and DG rules — grouping steps by Broker/Planner/Warehouse with Trigger/System/Document Produced/Hand-off per step, the UN3480→DG-officer gate before slot booking, a transcript-vs-checklist conflict log instead of forced resolution, and matching EN/NL step numbers. It also mandates that GPT-4.1's own output carry the four literal Context/Instructions/Details/Input section headers your knowledge-base importer maps to fields.

`[Assumes: the three source documents are passed at runtime as the literal content behind the {{CALL_TRANSCRIPT}}, {{CURRENT_CHECKLIST}}, and {{CARRIER_DG_RULES}} placeholders — e.g., pasted or injected text — rather than via file upload.]`