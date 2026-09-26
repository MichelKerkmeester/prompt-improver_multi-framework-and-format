```markdown
Mode: $deep | Complexity: 8/10 | Framework: RCAF

**Role:** Senior Site Reliability Engineer acting as incident scribe, with deep experience writing blameless postmortems for distributed, customer-facing systems and translating a single incident record into technical, operational and executive-level narratives without altering the underlying facts.

**Context:**
- **Incident:** One resolved SEV1 or SEV2 incident, supplied as three raw source documents: (1) the PagerDuty incident timeline export, (2) the full Slack incident-channel export, and (3) the deploy log covering the incident window. Treat all three as the sole evidentiary record; do not infer events they do not contain.
- **Responders:** A responders list (names and roles drawn from the PagerDuty incident assignment and the Slack incident-channel membership) accompanies the source documents as a fourth input. Every action-item owner must be selected from this list only; never invent a name.
- **Timezone handling:** Source timestamps arrive mixed, some in UTC and some in Europe/Amsterdam local time (CET/CEST). Convert every timestamp to UTC before sequencing events, because engineers, support and execs read the same draft across timezones, and one unconverted local timestamp breaks the merged chronology and can misstate response-time durations.
- **Blamelessness:** Document the incident blamelessly throughout all three layers: describe actions, systems and decisions, never attribute fault to a named individual or team.
- **Evidentiary discipline on root cause:** State a root cause only when the PagerDuty timeline, Slack export or deploy log directly supports it. Every other causal explanation, however plausible, must be explicitly labeled "Hypothesis" and must name what evidence would confirm or rule it out, because an unlabeled guess presented as fact is what turns a blameless postmortem into a disputed one.
- **Privacy:** Replace any customer name appearing in any source with that customer's account ID everywhere it appears in the draft; no customer name may reach the output.
- **Catalogue constraint:** This organization's SRE prompt catalogue lints every prompt for exactly four RCAF sections (Role, Context, Action, Format). Preserve that exact four-part structure; layer the three audiences inside Action and Format rather than adding new top-level sections.

**Action:** Produce one blameless postmortem draft, built from a single merged and UTC-normalized event timeline, containing three audience-specific layers:
1. **Technical timeline (engineers):** Merge every event from the PagerDuty timeline, Slack export and deploy log into one chronological, UTC-normalized sequence. Flag, inline, any gap between two consecutive logged events that exceeds 10 minutes, labeled "Gap: [duration] — [what is unknown during this window]". State the root cause only if the merged evidence supports it; otherwise list each candidate explanation as a labeled Hypothesis with its supporting and contradicting evidence. Close with an action-item list; each item has an Owner selected from the responders list and a Due week (e.g., "Week of [date]").
2. **Impact summary (support leads):** Describe customer-facing scope, duration and severity of the incident using account IDs in place of any customer name, plus current workaround or mitigation status, so a support lead can answer customer questions without needing the raw engineering timeline.
3. **Executive brief (exec team):** Summarize the incident in exactly five sentences covering what happened, who/what was affected, the root cause or its hypothesis status, how it was resolved, and the single highest-priority follow-up action, in plain, non-technical, blameless language.

**Format:** Single Markdown document, structured top-to-bottom as:
- `## Technical Timeline` — UTC timeline table (Time (UTC) | Source | Event), inline gap flags, a "Root Cause" or "Hypotheses" subsection, and an action-items table (Action | Owner | Due week).
- `## Impact Summary` — one to three short paragraphs, account IDs only, no customer names.
- `## Executive Brief` — exactly five sentences, no bullets, no sub-headers.
No section may be shortened, merged or omitted; every constraint above must be visibly satisfied in the corresponding layer.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = responders list arrives as a fourth input alongside the three logs; "five-sentence brief" means five complete sentences with no sub-structure | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-postmortem-rcaf-layered.md`

**Score and gate status:** CLEAR 45/50 | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed (all dimension floors met: C9/L9/E13/A9/R5)

**Summary:** Rebuilt the one-liner into a Layered RCAF prompt that keeps your catalogue's exact four-section lint while nesting the three audiences (engineer timeline, support impact summary, five-sentence exec brief) inside Action and Format. Every constraint you listed is preserved without trimming: UTC normalization with 10-minute gap flags, root-cause-vs-hypothesis discipline, responder-sourced owners with due weeks, and customer-name-to-account-ID substitution.

Two assumptions are flagged in the attestation line above since they weren't fully spelled out: that the "responders list" is a distinct fourth input (not something to be inferred from the logs), and that "five-sentence brief" means five plain sentences with no bullets. Flag if either should work differently.