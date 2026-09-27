```yaml
Mode: $video $yaml | Complexity: Low (4/10) | Framework: MOTION

platform: Kling 2.6
generation_type: text_to_video
duration: 10s
aspect_ratio: '16:9'
shot: single continuous take, no cuts, no scene changes

intention: opening shot of a brand film about the flower auction near Aalsmeer, establishing the hall's scale and dawn stillness before trading begins

camera:
  origin: three metres above the hall floor, gliding forward along the trolley lines
  beat_4s: rises smoothly upward, widening to reveal the entire hall
  beat_8s: settles into a static, forward-facing shot on the large auction clock as its hand begins to sweep

subject:
  primary: trolley trains loaded with red and yellow tulips, snaking past each other in two opposing directions across the hall floor
  secondary: three workers on electric tugs steering the trains, kept small and anonymous, never in close-up or clearly visible

setting: vast flower-auction hall near Aalsmeer at dawn, daylight entering through roof windows

lighting: cool blue dawn tone at the opening, warming gradually to gold by the final beat

style: naturalistic documentary aesthetic, unbroken continuous take, no stylized filters or grading

audio: ambient only, with the sound of a steady electric hum from the tugs, trolley wheels rolling over concrete, and a single distant chime as the clock hand starts to move; no music, no spoken dialogue

mood: quiet, industrial, dawn-hushed anticipation

constraints:
  - continuous camera motion for the full 10 seconds, holding static only at the final beat
  - one unbroken shot, no scene changes or cuts
  - workers remain small, anonymous figures, never the focal subject

---
Attestation: docs consulted = DEPTH Thinking Framework, Interactive Mode, Video Mode, Video Mode Library, Patterns and Evaluation, Format Guide YAML | assumptions = [Assumes: camera holds static through the final second after the 8s settle] | [Assumes: naturalistic documentary aesthetic since no visual style was specified] | format = YAML | execution = did not occur | save = did not occur
```

**Export-equivalent path:** `export/[###] - enhanced-aalsmeer-flower-auction-opening-shot.yaml`

**Score and gate status:** VISUAL 62/70 (Vivid 13, Intentional 9, Styled 9, Unambiguous 9, Atmospheric 9, Layered 4, Motion 9) | Gate passed (56+ threshold, all dimension floors met, camera + subject motion present throughout)

**Token overhead:** YAML adds roughly +3-7% tokens versus an equivalent Markdown version of this prompt.

**Brief summary:** Structured the shot as Kling 2.6 native-audio YAML with all three camera beats preserved (forward glide at 3m, the 4s rise, the 8s settle on the clock), kept the tulip-train choreography and worker anonymity intact, and folded your audio cues into Kling's "with the sound of..." convention while keeping the no-music/no-voices instruction explicit.

**Share Your Result for Refinement:** Try this prompt in Kling 2.6 and share the generated clip with me — I can help refine the camera pacing at each beat, adjust the dawn-to-gold light transition, or dial in the audio balance if anything renders differently than intended.