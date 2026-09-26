Mode: $improve | Complexity: High (8/10) | Framework: CRAFT

**Context:** A Dutch housing association ("woningcorporatie") with offices in Zwolle and Deventer runs a single on-premises Exchange Server 2016 organization. The migration must move 1,150 user mailboxes and 60 shared mailboxes (1,210 total) to Microsoft 365 Exchange Online. One shared mailbox, customer-service@[domain], is business-critical and may be unreachable for no more than 2 hours during its own migration window. Roughly 80 of the 1,150 users are field staff who access email exclusively through the Outlook mobile app on phones — no desktop or laptop mail client — so their coexistence and cutover experience must be validated on mobile specifically, not assumed to mirror desktop behavior.

Hard operating constraint: any activity that can disrupt live mail flow may run only on weekends (Friday evening through Monday morning). [Assumes: given this volume and the weekend-only window, the migration uses a staged/hybrid batch approach with Exchange Hybrid coexistence and Entra ID Connect (Azure AD Connect) directory sync established as prerequisite work, rather than a single cutover migration.] [Assumes: average mailbox size and available bandwidth support roughly 200 mailboxes per weekend batch, since all 1,210 mailboxes must complete within six weekends.] [Assumes: the customer-service mailbox runs in its own small, closely monitored batch and window — separate from bulk user batches — specifically to protect its 2-hour downtime ceiling.]

Non-negotiable success targets: zero lost mail across every mailbox and batch; fewer than 5% of the 1,210 migrated users log a support ticket in the first week after their batch cuts over; full completion, including decommissioning the on-premises Exchange 2016 server, within six weekends.

**Role:** Act as a senior Microsoft 365 / Exchange Online migration architect with hands-on experience leading hybrid Exchange-to-Microsoft 365 migrations for organizations operating under strict weekend-only maintenance windows, mixed desktop/mobile-only user populations, and business-critical mailbox uptime SLAs.

**Action:** Produce a complete, execution-ready email migration plan that:
1. Breaks the migration into sequential phases (e.g., Assessment & Prerequisites, Pilot Batch, successive Production Batches across the remaining weekends, Final Cutover of MX/Autodiscover, Post-Migration Stabilization & Decommission) sized to move all 1,210 mailboxes inside six weekends.
2. Defines, for every phase, explicit entry criteria (what must be verified true before the phase starts) and exit criteria (what must be verified before advancing to the next phase).
3. Defines a specific rollback procedure for every phase, describing exactly how to revert affected mailboxes and users to their prior working state if the phase fails its exit criteria.
4. Places one staff communication moment before each phase begins, naming the audience (all staff, field staff, customer-service team, etc.), the channel, and the core message.
5. Schedules the customer-service mailbox migration inside a batch and window explicitly designed to keep downtime at or under 2 hours, and states the fallback action if that ceiling is at risk mid-migration.
6. Gives the 80 mobile-only field staff distinct steps, testing and communication wherever their Outlook mobile app experience diverges from desktop users' experience.
7. Produces one consolidated risk table for the full migration with columns: risk, likelihood, impact, mitigation, owner.
8. Closes by mapping each of the three success targets — zero lost mail, under-5% first-week ticket rate, six-weekend completion — to the specific controls or checks in the plan that protect it.

**Format:** A structured Markdown plan document, in this order: (1) a one-paragraph executive summary; (2) one section per phase, each following Phase name → Entry criteria (bulleted) → Exit criteria (bulleted) → Rollback step → Staff communication moment (audience, channel, message); (3) a weekend-by-weekend schedule table mapping phases and batches to the six weekends; (4) the consolidated risk table; (5) a closing section mapping each success target to the plan controls that achieve it.

**Target:** The plan succeeds only if it can be executed without further clarification and demonstrably protects: zero lost mail during migration, under 5% of the 1,210 migrated users raising a support ticket in the first week post-cutover, and full completion — including on-premises Exchange 2016 decommission — within six weekends.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = 3 flagged | format = Markdown | execution = did not occur | save = did not occur
