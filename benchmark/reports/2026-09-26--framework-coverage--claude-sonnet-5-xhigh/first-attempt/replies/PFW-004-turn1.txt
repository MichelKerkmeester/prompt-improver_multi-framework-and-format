No Canvas panel is available in this session, so per the fallback rule the Deliverable Block is rendered below as a fenced block at the start of the reply, with the chat report following it.

```markdown
Mode: $improve | Complexity: 4/10 | Framework: COSTAR

**Context:** You are writing this month's parent newsletter for a primary school office. Each cycle, the office pastes three inputs: the headteacher's bullet-point notes, this month's event dates, and any lunch or bus timetable changes. Most parents read the newsletter on a phone in a few spare minutes, and many read it in a second language at an intermediate (CEFR B1) level, so plain wording and easy scanning matter more than polish.

Pasted inputs for this cycle:
- Headteacher's notes: [paste bullet notes here]
- Event dates: [paste dates and details here]
- Lunch/bus timetable changes: [paste changes here, or write "none this month"]

**Objective:** Turn the three pasted inputs above into one clear, scannable newsletter that tells parents everything they need to know this month, with event dates impossible to miss and any timetable changes stated plainly enough to act on.

**Style:** Plain B1-level wording: short sentences (under 20 words), one idea per sentence, everyday vocabulary, no idioms, acronyms or education jargon. Short paragraphs of 2-3 sentences maximum. Present the event dates and any timetable changes as bullet lists, not prose.

**Tone:** Warm and reassuring but not chatty: friendly and direct, minimal exclamation marks, no forced enthusiasm, no emoji.

**Audience:** Parents and guardians of primary school pupils, many reading in a second language at B1 level, checking the newsletter on a phone.

**Response:** One newsletter, maximum 350 words total, in this order:
1. A bulleted list of this month's event dates at the very top (date + short 3-6 word description each).
2. One short, warm opening line.
3. The headteacher's notes rewritten as 2-4 short paragraphs or bullets, grouped by topic.
4. A clearly labelled section covering any lunch or bus timetable changes: what is changing, from which date, and what (if anything) parents need to do. Write "No changes this month" if nothing was pasted.

Never name, initial or otherwise identify an individual pupil anywhere in the newsletter; refer to groups only (for example, "Year 2" or "the school choir").

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = output language follows the language of the pasted notes (B1 reading level applies regardless); "this month" = the current calendar month at time of writing | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-parent-newsletter-prompt.md`

**Score and gate status:** CLEAR 44/50 (C9·L9·E13·A9·R4) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed

**Assumptions flagged:** `[Assumes: newsletter language matches the pasted notes' language, not necessarily English]` and `[Assumes: "this month" means the current calendar month]` — both low-risk and left adjustable via the bracketed placeholders.

**Summary:** The vague one-liner is now a COSTAR-structured prompt that parameterizes the three pasted inputs, enforces B1 plain language and phone-friendly short paragraphs/bullets, locks the event-date list to the top, keeps a warm-not-chatty tone, hard-caps 350 words, and explicitly bans naming individual pupils. Reusable as-is every month — just repaste the three inputs.