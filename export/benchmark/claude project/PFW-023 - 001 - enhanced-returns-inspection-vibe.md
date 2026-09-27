Mode: $vibe | Complexity: High (7/10) | Framework: VIBE

Design the grading screen for a fashion e-commerce returns-inspection bench: a 24-inch touchscreen kiosk where a gloved inspector clears roughly 300 returned garments a shift, each judged in about twenty seconds. This is a repeated ritual, not a browsing session — think the unfussy confidence of a boarding-gate scanner crossed with the tactile satisfaction of a photo booth's countdown, not a spreadsheet and not a dark developer console.

Layout: once an item is scanned, the screen resolves into two anchored halves that never compete for attention — the customer's original order photo sits beside the live item, close enough that the eye travels between them in a single glance, with the return reason sitting quietly between the two like a caption, present but never shouting. Beneath that pairing, four confident zones span the width within easy reach of a gloved thumb: three grade tiles — A, B, C — sized and spaced for a fingertip in cotton, sharing one calm, related color family so no grade reads as a failure, and a visually distinct reject zone that breaks from that family just enough to register as a different kind of decision, not a punishment.

When reject is chosen, the screen shifts into a focused capture moment: a single damage-photo prompt takes the stage, unhurried, framed like a deliberate pause rather than an error state, then returns the inspector to the next item.

Motion should feel snappy but never anxious — a tap fills and settles immediately, confirming itself before the next item is already loading, so trust builds tap after tap rather than eroding by item 300. Avoid the generic AI-default clusters entirely: no near-black-plus-acid-accent developer-tool palette, no dense card-grid dashboard, no untouched off-the-shelf component surface. Instead, warm neutral surfaces, generous single-glance zones, and typography that reads instantly under warehouse lighting carry the calm. The kind of screen that still feels steady and unhurried at item 300, because it absorbs the pace instead of adding to it.

Use shadcn/ui components (https://ui.shadcn.com/docs/components) for all UI elements, customized rather than left in their default state, to keep the output accessible and production-consistent.

Layout must adapt across viewport widths, every interactive element needs a visible high-contrast focus indicator, motion respects `prefers-reduced-motion`, and text meets WCAG AA contrast against its background.

---
Attestation: docs consulted = Visual Mode, Visual Mode Library, DEPTH Framework, Interactive Mode, Patterns and Evaluation, Format Guide Markdown | assumptions = component library confirmed inline as shadcn/ui, target platform read as v0.dev from "for v0", 24-inch touchscreen treated as fixed device context | format = Markdown | execution = did not occur | save = did not occur
