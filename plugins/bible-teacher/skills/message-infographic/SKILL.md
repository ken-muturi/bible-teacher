---
name: message-infographic
description: Turn a sermon, teaching or reflective video transcript (or outline) into a short set of 16:9 infographic slides as one self-contained HTML file. Use when the user types "message-infographic" followed by a pasted transcript, or asks for infographics / slides / visuals from a sermon or video transcript. Add "--dark" for a dark on-screen look for video overlays.
argument-hint: "<title> [--dark] [--slides N]  (then paste the transcript)"
---

# Message Infographic — Transcript to Slides

Turns a spoken message (a sermon, a reflective video, a teaching talk) into
4–6 widescreen infographic slides that follow the message's own movement.
Use them as video B-roll, projector slides, or social cards.

**Prerequisite:** teacher-foundation (for translation and tone). No brief is
needed; the transcript is the source.

---

## Input

Provide:
- **The transcript or outline** (required; auto-generated transcripts are fine)
- **Title** (optional; otherwise take it from the message's key verse or line)
- **`--dark`** (optional): dark ground for on-screen / video use. Default is the house cream look.
- **`--slides N`** (optional, 3–8; default: as many beats as the message has, usually 5)

---

## Step 1 — Read the message for its beats

Before designing, find the message's movement. Most reflective messages have:

| Beat | What to look for | Typical slide |
|------|------------------|---------------|
| **Anchor** | The verse or statement the whole thing hangs on | Title card: the verse, its reference, the speaker's opening question |
| **Observation** | "We all know…", lists of examples, what people do | A grid of 3–4 short cards |
| **Tension** | The honest reasons, the "yet…", the resistance | A contrast line or a short list beside the observation |
| **Image** | The central metaphor or story (a parked car, a seed, a house) | A simple drawn sequence or diagram of the image |
| **Reframe** | "Maybe the opposite of X is not Y but Z" | A crossed-out pairing replaced by the new one, plus a two-way contrast |
| **Question** | The closing challenge, what the listener is left with | Large closing question, with the speaker's humility line if there is one |

Not every message has all six. Use the beats that are really there; merge or skip the rest.

Give the user a one-line plan (slide → beat) before or with the output, not a long preamble.

---

## Step 2 — Content rules

- **Use the speaker's own words.** Slide copy is lifted and tightened from the transcript,
  never rewritten into a different message. Short, punchy, one idea per slide.
- **Scripture:** show the verse as the speaker quoted it, with its reference in the
  teacher's translation. If the speaker paraphrased, add **[VERIFY: wording in <translation>]**
  in the chat notes (not on the slide).
- **Garbled or unreadable passages** (mixed scripts, random symbols, words that don't
  connect): leave them out and tell the user which part was skipped, quoting its first
  few words so they can find it. Never guess what was meant.
- **Unfinished endings:** if the transcript trails off, end on the last complete thought
  and say so.
- **No invented facts:** no statistics, dates, studies or quotes that are not in the
  transcript. Missing details become placeholders like **[YOUR CHANNEL NAME]**.
- **Illustrating a metaphor** may add simple visual stages (e.g. a car drawn in four
  states of decay), but the captions stay close to what the speaker said.
- Respect the teacher-foundation tone: reflective, not preachy; don't add moral
  conclusions the speaker didn't make.

---

## Step 3 — Visual style

**Canvas:** each slide is exactly **1920 × 1080 px** (16:9), generous padding (~110–140 px),
one idea per slide, large type (headlines 80–130 px, body 28–40 px).

**Default (house look):** follows the other guides: cream ground `#f5f0e8`, panel
`#faf7f2`, dark text `#2c2c2c`, **Gentium Book Plus** for everything, one accent
from the house palette chosen by the message's tone (blue `#3b6fd4` structural,
red `#c0392b` warning/judgment, purple `#6c4bbf` application, green `#2e8a4a` hope).
2.5px borders with 3px radius, as elsewhere.

**`--dark` (video look):** warm charcoal `#1B1915`, bone text `#EFE8DA`, muted text
`#A89F8E`, hairlines `#3A352D`, card fill `#221F1A`, one gold accent `#D9A441`.
Display type **Fraunces** (italic for the emphasised phrase), body **DM Sans**.
Rounded cards (20px), thin 1px borders.

**Both looks:**
- One accent colour only; use it for the single phrase on each slide that carries the punch.
- Icons, if any, are simple inline stroke SVGs (book, pulse line, coin, speech bubble…). No emoji, no photos, no external images.
- No gradients, drop shadows or stock-template flourishes.
- Text contrast at least 4.5:1.
- A small caps label above each headline naming the beat ("What we already know", "The opposite of poverty…").

---

## File Output

One **fully self-contained** HTML file: all CSS in a `<style>` block, fonts via the
Google Fonts `@import`, inline SVG only, no scripts required.

Structure:
- Each slide is a `<section class="slide">` fixed at 1920×1080, stacked vertically
  with a gap, and scaled down with CSS (`zoom` or a `transform: scale()` wrapper) so
  the whole deck fits the browser width.
- A print rule (`@page { size: 1920px 1080px; margin: 0 }`, one slide per page) so
  **Save as PDF** gives one slide per page, ready to drop into a video editor.
- Slide numbers are not printed on the slides.

**Where it goes (auto-detect):** inside the Bible Teacher repo (a `guides/` folder exists),
save to `guides/visuals/<slug>-infographics.html` and add its index card. **Otherwise**
(phone/web, or another project), deliver it as an artifact or a single `.html` file.

After the file, give 2–3 plain sentences: the slide plan, anything skipped from the
transcript, and any **[VERIFY]** items.

---

## Usage Examples

```
message-infographic "The poor you will always have" --dark
  <paste transcript>                    → 5 dark video slides

message-infographic --slides 4
  <paste sermon outline>                → 4 cream house-style slides
```

---

## What This Skill Will Not Produce

- A summary that replaces the speaker's message with a different one
- Guessed reconstructions of garbled transcript sections
- Statistics, scholar quotes or cross-references the speaker didn't give
- Images of real people, logos or copyrighted artwork
