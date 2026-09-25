Saved: `export/002 - enhanced-meeting-transcript-action-items-pm-prompt.json`

CLEAR 45/50 | Gate: passed (C 9, L 9, E 14, A 9, R 4; all floors met) | Energy: Standard | Framework: RCAF

The whole file now parses as JSON. I checked it with a parser. I dropped the one-line `Mode: $json ...` header from the earlier version, which overrides the format guide's header rule at your request. The prompt now targets a project manager who tracks delivery. It asks for tracker-ready items, with optional priority and dependencies, a `risks_and_blockers` list, and an optional `project_name` input. The rules against guessing owners or due dates and the verbatim source quotes are unchanged. Version 001 is still in `export/` for comparison.

- **Assumption:** `[Assumes: priority, dependencies and risks are recorded only when the transcript states them. I added these fields because a project manager would track them, so tell me if you want them removed.]`
- **Token overhead:** It's about 10% longer than the 001 version because of the added fields.