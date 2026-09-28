Saved: `export/002 - enhanced-meeting-transcript-action-items-pm-prompt.json`

CLEAR 45/50 | Gate: passed (C 9, L 9, E 13, A 10, R 4) | Mode: $improve | Energy: Standard | Framework: RCAF

This revision reframes the prompt so the extracted action items are written for a project manager to track and follow up on, and tightens the output rules to demand strictly valid JSON (no trailing commas, comments or non-JSON text). The core scope — tasks with owners and due dates — is unchanged. [Assumes: no extra fields such as priority or status are wanted; say the word and I'll add them.]