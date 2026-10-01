```markdown
Mode: $short | Complexity: Low (3/10) | Framework: COSTAR

---

**Context:** [Company] is announcing on LinkedIn that Priya Nair is joining as Head of Design, starting 14 October, and that she joins the team from Spotify. Those four details — name, title, start date and previous company — are the only confirmed facts; nothing else about her background, career history or the hiring process is available.

**Objective:** Write one LinkedIn post that announces Priya's arrival and leaves readers with the sense that the team is genuinely glad she is coming — a warm, human update, not a company statement.

**Style:** Plain, everyday language. Short sentences and short paragraphs. Write the way a colleague shares good news with people they already know.

**Tone:** Warm and personal, and not corporate. Avoid phrasing such as "pleased to announce", "thrilled to welcome", "strategic addition to our leadership team" and "we look forward to the expertise she brings". Contractions are fine, and so is a little first-person warmth from the team ("we").

**Audience:** Professional readers scrolling their LinkedIn feed — peers, candidates and people who follow the company.

**Response:** One complete, publish-ready post. Include Priya's name, her Head of Design title, her 14 October start date and that she joins from Spotify. Use only the details given — do not invent anything beyond those four facts, including further biography, other employers, achievements or quotes.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [company name not supplied → placeholder; post length, hashtags and links not specified → left to the downstream model; single post on the company page] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-linkedin-hire-announcement-priya-nair.md` — same revision slot, updated; this Project still cannot write files, so the block above stands in for the saved export.

**Score and gate status:** CLEAR 44/50 | Perspectives: 3 | Floors met (C 9, L 9, E 13, A 9, R 4) | Gate passed | Complexity unchanged at Low (3/10)

**Token overhead:** Markdown baseline, no overhead added.

**Summary:** Spotify is now the fourth confirmed fact, so it went into both the Context and the Response line that tells the downstream model what must appear in the post. The anti-fabrication guard was widened from three facts to four, which keeps the new detail from becoming a licence to invent a career timeline. No structural change was needed.

**Assumptions worth confirming:** the company name (still `[Company]`), company page versus personal profile, and whether length, hashtags and links stay open. Say the word and I will lock any of them in.