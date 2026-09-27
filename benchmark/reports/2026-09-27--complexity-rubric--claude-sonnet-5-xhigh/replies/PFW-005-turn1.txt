Mode: $yaml | Complexity: Complex (9/10) | Framework: COSTAR

```yaml
context:
  delivery_channel: Internal HR assistant (GPT-4.1) on the company intranet, publishing an all-staff HR policy announcement
  policy_facts:
    effective_date: 2026-03-01
    office_requirement: All staff are on-site every Tuesday and Thursday from the effective date
    exceptions_rule: Team leads may grant up to 2 exceptions per person per quarter to the Tuesday/Thursday requirement
    travel_allowance_change:
      previous: Reimbursed per kilometre travelled
      new: Flat EUR 60 per month
      effective_date: 2026-03-01
  staff_profile:
    headcount: 420
    locations: [Utrecht office, Ghent office]
    roles_span: Warehouse crew through engineers, so reading level and daily routine vary widely
  hard_boundaries:
    - State only the facts listed under policy_facts; invent no dates, amounts, exceptions or eligibility rules
    - Do not promise future flexibility, additional perks, or any exception beyond the stated 2-per-quarter allowance
    - Do not use corporate buzzwords or spin, for example "exciting journey", "synergy", "one big family", "empowerment"
    - Produce only the three deliverables listed in objective.deliverables; no cover email, poster or extra formats
objective:
  primary: Draft three staff-facing communications announcing the hybrid-work policy change, each usable as-is
  deliverables:
    - id: announcement
      length: Approximately 300 words, within 10 percent
      must_cover:
        - Effective date and the Tuesday/Thursday office requirement
        - How the per-person, per-quarter exception process works
        - The change from per-kilometre to a flat EUR 60 monthly travel allowance
        - Where to direct questions
    - id: faq
      length: Exactly 6 question-and-answer pairs
      must_cover_topics:
        - Who the policy applies to
        - What happens on the two required office days versus other days
        - How to request an exception and what counts as one
        - How the new flat allowance is paid and from when
        - Why the allowance changed from per-kilometre to flat-rate
        - What to do if a role's shift pattern conflicts with Tuesday/Thursday
    - id: slack_teaser
      length: Exactly 2 lines
      purpose: Prompt staff to open the full announcement on the intranet
style:
  register: Plain, direct, workplace-neutral language equally readable by warehouse crew and engineers
  sentence_construction: Short sentences, concrete facts, no hedging, no marketing adjectives
tone:
  primary: Direct and reassuring
  prohibited: Corporate spin, forced enthusiasm, vague reassurance not backed by a stated fact
audience:
  description: 420 staff across Utrecht and Ghent, spanning warehouse crew to engineers, mixed familiarity with HR or legal phrasing
  needs: Fast, unambiguous understanding of what changes, when, and who to ask, without inferring unstated details
response:
  format: Three clearly labeled sections in this order: announcement, faq, slack_teaser
  validation_before_delivery:
    - Every claim traces to a fact under context.policy_facts
    - Announcement word count falls within the stated range
    - Faq contains exactly 6 question-and-answer pairs
    - Slack_teaser is exactly 2 lines
    - No sentence promises anything beyond the stated policy
  output_language: English
```

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide YAML | assumptions = travel allowance effective date matches office-requirement date (1 March 2026); FAQ topics selected to cover the six most likely staff questions since exact questions weren't given; corporate-spin ban interpreted via a representative buzzword avoid-list | format = YAML | execution = did not occur | save = did not occur

**Export-equivalent path:** `export/001 - enhanced-hybrid-work-policy-announcement.yaml`

**Score and gate status:** CLEAR 44/50 (C9 L8 E14 A9 R4) | Perspectives: 3 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer) | Gate passed

**Token overhead:** YAML format adds roughly +3-7% tokens versus Markdown for this deliverable.

**Summary:** This prompt gives your intranet HR assistant a COSTAR-structured brief covering the 1 March hybrid policy (Tue/Thu on-site, 2 exceptions/quarter, flat €60/month allowance) for a mixed warehouse-to-engineer audience across Utrecht and Ghent. It locks the three required deliverables, their exact lengths, and hard guardrails against invented details or corporate spin, with a pre-delivery checklist the assistant runs against itself. `[Assumes: allowance change lands on the same 1 March date as the office-attendance change]` — flag this with HR if the effective dates actually differ.