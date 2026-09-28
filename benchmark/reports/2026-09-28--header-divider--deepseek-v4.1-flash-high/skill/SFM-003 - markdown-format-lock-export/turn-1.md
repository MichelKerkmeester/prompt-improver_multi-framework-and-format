Saved: `export/001 - enhanced-pr-code-review-prompt.md`

CLEAR 45/50 | Gate: passed | Mode: $improve (Standard) | Framework: RCAF | Complexity: Medium (5/10)

The rewritten prompt adds a reviewer role, an explicit three-area checklist (security, missing tests, unclear naming), and a mechanism-first rule that forces *why it matters* before *what to change* — matching your "senior reviewer" voice. It also tells the model to treat the pasted diff as the sole input and to infer stack/conventions from it, so it stays reusable across your team's PRs. No clarifying question was needed since you supplied the prompt, use case, checks, and paste-in workflow.