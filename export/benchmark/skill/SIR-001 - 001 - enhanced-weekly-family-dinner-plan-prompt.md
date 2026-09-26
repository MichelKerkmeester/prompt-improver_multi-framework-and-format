Mode: $short | Complexity: Low | Framework: RCAF

**Role:** Family meal planner who plans practical weeknight dinners and builds efficient grocery lists.

**Context:** A family of four needs seven dinners for one week, planned so they can shop once from one shared list. Exactly one of the seven dinners is vegetarian, on {{vegetarian_night: any night}}. The other dinners can include meat or fish. Assume standard pantry basics (oil, salt, pepper, common spices) are already on hand. Respect these optional constraints when they are filled in, and ignore any left as "none": {{dietary_restrictions_or_allergies: none}}, {{budget: none}}, {{max_cooking_time: none}}.

**Action:**
1. Plan seven dinners, one per day, and give each a clear dish name. Vary the main ingredients and cuisines so no two dinners feel alike.
2. Make exactly one dinner vegetarian and mark it.
3. Build one shared shopping list from all seven dinners, with quantities for four people. Merge repeated ingredients into one line with the combined quantity, and group items by store section (produce, meat and fish, dairy, pantry, frozen).
4. Before returning, check that there are seven dinners, exactly one is vegetarian, every ingredient the dinners need (apart from pantry basics) is on the list and no item appears twice.

**Format:** Two sections, in this order, and nothing else:
1. **Weekly dinner plan:** a table with the columns Day, Dinner and Vegetarian (yes/no).
2. **Shared shopping list:** a checklist grouped by store section, with a quantity beside each item.
