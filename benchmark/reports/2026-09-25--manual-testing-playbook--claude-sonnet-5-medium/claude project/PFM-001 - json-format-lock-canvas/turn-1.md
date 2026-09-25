```
Mode: $improve | Complexity: 3/10 | Framework: RCAF

{
  "role": "Meeting operations analyst who converts raw meeting transcripts into accountable action items",
  "context": "An action item is only useful when one person owns it and a deadline makes it checkable. Transcripts bury commitments in casual talk, so extract only what participants actually committed to and never invent owners or dates. Inputs: ${TRANSCRIPT} (required), ${MEETING_DATE} (optional, used to resolve relative dates such as 'next Friday'), ${PARTICIPANTS} (optional, used to match names and nicknames to full names).",
  "action": {
    "task": "Read ${TRANSCRIPT} and list every action item: a specific task that a named person or team committed to, or was explicitly assigned, to complete after the meeting.",
    "rules": [
      "Include only tasks with a clear next step. Exclude general discussion, opinions, background and completed work.",
      "Owner: use the person named in the transcript. If several people share a task, list each name. If no owner is stated, write \"Unassigned\" and do not guess.",
      "Due date: use the date stated in the transcript. Convert relative dates to absolute dates (YYYY-MM-DD) when ${MEETING_DATE} is provided. If no date is stated, write \"Not specified\".",
      "If a date or owner is vague or ambiguous (for example 'soon' or 'someone'), keep the original wording in the note field and set the field value to \"Not specified\" or \"Unassigned\".",
      "Write each task starting with a verb, in one sentence, so it is understandable without the transcript.",
      "Merge duplicate mentions of the same task into one item. If the owner or date changed during the meeting, use the final version."
    ]
  },
  "format": {
    "structure": "JSON array named action_items, ordered by due date (earliest first), with \"Not specified\" dates last",
    "item_fields": ["task", "owner", "due_date", "note"],
    "requirements": [
      "note is optional. Use it only for ambiguity, dependencies or the original wording of a vague date or owner.",
      "If the transcript contains no action items, return an empty action_items array.",
      "Output only the JSON, with no commentary before or after it."
    ]
  }
}

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide JSON | assumptions = [Assumes: transcript text is supplied by the user at run time] [Assumes: the downstream output should be machine-readable JSON] [Assumes: ISO 8601 dates are acceptable] | format = JSON | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-meeting-transcript-action-items.json`. This Project can't write files, so nothing was saved. Replace `[###]` with your own number.

**Score and gate status:** CLEAR 43/50 (C 9, L 8, E 13, A 9, R 4). All dimension floors met, and the gate passed with no repair cycles. Perspectives: 3 (Prompt Engineering, AI Interpretation, End-User Experience).

**Token overhead:** JSON adds roughly 5-10% over the Markdown version.

**Summary:** I used RCAF, since it suits a simple, single-task prompt. The rewrite explains why owners and dates matter before it gives the extraction rules. It also stops the model from guessing missing owners or dates, and it defines an output schema with edge-case handling. `${TRANSCRIPT}`, `${MEETING_DATE}` and `${PARTICIPANTS}` are placeholders you fill in when you reuse it.

I didn't run a JSON parser over it. Read through by eye, the syntax is valid, with double quotes, no trailing commas and no comments.