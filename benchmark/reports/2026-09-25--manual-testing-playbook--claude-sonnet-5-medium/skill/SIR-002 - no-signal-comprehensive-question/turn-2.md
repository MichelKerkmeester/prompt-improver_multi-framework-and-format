Saved: `export/001 - enhanced-support-chatbot-prompt.md`

CLEAR 44/50 | Gate: passed | Mode: `$text` (Standard) | Framework: RCAF

The prompt now sets a support-agent role and gives the chatbot a fixed sequence:
- Find the real problem, asking one question if it's unclear.
- Give numbered steps from approved sources.
- Confirm the fix worked.
- Escalate when it can't resolve the issue.

It also bans invented policies and details, and sets a tone and a reply-length limit.

`[Assumes: the bracketed placeholders (company, approved sources, scope, escalation path, word limit) are yours to fill in, since your draft didn't include them.]` I picked Standard energy and Markdown because you gave no mode or format. Tell me if you want `$short`, `$json` or `$yaml` instead.