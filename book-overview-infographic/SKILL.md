# Book Overview Infographic — Visual Teaching Panel

Generates a self-contained HTML teaching panel from a completed book-overview brief.
Output is a single HTML file — screenshot it, print it, or use it as a video reference card.

**Prerequisite:** a completed book-overview brief for this book.

---

## Input

Provide:
- **Book name** (required)
- The completed book-overview brief (paste it or confirm it was just run)
- **Layout mode** (optional flag — see below)

---

## Layout Modes

### Default — 3-Column Layout

Unless a flag is given, always use a standard three-column grid:

| Column | Content |
|--------|---------|
| **Left** | Book identity, structural device (cycle, arc, flow, map), period/setting |
| **Center** | Main content units (judges, offerings, movements, sections), key passage callout, hardest interpretive moment |
| **Right** | Key words, cross-Bible links, Then→Now bridge, final verdict |

The three-column layout is predictable, printable, and consistent across all 66 books. It is the default because it works for most books and keeps the series visually coherent.

Within the three-column structure, the structural device in the left column still adapts to the book:
- Narrative books → cycle or arc diagram
- Epistles → argument flow summary
- Wisdom/Poetry → thematic clusters
- Prophetic → judgment/restoration split

---

### `--non-constrained` — Theme-Driven Layout

Pass this flag when the book's structure genuinely cannot be served by three columns — when the spatial logic of the content requires a different form.

Before writing any HTML, identify the book's dominant structural logic:
- What are the major movements or themes?
- What is the book's central tension or organizing device?
- What does a reader need to see spatially to understand how the book works?

Then design the layout to express that. Choose or invent the right visual form:

- **Downward descent** — sequential deterioration (Judges)
- **Argument cascade** — logical steps feeding into each other (Romans)
- **Inward spiral** — oracles circling toward a target (Amos)
- **Two-panel contrast** — side-by-side tension (Ruth, Daniel)
- **Vision sequence** — a series of distinct scenes (Ezekiel, Revelation)
- **Chiasm map** — mirrored themes around a center
- **Journey timeline** — geographic or chronological movement (Acts, Exodus)

One book may combine forms. Let the brief determine which to use. Ask: what spatial arrangement helps a viewer grasp this book's logic at a glance?

Every `--non-constrained` panel still includes all fixed elements (see below) — only the grid structure is freed.

---

### Usage Examples

```
book-overview-infographic genesis          → 3-column (default)
book-overview-infographic judges --non-constrained  → theme-driven descent layout
book-overview-infographic romans --non-constrained  → argument cascade layout
```

---

## Fixed Elements (appear in every panel)

These are present regardless of layout:

| Element | Content |
|---------|---------|
| **Title bar** | Book name (large), series position, one-line characterization |
| **Key passage callout** | The one verse to read aloud — left-bordered, prominent |
| **Cross-Bible links** | Tagged ← OT, NT →, ≈ parallel — can be a sidebar, footer, or strip |
| **Then → Now bridge** | The application in two sentences |
| **Question to sit with** | From section 7 of the brief |
| **Next in series** | The following book and why the contrast or continuity matters |
| **Final verdict** | The book's controlling idea or last word, centered, with reference |

---

## Visual Style (consistent across all 66 books)

**Typography**
- One serif family throughout: **Gentium Book Plus** (Google Fonts) — a Bible-typesetting serif (SIL) with high readability and full Greek/Hebrew coverage
- Body / labels / verses: Gentium roman
- Book name / titles: letter-spaced caps (the "PROVERBS" look); section subheads: italic of the same family
- Distinguish headings by size, weight (700), caps, or italic — not by a second font family
- Loaded via `@import url('https://fonts.googleapis.com/css2?family=Gentium+Book+Plus:ital,wght@0,400;0,700;1,400;1,700&display=swap');` in the `<style>` block

**Color system**
| Color | Hex | Use |
|-------|-----|-----|
| Blue | #3b6fd4 | Structural, key passages, faithful moments |
| Green | #2e8a4a | Positive, rest, covenant faithfulness, resolution |
| Red | #c0392b | Failure, judgment, tension, the book's hardest moment |
| Orange | #d47c1a | Warning, historical context, mixed outcomes |
| Purple | #6c4bbf | Application, Then→Now, thematic bridge |
| Dark | #2c2c2c | Final verdict, structural spine, labels |
| Light bg | #faf7f2 | Panel background |
| Page bg | #f5f0e8 | Body background |

**Box rules**
- All bordered elements: 2.5px border, 3px border-radius, matching light-tinted background fill
- Callout (key passage): left border only, 5px, no full border
- Final verdict: full 3px dark border, centered text
- Dark note boxes (misreads, warnings): #1a1a1a background, #f5f0e8 text

**No:** drop shadows, gradients, icons, images, decorative dividers

---

## File Output

Save to: `guides/visuals/<bookname-lowercase>-panel.html`

The file must be fully self-contained — all CSS in a `<style>` block, fonts via `@import`. No external scripts or stylesheets beyond the Google Fonts CDN.

After saving, navigate the preview to the file and confirm with a clickable link: `[guides/visuals/<bookname-lowercase>-panel.html](http://localhost:7654/guides/visuals/<bookname-lowercase>-panel.html)`

---

## Constraints

- Do not fill gaps with content not in the research brief
- Flag any claim that needs verification: **[VERIFY: what to check]**
- Never fabricate cross-references or scholar positions
- Every cited scholar or commentator must include: full name, book title, and one URL where the work can be accessed or purchased. Flag with **[VERIFY]** if the URL is uncertain. Include a tradition tag (conservative evangelical / reformed / critical-scholarly / pastoral / etc.)
- The panel is a reference card, not a summary — it surfaces structure and key terms, not the full argument
