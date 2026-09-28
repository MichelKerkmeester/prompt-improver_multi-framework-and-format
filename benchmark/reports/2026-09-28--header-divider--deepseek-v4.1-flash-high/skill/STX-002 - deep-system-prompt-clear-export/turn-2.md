Saved: `export/002 - enhanced-helpdesk-triage-system-prompt-multilingual.md`

**CLEAR 45/50 | Gate: passed** — Correctness 9, Logic 9, Expression 14, Arrangement 9, Reusability 4 (all floors met). Deep energy retained; the original `001` export is untouched.

This revision adds a language dimension to the triage rules: the bot reads English or Dutch, always writes the internal note in English so any agent can act on it, and adds a `Customer quote` field that copies the customer's key sentence verbatim in their own language — never translated or paraphrased. The examples now include Dutch billing and escalation cases, and the anti-pattern shows the failure mode of translating instead of quoting.

[Assumes: the internal note field order is Category → Priority → Escalate → Customer quote → Summary, and the quote is limited to one sentence.] Want a JSON/YAML variant for the Zendesk webhook, or should the quote field also capture the customer's requested remedy (e.g., refund asks) without committing to it?