Saved: `export/001 - enhanced-support-chatbot-prompt.md`

**CLEAR 44/50 | Gate: passed**

I used RCAF (fits a low-complexity, single-outcome chatbot instruction) and turned the two vague verbs — "answer nicely" and "fix their problem" — into a concrete Role/Context/Action/Format spec: empathetic acknowledgment → root-cause diagnosis → step-by-step resolution or a clear escalation path, with plain-language tone and a mandatory close-out confirmation. Bracketed placeholders (`[product/company name]`, `[support channel]`, `[escalation policy]`) keep it reusable across your actual stack — swap those in and it's ready to drop into the bot's system prompt.

Want me to tighten it further into a single-line version, or expand the escalation branch (e.g., billing vs. technical routing)?