---
name: passage-study
description: Create a self-contained HTML study panel for any Bible verse or chapter. Use when the user types "passage-study <reference>" for a quick panel, or "passage-study <reference> --deep" for a full exegetical study with word studies, cited commentaries, cross-references, and application.
argument-hint: "<reference> [--deep]"
---

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

Save to `guides/passages/<book-chapter-verse>-study.html` when a `guides/` folder exists, else deliver as a self-contained artifact

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

Save to `guides/passages/<book-chapter-verse>-study.html` when a `guides/` folder exists, else deliver as a self-contained artifact
(overwrites the quick panel if one exists)

---

## Visual Style (both modes)

- Font: Gentium Book Plus — one serif family throughout (body, labels, titles, headers) via Google Fonts `@import`. A Bible-typesetting serif (SIL) chosen for high readability and full Greek/Hebrew coverage: `@import url('https://fonts.googleapis.com/css2?family=Gentium+Book+Plus:ital,wght@0,400;0,700;1,400;1,700&display=swap');`. Distinguish headings by size, weight (700), letter-spaced caps, or italic — not by a second font family.
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
- **Always fully self-contained** — all CSS inline in `<style>`, fonts via `@import`, no external files. The panel must render on its own as an artifact, an emailed file, or a printed page.
- **Where it goes (auto-detect):** if a `guides/` folder exists in the project (you're in the Bible Teacher repo), save to `guides/passages/<filename>.html` and add its index card. **Otherwise** (the plugin is installed in some other project), just deliver the finished HTML — as an artifact, or a single `.html` file in the working folder — and skip the `guides/` path, the index card, and the preview step.
- **Preview (repo only):** if the repo's preview server is running, you may open `http://localhost:7654/guides/passages/<filename>.html` and give a clickable link. Otherwise skip it — the file stands alone.

### Quality rules
- Flag every unverified claim: **[VERIFY: what to check]**
- Never fill a section with generic content — if no chiasm exists, don't force one
- Every commentator card must include a source line: full name, book title, and one URL where it can be accessed or purchased. Flag with **[VERIFY]** if the URL is uncertain.
- Never fabricate word meanings, commentary positions, or historical details

---

## House style — keep every guide consistent

Two ways to style a guide; **auto-detect which applies**:

- **Default (works anywhere, incl. installed in another project):** emit a
  **fully self-contained** `<style>` that follows the house look — cream ground
  `#f5f0e8`, card `#faf7f2`, ink `#2c2c2c`, Gentium Book Plus serif, one accent
  colour family per page, and the standard components (`.passage-callout`,
  `.word-*` studies, dark `.comm-*` commentary cards, `.pressure-box`,
  `.xref-*`, `.then-now`, `.verdict`). Everything inline; no external CSS.
- **Inside the Bible Teacher repo (optional optimisation):** if
  **`styles/base.css`** exists, don't hand-write the base — start the `<style>`
  with the marker pair and add only the per-page tokens + unique components,
  then run **`python3 scripts/build_guides.py`** to inject the shared base
  (single source of truth). `styles/GUIDE-TEMPLATE.html` is the skeleton and
  lists the colour families.

  ```
  <style>
  /* @base:start */
  /* @base:end */
    :root { --accent:#...; --accent-soft:#...; --accent-ink:#...;
            --accent-lt:#...; --accent-mid:#...; --accent-hair:#...; }
    /* page-specific components only (signature strips, etc.) */
  </style>
  ```

Either way, pick ONE accent family per page and drive all accent colour from
the tokens — never scatter hardcoded accent hexes through the components.
