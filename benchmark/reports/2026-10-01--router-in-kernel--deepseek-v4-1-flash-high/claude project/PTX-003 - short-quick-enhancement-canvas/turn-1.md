```markdown
Mode: $short | Complexity: Low (3/10) | Framework: COSTAR

---

**Context:** [Company] is announcing on LinkedIn that Priya Nair is joining as Head of Design, starting 14 October. The only confirmed details are her name, her title and her start date — nothing else about her background, previous roles or the hiring process is available.

**Objective:** Write one LinkedIn post that announces Priya's arrival and leaves readers with the sense that the team is genuinely glad she is coming — a warm, human update, not a company statement.

**Style:** Plain, everyday language. Short sentences and short paragraphs. Write the way a colleague shares good news with people they already know.

**Tone:** Warm and personal, and not corporate. Avoid phrasing such as "pleased to announce", "thrilled to welcome", "strategic addition to our leadership team" and "we look forward to the expertise she brings". Contractions are fine, and so is a little first-person warmth from the team ("we").

**Audience:** Professional readers scrolling their LinkedIn feed — peers, candidates and people who follow the company.

**Response:** One complete, publish-ready post. Include Priya's name, her Head of Design title and her 14 October start date. Use only the details given — do not invent anything about her beyond those three facts, including previous employers, biography or quotes.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [company name not supplied → placeholder; post length, hashtags and links not specified → left to the downstream model; single post on the company page] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-linkedin-hire-announcement-priya-nair.md` — this Project cannot write files, so the block above stands in for the saved export; the `sk-prompt-improver/` CLI performs the actual write.

**Score and gate status:** CLEAR 44/50 | Perspectives: 3 (Prompt Engineering Expert, AI Interpretation Specialist, End-User Experience Designer) | Floors met (C 9, L 9, E 13, A 9, R 4) | Gate passed

**Token overhead:** Markdown baseline, no overhead added (JSON or YAML would add roughly +5-10% or +3-7%).

**Summary:** Your brief already carried the essentials — what to announce, who, when and the tone — so this was a Quick-energy pass: RFC-style framing replaced with COSTAR, since audience and tone carry the weight here. The one real gap was that "not corporate" is a feeling, not an instruction, so the prompt names a few phrases the post must avoid and says which three facts are the only usable material. That last line is a guard against fabricated biography, not an extra section.

**Assumptions worth confirming:** the company name (left as `[Company]`), that this runs on the company page rather than a personal profile, and that length, hashtags and links are yours to decide. Tell me any of those and I will lock them into the prompt.