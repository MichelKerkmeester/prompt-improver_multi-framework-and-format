Mode: $deep | Complexity: High (8/10) | Framework: CRAFT

**Context:** The organization is rolling out a new Warehouse Management System (WMS) from a single vendor across two distribution centres (DCs): Tilburg (38,000 outbound order lines/day) and Liège (12,000 outbound order lines/day). The WMS integrates with the SAP ERP system and three carrier systems for shipping. No go-live date may fall between 15 November and 10 January (peak-season blackout window). Liège is the pilot site and goes live first; Tilburg may only begin its own cutover after Liège has sustained pick accuracy above 99.5% for four consecutive weeks following its go-live. Training must reach all 260 pickers across both sites, delivered in two languages. Treat these facts as fixed constraints — do not introduce additional sites, systems, vendors, budgets, headcounts, or deadlines beyond what is stated here.

**Role:** Act as a senior WMS go-live program manager and cutover lead with proven expertise in phased, multi-site warehouse deployments; SAP ERP and carrier-integration cutover sequencing; pick-accuracy-gated rollout governance; and warehouse hypercare and rollback risk management.

**Action:** Produce a single, complete go-live plan covering both DCs that includes, at minimum, all of the following, with nothing omitted or merged away:

1. **Workstreams** — define scope, key activities, and readiness criteria for each of:
   - Data migration (master data, inventory, open orders) into the new WMS.
   - Integrations: SAP ERP plus each of the three carrier systems, including interface testing and cutover sequencing.
   - Training: plan to certify all 260 pickers, delivered in two languages, completed before each site's respective go-live.
   - Cutover: step-by-step transition activities per site, distinguishing Liège's pilot cutover from Tilburg's follow-on cutover.
2. **Dependency map** — show explicit dependencies within and across workstreams and across sites, including at minimum: Tilburg's cutover cannot start until Liège has recorded 4 consecutive weeks of pick accuracy above 99.5%; integration sign-off must precede cutover; training completion must precede cutover; no cutover activity may be scheduled between 15 November and 10 January for either site.
3. **Go/No-Go checklist** — separate checklists for the Liège pilot go-live and the Tilburg go-live, each listing the specific pass/fail criteria that must be true before cutover proceeds (including the pick-accuracy gate for Tilburg and the blackout-window check for both sites).
4. **Hypercare plan** — the post-go-live support period for each site: duration, monitoring focus (including pick accuracy and carrier cut-off adherence), escalation path, and exit criteria back to standard support.
5. **Rollback path** — a documented procedure to revert to the legacy WMS within 12 hours of a rollback decision, including the decision-maker, trigger conditions, and the sequence of steps required to restore the old system within that window.

Where a specific date, name, owner, or number is not provided in the Context, use an explicit bracketed placeholder (e.g., [Owner], [Target Date]) rather than inventing a value.

**Format:** Deliver the plan as a structured document with these sections, in this order:
1. Executive Summary (5-8 sentences).
2. Rollout Sequence & Constraints (states the blackout window and the Liège-first, accuracy-gated Tilburg sequencing in plain terms).
3. Workstreams (one subsection each for Data Migration, Integrations, Training, Cutover).
4. Dependency Map (table: Dependency | Depends On | Blocking Condition).
5. Go/No-Go Checklist (one checklist table for Liège, one for Tilburg; columns: Criterion | Pass Threshold | Status).
6. Hypercare Plan (one subsection per site).
7. Rollback Plan (numbered steps, with the 12-hour restoration target stated explicitly).
8. Success Metrics.
Use tables and checklists rather than dense prose wherever they improve scannability. Keep each workstream and section self-contained enough to be extracted and assigned to a separate owner.

**Target:** The plan succeeds if, when followed, it results in zero missed carrier cut-offs across all three carriers at a site during that site's first two weeks live on the new WMS. It must also make the following explicit and verifiable: Liège's 4-week, >99.5% pick-accuracy gate as the sole trigger for starting Tilburg's cutover; full compliance with the 15 November-10 January blackout window for both sites; and a rollback path proven capable of restoring the legacy system within 12 hours. Flag any point where the plan had to assume information not given in the Context.
