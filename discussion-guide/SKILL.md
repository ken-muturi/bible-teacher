# Discussion Guide — Small-Group Lesson Skill

Produces a printable **small-group meeting guide** for a passage or topic. The guide is a
complete meeting agenda: it moves a group from arrival through worship, a Bible lesson,
accountability, and community, to closing. This is a standalone resource a leader can run
a meeting from directly.

**Prerequisite:** teacher-foundation. A completed passage-study or book-overview for the
same text is helpful but not required.

---

## Input

Provide:
- **Passage or topic** (e.g., "Matthew 16:24–26" or "Commitment / Take Up Your Cross")
- **Theme title** (optional — a short label like "Commitment," "Faith," "Forgiveness";
  if omitted, derive one from the passage)
- **Series context** (optional — e.g., "week 5 of a discipleship series"; affects the
  Accountability section's memory-verse recall count)
- **Group context** (optional — "small group of 6–8 adults," "youth group," "self-study")

---

## Output Structure

The guide follows a fixed six-part meeting flow. Sections I, II, IV, V, and VI use standard
framing instructions (below) — lightly adaptable but kept consistent so groups know the rhythm.
The **variable teaching content** is generated for Section III (Lesson Time).

### Title
Format: **`[Theme]: [Short Title], [Passage]`**
Example: `Commitment: Take Up Your Cross, Matthew 16:24–26`

---

### I. CONNECTING
Standard framing (adapt lightly to the theme):
> *Share what happened in your lives during the last week. Use an ice-breaker or other
> approach to get to know each other better.*

Optionally add one theme-tied ice-breaker question.

---

### II. SEEKING GOD
Standard framing:
> *(If your group is larger than 8 persons, break into groups of 3–4 for this.) Discuss any
> personal roadblocks, challenges, or fears that threaten your ability to walk by faith.
> Pray about things that will really make a difference in your life today.*

---

### III. LESSON TIME

This is the generated heart of the guide. It contains five parts:

**Observation** (3–5 numbered questions)
What the text actually says and means. Draw out structure, key words, contrasts, and
cultural/historical background. These should send the group back into the verses.

**Application** (3–4 numbered questions)
What the text means for how we think and live. At least one should press personal
self-examination; one may be a True/False or a sharpening prompt.

Rules for all questions:
- No yes/no questions that close down discussion (a deliberate True/False used to provoke
  debate is fine)
- No questions with a single obvious "right" answer
- At least one question that does not have a tidy answer
- Number Observation and Application separately, each starting at 1

**Prayer**
A short written prayer (3–5 lines) the group can pray together, drawn directly from the
lesson's theme. Plain, first-person-plural ("we"), no archaic language required.

**Quote**
One real, relevant quotation from a recognised Christian voice (e.g., a church father,
reformer, or respected teacher), **with attribution**. It should sharpen or deepen the
lesson's theme. Flag for checking: **[VERIFY QUOTE]**.

**Memory Verse**
One verse reference (usually from the passage) chosen as the week's verse to memorise.
Give the reference; optionally include the text.

---

### IV. ACCOUNTABILITY
Standard framing (adjust the memory-verse count to the series week if known):
> *Break into small groups of 3–4 persons. Recite your memory verses from the last few
> weeks. Share what you have done/learned in your daily devotion times. Share how you have
> sought opportunities to build relationships with unbelievers on your evangelism list, and
> the outcome of this.*

---

### V. BUILDING COMMUNITY
Standard framing:
> *Do an exercise or have a discussion that builds stronger and deeper relationships. Make
> announcements and plans that affect the entire group.*

---

### VI. CLOSING
Standard framing:
> *Close in prayer. Enjoy refreshments and fellowship.*

---

## File Output

Save to: `guides/discussions/<passage-or-topic-slug>-discussion-guide.html`
(e.g., `matthew-16-24-26-discussion-guide.html`)

Match the house visual style used across the site:
- Font: one serif family throughout — `Gentium Book Plus` (a Bible-typesetting serif, SIL),
  Google Fonts import, 18px base:
  `@import url('https://fonts.googleapis.com/css2?family=Gentium+Book+Plus:ital,wght@0,400;0,700;1,400;1,700&display=swap');`
- Background `#f5f0e8`, page card `#faf7f2`, borders `2–3px solid #2c2c2c`
- Roman-numeral section headings in Gentium (bold/roman); the standard framing text in small,
  letter-spaced caps (as in the source sheet); questions and prose in Gentium roman
- Tag Observation vs Application blocks; number questions within each
- `.home-nav` back-to-index link; `@media print` hides nav and fits one to two pages

After saving, navigate the preview to the file and confirm with a clickable link.

Then add an index card under the **Discussion Guides** section of `index.html`
(`card-orange`), with the theme + passage as the card title.

---

## Format Rules

- Fits one to two printed pages
- Plain language throughout — no assumed church vocabulary in the questions
- Bold only section labels, question numbers, and the Prayer/Quote/Memory Verse labels
- Do **not** include answers to any question
- Flag any quote or resource needing verification: **[VERIFY QUOTE]** / **[VERIFY]**
