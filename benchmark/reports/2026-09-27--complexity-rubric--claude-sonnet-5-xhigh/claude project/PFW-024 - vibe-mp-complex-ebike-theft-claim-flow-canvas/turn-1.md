```markdown
Mode: $vibe | Complexity: High (7/10) | Framework: VIBE-MP

Design a five-screen theft-claim intake flow for a commuter e-bike insurance app — built for the few minutes right after someone finds an empty rack where their e-bike used to be. She's on her phone, upset, adrenaline still up. The flow has one job: a complete, insurable claim filed in under five minutes, without ever making her repeat herself.

Screen one holds only what happened, nothing else competing for attention. Screen two carries her into where and when, the station already filled in because the app already knows where she's standing — she confirms rather than types. Screen three gathers photos and the frame number as evidence, not paperwork. Screen four asks for the police report number but never blocks on it: a clear "add this later" path lets her keep moving. Screen five lands on a confirmation that reads less like a finish line and more like a handover — a live tracker showing the claim already moving through the system on its own.

Every screen carries her answers backward as easily as forward: the back link never resets a field, and a dropped signal never erases a character — the draft holds until she's reconnected. Progress reads like a case file being assembled, not a game — a quiet numbered rail, never a bouncy meter. Steer hard away from the badge-and-confetti energy of Duolingo-style flows, and equally away from the purple-to-blue gradient fintech-onboarding look; this sits closer to a well-run intake desk than a growth-stage app launch.

Keep the palette low and steady — graphite, slate, paper-white — with one restrained accent reserved only for confirmed actions and the live tracker. Typography reads like a form built by someone competent, not a brand. As the one deliberate risk: let that numbered progress rail carry evidentiary weight, like a case log, instead of the rounded gamified stepper this category defaults to.

Fields settle in without ceremony — a resolved location, a locked-in photo — and moving between screens feels like turning a page, not swiping a carousel. The flow speaks Dutch and English natively, not as a bolted-on toggle. Every screen holds up across phone widths and in daylight glare, with unmistakable touch targets, visible focus states, and no motion she didn't ask for.

No component library — let MagicPath choose its own materials.

---
Attestation: docs consulted = Visual Mode, Visual Mode Library, DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Format Guide Markdown | assumptions = [Assumes: mobile-only, phone-first flow, no tablet/desktop variant needed] · [Assumes: Dutch/English is native dual-language support, not a user-facing toggle] · [Assumes: no existing brand palette supplied, so "steady, not fintech" is interpreted as low-saturation graphite/slate with one restrained accent] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-ebike-theft-claim-magicpath-brief.md`

**Score and gate status:** EVOKE-MP 46/50 (Evocative 11/12, Visual 11/12, Open 7/8, Kinetic 12/13, Emotional 5/5) | Grounding pre-check: passed (subject, audience, single job, anti-default all named) | K+V 23/25 | Gate passed at 42+/50 threshold | Perspectives: 5 (Vision, Inspiration, Behavior, Experience, Anti-Default/Grounding)

**Brief summary:** The brief grounds the flow in a commuter filing a theft claim under time and emotional pressure, names and deviates from two recognizable defaults (gamified Duolingo-style progression, gradient fintech onboarding), and carries all five screens plus the no-data-loss, offline-draft and bilingual requirements as narrative rather than a spec list. A single justified aesthetic risk — a case-file-style progress rail instead of a rounded stepper — anchors the "steady, competent" tone throughout.

**Share your result for refinement:** Try this in MagicPath and share what it generates — screenshot or description both work. I can help dial in the progress-rail treatment, the accent color's restraint, or the screen-to-screen transition feel if the output drifts toward either the gamified or the gradient-fintech default this brief steers away from.