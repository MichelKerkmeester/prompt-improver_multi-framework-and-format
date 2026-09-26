```yaml
Mode: $video | Complexity: 6/10 | Framework: MOTION

platform: kling_2.6
generation_mode: text_to_video
aspect_ratio: "16:9"
duration_seconds: 10
continuity: single continuous shot, no cuts, no scene changes

setting: cavernous flower auction hall near Aalsmeer at dawn

subject:
  trolley_trains: rows of trolley trains loaded with crates of red and yellow tulips, snaking past each other in two opposing directions across the hall floor
  workers: three anonymous workers riding electric tugs, steering the trains, kept small-scale and distant in frame throughout
  focal_object: the hall's large mechanical auction clock

camera:
  beat_1:
    timing: 0-4s
    movement: glides forward at a steady pace, holding roughly three metres above the hall floor, tracking low over the trolley trains
  beat_2:
    timing: 4s
    movement: rises slowly and steadily, elevating to reveal the full width and length of the hall below
  beat_3:
    timing: 8-10s
    movement: settles into a static frame facing the auction clock as its sweep hand begins to move
  quality: smooth, continuous, single unbroken take across all three beats

lighting:
  opening: cool blue daylight filtering down through the roof windows
  closing: warms gradually to gold by the final beat
  transition: continuous, gradual shift spanning the full ten seconds

audio:
  native: true
  description: with the sound of a steady electric motor hum, trolley wheels rolling over concrete, and a single distant bell chime as the clock hand begins its sweep in the final beat
  register: industrial ambience only, sparse and quiet

style:
  tone: quiet, observational, cinematic brand-film opening shot
  subject_treatment: workers remain small and anonymous, never the visual focus

---
Attestation: docs consulted = Video Mode, Video Mode Library, Patterns and Evaluation, Format Guide YAML | assumptions = [Assumes: "glides forward" rendered as natural-language elevated tracking description since Kling 2.6's directional brackets cover zoom/move-left-right/move-up-down/rotate only, not forward-back] [Assumes: standard airport-style electric tug for the steering vehicle] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/001 - enhanced-flower-auction-opening-shot.yaml`

**Score and gate status:** VISUAL 63/70 (Vivid 14, Intentional 9, Styled 8, Unambiguous 9, Atmospheric 9, Layered 5, Motion 9) | Threshold 56+ | All dimension floors met | Gate passed

**Token overhead:** YAML format adds approximately +3-7% tokens versus Markdown baseline for this deliverable.

**Summary:** The prompt structures your continuous 10-second Kling 2.6 dawn shot into three explicit camera beats (forward glide, rise-to-reveal, settle-on-clock) with the tulip trolley choreography, worker anonymity, blue-to-gold lighting arc, and native audio cue all preserved. Camera direction uses natural-language phrasing rather than Kling's bracket syntax, since "forward/back" isn't one of Kling's reversed directional controls (only zoom, left/right, up/down, rotate) — flagged above as an assumption.

---
**Share Your Result for Refinement**

Try this prompt in Kling 2.6 and share the generated clip with me! I can help you:
- Refine the camera beats if the timing or reveal doesn't land right
- Adjust the lighting transition if the blue-to-gold shift feels off
- Fix the audio mix if the hum, wheels or chime aren't balanced correctly

Just share the result and tell me what you'd like to change.