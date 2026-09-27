Mode: $deep | Complexity: High (7/10) | Framework: CRAFT

---

**Context:** [Company] is implementing a new warehouse management system (WMS) from a single vendor, [WMS vendor], across two distribution centres — Tilburg (38,000 order lines/day) and Liège (12,000 order lines/day). The WMS integrates with the SAP ERP system and three carrier systems ([Carrier 1], [Carrier 2], [Carrier 3]). No go-live activity may occur between 15 November and 10 January. Liège goes live first as the pilot site; Tilburg may only follow once Liège has sustained pick accuracy above 99.5% for four consecutive weeks. Training must reach 260 pickers across both sites, delivered in two languages.

**Role:** Senior WMS implementation and cutover program manager with experience sequencing multi-site go-lives, SAP and carrier system integrations, and warehouse floor operations.

**Action:** Build a phased go-live plan for Liège (pilot) followed by Tilburg (gated), covering:
- **Data migration workstream:** scope, validation steps and sign-off criteria for master and transactional data at each site.
- **Integrations workstream:** SAP ERP and the three carrier system connections, including test and validation steps per site.
- **Training workstream:** delivery plan for 260 pickers in two languages, sequenced per site.
- **Cutover workstream:** step-by-step sequence for switching each site from the legacy system to the new WMS.
- **Dependency map:** explicit dependencies between and within the workstreams above, and between the two site go-lives, encoding:
  - the 15 November-10 January blackout as a hard no-go window for either site
  - Liège preceding Tilburg
  - the Tilburg gate: go-live blocked until Liège records four consecutive weeks of pick accuracy above 99.5%
- **Go/no-go checklist:** decision criteria for each site's go-live, covering workstream completion, integration validation, blackout-window compliance and, for Tilburg, the pick-accuracy gate.
- **Hypercare plan:** stabilization coverage, monitoring cadence and escalation path for the weeks immediately following each site's go-live.
- **Rollback path:** trigger conditions and step sequence to restore the legacy system within 12 hours at either site.

**Format:** Markdown plan with one section per workstream listed above, a dependency table or map showing cross-workstream and cross-site dependencies, a checklist-style go/no-go section, a dedicated hypercare section and a dedicated rollback section whose steps carry time estimates summing to 12 hours or less.

**Target:** A plan detailed enough for ops, IT and the WMS vendor to execute both go-lives with zero missed carrier cut-offs in the first two weeks following each site's go-live, while fully respecting the blackout window and the Liège-to-Tilburg pick-accuracy gate.
