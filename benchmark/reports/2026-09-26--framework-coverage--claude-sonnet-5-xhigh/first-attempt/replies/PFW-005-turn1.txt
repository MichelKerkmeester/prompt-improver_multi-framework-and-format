```
Mode: $yaml | Complexity: 6/10 | Framework: COSTAR

context:
  platform: Company intranet HR assistant, GPT-4.1
  organization_profile: Single company with two office sites, Utrecht (Netherlands) and Ghent (Belgium)
  audience_size: 420 employees total across both sites
  role_range: Full range from warehouse crew to engineers
  policy_facts:
    effective_date: >-
      1 March [Assumes: the next 1 March from today, 26 September 2026, i.e. 1 March 2027 --
      confirm exact year before publishing]
    in_office_days: Tuesday and Thursday, every week, for all staff
    exception_rule: Team leads may grant up to 2 exceptions per employee per quarter
    travel_allowance_change: Moves from per-kilometre reimbursement to a flat EUR 60 per month
  hard_boundary: >-
    Use only the four policy facts listed above. Do not add benefits, dates, eligibility
    rules, or promises that are not explicitly stated here.
  why_boundary_matters: >-
    Staff will quote this announcement back once they calculate their own commuting costs,
    so any invented or implied detail becomes a commitment the company never intended to make.

objective: >-
  Draft three ready-to-post HR communications that tell all 420 employees, from warehouse
  crew to engineers at both sites, exactly what changes on 1 March, how the exception
  process works, and how the travel allowance changes, so no one is caught unaware and
  the obvious questions are pre-answered.

style: >-
  Direct, concrete, plain language. Sentences short enough that a warehouse-floor employee
  and an engineer both understand on first read. No corporate buzzwords, no euphemisms,
  no filler transitions.

tone: >-
  Direct and reassuring, never spin. Name the change plainly -- per-kilometre reimbursement
  is being replaced by a flat EUR 60 per month -- rather than framing it as a perk. Do not
  over-apologize for the change and do not oversell the new schedule as flexibility.

audience:
  profile: 420 staff across Utrecht and Ghent, spanning warehouse crew to engineers
  reading_conditions: >-
    Mixed roles, mixed daily intranet and Slack usage. Assume no prior context beyond
    "there is a new hybrid-work policy."
  language: >-
    [Assumes: English is the working language for intranet and Slack at this company;
    flag for local translation review if Ghent staff need Dutch or French]

response:
  deliverables:
    - name: announcement
      format: Intranet post, approximately 300 words
      must_include:
        - Effective date (1 March)
        - The Tuesday and Thursday in-office requirement for all staff
        - How and from whom to request one of the two quarterly exceptions
        - The travel allowance change from per-kilometre to a flat EUR 60 per month
        - Where to direct questions
      must_avoid:
        - Any fact, date, or entitlement not listed in context.policy_facts
    - name: faq
      format: Exactly 6 question-and-answer pairs
      must_address: >-
        The 6 questions employees will actually ask, covering schedule, exceptions, the
        allowance change, the start date, who the policy applies to, and where to escalate
        questions. Do not invent a seventh topic or pad a thin one to reach the count.
      must_avoid:
        - Speculation on details the policy facts do not cover
    - name: slack_teaser
      format: Exactly 2 lines
      purpose: Prompt staff to open the full intranet announcement
      must_avoid:
        - Restating the full policy; tease it instead
  cross_deliverable_rules:
    - All three outputs must agree on every fact; no contradictions between announcement, faq, and slack_teaser
    - Label each deliverable clearly and deliver in this order, announcement, faq, slack_teaser
  quality_bar: >-
    If any sentence could be read as a promise beyond the four policy facts in
    context.policy_facts, rewrite it before delivering.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide YAML] | assumptions = [1 March read as the next occurrence, 1 March 2027; English as working language for intranet/Slack] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-hybrid-work-policy-announcement.yaml`

**Score and gate status:** CLEAR 44/50 | Perspectives: 5 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer, Framework Architecture Expert, Token Optimisation Specialist) | Gate passed

**Token overhead:** YAML format adds approximately +3-7% tokens versus an equivalent Markdown version.

**Summary:** Built with COSTAR (audience-specific communication task, matches the framework's decision-table trigger) since the request named specific audience segments, tone constraints and three distinct deliverables. The four policy facts (schedule, exceptions, allowance) are isolated in `context.policy_facts` and referenced by name in the `response` constraints so the announcement, FAQ and Slack teaser can't drift from each other or invent anything beyond what you supplied. Two assumptions were filled sensibly rather than asked about: the year for "1 March" (assumed 2027, the next occurrence from today) and English as the working language across both sites — both flagged inline in the YAML for you to confirm before publishing.