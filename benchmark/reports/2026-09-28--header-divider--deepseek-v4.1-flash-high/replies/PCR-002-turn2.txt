```
Mode: $video $yaml | Complexity: Low (2/10) | Framework: MOTION

---

prompt_meta:
  target_platform: Veo 3.1+
  duration_seconds: 6
  clip_note: single continuous 6-second take, one location, no cuts
  framework: MOTION
  scoring: VISUAL (70)

movement:
  camera: one slow continuous push-in toward the bottle (dolly forward)
  camera_start: low three-quarter angle, bottle framed medium against the wet rock
  camera_end: framed squarely on the bottle's logo face
  subject_motion:
    - condensation beads form and slide slowly down the matte shell
    - droplets gather at the bottle base
    - stream water ripples and flows over stones
    - fine mist drifts through the scene
  pacing: slow and uninterrupted

origin:
  anchor: matte black insulated water bottle resting on a wet rock beside a clear mountain stream
  starting_state: low three-quarter view of the bottle
  ending_state: push-in resolves close on the bottle's logo face

temporal:
  duration: 6 seconds
  pacing: slow, continuous, single uninterrupted push-in
  keyframes:
    - "0-1.5s: establish the bottle on the wet rock, stream flowing behind"
    - "1.5-4.5s: camera pushes in slowly as condensation slides down the shell"
    - "4.5-6s: push-in settles on the bottle's logo face"

intention:
  purpose: premium product hero shot for the insulated bottle
  narrative: stillness of a cold drink in a quiet mountain setting

orchestration:
  elements: [bottle, wet rock, mountain stream, condensation, mist]
  frame_content: only the bottle, the wet stone and the flowing stream fill the frame
  continuity: one continuous location, no scene changes

nuance:
  lighting: soft diffused morning light
  mood: calm, crisp, premium
  depth_of_field: shallow, bottle sharp with the stream softly blurred
  style: crisp product-commercial realism

audio:
  platform_support: native audio (Veo 3.1+)
  ambient: stream water trickling over rocks, faint distant birdsong
  action: soft patter of condensation drops

veo_prompt: |
  Product hero shot: a matte black insulated water bottle rests on a wet
  rock beside a clear mountain stream. The camera pushes in slowly and
  continuously toward the bottle, starting at a low three-quarter angle
  and ending framed squarely on the bottle's logo face. Cold condensation
  beads on the matte shell; droplets slide slowly down and gather at the
  base. Behind it, water ripples over stones, catching soft morning light.
  Gentle mist drifts. Only the bottle, the wet stone and the flowing
  stream fill the frame. Soft diffused morning light, shallow depth of
  field, crisp product-commercial realism. Audio: stream water trickling
  over rocks, faint distant birdsong, the soft patter of condensation drops.

---
Attestation: docs consulted = [Video Mode, Video Mode Library, DEPTH, Patterns and Evaluation, Format Guide YAML, Interactive Mode] | assumptions = [orbit replaced entirely by a slow push-in, no orbit remains; "no text on screen" read as no captions/overlays, bottle's own logo mark stays visible; target Veo 3.1+, 6-second single take] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-veo-water-bottle-product-shot-6s-pushin.yaml`

**Score and gate status:** `VISUAL 62/70 (Vivid 14, Intentional 9, Styled 8, Unambiguous 9, Atmospheric 9, Layered 4, Motion 9) | Perspectives: 5 (Video Mode) | Gate passed (56+ required)`

**Token overhead:** YAML carries roughly +3-7% tokens versus an equivalent Markdown deliverable.

**Summary:** Duration shortened to 6 seconds and the camera move is now a single slow push-in that resolves on the logo face, with the three keyframes retimed to 0-1.5s, 1.5-4.5s and 4.5-6s. Subject motion (condensation, water, mist) still runs the full clip, and the push-in keeps one continuous move so there is no contradiction with the "slow" pacing.

**One flag:** you said "instead of the orbit", so I removed the orbit entirely. If you actually wanted a short establishing orbit that then transitions into the push-in, say so and I will rebuild it as a two-stage move.

**Share your result for refinement:** Generate with this prompt and send back the clip or a description. Tell me what to change and I can refine the push-in speed, the logo reveal landing, the 6-second pacing, or the audio mix.