# Bible Teacher — AI Skill Toolkit

A set of workflow tools for producing Bible teaching content.
Adapted from the [pastor-ai-skills](https://github.com/tkcostello/pastor-ai-skills/) architecture by Thomas Costello.

---

## Installation

### 1. Get Claude

This toolkit runs on [Claude](https://claude.ai) by Anthropic. You need one of the following:

**Option A — Claude.ai (browser, easiest)**
1. Go to [claude.ai](https://claude.ai) and create a free account
2. Upgrade to Claude Pro for best results (required for long research sessions)
3. Create a **Project** — this keeps your teacher profile and skills persistent across conversations

**Option B — Claude Desktop (recommended for most teachers)**
1. Download the Claude desktop app for [Mac or Windows](https://claude.ai/download)
2. Sign in with your Anthropic account (or create one)
3. Create a **Project** and add your skill files — works identically to Claude.ai but as a native app
4. Upgrade to Claude Pro for best results

**Option C — Claude Code (terminal, for power users)**
1. Install [Node.js](https://nodejs.org) if you don't have it
2. Install Claude Code:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
3. Authenticate:
   ```bash
   claude
   ```
   Follow the prompts to connect your Anthropic account.

---

### 2. Get This Toolkit

Clone the repository:

```bash
git clone https://github.com/ken-muturi/bible-teacher.git
cd bible-teacher
```

Or [download the ZIP](https://github.com/ken-muturi/bible-teacher/archive/refs/heads/main.zip) and unzip it.

---

### 3. Using the Skills

**With Claude Code** — open the toolkit directory and start Claude:
```bash
cd bible-teacher
claude
```
Claude Code automatically reads the skill files in the directory. Reference any skill by name in conversation:
```
book-overview judges
book-overview-infographic judges --non-constrained
discussion-guide judges
```

**With Claude.ai Projects**
1. Create a new Project in Claude.ai
2. Go to **Project instructions** and paste the contents of `foundation/teacher-foundation/SKILL.md`
3. Add each skill file you want to use as a Project file (or paste into the instructions)
4. Start a conversation and reference the skills by name

---

## Setup (do this once)

1. Open `foundation/teacher-foundation/SKILL.md`
2. Fill in your profile variables — name, teaching context, audience, Bible translation, denominational tradition, posture, and tone
3. The file includes a full list of translation options (ESV, NIV, NLT, KJV, NABRE, NJB, and more) and denominational traditions (Baptist, Catholic, Reformed, Orthodox, Pentecostal, and more) to choose from
4. Every skill output is shaped by this profile — research emphasis, interpretive framing, commentary recommendations, and application bridges all adapt to your tradition and audience

---

## Skills

| Skill | File | What It Does |
|-------|------|--------------|
| Teacher Foundation | `foundation/teacher-foundation/SKILL.md` | Personalizes all outputs with your profile |
| Book Overview | `book-overview/SKILL.md` | Deep research brief for any of the 66 books |
| Book Overview Infographic | `book-overview-infographic/SKILL.md` | HTML visual teaching panel from the research brief |
| Video Outline | `video-outline/SKILL.md` | Talking-points outline for a teaching session |
| Discussion Guide | `discussion-guide/SKILL.md` | Printable one-page study companion for groups |
| Passage Study | `passage-study/SKILL.md` | Deep dive on a verse or chapter — word studies, illustrations, and HTML visual panel |

### Discussion Guide

A one-page printable HTML resource generated from the completed teaching outline. Designed for small groups, classrooms, or self-study — no prior Bible knowledge assumed.

Each guide includes:
- **Before you engage** — 3 questions anyone can answer before the session
- **Key terms** — plain-language definitions, no jargon
- **Discussion questions** — tagged by type (Observation / Context / Application); no yes/no questions, no easy answers
- **Going deeper** — one book, one resource, one passage to read alongside
- **Closing thought** — one sentence on what this book uniquely contributes

Output: `guides/discussions/<book>-discussion-guide.html` — print-ready via browser.

![Judges Discussion Guide](guides/discussions/screenshots/judges-discussion-guide.png)

---

## Workflow Per Book

```
1. Run book-overview             →  research brief
2. Run book-overview-infographic →  HTML visual teaching panel
3. Run video-outline             →  talking-points structure
4. Run discussion-guide          →  companion resource
5. python3 scripts/to-pdf.py --all  →  PDF versions of all guides
```

---

## PDF Export

Convert any HTML guide or visual panel to PDF:

```bash
# Install dependency (once)
pip3 install -r requirements.txt

# Convert a specific file
python3 scripts/to-pdf.py guides/discussions/judges-discussion-guide.html

# Convert all guides and panels at once
python3 scripts/to-pdf.py --all
```

Discussion guides export as A4 portrait. Visual panels export as A3 landscape.
PDFs are saved alongside the HTML files in the same folder.

---

## Infographic Layout Modes

```
book-overview-infographic genesis                      # 3-column grid (default)
book-overview-infographic judges --non-constrained     # theme-driven layout
```

The default 3-column layout is consistent and printable across all 66 books.
`--non-constrained` lets the layout emerge from the book's own structure.

---

## Sample Infographics

### Judges — `--non-constrained` (downward descent layout)
The layout mirrors the book's spiral: each judge card is indented further right as quality deteriorates, collapsing into a dark zone for chapters 17–21 where no judge appears.

![Judges Teaching Panel](guides/visuals/screenshots/judges-panel.png)

---

### Leviticus — `--non-constrained` (two-part arc layout)
Structured around the two halves of the book with the Day of Atonement (ch. 16) as the red hinge between "Approaching God" and "Living as Holy."

![Leviticus Teaching Panel](guides/visuals/screenshots/leviticus-panel.png)

---

### Romans — `--non-constrained` (argument cascade layout)
Four numbered movements flow downward from the thesis (1:16–17), each feeding logically into the next: Problem → Solution → Israel Question → Practice.

![Romans Teaching Panel](guides/visuals/screenshots/romans-panel.png)

---

### Amos — 3-column (default layout)
Standard three-column grid: left holds identity, the compact trap diagram, and three-sermon summary; center holds the indictment/requirement contrast, key passage, five visions, and confrontation; right holds key words, cross-links, and application.

![Amos Teaching Panel 3-Column](guides/visuals/screenshots/amos-panel-3col.png)

---

### Amos — `--non-constrained` (funnel trap layout)
The rhetorical trap structure drives the layout: six nations flow across the top, close down through Judah, then snap onto Israel — visually enacting what Amos does rhetorically in chapters 1–2. Below: the indictment vs. requirement contrast, the full-width 5:24 passage, five escalating visions, and the application grid.

![Amos Teaching Panel](guides/visuals/screenshots/amos-panel.png)

---

## Channel Curriculum

See `CURRICULUM.md` for the full 66-book curriculum organized into 9 playlist series.

**Suggested starting order:** Mark → Genesis → Romans → Psalms

---

## Philosophy

These are research and structure tools. They do not teach for you.
The historical knowledge, interpretive judgment, and application are yours.
