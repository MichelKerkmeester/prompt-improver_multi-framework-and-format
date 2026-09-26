File saved: `export/001 - enhanced-outage-communication-prompt.md`

CLEAR 45/50 | Gate: passed (C9 · L9 · E13 · A9 · R5, all floors cleared)

Built with COSTAR at Deep energy (5 perspectives, all blocking): global Context/Objective/Style/Tone carry the shared rules, while Audience and Response each break into SMS, Email, and Phone Script sub-blocks with channel-specific specs (300-char SMS cap with a trim rule that protects the four mandatory facts, subject+body email structure, spoken-line phone script). The prompt takes `{INCIDENT_FACTS}` as a single reusable input and enforces the cause/data-exposure guardrails through a pre-delivery self-check rather than a passive instruction, so it's ready to reuse for the next outage without editing.

[Assumes: front-desk phone script is read/paraphrased live rather than sent verbatim; a single direct clinic phone number is published per incident rather than 14 separate numbers — adjust `{INCIDENT_FACTS}` if that's not the case.]