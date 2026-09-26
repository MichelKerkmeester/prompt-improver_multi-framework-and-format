Mode: $image | Complexity: High (7/10) | Framework: FRAME

**Positive Prompt:**
Flat 1960s screen-print poster illustration for Night of Science at Leiden city library, 2:3 portrait format, (three-layer depth composition:1.3). Foreground: two children about 8 to 10 years old at a tall brass telescope on a tripod, one looking through the eyepiece and one pointing up at the sky, bold flat silhouetted shapes, (non-photoreal stylized children:1.3), simplified mid-century illustration style, not realistic faces. Midground: the library's brick facade rising behind them, rows of tall arched windows glowing warm mustard and vermilion against flat navy brick shadow. Background: (Orion rising above the rooftops:1.2), drawn as a simple flat constellation of dots and connecting lines in mustard against a deep navy night sky. (Top quarter of the composition left as empty flat navy sky, pure negative space, no text or lettering anywhere:1.4), reserved for a title to be added later.

(Flat 1960s silkscreen poster art style:1.4), bold graphic shapes, hard flat color edges, no gradients, no soft airbrush shading, mid-century science-outreach poster aesthetic. Strict four-color palette only: navy #1B2A49, mustard #F2C14E, vermilion #E4572E, and paper #F4F1E8 as the base tone. (Visible paper grain texture across the whole print:1.2), (slight ink misregistration between color layers:1.3) with each color plate offset by a hair for an authentic hand-pulled screen-print look. Quiet, curious nocturnal mood, warm window glow contrasting the cool night sky, sense of wonder toward the stars. masterpiece, best quality.

**Negative Prompt:**
lettering, text, typography, numbers, words, title, caption, logo, watermark, signature, photorealistic, photograph, photo, 3D render, CGI, realistic skin texture, realistic human faces, adult faces on children, gradient shading, soft airbrush blending, glossy finish, clean unprinted vector look, perfectly registered flat color, extra colors, additional hues outside the four-color palette, sepia, full color photograph, blurry, low quality, jpeg artifacts, bad anatomy, extra limbs, deformed hands, cropped, out of frame, modern cars, smartphones, contemporary clothing, cartoon chibi style, anime style, cluttered dense starfield obscuring Orion

**Technical Parameters:**
- Aspect ratio: 2:3 portrait. Generate the base pass at 832x1216 (native SDXL bucket closest to 2:3) then hires-fix/upscale to 1024x1536 for a true 2:3 print file.
- CFG Scale: 7 (range 6-8; higher pushes flatter, more graphic color separation; lower risks drift toward painterly blending)
- Steps: 32 (range 28-36)
- Sampler: DPM++ 2M Karras (clean flat edges, stable at moderate step counts)
- Weight range used: 1.2-1.4 on style, texture and negative-space terms; telescope/children phrasing left unweighted so SDXL doesn't over-fixate on one figure

---
Attestation: docs consulted = [Image Mode, Image Mode Library, Patterns and Evaluation, Format Guide Markdown] | assumptions = [Assumes: an SDXL 1.0-class checkpoint running in a standard ComfyUI KSampler node; Assumes: paper #F4F1E8 functions as both an ink and the visible background substrate; Assumes: no fixed reference sheet is needed for the two children since they're generic, not recurring named characters] | format = Markdown | execution = did not occur | save = did not occur
