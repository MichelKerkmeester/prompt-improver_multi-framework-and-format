Saved: `export/001 - enhanced-meeting-transcript-action-items-prompt.json`

CLEAR 44/50 | Gate: passed (C 9, L 9, E 13, A 9, R 4; all floors met) | Energy: Standard | Framework: RCAF | Perspectives: 3 (prompt engineering, AI interpretation, end-user clarity)

The one-line request is now a structured RCAF prompt. It explains why owners and due dates matter, and it takes the transcript, meeting date and an optional participant list as parameters. It tells the model to extract only real commitments and to resolve relative dates against the meeting date. It also forbids guessing missing owners or deadlines, and it returns a fixed JSON schema. Each item carries a source quote, and gaps go into an `open_questions` list.

- **Header line:** The file starts with the required one-line header (`Mode: $json | ...`), so the whole file isn't parseable as JSON. I checked that the JSON body after the header parses cleanly. Strip the first line if you feed it straight to an API.
- **Assumption:** `[Assumes: the meeting date is supplied so relative dates like "next Friday" can be resolved. Without it, those dates are kept as stated.]`
- **Token overhead:** JSON adds roughly 5-10% over Markdown.