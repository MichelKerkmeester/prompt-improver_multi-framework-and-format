JSON validated. The prompt is exported and CIDI-structured with all four required sections.

**Saved:** `export/001 - enhanced-lithium-battery-work-instruction.json`
**CLEAR: 44/50** (C9 · L9 · E13 · A9 · R4) | Gate: passed | Complexity: Complex (9/10) | Framework: CIDI | Perspectives: 5 (Deep)

Summary: The prompt turns "Document this process" into a fully-specified CIDI-structured instruction for GPT-4.1 — role-grouped steps (broker/planner/warehouse/DG officer) each with trigger, system, document, hand-off; a mandatory UN3480-before-slot-booking gate; a rule to log transcript-vs-checklist conflicts instead of resolving them; and parallel English/Dutch output sharing identical step numbers.

`[Assumes: the knowledge-base importer keys on the English CIDI labels "Context/Instructions/Details/Input" regardless of body language, so those four headers stay in English inside the Dutch version too — flag this with your importer owner if the mapping is actually locale-aware.]`