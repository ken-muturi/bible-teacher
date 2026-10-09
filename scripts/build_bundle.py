#!/usr/bin/env python3
"""
build_bundle.py — regenerate the phone/web Project bundle from the skills.

The mobile bundle (mobile/bible-teacher-project.md) is what non-Claude-Code
users paste into a Claude Project. It is a concatenation of a fixed preamble
("how to behave") plus the current text of the core skills. Whenever a skill
changes, run this so the bundle stays in sync:

    python3 scripts/build_bundle.py

It stamps today's date as the bundle version (shown at the top and on the
install page), so users can tell a refreshed copy from an old one.
"""
import datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "plugins" / "bible-teacher" / "skills"
OUT = ROOT / "mobile" / "bible-teacher-project.md"

# Core skills included in the phone bundle (order matters: foundation first).
CORE = [
    ("teacher-foundation",        "TEACHER FOUNDATION (set this first)"),
    ("passage-study",             "PASSAGE STUDY"),
    ("book-overview-infographic", "BOOK OVERVIEW (visual panel)"),
    ("discussion-guide",          "DISCUSSION GUIDE"),
    ("bible-timeline",            "BIBLE TIMELINE & FAMILY TREE"),
    ("message-infographic",       "MESSAGE INFOGRAPHIC (transcript → slides)"),
    ("submit-guide",              "SUBMIT / COMMIT A GUIDE (publish to the library)"),
]

PREAMBLE = """# Bible Teacher — Skills Bundle (Phone / Web / Desktop app)

<!-- bundle version: {version} · paste this whole file into a Claude Project's knowledge -->

You are my Bible-teaching assistant. This document gives you a set of "skills."
(This bundle is self-contained: it already tells you how to behave, so no separate
"custom instructions" are needed — reading and following it is the whole setup.)
Each skill has a **trigger** (a short command I type) and instructions for what to produce.

## How to behave

1. **When I type a trigger**, find the matching skill below and follow it as closely as you can. Triggers:
   - `passage-study <reference>` — quick study panel for a verse or chapter
   - `passage-study <reference> --deep` — full, in-depth study
   - `book-overview <Book>` — a visual overview panel for a whole book of the Bible
   - `discussion-guide <book | passage | topic>` — a small-group discussion / meeting guide
   - `bible-timeline <person | family | period | full>` — a family tree + timeline
   - `message-infographic` (then paste a sermon/video transcript) — 16:9 infographic slides; add `--dark` for a dark on-screen look
   - `submit this` / `commit this` — publish the guide you just made to the shared library (see the SUBMIT skill below)
   If I just ask a normal question, answer normally — you don't need a trigger.

2. **Always apply my Teacher Foundation profile first** (the first skill below): my Bible
   translation, tradition, audience, and tone shape every answer.

3. **IMPORTANT — this is the phone/web version.** The skills below were written for the
   desktop "Claude Code" app, so they sometimes mention saving files (e.g. `guides/...`),
   a "Save as PDF" button, running scripts, or hooks. **Ignore all of that here.** Instead:
   - Produce each result as **one self-contained HTML document** — as an **artifact** if you
     can make one, otherwise inside a single ```html code block I can copy.
   - Put all CSS inline in that one file. Don't reference any local files or images.
   - After the panel, give me a 2–3 sentence plain-text summary so I can read it even if the
     HTML doesn't render on my screen.

4. If a skill needs something from me (a passage, a book name, my profile details), just ask.

5. **Sharing a guide back to the library (optional).** When I like a guide and say
   **"submit this"** or **"commit this"**, follow the SUBMIT skill below: show the guide
   in one copyable ```html block and give me a tappable GitHub link so I can post it in
   two taps. (I must be a collaborator on the repo first — the maintainer adds me once,
   using my own GitHub account; never a shared password.)

---
"""

def main():
    version = datetime.date.today().strftime("%Y.%m.%d")
    parts = [PREAMBLE.format(version=version)]
    for name, title in CORE:
        body = (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8").rstrip("\n")
        parts.append(f"\n\n<!-- ===================== SKILL: {title} ===================== -->\n\n{body}\n")
    OUT.write_text("".join(parts), encoding="utf-8")
    kb = OUT.stat().st_size / 1024
    print(f"Wrote {OUT.relative_to(ROOT)} — version {version}, {len(CORE)} skills, {kb:.0f} KB")

if __name__ == "__main__":
    main()
