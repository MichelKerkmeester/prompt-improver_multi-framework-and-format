Saved: `export/001 - enhanced-postmortem-prompt.md`

CLEAR 44/50 | Gate: passed (floors met — C9, L9, E13, A9, R4)

This is a Deep-energy, layered-RCAF rewrite (Role/Context/Action/Format, catalogue-lint compliant) that turns your one-liner into an operational spec: it ingests the PagerDuty timeline, Slack export and deploy log for one SEV1/SEV2 incident, normalizes timestamps to UTC with 10-minute gap-flagging, enforces confirmed-root-cause-vs-hypothesis labeling, mandates account-ID anonymization, and requires responders-list owners plus due weeks on every action item. The Format section fixes the three audience layers (Technical Timeline, Impact Summary, five-sentence Executive Brief) in order, with nothing streamlined or dropped per your instruction.

Since you asked to skip questions and everything needed was already in your message, no clarification was raised — flag if you want the exec brief's five-sentence rule loosened for edge cases (e.g., incidents with no confirmed root cause yet).