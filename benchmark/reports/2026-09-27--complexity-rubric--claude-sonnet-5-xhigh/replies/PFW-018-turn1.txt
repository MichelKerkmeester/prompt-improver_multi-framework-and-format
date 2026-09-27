```markdown
Mode: $deep | Complexity: High (8/10) | Framework: CRAFT

**Context:** We are replacing the warehouse management system (WMS) across two distribution centres served by a single WMS vendor: Liège (12,000 order lines/day) and Tilburg (38,000 order lines/day). The new WMS integrates with our SAP ERP and three carrier systems. Today this rollout is requested with only "Make a go-live plan" — an instruction too unconstrained to produce anything beyond a generic phase checklist. A high-volume, dual-site WMS cutover fails when workstreams are planned in isolation: data migration, integrations, training and cutover each carry different lead times and failure risks, and Tilburg's volume means it cannot inherit Liège's risk tolerance. The plan must make every dependency, sequencing gate and fallback explicit rather than assumed.

Fixed facts and constraints the plan must respect:
- Two sites, one shared WMS vendor: Liège (pilot, 12,000 order lines/day), Tilburg (38,000 order lines/day).
- Integrations in scope: SAP ERP and three carrier systems.
- Blackout window: no go-live activity between 15 November and 10 January at either site.
- Sequencing: Liège goes live first. Tilburg may only follow after Liège sustains pick accuracy above 99.5% for four consecutive weeks post go-live.
- Training scope: 260 pickers across both sites, delivered in two languages.
- Rollback requirement: the old system must be fully restorable within 12 hours of a rollback decision at either site.
- Success definition: zero missed carrier cut-offs at a site during its first two weeks live.

**Role:** Act as a senior WMS implementation program manager experienced in phased, multi-site warehouse management system cutovers that integrate with ERP and carrier systems, including pilot-then-scale sequencing, hypercare operations and rollback design.

**Action:** Produce a single go-live plan covering both sites that:
1. Defines four workstreams — data migration, integrations (SAP ERP + three carriers), training (260 pickers, two languages), and cutover — each with milestones and explicit Liège vs. Tilburg variants.
2. Maps the dependencies between these four workstreams (what must complete, and to what level, before the next can start), noting where sequencing differs between the Liège pilot and the Tilburg follow-on.
3. Schedules both go-lives outside the 15 November–10 January blackout window, sequences Tilburg strictly after Liège, and encodes the four-consecutive-week, >99.5% pick-accuracy requirement as the explicit gate controlling the Tilburg start date.
4. Provides a go/no-go checklist for each site's go-live, covering data migration completeness, integration readiness (SAP ERP + each carrier), training completion for that site's picker population, and cutover readiness.
5. Provides a hypercare plan for each site's first two weeks live: monitoring focused on pick accuracy and carrier cut-off adherence, escalation paths, and exit criteria.
6. Provides a rollback plan restoring the old system within 12 hours of a rollback decision: trigger conditions and the steps required to hit that 12-hour target.

**Format:** Structure the output as:
- Executive overview (scope, sites, blackout window, sequencing logic — one paragraph)
- Workstream plans: one subsection each for Data Migration, Integrations, Training, Cutover, with milestones and Liège vs. Tilburg variants
- Dependency map: which workstream outputs gate which other workstream's start, per site
- Go/No-Go checklist: itemized, applicable per site before its go-live
- Hypercare plan: first-two-weeks monitoring, escalation, exit criteria, per site
- Rollback plan: trigger conditions, 12-hour restoration steps

**Target:** The plan succeeds if a program lead could execute both go-lives from it unmodified, and if following it produces zero missed carrier cut-offs at each site during its first two weeks live. Primary audience: the program lead and the data migration, integrations, training and cutover workstream owners who must sign off on each go/no-go decision.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = [Assumes: pick accuracy is measured the same way at Liège and Tilburg] [Assumes: the 12-hour rollback clock starts at the rollback decision, not at incident detection] [Assumes: the plan's audience is internal program/workstream leads, not external vendor or carrier contacts] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-wms-golive-plan-prompt.md`

**Score and gate status:** CLEAR 44/50 (C9, L9, E13, A9, R4) | Perspectives: 5 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer, Framework Architecture Expert, Token Optimisation Specialist) | Gate passed

**Summary:** Rebuilt the bare "make a go-live plan" instruction into a CRAFT prompt (your explicit framework choice — fits the 8/10 complexity, multi-stakeholder, comprehensive-documentation profile) that carries forward every fact and constraint you gave: both sites' volumes, the single vendor, SAP + three-carrier integrations, the blackout window, Liège-first sequencing with the four-week/99.5% Tilburg gate, all four workstreams, dependency mapping, go/no-go checklist, hypercare and the 12-hour rollback bar, plus your no-missed-cutoff success metric. Nothing was added beyond what makes those requested elements executable.