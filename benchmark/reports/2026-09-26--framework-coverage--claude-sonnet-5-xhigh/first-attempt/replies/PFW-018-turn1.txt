```markdown
Mode: $deep | Complexity: 8/10 | Framework: CRAFT

**Context:** [Company] is deploying a new Warehouse Management System (WMS) from a single vendor across two distribution centres — Tilburg (38,000 order lines/day) and Liège (12,000 order lines/day) — integrated with the SAP ERP and three carrier systems. Liège launches first as the pilot site. Tilburg's cutover may only begin after Liège has sustained pick accuracy above 99.5% for four consecutive weeks post-launch. No cutover activity for either site may occur between 15 November and 10 January. Training must reach 260 pickers across two languages. Today's plans are produced from a single-line request ("Make a go-live plan"), which returns generic output with no site sequencing, dependency logic, or contingency detail.

**Role:** Act as a senior WMS implementation program manager experienced in phased, multi-site go-lives involving ERP and carrier integrations, accuracy-gated rollout sequencing, and formal cutover/rollback procedures.

**Action:** Produce a single, complete go-live plan covering both distribution centres that:
- Defines four workstreams: data migration, integrations (SAP ERP plus the three carrier systems), training (260 pickers, delivered in two languages), and cutover.
- Maps explicit dependencies within and across workstreams, including: (a) Tilburg's cutover cannot start until Liège has recorded four consecutive weeks of pick accuracy above 99.5%, and (b) no cutover step at either site is scheduled between 15 November and 10 January.
- Includes a go/no-go checklist to be run immediately before each site's cutover.
- Includes a hypercare plan for the post-go-live stabilization window at each site.
- Includes a rollback path that restores the legacy WMS within 12 hours of a rollback decision, including the criteria that trigger rollback.
- States the success criterion explicitly: zero missed carrier cut-off times in the first two weeks after each site's go-live.

**Format:** Structure the plan in this order:
1. **Rollout Sequence & Constraints** — site order (Liège pilot, then Tilburg), the 15 November–10 January blackout window, and the four-week >99.5% pick-accuracy gate as the explicit condition for advancing to Tilburg.
2. **Workstream Breakdown** — one subsection per workstream (data migration, integrations, training, cutover) covering objectives, key activities, and site-specific variations driven by the Tilburg/Liège order-line volume difference.
3. **Dependency Map** — a table or ordered list showing what must complete before what, both within a site's workstreams and between the two sites' go-lives.
4. **Go/No-Go Checklist** — itemized per site, flagging where criteria differ due to volume or language.
5. **Hypercare Plan** — duration, monitoring cadence (including pick-accuracy tracking toward the Tilburg gate), escalation path, and exit criteria.
6. **Rollback Plan** — trigger conditions, step-by-step restoration sequence, the 12-hour recovery target, and validation steps confirming the legacy system is fully operational again.

Use headers and tables/lists throughout; each section must be usable directly by a site lead without needing the other sections for context.

**Target:** A go-live plan where success is measured by zero missed carrier cut-offs in each site's first two weeks live, Tilburg's cutover triggering only once Liège's four-week >99.5% pick-accuracy gate is verifiably met, and full legacy-system restoration achievable within 12 hours whenever rollback is invoked.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = [Assumes workstream owners/roles are left as placeholders for the user's org chart] [Assumes carrier and system names beyond "SAP ERP" and "three carriers" are not required in the prompt itself] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-wms-go-live-plan.md`

**Score and gate status:** CLEAR 44/50 (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4) | Perspectives: 5 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer, Framework Architecture Expert, Token Optimisation Specialist) | Gate passed | Improvement cycles: 0

**Summary:** The prompt replaces the single-line "Make a go-live plan" request with a CRAFT structure that locks in every fact you gave — the two-DC volumes, the SAP + three-carrier integrations, the Liège-first/Tilburg-gated sequencing, the 15 Nov–10 Jan blackout, the 260-picker bilingual training need, and the 12-hour rollback and no-missed-cutoff success bar — so the downstream AI builds dependencies and checklists around them instead of inventing generic ones. Nothing beyond what you listed (workstreams, dependencies, go/no-go, hypercare, rollback) was added.