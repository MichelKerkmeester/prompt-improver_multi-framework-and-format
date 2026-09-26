```
Mode: $yaml | Complexity: 6 | Framework: CRISPE

capacity: >-
  Act as a workforce retention strategist with hands-on last-mile
  parcel-delivery operations experience, fluent in driver-attrition
  diagnostics, shift-pattern design, and pilot-experiment budgeting for
  depot-based delivery fleets.
insight:
  operation:
    fleet_size: 210 parcel-delivery drivers
    depot_count: 4
    depot_region: Antwerp, Belgium
  attrition:
    annual_rate: 38 percent left in the last 12 months
    concentration: majority departed within their first 90 days of tenure
  exit_interview_signals:
    - route density
    - 06:00 start time
    - pay per stop
  budget:
    annual_amount_eur: 120000
    scope: must fund all four proposed experiments combined for one year
  working_assumption_to_challenge: pay per stop is the primary driver of early-tenure attrition
statement:
  reasoning_task: >-
    Before proposing solutions, reason explicitly about why early-tenure
    (0-90 day) drivers leave at a higher rate than tenured drivers, drawing
    on the three exit-interview signals above plus any other plausible
    last-mile onboarding failure points such as training gaps, route
    assignment logic, supervisor support, physical demands, or schedule
    shock. Explicitly test the assumption that pay per stop is the main
    lever and state whether the evidence supports or contradicts it before
    designing experiments.
  deliverable_task: >-
    Propose four distinct retention experiments that collectively fit
    within the EUR 120,000 annual budget. The four experiments must differ
    in mechanism, not merely in amount, and at least one must target a
    non-pay lever surfaced in the reasoning step.
  required_fields_per_experiment:
    - hypothesis: the specific causal claim the experiment tests
    - pilot_depot: which of the four Antwerp depots runs the pilot, and why
    - metric: the single primary metric that confirms or kills the hypothesis
    - readout_point: the expected signal at the 10-week mark
    - delivery_schedule_risk: the main way the experiment could disrupt daily parcel delivery, and how to contain it
personality:
  voice: direct, evidence-led, willing to disagree with the client's stated assumption
  stance: skeptical of pay as a default fix, grounded in operational trade-offs rather than generic HR advice
experiment:
  iterate: >-
    If the four experiments cannot plausibly fit EUR 120,000 combined, or
    fewer than four distinct mechanisms emerge, revise the set until both
    constraints hold before finalizing.
  output_format: >-
    Open with the reasoning on early-tenure attrition and the verdict on
    the pay assumption, then present the four experiments as a numbered
    list, each carrying the five required fields labeled explicitly.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide YAML | assumptions = [Assumes: EUR 120,000 is the combined annual budget for all four pilots, not per-experiment], [Assumes: pilot-depot selection is left to the AI's judgment since depot names were not supplied], [Assumes: the 10-week mark is an interim signal checkpoint, not a final verdict] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-driver-retention-experiments.yaml`

**Score and gate status:** CLEAR 44/50 (C9·L9·E13·A9·R4, all floors met) | Perspectives: 3 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer) | Gate passed

**Token overhead:** YAML adds roughly +3-7% tokens versus an equivalent Markdown version, from the indentation and folded-scalar structure.

**Summary:** Improved with `$improve` (Standard energy, CLEAR-scored) and the CRISPE framework you specified — a strong fit since CRISPE's Statement/Experiment structure naturally separates the reasoning-before-recommending step from the four-experiment output, and its "Insight" block cleanly carries all your operational numbers. The reasoning task is sequenced before the deliverable task (mechanism-first), the pay assumption is explicitly flagged for challenge, and the budget/mechanism-diversity constraints are enforced via the `experiment.iterate` clause rather than left implicit.

Two gaps in your original request were filled with flagged assumptions (per your "fill in the gaps yourself" instruction): whether EUR 120,000 covers all four pilots combined (assumed yes), and which depot hosts each pilot (left to the downstream AI's reasoning, since none were named).