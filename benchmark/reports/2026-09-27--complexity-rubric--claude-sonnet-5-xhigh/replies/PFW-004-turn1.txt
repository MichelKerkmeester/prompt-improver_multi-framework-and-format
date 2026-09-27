```markdown
Mode: $improve | Complexity: High (7/10) | Framework: COSTAR

**Context:** You are drafting a monthly newsletter for a primary school's front office to send to parents. Each month the office pastes in three inputs: the headteacher's bullet-point notes, the dates of upcoming events, and any changes to the lunch menu or bus timetable. Parents mostly read the newsletter on their phones, so long blocks of text are hard to scan. Many parents read Dutch as an additional language rather than as their first language, so wording that is idiomatic or dense causes real confusion, not just mild inconvenience.

**Objective:** Combine the three pasted inputs into one clear, cohesive monthly newsletter that keeps parents informed and reassured about what is happening at school this month.

**Style:** Write in Dutch at CEFR B1 level [Assumes: Dutch is the school's home-communication language, since the stated barrier is parents reading Dutch as an additional language]. Use short sentences (aim under 20 words), everyday vocabulary, and no idioms, jargon or education-sector acronyms. Break the body into short paragraphs of 2-3 sentences so it scans easily on a small screen.

**Tone:** Warm and welcoming, the way a trusted school speaks to families, but not chatty or casual. No exclamation marks, slang or forced enthusiasm.

**Audience:** Parents of primary school pupils, reading on mobile phones, many of whom read Dutch as an additional language.

**Response:** Produce one newsletter, structured in this order:
- A bulleted list of this month's event dates, placed first, before any other text.
- The headteacher's updates, rewritten from the bullet notes into short paragraphs grouped by topic.
- Any lunch or bus timetable changes, in their own short, clearly labelled section.
- One brief, warm closing line.

Hard limits: total length under 350 words. Never name an individual pupil; refer to a class, year group or "pupils" in general instead.

Paste this month's inputs here before sending to the AI:
- Headteacher's bullet notes: [paste here]
- Event dates: [paste here]
- Lunch/bus timetable changes: [paste here]

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [newsletter is written in Dutch at B1 level, since parents' stated barrier is Dutch as an additional language; target model is ChatGPT (GPT-4 class) as stated; monthly inputs are supplied as bracketed placeholders for reuse] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-monthly-parent-newsletter-prompt.md`

**Score and gate status:** CLEAR 42/50 | Perspectives: 5 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer, Framework Architecture Expert, Token Optimisation Specialist) | Gate passed

**Summary:** The vague one-line request became a reusable COSTAR prompt that encodes the office's actual monthly workflow (three pasted inputs, phone-first reading, B1 plain language, warm-not-chatty tone), locks in the hard constraints you named (dates list first, under 350 words, no pupil names), and parameterises the three inputs so the same prompt is reused every month. One judgment call, flagged inline: since you said many parents read Dutch as a second language rather than English, I assumed the newsletter itself is written in Dutch at B1 level — flag if the target language should instead be English.