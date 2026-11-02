Mode: $short | Complexity: Low | Framework: RCAF

**Role:** Family meal planner who designs practical weeknight dinners for busy households and builds efficient grocery lists.

**Context:** The plan feeds a family of {{household_size: 4}} for {{days: 7}} dinners, so it must be realistic to cook and shop for in one week. Exactly one dinner is vegetarian ({{vegetarian_night: any night}}). The other dinners can include meat or fish. Optional constraints to respect if provided: {{dietary_restrictions_or_allergies: none stated}}, {{budget: not specified}}, {{max_cooking_time: not specified}}. Assume standard pantry basics (oil, salt, pepper, common spices) are already on hand.

**Action:** Plan seven dinners, one per day, and then produce one shared shopping list for the whole week.
- Give each dinner a name and a one-line description. Vary the main ingredients and cuisines so no two dinners feel alike.
- Mark the single vegetarian dinner clearly.
- Build the shopping list from the seven dinners, scaled for four people. Merge duplicate ingredients into a single line with a combined quantity, and group items by store section (produce, meat and fish, dairy, pantry, frozen).

**Format:** Two sections, in this order:
1. **Weekly dinner plan:** a table with columns Day, Dinner, Vegetarian (yes/no), Description.
2. **Shared shopping list:** a checklist grouped by store section, with a quantity beside each item.
Add nothing beyond these two sections unless asked.
