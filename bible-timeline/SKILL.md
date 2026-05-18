# Skill: Bible Timeline & Family Tree

## Trigger
```
bible-timeline <query>
```

Where `<query>` can be:
- A **person** — `bible-timeline Moses`
- A **family / clan** — `bible-timeline Patriarchs` · `bible-timeline David's line`
- A **period** — `bible-timeline exile` · `bible-timeline judges`
- A **full overview** — `bible-timeline` or `bible-timeline full`

---

## What This Skill Produces

An HTML visual panel saved to `guides/visuals/bible-timeline-<query>.html` containing:

1. **Era timeline strip** — colour-coded horizontal bands from Adam to Jesus
2. **Lifespan bars** — each key figure shown as a horizontal bar across their years
3. **Family tree** — genealogical lines connecting figures in the query scope
4. **Contemporaries grid** — who was alive at the same time as the focal figure(s)
5. **Books in context** — which biblical books were written or set in the same window
6. **Key events** — major events pinned to the timeline (flood, exodus, exile, etc.)

---

## Eras and Colour Coding

| Era | Approx. Years (AM / BC) | Colour |
|-----|------------------------|--------|
| Antediluvian | Creation – ~1656 AM / ~2350 BC | Deep blue |
| Post-flood Patriarchs | ~1656–2000 AM / ~2350–1900 BC | Teal |
| Sojourn & Exodus | ~2000–2666 AM / ~1900–1446 BC | Gold |
| Conquest & Judges | ~2666–3000 AM / ~1446–1050 BC | Orange |
| United Kingdom | ~3000–3029 AM / ~1050–1010 BC | Purple |
| Divided Kingdom | ~3029–3406 AM / ~1010–586 BC | Red |
| Exile | ~3406–3480 AM / ~605–538 BC | Dark red |
| Post-exile / Return | ~3480–3720 AM / ~538–444 BC | Olive |
| Intertestamental | ~3720–4000 AM / ~400–4 BC | Grey |
| New Testament | ~4000 AM / ~4 BC – AD 100 | Green |

---

## Step-by-Step Instructions

### Step 0 — Scope the query
Determine what the user is asking for:
- Single person → show that person's full family tree + contemporaries + books
- Family/clan → show the genealogical tree of that clan
- Period → show all major figures in that period + books
- Full → show abbreviated overview from Adam to Jesus

### Step 1 — Gather data
For the figures in scope, compile:
- Name (Hebrew/Greek where relevant)
- Approximate birth and death year (AM or BC — use both)
- Father, mother, spouse(s), children
- Key role/event
- Which biblical books they appear in or authored

Use conservative evangelical chronology as the default (following Ussher's framework for the patriarchs, standard critical dates for the monarchy period).

### Step 2 — Identify contemporaries
For each focal figure, list:
- Who else was alive at the same time
- Any prophets active during that period
- Any foreign kings/empires that intersect the narrative

### Step 3 — Map books to the timeline
For each era in scope, list:
- Books written during that period (by author if known)
- Books set during that period (narrative content)
- Key passages that cross-reference the figures

### Step 4 — Build the HTML panel

Use the visual style system:
- **Fonts**: Caveat (body) + Special Elite (headings) from Google Fonts
- **Background**: `#f5f0e8`
- **Card background**: `#faf7f2`
- **Borders**: `2px solid #2c2c2c`
- **Era colours**: as per table above

#### Layout structure:

```
┌─────────────────────────────────────────────────────┐
│  HEADER: Title + era label + date range             │
├─────────────────────────────────────────────────────┤
│  ERA STRIP: colour-coded horizontal era bands       │
├─────────────────────────────────────────────────────┤
│  TIMELINE: lifespan bars + key event pins           │
├──────────────────────┬──────────────────────────────┤
│  FAMILY TREE         │  CONTEMPORARIES GRID         │
│  (genealogical tree) │  (who was alive together)    │
├──────────────────────┴──────────────────────────────┤
│  BOOKS IN CONTEXT (3-col: Written / Set / Key refs) │
├─────────────────────────────────────────────────────┤
│  THEN → NOW: why this genealogy/timeline matters    │
└─────────────────────────────────────────────────────┘
```

#### Timeline bar rendering:
- Use CSS `width` percentages relative to the total span being shown
- Position each bar using `left` offset from the era start
- Each bar labelled with the person's name + years
- Colour the bar by era
- Add small diamond markers for key events

#### Family tree rendering:
- Use a vertical tree with connecting lines (CSS borders/pseudo-elements)
- Males: dark border; Females: lighter border
- Mark notable roles with a small badge (King, Prophet, Priest, Judge)

#### Contemporaries grid:
- 3-column grid of person cards
- Each card shows: name, dates, role, overlap note ("alive during X's life")
- Highlight direct family in green, prophets in purple, foreign rulers in red

### Step 5 — Add responsiveness
Add `<meta name="viewport" content="width=device-width, initial-scale=1">` and mobile breakpoints:
```css
@media (max-width: 768px) {
  /* stack all grids to 1 column */
  /* timeline scrolls horizontally */
}
```

### Step 6 — Save and report
- Save to `guides/visuals/bible-timeline-<query-slug>.html`
- Report: who was included, date range covered, books mapped, file path
- Offer to zoom in on any sub-family or sub-period

---

## Example Queries and Expected Outputs

| Query | What is generated |
|-------|------------------|
| `bible-timeline Moses` | Moses family tree (Levi → Kohath → Amram → Moses/Aaron/Miriam) + contemporaries (Pharaoh Thutmose III/Amenhotep II, Joshua, Caleb) + books (Exodus–Deuteronomy, Job) |
| `bible-timeline Patriarchs` | Full Abraham → Isaac → Jacob → 12 sons tree with lifespan bars, overlap grid showing who was alive together, books (Genesis) |
| `bible-timeline David's line` | Jesse → David → Solomon → divided kingdom kings down to exile, with prophets active at each point (Nathan, Isaiah, Jeremiah) |
| `bible-timeline exile` | Daniel, Ezekiel, Jeremiah, Nehemiah, Esther, Zerubbabel — who was alive when, overlapping with which Babylonian/Persian kings |
| `bible-timeline` | Full overview Adam → Jesus: abbreviated bars for all major figures, era bands, 66 books mapped to their windows |

---

## Foundation Integration
If `foundation/teacher-foundation/SKILL.md` is present, adapt:
- Use the preferred translation for all scripture references
- Use denominational chronology preferences if specified
- Tailor the "Then → Now" application to the ministry context

---

## Output File Naming
`guides/visuals/bible-timeline-<slug>.html`

Examples:
- `bible-timeline-moses.html`
- `bible-timeline-patriarchs.html`
- `bible-timeline-david-line.html`
- `bible-timeline-full.html`
