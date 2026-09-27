Confirmed FRAME is the correct framework for `$image`. Proceeding to deliver — no clarifying question needed since the user gave complete brief, platform, aspect ratio, exclusions, and explicitly said "no questions, pick sensible parameters yourself."

Since no Canvas panel exists in this environment, the Deliverable Block is rendered as a single fenced block first, per the no-panel delivery rule.

```markdown
Mode: $image | Complexity: Low (4/10) | Framework: FRAME

**F — Focus (Subject & Composition):**
A lone gravel cyclist in a solid olive jersey rides a gravel bike directly toward camera along a raised dyke path, captured from a low angle for a dominant, heroic perspective. Coarse gravel texture fills the immediate foreground; the rider occupies the midground, positioned in the right two-thirds of the frame with the left third left calm and empty for a headline overlay. The Oosterschelde estuary stretches out in the background below the dyke, its shoreline forming a natural leading line toward the rider.

**R — Rendering (Medium & Style):**
Photorealistic photography styled like a premium outdoor-apparel catalogue campaign, shot on a 24mm wide-angle lens with f/5.6 depth of field keeping both rider and estuary sharp, natural true-to-life color rendering with editorial polish, unbranded jersey and logo-free bike frame.

**A — Atmosphere (Lighting & Mood):**
Golden hour light (roughly 3000K) low on the horizon behind the rider, casting long dramatic shadows across the dyke path, warm amber-gold color cast over the water and sky, a few softly lit clouds, calm air, serene athletic and adventurous mood.

**M — Modifiers (Technical Parameters):**
`--ar 21:9 --style raw --v 6.1 --s 100 --q 2`

**E — Exclusions (Negative Guidance):**
`--no text, logo, branding, watermark, signature, people, crowd, second rider, cars, road signage`

**Full Prompt (paste-ready):**
A lone gravel cyclist in a solid olive jersey rides a gravel bike directly toward camera along a raised dyke path, captured from a low angle for a dominant, heroic perspective. Coarse gravel texture fills the immediate foreground; the rider occupies the midground, positioned in the right two-thirds of the frame with the left third left calm and empty for a headline overlay. The Oosterschelde estuary stretches out in the background below the dyke, its shoreline forming a natural leading line toward the rider. Photorealistic photography styled like a premium outdoor-apparel catalogue campaign, shot on a 24mm wide-angle lens with f/5.6 depth of field keeping both rider and estuary sharp, natural true-to-life color rendering with editorial polish, unbranded jersey and logo-free bike frame. Golden hour light (roughly 3000K) low on the horizon behind the rider, casting long dramatic shadows across the dyke path, warm amber-gold color cast over the water and sky, a few softly lit clouds, calm air, serene athletic and adventurous mood. --ar 21:9 --style raw --v 6.1 --s 100 --q 2 --no text, logo, branding, watermark, signature, people, crowd, second rider, cars, road signage

---
Attestation: docs consulted = Image Mode, Assets - Image Mode Library, DEPTH Thinking Framework, Interactive Mode, Patterns and Evaluation, Format Guide Markdown | assumptions = [Assumes: 24mm/f5.6 as sensible catalogue-hero camera settings] [Assumes: --s 100 --q 2 balances Midjourney realism with quality] [Assumes: "no visible logos" extends to jersey and bike frame] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-zeeland-gravel-hero-midjourney.md`

**Score and gate status:** VISUAL 55/60 | Vivid 14/15, Intentional 9/10, Styled 9/10, Unambiguous 9/10, Atmospheric 9/10, Layered 5/5 | All floors met | Gate passed

**Summary:** Built as five FRAME-labeled blocks (Focus/Rendering/Atmosphere/Modifiers/Exclusions) so each element can be tweaked independently, plus a single paste-ready assembled prompt for Midjourney v6.1. Low angle, empty left-third negative space, olive jersey, Oosterschelde backdrop, golden-hour long shadows and catalogue photorealism are all explicit; `--no` handles the logo/text/people exclusions since Midjourney supports partial negatives.

**Share Your Result for Refinement**
Try this prompt in Midjourney v6.1 and share the result with me — I can help refine composition, adjust the golden-hour atmosphere, or tighten the left-third negative space if the headline area isn't clean enough.