```markdown
Mode: $short | Complexity: Low (3/10) | Framework: RCAF

---

**Role:** You are a practical home meal planner who builds realistic dinners for households with mixed diets.

**Context:** The household has four people. Seven dinners will be cooked at home across seven consecutive days. Exactly one of those dinners must be fully vegetarian. All ingredients for the week are bought in one shop and come from a single shared list.

**Action:** Plan seven dinners, one for each day of the week, each serving four people, with exactly one dinner fully vegetarian. State which day the vegetarian dinner falls on. Then build one shared shopping list that covers all seven dinners, so that no ingredient appears twice and nothing is missed.

**Format:**
- Seven dinners, Monday through Sunday, each as one line: day, dish name, main ingredients.
- One "Shopping List" section covering all seven dinners, grouped by store section (produce, protein, dairy, pantry, other), with item and quantity for a four-person household per line.
- Dinners and short ingredient notes only. No full recipes, no cooking instructions, no per-day shopping lists.

---
Attestation: docs consulted = [DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Framework Pattern Library, Format Guide Markdown] | assumptions = [format defaulted to Markdown, no format command given; vegetarian night day left to the model to assign and state; dinners are home-cooked and shop bought in one weekly trip; quantities scaled to four servings] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-weekly-meal-plan-generator-prompt.md`

**Score and gate status:** CLEAR 44/50 (Correctness 9, Logic 9, Expression 13, Arrangement 9, Reusability 4) | Perspectives: 2 (Prompt Engineering Expert, AI Interpretation Specialist) | Gate passed (threshold 40+, all floors met)

**Summary:** Your one-line request is now an RCAF prompt that keeps exactly what you asked for — seven dinners, four people, one vegetarian night, one shared list — and fixes the two gaps that made the original ambiguous: who the dinners are for in quantity terms, and how the shopping list relates to the dinners (one consolidated list, not seven separate ones). Quick energy meant no new sections were added, so the output stays lean.

Mode conflict resolved as `$short` per your confirmation. Want me to run a `$deep` pass on the same prompt, or extend it with dietary or budget constraints?