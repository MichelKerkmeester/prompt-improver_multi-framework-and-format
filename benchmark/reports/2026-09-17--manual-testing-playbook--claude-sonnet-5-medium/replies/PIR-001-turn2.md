<DELIVERABLE>
```markdown
Mode: $short | Complexity: 2/7 | Framework: RCAF | Score: CLEAR 44/50

Act as a meal-planning assistant. Create a 7-day dinner plan for a family of four, including exactly one vegetarian night, plus one consolidated shopping list.

For each of the 7 dinners, include:
- Dish name
- 1-line description
- Total prep + cook time
- Key ingredients

Then generate a single shopping list that:
- Combines ingredients across all 7 dinners (no duplicates)
- Is organized by grocery category (produce, protein, dairy, pantry, etc.)
- Has quantities scaled for 4 servings per dinner

Flag the vegetarian night clearly and note any substitution used in place of meat.

Output as Markdown: a table for the 7-night plan, followed by a bulleted shopping list by category.

---
Attestation: docs consulted = patterns-evaluation, framework-pattern-library, format-guide-markdown | assumptions = "family of four" = standard adult portions, no allergies/budget specified | format = Markdown | execution = did not occur | save = did not occur
```
</DELIVERABLE>

**Export-equivalent path:** `export/001 - enhanced-weekly-meal-plan-generator.md`
**Score:** CLEAR 44/50 | Gate passed
**Assumptions:** No dietary restrictions, budget, or cuisine preference stated — added standard portion sizing and left substitutions open-ended. Flag if any of those need locking in.

Want me to run a Deep pass on this instead, to add things like weekly variety rules, leftover/pantry logic, or a budget cap?