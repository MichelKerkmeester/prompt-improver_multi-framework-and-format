Saved: `export/001 - enhanced-blog-post-coffee-brewing-prompt.md`

**CLEAR 45/50 | Gate: passed** (C 9, L 9, E 14, A 9, R 4) | Perspectives: 3 (Prompt Engineering, AI Interpretation, End-User Experience) | Energy: Standard | Framework: COSTAR

Your original one-line instruction left the downstream AI guessing on audience level, tone, length, and structure, so output would drift. I rebuilt it with a COSTAR structure (Context, Objective, Style, Tone, Audience, Response) that pins the beginner skill level, defines the taste variables to teach, specifies two concrete methods, and locks a scannable format with a first-try recipe. The `[...]` brackets mark the one deliberately editable parameter (word count) so the prompt stays reusable.

Assumptions flagged:
- [Assumes: target model is a general-purpose text LLM (GPT-4 class or equivalent)]
- [Assumes: 800-1,200 words and an audience aged ~20-45 fit your blog; adjust the bracket or Audience line if not]
- [Assumes: French press and pour-over are the two methods you want covered]

Want me to tune this for a specific platform (WordPress, Substack), add an SEO constraint, or produce a JSON/YAML version?