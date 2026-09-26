Mode: $deep | Complexity: 8/10 | Framework: CIDI

```json
{
  "context": {
    "process": "Work instruction for clearing inbound sea containers carrying lithium batteries at the Port of Rotterdam",
    "roles_in_scope": ["Broker", "Planner", "Warehouse", "DG Officer (conditional)"],
    "process_flow": ["Broker", "DG Officer (only if UN3480 is declared)", "Planner", "Warehouse"],
    "downstream_consumer": "A knowledge-base importer that parses this document by its four top-level section labels (Context, Instructions, Details, Input) and maps each section to its own field. Keep these four labels in English in both language versions so the importer keys on the same labels regardless of language; only the body content is bilingual.",
    "source_material_conflict_risk": "The call transcript (senior customs broker) and the current checklist may describe the same step differently: different trigger, system, responsible role, document, or hand-off. Do not resolve these silently."
  },
  "instructions": {
    "target_model": "GPT-4.1",
    "primary_task": "Using the three source documents supplied in Input, write one work instruction with Dutch and English versions for clearing inbound sea containers carrying lithium batteries at the Port of Rotterdam. Ground every detail in the three sources; do not add generic freight-forwarding knowledge that is not supported by them.",
    "output_format": "Plain-text or markdown document (not JSON), organized under exactly four top-level section headings in this order: Context, Instructions, Details, Input. Produce the full document twice: once in Dutch, once in English, each using the same four headings and the same step numbers.",
    "step_schema": {
      "required_fields_per_step": ["step_number", "role", "trigger", "system", "document_produced", "hand_off"],
      "field_definitions": {
        "step_number": "Stable identifier, identical across the Dutch and English versions",
        "role": "Broker, Planner, Warehouse, or DG Officer",
        "trigger": "The specific event or condition that starts this step",
        "system": "The named system in which the step is carried out",
        "document_produced": "The named document or record the step outputs",
        "hand_off": "Who or what receives the output, and what it enables next"
      },
      "grouping": "Group and order steps under role headings following process_flow in Context: Broker steps first, then the conditional DG Officer step, then Planner steps, then Warehouse steps"
    },
    "un3480_rule": "Any shipment declared under UN3480 must be routed to the DG Officer for review before the Planner books a slot. Represent this as an explicit, numbered step: the Broker's UN3480 declaration is the DG Officer step's trigger, and the DG Officer's hand-off is a precondition of the Planner's slot-booking step. Number and include this step even though it only executes when UN3480 applies; do not fold it into the Planner's step.",
    "conflict_handling": "When the transcript and the checklist disagree on any step's trigger, system, role, document, or hand-off, do not pick one. Keep the step in the sequence, mark it as disputed, and record it in the Details section as: step_number, the transcript's version, the checklist's version. Do not add a recommended resolution. If the carrier's DG rules conflict with either source on a DG-specific point, log it the same way, with the DG rules cited as one of the two positions.",
    "grounding_rule": "If a step implied by the process is not covered by any of the three sources, do not invent its trigger, system, document, or hand-off. State in Details that the step is not covered by the sources, naming which role and the gap."
  },
  "details": {
    "details_section_content": "The Details section of the output must contain two lists: (1) Conflicts, one entry per disagreement found under conflict_handling; (2) Gaps, one entry per uncovered step found under grounding_rule. Leave both empty only if none exist.",
    "standing_rule_note": "State the UN3480-to-DG-Officer rule once in Details as a standing rule, in addition to its numbered step in Instructions.",
    "terminology_rule": "Use correct Dutch customs and logistics terminology in the Dutch version. Where a term's Dutch equivalent cannot be confirmed from the three sources, keep the English term in brackets instead of guessing a translation."
  },
  "input": {
    "call_transcript": "${CALL_TRANSCRIPT}",
    "current_checklist": "${CURRENT_CHECKLIST}",
    "carrier_dg_rules": "${CARRIER_DG_RULES}"
  }
}
```

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide JSON | assumptions = CIDI section labels (Context/Instructions/Details/Input) stay in English in both language versions since the importer keys on section labels [Assumes: importer matches by literal label, not translated headings] | DG Officer modeled as a fourth, conditional role triggered only by a UN3480 declaration | format = JSON | execution = did not occur | save = did not occur

**Export-equivalent path:** `export/001 - enhanced-rotterdam-lithium-battery-work-instruction-prompt.json`

**Score and gate status:** CLEAR 44/50 | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimization) | Gate passed (all dimension floors met: C9/L9/E13/A9/R4)

**Token overhead:** JSON format carries an estimated +5-10% token overhead versus an equivalent Markdown deliverable, due to explicit key/value structure and nested schema definitions.

**Summary:** The prompt locks CIDI as both the instruction framework and the required output headings (so your knowledge-base importer can map sections to fields directly), defines a per-step schema (trigger/system/document_produced/hand_off) grouped by role, makes the UN3480→DG Officer gate an explicit numbered step, and forces conflicts and coverage gaps into a non-resolving Details log instead of letting the model pick a source. Complexity was kept at full scope (level 8/10) per your instruction, with no simplification offered.