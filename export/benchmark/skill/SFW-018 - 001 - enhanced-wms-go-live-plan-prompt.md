Mode: $deep | Complexity: High (8/10) | Framework: CRAFT

**Context:** You are planning the go-live for a new Warehouse Management System (WMS) replacing the legacy system across two distribution centres (DCs): Liège (12,000 order lines/day) and Tilburg (38,000 order lines/day, roughly three times Liège's volume). One WMS vendor supplies and configures the platform for both sites. The new WMS integrates with the company's SAP ERP and three separate carrier systems for outbound shipping. Business rules fix the rollout sequence and timing:
- No go-live date may fall between 15 November and 10 January, to protect peak-season operations.
- Liège goes live first, as the pilot site, to prove the system at lower volume before the higher-volume site is exposed to it.
- Tilburg's go-live may only be scheduled after Liège has sustained pick accuracy above 99.5% for four consecutive weeks following its own go-live.
260 pickers across both sites need training, delivered in two languages. If a go-live fails, the legacy WMS must be fully restored within 12 hours.

**Role:** Act as a senior WMS rollout program manager with experience sequencing multi-site go-lives, coordinating ERP and carrier integration cutovers, and running hypercare for high-volume distribution centres.

**Action:** Produce the go-live plan for both DCs, sequenced per the constraints above. The plan must include:
- Workstreams for data migration, integrations (SAP ERP and the three carriers), picker training (260 pickers, two languages), and cutover, each with the activities and milestones needed to reach go-live readiness at a DC.
- The dependencies within and across these workstreams, including how Tilburg's workstreams depend on Liège's four-week pick-accuracy result and how the blackout window constrains scheduling for both sites.
- A go/no-go decision checklist to run before each site's go-live, covering data migration validation, integration test completion (SAP and all three carriers), training completion, and cutover readiness.
- A hypercare plan for the period immediately following each site's go-live, including how pick accuracy is monitored against the 99.5% Tilburg-gating threshold at Liège.
- A rollback plan that restores the legacy WMS within 12 hours if a go-live must be reversed, including the trigger conditions for invoking it.
Explain the dependency and sequencing logic, not just list it, so the reasoning behind the Liège-first, gated-Tilburg approach is traceable.

**Format:** Deliver a structured plan document with these named sections in order: Workstream Breakdown (one subsection per workstream: Data Migration, Integrations, Training, Cutover), Dependency Map (cross-workstream and cross-site dependencies, including the blackout window and the four-week gating condition), Go/No-Go Checklist (a separate checklist for Liège and for Tilburg), Hypercare Plan (per site, including the pick-accuracy monitoring approach), Rollback Plan (steps and timeline to restore the legacy system within 12 hours). Use headings and bullet or numbered lists; keep each section self-contained enough to hand to the workstream owner responsible for it.

**Target:** The plan succeeds if: no go-live is scheduled between 15 November and 10 January; Tilburg's go-live is scheduled only after Liège records four consecutive weeks of pick accuracy above 99.5%; the rollback plan can restore the legacy WMS within 12 hours of a decision to roll back; and, for each site, there are no missed carrier cut-offs in the first two weeks of live operation.
