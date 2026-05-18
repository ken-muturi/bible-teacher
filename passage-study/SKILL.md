# Passage Study — Verse and Chapter Deep Dive

Two modes: a fast overview panel, and a full deep study. Both output HTML only — no study brief in chat.

**Prerequisite:** teacher-foundation (shapes translation, tradition, tone).

---

## Input

```
passage-study Romans 8:1-11           → quick panel (default)
passage-study Romans 8:1-11 --deep    → full study panel
```

Optional focus for `--deep`: `word-study`, `context`, `illustrations`, `structure`

---

## Mode 1 — Quick Panel (default)

**When to use:** First pass on a passage, prep starting point, live reference during teaching.

**Research (internal — do not output in chat):**
- Passage text in teacher's translation
- One-sentence placement in the book
- 2 key word studies (English → transliterated original → plain meaning)
- Passage structure in plain labels (3 beats max)
- 2 teaching illustrations — one everyday, one from history or literature
- Then → Now bridge (two sentences)
- 2 cross-references, tagged

**Panel sections:**
- Title bar — reference, book, one-line summary
- Passage callout — key verse(s), left-bordered
- Word study strip — 2 terms
- Structure map — 3 beats or turns, color-coded
- Illustrations — 2 cards
- Then → Now bridge — purple, two sentences
- Cross-references — 2 tagged cards
- Verdict — controlling idea, dark banner

Save to: `guides/passages/<book-chapter-verse>-study.html`

---

## Mode 2 — Deep Study (`--deep`)

**When to use:** Sermon or lesson prep, teaching a passage for the first time, need the full exegetical picture.

Builds on Mode 1 and adds:

**Additional research (internal — do not output in chat):**
- 3–5 word studies (full: translations compared, what is lost in English)
- Historical/cultural context — specific, verifiable detail; cite sources; flag **[VERIFY]**
- Full structure map (chiasm, argument cascade, narrative arc as appropriate)
- 3–5 teaching illustrations (everyday / history / works for non-religious audience)
- 2–3 cited commentaries — author, title, what they say about this specific text; tradition tag; source link (URL where the work or author’s ministry can be found); **[VERIFY]** if uncertain
- Interpretive pressure points — main scholarly debate, most common misreading, open question
- 3–5 cross-references with one sentence each
- Then → Now bridge calibrated to teacher's AUDIENCE

**Additional panel sections (added to Mode 1 layout):**
- Extended word study strip — 3–5 terms
- Historical context box — orange
- Full commentary shelf — 2–3 source cards with tradition tags and source links
- Interpretive pressure points — dark box
- Extended cross-reference strip

Save to: `guides/passages/<book-chapter-verse>-study.html`
(overwrites the quick panel if one exists)

---

## Visual Style (both modes)

- Fonts: Caveat (body/labels) + Special Elite (titles/headers) via Google Fonts `@import`
- Colors: blue #3b6fd4 (structural), green #2e8a4a (positive), red #c0392b (tension), orange #d47c1a (context), purple #6c4bbf (application), dark #2c2c2c (spine), bg #faf7f2
- Borders: 2.5px, 3px radius, matching tinted fills
- Passage callout: left border only, 5px
- No drop shadows, gradients, icons, or images

---

## Format Rules

### Chat output (before the HTML)
Output a concise study brief in chat first — this is the teacher's prep summary, not the full exegetical dump. Keep it tight:

**Quick mode brief (chat):**
- Passage reference + one-sentence placement
- Key verse quoted
- 2 word studies (term → transliterated original → one-sentence meaning)
- Structure in 3 labelled beats
- 2 illustrations (one sentence each)
- Then → Now (two sentences total)

**Deep mode brief (chat):**
No length limit — write the full study. Cover everything:
- Passage reference + placement in the book
- Full passage text in teacher's translation
- 3–5 word studies (term → transliterated original → translations compared → what is lost in English)
- Complete structure map with all movements labelled
- 3–5 illustrations — fully developed, specific, no moralizing
- Historical/cultural context — as much detail as is useful; cite sources; flag **[VERIFY]**
- Commentary shelf — author, title, what they say about this specific text, tradition tag, source link
- Interpretive pressure points — main scholarly debate, most common misread, open question
- 3–5 cross-references with full explanation
- Then → Now bridge calibrated to the teacher's audience

After the chat brief, generate and save the HTML panel, then open the preview.

### HTML panel
- Self-contained — all CSS in `<style>`, fonts via `@import`
- After saving, open the preview at `http://localhost:7654/guides/passages/<filename>.html`
- Confirm with one line as a clickable link: `[guides/passages/<filename>.html](http://localhost:7654/guides/passages/<filename>.html)`

### Quality rules
- Flag every unverified claim: **[VERIFY: what to check]**
- Never fill a section with generic content — if no chiasm exists, don't force one
- Every commentator card must include a source line: full name, book title, and one URL where it can be accessed or purchased. Flag with **[VERIFY]** if the URL is uncertain.
- Never fabricate word meanings, commentary positions, or historical details
