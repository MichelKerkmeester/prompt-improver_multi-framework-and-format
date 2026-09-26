```markdown
Mode: $image | Complexity: 7/10 | Framework: FRAME

Prompt:
Flat 1960s screen-print poster illustration for Leiden's Night of Science at the city library, 2:3 vertical portrait format. Three-layer depth composition: (foreground: two children around eight to ten years old peering excitedly through a large brass telescope on a tripod:1.3), non-photorealistic flat-illustrated figures with simplified rounded features, clean confident linework, and no photoreal skin or rendering; (midground: the library's red-brick facade with a row of warm lit windows:1.2); (background: the constellation Orion rising low over distant rooftops:1.1). The top quarter of the poster is flat, empty negative-space sky reserved for a title, with no lettering, words, or typography anywhere in the image. Strictly limited four-colour palette using only (#1B2A49 deep navy:1.2), (#F2C14E mustard yellow:1.2), (#E4572E vermilion orange:1.2), and #F4F1E8 warm paper cream as the base tone. Bold flat colour blocks with no gradients or blending, coarse halftone dot shading, visible paper grain texture across the full image, slight ink misregistration offsetting the colour layers, mid-century Dutch travel-poster graphic design, hand-pulled silkscreen print aesthetic, symmetrical centred poster composition, high-contrast flat shapes.

Negative:
text, lettering, typography, words, letters, numbers, title, caption, subtitle, watermark, signature, logo, stamp, UI elements, border, frame, photorealistic, photograph, realistic skin texture, 3D render, CGI, hyperrealism, smooth airbrushed shading, soft photographic lighting, gradient sky, gradient shading, painterly blending, adult facial proportions on children, elderly or teenage features, colors outside the four-colour palette, neon colors, pastel colors, sepia, greyscale, black and white, low quality, blurry, jpeg artifacts, extra limbs, deformed hands, extra fingers, fused fingers, bad anatomy, disfigured, asymmetrical eyes, cluttered composition, modern cars, contemporary architecture, glossy digital illustration, vector clip-art look, anime style, chibi style, cartoon mascot style, cropped, out of frame

Technical Parameters:
- Resolution: 1024×1536 (native SDXL 2:3 bucket)
- Sampler: DPM++ 2M Karras
- Steps: 32
- CFG Scale: 7 (keep in the 6.5–7.5 band; SDXL tends to blow flat colour blocks into oversaturation or drift outside the four-colour palette above ~8)
- Denoise: 1.0 (txt2img)

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Image Mode, Assets - Image Mode Library, Patterns and Evaluation, Format Guide Markdown | assumptions = [Assumes: 2:3 rendered at 1024×1536, the standard SDXL-native bucket]; [Assumes: base SDXL checkpoint with no specialised poster/illustration LoRA, so CFG/steps may need a small adjustment per checkpoint] | format = Markdown | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-night-of-science-poster.md`

**Score and gate status:** VISUAL 56/60 (threshold 48+) | Vivid 14/15, Intentional 9/10, Styled 10/10, Unambiguous 9/10, Atmospheric 9/10, Layered 5/5 | Perspectives: 5 (Focus, Rendering, Atmosphere, Modifiers, Exclusions) | Gate passed

**Summary:** Built with FRAME for SDXL/ComfyUI: the three depth layers, exact four-colour hex palette, non-photoreal 8-10-year-old children, empty top-quarter sky with a hard no-lettering constraint, and the paper-grain/ink-misregistration texture are all carried through with SD weighted syntax on the highest-priority elements. Since ComfyUI's negative field is fully supported on SDXL, exclusions (text, photorealism, off-palette colors, anatomy errors) sit in a dedicated negative prompt rather than positive rephrasing. CFG and steps are tuned to hold the strict flat palette without SDXL's typical oversaturation at higher guidance.

**Share Your Result for Refinement**

Try this prompt in ComfyUI and share the result with me!
- **Refine the prompt** if the palette drifts, the children read too photoreal, or the depth layers flatten together
- **Adjust the direction** if the screen-print texture (grain, misregistration) is too subtle or too strong
- **Dial in specifics** like telescope placement, window count, or Orion's position if the AI interpreted them differently

Just share the result and tell me what you'd like to change.