Mode: $vibe | Complexity: Medium (6/10) | Framework: VIBE

---

Create a daily-bakery operations screen for the owner of a small three-shop bakery chain that feels like a warm, quiet start to the day — closer to a baker's morning prep sheet than a corporate analytics tool.

She opens it on an iPad at six in the morning, standing in a dim shop before the ovens are on. Within a minute she needs to know four things: how yesterday's waste looks per shop, what today's sales are tracking at, which ingredients are running low, and how many pre-orders are waiting for tomorrow. The job is to decide what to act on before she unlocks the doors.

Layout: one calm sheet, not a wall of tiles. The three shops read as three gently separated banks, each keeping its own daily story, so her eye can move shop-by-shop or compare the same measure across shops. Yesterday's waste sits closest to the top — it is the lesson from yesterday — with today's sales, low stock, and tomorrow's pre-orders settling beneath it in that order of morning urgency. Numerals feel like hand-kept figures on a well-worn ledger: large enough to read at arm's length, quiet enough not to shout.

The interface speaks in soft, rounded, kitchen-warm typography — friendly and unhurried, never clinical or condensed. Colors: floured parchment and unbaked-dough neutrals, with one warm accent (toasted, not electric) reserved for what genuinely needs her attention today. Low stock reads as a gentle nudge, an ingredient quietly asking to be reordered, not a red alarm.

Interactions feel slow and reassuring — the way the shop feels before it opens. Moving between shops and days feels like turning a page, and states settle with a small, unhurried ease. Tapping a shop feels like stepping into that shop.

Constraints: designed for a large iPad held in one hand at a glance; all four views must be readable without drilling in; the whole screen stays legible in early-morning low light.

Steer away from the SaaS analytics default — no gradient hero, no card-grid KPI wall, no dashboard chrome. Also steer away from the artisan-bakery brand cliché of cream plus serif plus terracotta; this is a working tool, worn and used, not a packaging mood board.

Single aesthetic risk: treat yesterday's waste as a small, honest daily note the owner would fold into her apron pocket, rather than a chart trying to look important.

Use shadcn/ui components (https://ui.shadcn.com/docs/components) for all UI elements, customized so no surface reads as an untouched library default.

Must remain responsive across iPad orientations, give every interactive element a visible keyboard focus state, respect prefers-reduced-motion, and meet WCAG AA contrast against the warm neutral background.
