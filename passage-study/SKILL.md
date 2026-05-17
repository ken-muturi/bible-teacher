# Passage Study — Verse and Chapter Deep Dive

Deep exegetical study of a specific Bible passage. Works on a single verse,
a paragraph, or a full chapter.

**Prerequisite:** teacher-foundation (shapes translation, tradition, tone).

---

## Input

Provide:
- **Passage reference** (required) — e.g., `John 3:16`, `Romans 8:1-11`, `Matthew 5:1-12`, `Psalm 23`
- **Focus** (optional) — `word-study`, `context`, `illustrations`, `structure`, or leave blank for full study

---

## Process (internal — do not output in chat)

Research and prepare the following before writing the HTML. Do not print these as chat output.

1. **Passage + orientation** — full text in teacher's translation; one-sentence placement in the book
2. **Immediate context** — what comes before and after; the question this passage answers; literary type
3. **Word studies (3–5 terms)** — English → transliterated original → meaning → what is lost in translation
4. **Historical/cultural context** — what the original audience understood that modern readers miss; cite sources; flag with **[VERIFY]**
5. **Structure** — argument steps, narrative turns, chiasm, or list — plain labels, no jargon
6. **Teaching illustrations (3–5)** — specific, not generic; at least one from everyday life, one from history/literature, one that works for a non-religious audience; never moralize
7. **Cited commentaries (2–3)** — author, title, what they say about this specific text; flag tradition; **[VERIFY]** anything uncertain
8. **Interpretive pressure points** — main scholarly disagreement; most common misreading; open question
9. **Cross-references (3–5)** — tagged ← OT, NT →, ≈ parallel; one sentence each
10. **Then → Now bridge** — what it meant then; what it means for this teacher's audience

---

## Output: HTML Visual Panel

Produce only the HTML file. No study brief in chat — just confirm the file was saved.

Save to: `guides/passages/<book-chapter-verse>-study.html`
(examples: `guides/passages/john-3-16-study.html`, `guides/passages/romans-8-1-11-study.html`)

### Panel Structure

**Title bar** — passage reference (large), book + literary type, one-line summary

**Full passage callout** — complete text, left-bordered, prominent

**Word study strip** — key terms in a horizontal row: English → transliterated original → meaning

**Structure diagram** — visual map of the passage (argument steps, narrative turns, chiasm, or list)

**Illustrations block** — 2–3 strongest illustrations as short cards

**Then → Now bridge** — two-sentence application, visually distinct (purple)

**Commentary shelf** — 2–3 cited sources as compact reference cards

**Interpretive pressure points** — dark box: main debate, common misread, open question

**Cross-references strip** — tagged passage links at the bottom

**Verdict / controlling idea** — centered dark banner, the passage's one-sentence core

### Visual Style
Follow the same style system as book-overview-infographic:
- Fonts: Caveat (body/labels) + Special Elite (titles/headers) via Google Fonts `@import`
- Colors: blue #3b6fd4 (structural), green #2e8a4a (positive), red #c0392b (tension), orange #d47c1a (context), purple #6c4bbf (application), dark #2c2c2c (spine), bg #faf7f2
- Borders: 2.5px, 3px radius, matching tinted fills
- Passage callout: left border only, 5px
- No drop shadows, gradients, icons, or images

---

## Format Rules

- Do not output the study notes in chat — all content goes into the HTML panel
- Confirm completion with one line: `Saved: guides/passages/<filename>.html`
- HTML must be fully self-contained — all CSS in `<style>`, fonts via `@import`
- Flag every unverified claim in the HTML: **[VERIFY: what to check]**
- Never fill a section with generic content — if the passage has no chiasm, don't invent one
- Never fabricate word meanings, commentary positions, or historical details
