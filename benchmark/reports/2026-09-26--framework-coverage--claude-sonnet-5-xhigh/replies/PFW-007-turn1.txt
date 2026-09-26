Mode: $improve | Complexity: Medium (5/10) | Framework: CIDI

```yaml
context: >
  A senior accounts-payable (AP) clerk has narrated a screen recording while booking a
  supplier credit note against an open invoice. The transcript below captures their spoken
  actions, system screens and field names in real time. New AP clerks with no prior exposure
  to this procedure will use the resulting document as their only reference, so every step
  must be followable without watching the recording.

instructions: >
  Convert the transcript into a numbered step-by-step standard operating procedure (SOP) for
  booking a supplier credit note against an open invoice, written for new AP clerks and ready
  to publish to Confluence. Preserve the clerk's intent and sequence exactly; do not add, skip
  or reorder steps, and do not invent system behavior the transcript does not describe.

details:
  step_structure:
    - "One action per step: a single verb-driven instruction, never two actions combined."
    - "Name the screen or field where the action happens, using the clerk's exact spoken wording (no renaming, standardizing or correcting terminology, even if it differs from typical system labels)."
    - "State what the clerk should see immediately after completing the action (confirmation message, status change, new field value, updated total, etc.), so the clerk can self-verify before moving on."
  approval_marking:
    - "The second-approver requirement applies specifically to credit notes above EUR 5,000."
    - "Mark each step where this applies with a clearly visible label at the start of the step, for example '[Approval Required: >EUR 5,000]'."
    - "If the transcript does not state the credit note amount, keep the approval label on the relevant step and add a one-line note that the threshold check applies regardless of the amount shown in this example."
  exclusions:
    - "Remove conversational filler, asides, hesitations and commentary that is not a procedural action (small talk, apologies, thinking-out-loud)."
    - "Do not summarize or paraphrase the clerk's field names; quote them exactly as spoken, including capitalization style if stated."
  output_format:
    - "Confluence-ready structure: numbered steps grouped under short section headings if the procedure has natural phases (e.g., 'Open the Invoice', 'Enter Credit Note Details', 'Submit for Approval')."
    - "Use a table only if it improves scannability for repeated field-value pairs; otherwise keep steps as a numbered list."
    - "No narrative prose outside the steps; the SOP is reference documentation, not an explanation."

input: "[Paste the full transcript of the senior clerk's screen-recording narration here]"
```

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide YAML | assumptions = 4 flagged | format = YAML | execution = did not occur | save = did not occur

**Export-equivalent path:** `export/001 - enhanced-sop-supplier-credit-note.yaml`

**Score and gate status:** CLEAR 44/50 (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4) | Perspectives: 3 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer) | Gate passed

**Token overhead:** YAML format adds roughly +3-7% tokens versus the Markdown baseline for this deliverable.

**Assumptions flagged:** transcript is pasted directly under `input:`; the EUR 5,000 approval rule applies to the credit-note total regardless of whether an amount appears in this particular transcript; "Confluence-ready" means plain numbered lists/headings/tables rather than a specific Confluence macro; "exactly as spoken" overrides normal terminology standardization even for inconsistent field names.

**Summary:** The original one-line request had no defined step atomicity, no rule for handling the approval threshold when the amount is unstated, and no output-format guidance for Confluence. The CIDI structure now locks in one-action-per-step, verbatim field naming, a visible approval tag tied to the EUR 5,000 rule, chit-chat removal, and a Confluence-ready layout, with the transcript left as a reusable input slot.