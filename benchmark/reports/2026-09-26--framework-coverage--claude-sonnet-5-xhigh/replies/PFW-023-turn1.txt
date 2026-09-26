```markdown
Mode: $vibe | Complexity: Medium | Framework: VIBE

Build the grading screen for a warehouse returns-inspection bench: a 24-inch touchscreen an inspector uses standing up, often wearing cotton gloves, to clear roughly 300 returned fashion items a shift — about 20 seconds of decision time per item.

The default a returns tool usually becomes is a spreadsheet row-editor or a dark developer console — dense grids, tiny type, a cursor waiting on the next field. Both are wrong here: gloved hands can't land on small targets, and a near-black technical canvas turns repetitive physical work into screen fatigue by item 200. Instead, think of a photo lightbox on a film-inspection bench — a warm, neutral daylight surface built for holding two images against each other and making one confident call.

Layout: the scanned item's photo sits beside the original order photo, large enough to compare at arm's length, with the customer's return reason resting between them like a caption card, never competing for attention. Below, four grade targets — A, B, C, Reject — are sized and spaced for a gloved thumb, each pressing like a weighted rubber stamp rather than a flat website button: a firm, satisfying give that confirms the choice before the next item loads. Choosing Reject opens one calm step asking for a single damage photo — a deliberate pause, not a form or an alarm.

The rhythm should feel like a diamond grader's steady cadence: quick, wordless, repeatable, never rushed and never sluggish, so item 300 feels as clear-headed as item one. Controls keep a visible focus outline for scanner or backup-keyboard input, text holds up under harsh warehouse fluorescents, and every micro-motion can be switched off without losing information. Build with shadcn/ui components, customized past their off-the-shelf look so no surface reads as an unstyled kit.

---
Attestation: docs consulted = [Visual Mode, Assets - Visual Mode Library, Patterns and Evaluation, DEPTH Thinking Framework, Interactive Mode, Format Guide Markdown] | assumptions = [item photo capture already happens at the scan step, so this screen receives both images pre-loaded; no additional review/undo screens beyond the grading step and the reject damage-photo step] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-returns-inspection-vibe-brief.md`

**Score and gate status:** EVOKE ~45/50 (Evocative 13/15, Visual 9/10, Open 8/10, Kinetic 9/10, Emotional 5/5) | Grounding pre-check: passed (subject, audience, single job, anti-default all named) | Threshold 40+: passed | Perspectives: 5 applied (Vision, Inspiration, Behavior, Experience, Grounding)

**Summary:** This brief grounds the screen in your bench, gloves and 20-second cadence, names the two defaults you flagged (spreadsheet, dark dev tool) and deviates toward a film-lightbox metaphor instead. All four states you specified survive intact: order-photo-vs-item comparison, visible return reason, four large grade targets, and the reject → single damage-photo step. shadcn/ui is baked in as the component library, explicitly customized so it won't read as a default kit.

**Assumptions flagged:** item and order photos arrive already loaded when this screen opens (capture happens upstream at scan); no extra confirmation or undo screens were added beyond what you described.

---
**Share Your Result for Refinement**

Try this prompt in v0 and share what it generates — screenshot or description both work. I can help refine the tactile/rhythm direction, adjust the lightbox metaphor if v0 leans too literal or too sterile, or dial in the reject-flow pacing if it comes out feeling like a form instead of a pause.