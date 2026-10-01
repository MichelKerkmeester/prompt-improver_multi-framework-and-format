## Deliverable

**Canvas Artifact — Deliverable Block** (`export/[###] - enhanced-coffee-brewing-beginners-blog-post.md`)

```markdown
Mode: $improve | Complexity: Low (2/10) | Framework: COSTAR

---

**Context:** A blog post for people who have never brewed coffee beyond a drip machine or instant. They don't yet know equipment names, grind sizes, ratios or water temperature, so unexplained jargon or assumed gear loses them immediately. Purpose: give a beginner enough understanding, plus one repeatable recipe, to brew a cup they enjoy and know why it worked.

**Objective:** Write a blog post titled "Coffee Brewing for Beginners" that moves a reader from zero brewing knowledge to one good, repeatable cup, and leaves them able to name the variables that change how coffee tastes.

**Audience:** Complete beginners. No specialty coffee background, likely owning a kettle, a mug and at most one simple brewer; some may only have a drip machine. Assume no scale, no thermometer and no grinder unless the post explains how to manage without one.

**Style and Tone:** Plain, encouraging, concrete. Short sentences. Define every term (bloom, extraction, ratio, grind size) in-line the first time it appears. No gatekeeping, no gear snobbery.

**Response:** Markdown blog post containing:
- A working title plus two alternates
- Opening (2-3 sentences) stating what the reader will be able to do after reading
- A "start here" section naming one recommended beginner method and why it is the first choice
- Numbered step-by-step brew instructions with quantities, water temperature and timing
- A short explainer of the four variables that change taste (grind, coffee-to-water ratio, water temperature, brew time), each with one concrete adjustment direction
- "Common beginner mistakes" with the fix for each
- Closing section on what to try next
- Length: [1,200-1,500] words [adjust to your target]
- Every instruction executable with a kitchen scale or a measuring spoon; mark any step that needs equipment a beginner may not own

**Constraints:**
- Recommend only methods and gear that are inexpensive or commonly already owned
- State the common case and one alternative wherever gear, beans or water differ by region
- Use generic descriptions rather than invented brand rankings, prices or product claims
- Keep any caffeine or health statement factual, general and non-medical, with a note to consult a professional where relevant
- If a detail is genuinely unknown to you, use the bracketed default and flag it rather than guessing

**Success Criteria:** A reader with no brewing background can follow the post start to finish without looking anything else up and produce a drinkable cup, and can repeat it because quantities and timings are explicit.

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown | assumptions = [Assumes: audience = complete beginners with no specialty coffee gear] [Assumes: publication = general-interest blog with no SEO, brand or editorial house-style constraints] | format = Markdown | execution = did not occur | save = did not occur
```

---

**Export-equivalent path:** `export/[###] - enhanced-coffee-brewing-beginners-blog-post.md` — this Project cannot write to disk, so the Artifact above is the deliverable and the path is what the CLI runtime would produce.

**Score and gate:** CLEAR 44/50 (C 9, L 9, E 13, A 9, R 4 — all floors met) | Perspectives: 5 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture, Token Optimisation) | Gate passed | Format: Markdown baseline, no token overhead.

**Framework choice:** COSTAR over the RCAF default — the request is audience-specific content creation (94% fit in the framework matrix), and the Style/Tone/Audience fields are exactly where the original prompt was silent.

**Assumptions flagged:** audience is complete beginners, and the destination is a general-interest blog with no SEO or house-style constraints. Both are marked as open in the chat summary; tell me the real context and I'll re-cut them.

**What changed and why:** The original named a topic but not the reader's starting point, the post's job, or how the output would be judged usable. The enhanced prompt fixes those three gaps, then flips the conventional "explain everything about coffee" instinct into "get the reader to one repeatable cup", since comprehensiveness is what makes beginner guides unreadable. The counter-argument (over-specifying a writing task) is handled by bracketing the choices that belong to you — word count, brand and region specifics — so the downstream model fills format gaps but never invents facts.

One note on scope: I held to what you asked for and did not add sections (buying guides, equipment reviews, SEO structure). If you want any of those, say so and I'll add them as a new pass.