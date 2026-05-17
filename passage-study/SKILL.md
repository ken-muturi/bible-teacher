# Passage Study — Verse and Chapter Deep Dive

Deep exegetical study of a specific Bible passage, with teaching illustrations
and a self-contained HTML visual panel. Works on a single verse, a paragraph,
or a full chapter.

**Prerequisite:** teacher-foundation (shapes translation, tradition, tone).

---

## Input

Provide:
- **Passage reference** (required) — e.g., `John 3:16`, `Romans 8:1-11`, `Matthew 5:1-12`, `Psalm 23`
- **Focus** (optional) — `word-study`, `context`, `illustrations`, `structure`, or leave blank for full study

---

## Output: Study Brief

### 1. Passage Header
- Reference + full text in teacher's primary translation
- One-sentence orientation: where this sits in the book and why it matters

---

### 2. Immediate Context
- What comes directly before and after — 2-3 sentences
- The question this passage is answering, or the problem it is solving
- Literary type: narrative, argument, poetry, prophecy, law, wisdom

---

### 3. Word Studies (3-5 key terms)
For each term:
- English word as it appears in the translation
- Original language word (transliterated: Hebrew or Greek) + brief meaning
- How different translations render it and why it matters
- One sentence on what is lost if you read the English alone

---

### 4. Historical and Cultural Context
- What would the original audience have immediately understood that a modern reader misses?
- Specific details: geography, social customs, political situation, religious practice
- At least one concrete, verifiable historical detail — cite the source **[VERIFY if uncertain]**

---

### 5. Structure and Movement
Map how the passage is built:
- If it is an argument: show the logical steps
- If it is a narrative: show the scene turns
- If it is a poem or chiasm: show the mirroring structure
- If it is a list: show what holds the items together

Use plain labels, not academic jargon.

---

### 6. Teaching Illustrations (3-5)
Concrete illustrations that make the passage's meaning land for a modern audience.

Rules for illustrations:
- Specific, not generic — a named situation, not "in life we often..."
- True to the text — the illustration illuminates what the passage actually says, not a surface resemblance
- At least one from everyday life (work, family, ordinary decisions)
- At least one from history or literature
- At least one that would resonate with someone with no church background
- Never moralize — show the idea, let the audience draw the conclusion

---

### 7. Cited Commentaries (2-3)
Named, verifiable sources that speak directly to this passage:
- Author, title, what they say about this specific text
- Flag tradition alignment: Reformed, Catholic, Baptist, etc.
- **[VERIFY]** anything uncertain

---

### 8. Interpretive Pressure Points
- The main scholarly disagreement about this passage (if one exists)
- The most common misreading — what people think it says vs. what it actually says
- The question this passage leaves open

---

### 9. Cross-References (3-5)
Passages that speak directly to the same idea:
- Tagged ← OT source, NT → fulfillment, ≈ parallel theme
- One sentence on what the cross-reference adds

---

### 10. Then → Now Bridge
Two sentences:
- What this meant to the original audience
- What that same truth means for the teacher's specific audience (calibrated to AUDIENCE in foundation)

---

## Output: HTML Visual Panel

After the study brief, generate a self-contained HTML teaching panel for the passage.

Save to: `guides/passages/<book-chapter-verse>-study.html`
(example: `guides/passages/john-3-16-study.html`, `guides/passages/romans-8-1-11-study.html`)

### Panel Structure

**Title bar** — passage reference (large), book + literary type, one-line summary

**Full passage callout** — complete text, left-bordered, prominent

**Word study strip** — key terms in a horizontal row: English → transliterated original → meaning

**Context diagram** — visual map of the passage structure (argument steps, narrative turns, chiasm, or list)

**Illustrations block** — 2-3 of the strongest illustrations as short cards

**Then → Now bridge** — two-sentence application, visually distinct (purple, as per style guide)

**Commentary shelf** — 2-3 cited sources as compact reference cards

**Cross-references strip** — tagged passage links at the bottom

### Visual Style
Follow the same style system as book-overview-infographic:
- Fonts: Caveat (body/labels) + Special Elite (titles/headers) via Google Fonts
- Color system: blue (structural), green (positive/resolution), red (tension/pressure), orange (context/warning), purple (application/bridge), dark #2c2c2c (spine), light bg #faf7f2
- Borders: 2.5px, 3px radius, matching tinted fills
- Key passage callout: left border only, 5px
- No drop shadows, gradients, icons, or images

---

## Format Rules

- Study brief: readable sections with generous spacing — designed to be used during prep, not published directly
- HTML panel: self-contained, all CSS in `<style>`, fonts via `@import`
- Flag every claim that needs verification: **[VERIFY: what to check]**
- Never fill a section with generic content — if the passage doesn't have a chiasm, don't force one
- Never fabricate word meanings, commentary positions, or historical details
