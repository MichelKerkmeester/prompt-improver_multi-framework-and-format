No Canvas panel is available in this environment, so the Deliverable Block is rendered as a fenced block below, per the no-panel delivery rule.

```
Mode: $deep | Complexity: 8/10 | Framework: CIDI

{
  "context": {
    "ai_role": "Senior logistics process analyst producing a controlled work instruction for a freight-forwarding operations team",
    "scenario": "End-to-end clearance of inbound sea containers carrying lithium batteries at the Port of Rotterdam, spanning the Customs Broker, Freight Planner and Warehouse roles, with a conditional Dangerous Goods (DG) Officer review",
    "regulatory_trigger": "Any shipment declared under UN3480 must be reviewed by the DG Officer before the Freight Planner books a delivery slot; this dependency must appear as a structural gate in the step sequence, not a footnote",
    "downstream_use": "Output feeds a knowledge-base importer that maps CIDI sections (Context, Instructions, Details, Input) to structured fields; both language versions must expose the same four section labels in English so the importer maps consistently, while step content itself is translated",
    "why_role_segmentation_matters": "Each step is owned by exactly one role because the instruction exists to make hand-offs traceable: trigger, system and document fields only carry accountability value when tied to a single accountable owner",
    "why_conflicts_are_logged_not_resolved": "The transcript reflects how the senior broker actually works today; the checklist reflects the currently written standard. Silently picking one would encode an unreviewed process change into a controlled document, so disagreements must surface as decisions for a human process owner, not be resolved by the model"
  },
  "instructions": {
    "step_0_synthesis": "Read the call transcript, current checklist and carrier dangerous-goods rules in full before drafting anything; treat them as the only source of truth for role names, systems and documents",
    "step_1_reconstruct_sequence": "Reconstruct the process as a single numbered sequence of steps from broker engagement through warehouse receipt, assigning each step to exactly one role: Broker, Planner, Warehouse, or DG Officer",
    "step_2_capture_fields": "For every step, record: trigger (the event or condition that starts it), system (the application or platform named in the source materials where the step is executed), document_produced (the artifact the step generates), hand_off (which role or system receives the output and what is transferred)",
    "step_3_apply_dg_gate": "Wherever a shipment is declared under UN3480, insert an explicit conditional step assigning review to the DG Officer, sequenced before the Planner's slot-booking step, and mark the dependency in both the Broker's and Planner's step entries",
    "step_4_log_conflicts": "Whenever the checklist and transcript disagree on a step's procedure, owner, sequence or required document, do not select one: add a Conflict entry at that step number stating the checklist's position and the transcript's position separately, and leave it unresolved",
    "step_5_produce_bilingual_pair": "Produce two complete versions of the work instruction, one Dutch and one English, using identical step numbers, identical conflict placements and identical gate placement, so both read as translations of one canonical sequence rather than independently structured documents",
    "step_6_label_output_sections": "In both versions, present the work instruction under four headers in this fixed order, kept in English regardless of body language: Context, Instructions, Details, Input, matching the mapping defined in this prompt"
  },
  "details": {
    "scope": {
      "included": "Rotterdam inbound sea-container clearance for lithium-battery shipments, from broker engagement through warehouse receipt",
      "excluded": "Outbound shipments, non-lithium-battery cargo, other ports or transport modes"
    },
    "step_field_rules": {
      "mandatory_fields": ["trigger", "system", "document_produced", "hand_off"],
      "on_missing_information": "If a field cannot be determined from the three source inputs, write '[Not specified in source - confirm with process owner]' instead of inventing a value"
    },
    "conflict_entry_format": "Conflict at Step [N]: Checklist states [X]; Transcript states [Y]. Unresolved - requires process-owner decision.",
    "un3480_gate_rule": "The DG Officer review step must be sequenced before the Planner's slot-booking step whenever UN3480 applies, and this dependency must be visible in the numbering or an explicit 'depends on Step [N]' note",
    "bilingual_parity_rule": "Dutch and English versions must share identical step counts, step numbers, conflict placements and gate placements; translate step content but keep UN3480, IMDG references, system names and document names unchanged in both versions",
    "source_fidelity_rule": "Do not invent systems, document names or role titles beyond what the three inputs state or clearly imply",
    "output_structure": "Each language version is organised under the four labelled sections Context, Instructions, Details, Input: Context carries the process purpose and the UN3480 trigger rule; Instructions carries the full numbered, role-tagged step sequence; Details carries the per-step trigger/system/document/hand-off table plus the conflict log; Input carries a short list of the source documents referenced"
  },
  "input": {
    "call_transcript": "[Insert full call transcript with the senior customs broker]",
    "current_checklist": "[Insert current internal clearance checklist]",
    "carrier_dg_rules": "[Insert carrier's dangerous-goods rules covering lithium battery shipments]",
    "target_model": "GPT-4.1",
    "output_languages": ["nl", "en"]
  }
}

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide JSON] | assumptions = [system/document/role names sourced only from inputs, not invented; CIDI section headers stay in English in both language versions for stable importer field-mapping; scope limited to Rotterdam inbound lithium-battery sea-container clearance (broker→planner→warehouse, DG gate); "same step numbers" means identical sequence, count, conflict and gate placement across NL/EN] | format = JSON | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-rotterdam-lithium-battery-work-instruction-prompt.json`

**Score and gate status:** CLEAR 44/50 (C9 · L9 · E13 · A9 · R4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimization) | Gate passed

**Token overhead:** JSON adds roughly +5-10% tokens versus the Markdown-baseline equivalent of this same CIDI structure.

**Summary:** Replaced "Document this process" with a CIDI-structured JSON prompt that forces GPT-4.1 to synthesize (not paraphrase) the transcript, checklist and DG rules into a role-tagged, numbered work instruction — each step carrying trigger/system/document/hand-off, checklist-vs-transcript disagreements logged as unresolved conflicts rather than adjudicated, and a UN3480→DG-Officer gate placed structurally before slot booking. CIDI was kept as the framework specifically because your knowledge-base importer maps CIDI sections to fields, overriding the usual JSON/RCAF default pairing; the same four section labels are required in English in both the Dutch and English deliverables so the importer's field-mapping stays stable while step content is translated.