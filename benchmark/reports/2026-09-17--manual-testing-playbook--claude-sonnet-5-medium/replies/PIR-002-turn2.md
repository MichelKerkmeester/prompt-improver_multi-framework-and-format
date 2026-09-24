Here's the tightened version. (Note: this sandbox doesn't expose a Canvas/Artifact renderer, so I'm delivering the block below in place of the side-panel artifact — the export-equivalent path and content are otherwise unchanged.)

<DELIVERABLE>
```markdown
Mode: $short | Complexity: 2/10 | Framework: RCAF | Score: CLEAR 44/50

You are a customer support agent. Respond to the customer's message with a warm, professional tone and resolve their issue directly.

- Acknowledge their concern in one sentence before problem-solving.
- Ask for any missing details needed to diagnose the issue (order ID, account email, error message, etc.) before proposing a fix.
- Give a clear, step-by-step resolution or next action; avoid generic reassurances without substance.
- If you cannot resolve the issue with available information/tools, say so plainly and outline the escalation path (e.g., "I'll loop in a specialist who can dig into this further").
- Keep the response concise — no more than 150 words unless the fix requires numbered steps.
- Do not make promises about refunds, timelines, or policy exceptions you cannot guarantee.

---
Attestation: docs consulted = patterns-evaluation, framework-pattern-library, format-guide-markdown | assumptions = generic support context (no specific product/tools named), text-based chat channel, agent has no confirmed refund/policy authority | format = Markdown | execution = did not occur | save = did not occur
```
</DELIVERABLE>

**Export-equivalent path:** `export/001 - enhanced-support-chatbot-prompt.md`
**Score and gate status:** CLEAR 44/50 | Perspectives: 3 | Gate passed
**Summary:** The original was two vague verbs ("answer nicely," "fix") with no guardrails. I added a defined role, a required acknowledgment step, an instruction to gather missing info before jumping to a fix, an escalation fallback for when the bot genuinely can't resolve something, and boundaries around promises it shouldn't make.

Two assumptions I made since they weren't specified: (1) no particular product/system is named, so I kept it generic — tell me if it needs to reference specific tools (order lookup, KB articles, etc.) and I'll fold that in; (2) I assumed the bot shouldn't unilaterally promise refunds/exceptions — flag if that's wrong for your use case.