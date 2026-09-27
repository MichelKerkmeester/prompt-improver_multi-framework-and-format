Mode: $improve | Complexity: High (7/10) | Framework: CRAFT

**Context:** A Dutch housing association is migrating email from an on-premises Exchange Server 2016 environment to Microsoft 365 (Exchange Online), across two offices in Zwolle and Deventer. Scope: 1,150 user mailboxes and 60 shared mailboxes (1,210 total), including one customer-service mailbox the business treats as mission-critical. [Assumes: the customer-service mailbox is one of the 60 shared mailboxes.] Cutover — the actual mailbox move/switchover — may only happen on weekends; weekday business operations must not be disrupted. The customer-service mailbox may be offline for no more than 2 hours during its own cutover. 80 field staff work mobile-only and never use a desktop Outlook client, so their mail access depends entirely on phone/tablet mail-app reconfiguration. [Assumes: target platform is Exchange Online / Microsoft 365 Outlook; the hybrid-vs-cutover migration method and batching mechanics are the AI's choice unless stated otherwise.] The entire migration must complete within six weekends total.

**Role:** Microsoft 365 messaging migration architect with hands-on Exchange Server 2016-to-Exchange-Online cutover/hybrid migration experience, mobile device mail-profile reconfiguration expertise for phone-only end users, and IT change-management communications planning for staff spread across multiple offices.

**Action:** Design a weekend-by-weekend phased migration plan that moves all 1,150 user mailboxes and 60 shared mailboxes from Exchange 2016 to Microsoft 365 within six weekends or fewer, because every disruptive cutover step is confined to weekends to protect weekday operations. For every phase, define:
- **Entry criteria:** what must be true and ready before that phase's weekend cutover window opens
- **Exit criteria:** what must be verified before the phase is declared complete, including a mail-integrity or item-count reconciliation check confirming zero lost mail for every mailbox moved in that phase
- **Rollback step:** the specific action to reverse that phase's cutover and restore affected users to the on-premises system if exit criteria are not met before Monday business hours resume
- **Staff communication moment:** occurring before that phase's cutover weekend begins, stating audience, channel and core message

Within the phase design, explicitly:
- Isolate the customer-service mailbox into a phase or sub-step engineered to keep its downtime at or under 2 hours, and state the technique used to hit that ceiling
- Isolate the 80 phone-only field staff into a phase or sub-step covering mobile mail-profile reconfiguration, timed so these users regain phone mail access without needing desktop support
- Build in a first-week post-migration monitoring step that tracks help-desk ticket volume against the under-5%-of-users target and defines what triggers escalation if that threshold is at risk

Produce a risk table covering migration-specific risks (for example: mail or calendar item loss, mobile profile reconfiguration failures, DNS/MX/Autodiscover cutover errors, weekend-batch throttling or bandwidth limits, customer-service downtime overrun, missed-communication confusion), with columns: Risk, Likelihood, Impact, Mitigation, Owner.

**Format:** A written migration plan in Markdown, structured as:
1. Scope summary — mailbox counts, offices, six-weekend ceiling, weekend-only cutover rule
2. Phase-by-phase sections (the AI determines how many phases are needed to fit six weekends), each containing: Objective, Entry Criteria, Exit Criteria, Rollback Step, Staff Communication Moment, Execution Summary
3. Dedicated sub-sections addressing the customer-service mailbox (2-hour downtime ceiling) and the 80 phone-only field staff
4. Risk table (Risk / Likelihood / Impact / Mitigation / Owner)
5. Success-metrics tracking section: zero-lost-mail verification method, and first-week ticket-rate monitoring against the under-5% target

**Target:** All 1,210 mailboxes fully migrated within six weekends; zero mail lost across every phase; fewer than 5% of the 1,150 users raise a help-desk ticket in the first week post-migration; the customer-service mailbox's downtime during its own cutover does not exceed 2 hours.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = target platform is Exchange Online/M365 Outlook; migration method and batching mechanics left to the AI; customer-service mailbox is one of the 60 shared mailboxes; weekday business hours are protected, all cutover confined to weekends | format = Markdown | execution = did not occur | save = did not occur
