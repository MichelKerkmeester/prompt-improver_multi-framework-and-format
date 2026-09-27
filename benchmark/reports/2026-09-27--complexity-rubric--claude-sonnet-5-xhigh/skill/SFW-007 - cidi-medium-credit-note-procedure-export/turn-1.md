The YAML body (everything below the single-line header, per the format guide's own convention) parses cleanly and matches the intended CIDI structure. File is verified and saved.

**Saved:** `export/001 - enhanced-ap-credit-note-sop-prompt.yaml`
**CLEAR: 46/50** | Gate: passed (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4)

I structured this with **CIDI** (Context, Instructions, Details, Input) since it's the framework built for process documentation/tutorials — a strong fit for transcript-to-SOP work. The prompt locks in your four hard requirements (one action + screen/field + result per step, verbatim field names, EUR 5,000 approval flag, no chit-chat) as explicit instructions/details rather than loose suggestions, and turns "no questions, just judgment" into a standing rule telling the model to resolve ambiguity from the transcript itself instead of stalling. The `input.transcript` field is a clear paste-in slot so the prompt is reusable run after run.