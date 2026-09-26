```
Mode: $video $yaml | Complexity: 6/10 | Framework: MOTION

platform: Kling 2.6
generation_type: text-to-video
duration_seconds: 10
aspect_ratio: "16:9"
audio: native
continuity: single continuous take, no cuts, no scene changes

scene:
  setting: Interior of a flower auction hall near Aalsmeer, at dawn
  subject: Rows of trolley trains loaded with red and yellow tulips, snaking past each other in two directions across the hall floor
  operators: Three workers on electric tugs steering the trolley trains, kept small in frame and anonymous, no faces emphasized
  focal_point: The hall's large auction clock, reached by the end of the shot

origin: Opens already in motion, three metres above the hall floor at dawn, with the nearest trolley train entering frame as the camera advances

camera:
  beat_1:
    timing: 0 to 4 seconds
    movement: Glides forward at roughly three metres above the hall floor, low and level, moving with the flow of the crossing trolley trains
  beat_2:
    timing: 4 to 8 seconds
    movement: Rises slowly and steadily, gaining altitude to reveal the full scale of the hall, its rows of trolley trains, and the roof windows above
  beat_3:
    timing: 8 to 10 seconds
    movement: Settles into a static frame facing the large auction clock as its hand begins to sweep

depth:
  foreground: Nearest trolley train and tulips close to the lens in the opening beat
  midground: Crossing trolley trains and the three tug operators threading between them
  background: Hall walls, roof windows, and the auction clock growing prominent as the camera rises and settles

lighting:
  start: Cool blue daylight spilling down through the roof windows at dawn
  end: Warms gradually to gold tones by the final second
  transition: Continuous and gradual across the full ten seconds, tracking the rising camera and the passing time

audio:
  ambient_hum: Steady electric hum from the trolley tug motors
  mechanical: Trolley wheels rolling over the concrete floor
  accent: A single distant chime sounding right at the end, as the clock hand starts its sweep
  exclusions: Ambient industrial sound only, no music and no voices

intention: Opening brand-film shot establishing the auction hall's scale and dawn-to-day precision moments before trading begins

mood: Quiet, orderly, dawn-lit industrial calm building toward the day's first movement

style: Cinematic documentary realism, wide-format brand-film opening, no on-screen text or graphics

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Video Mode, Video Mode Library, Patterns and Evaluation, Format Guide YAML | assumptions = [Assumes: unbranded/generic auction hall near Aalsmeer, no specific company name invented], [Assumes: structured YAML field breakdown is an acceptable equivalent to Kling 2.6's natural-language plus bracket-camera ingestion, per the explicit $yaml format lock] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-flower-auction-dawn-opening-shot.yaml` (`###` is a placeholder for you to reconcile against your own numbering).

**Score and gate status:** VISUAL (video) ≈ 64/70 (threshold 56+) — Motion, Atmospheric, Layered and Unambiguous dimensions all clear their floors given the three timed camera beats, the light transition, and the depth layering. Gate passed.

**Token overhead:** YAML deliverables run roughly +3-7% tokens versus the Markdown baseline for equivalent content.

**Summary:** This is a Kling 2.6 text-to-video prompt for a single continuous 10-second, 16:9, native-audio opening shot: a 3-metre forward glide over crossing tulip trolley trains (0-4s), a slow rise revealing the full hall (4-8s), and a settle on the sweeping auction clock (8-10s), with hum/wheel/chime-only audio and a blue-to-gold light shift. Every beat, timing marker, and constraint from your brief (including the no-music/no-voices and anonymous-workers rules) is preserved in the YAML structure with no added scenes or elements.

---

**Share Your Result for Refinement**

Try this prompt in Kling 2.6 and share the result with me!
- **Refine motion** if the forward glide, rise, or settle-on-clock beat isn't landing at the right second
- **Adjust the light or audio** if the dawn-to-gold transition or the hum/wheel/chime balance needs tuning
- **Fix consistency** if the trolley trains, tugs, or clock face drift or distort across the ten seconds

Just share the result and tell me what you'd like to change.