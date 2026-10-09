---
name: submit-guide
description: Publish the guide just made to the shared library. Use when the user says "submit this", "commit this", "publish this", or "add this to the library" after a guide has been generated.
argument-hint: "(say it right after a guide is made)"
---

# Submit / Commit a Guide

When the user says **"submit this"** or **"commit this"** (or publish / add to the
library), take the guide you just made and get it into the repo
**github.com/ken-muturi/bible-teacher** — the simplest way that actually works here.
Never make the user learn git or type commands.

---

## Step 1 — identify the file

- Use the **most recent guide** you produced in this chat. If it's unclear which one,
  ask "which guide?" in one line.
- **Folder by type:**
  - sermon outline → `guides/sermons/`
  - passage study or simple one-page teaching → `guides/passages/`
  - book panel, infographic deck, or comparison → `guides/visuals/`
  - discussion guide → `guides/discussions/`
- **Filename:** short, lowercase, hyphenated, ending in `.html`
  (e.g. `communion-with-the-spirit-outline.html`).

## Step 2 — submit, using the first method that works here

**A — You can run commands and git (e.g. Claude Code inside the repo).**
Save the file to the folder, run `python3 scripts/build_guides.py` (this injects the
shared stylesheet and stamps the contributor byline), then commit on a **new branch**
and open a pull request to `main` (default), or push directly if the user asks.
Report the file path and the commit/PR link.

**B — A GitHub tool/connector is available (can create files / commit).**
Create the file at the chosen path on a new branch through it and open a pull request
to `main`. Report the PR link.

**C — No file or GitHub access (phone or web Project chat).**
You can't push from here, so hand it off in the fewest taps:
1. Show the complete guide in **one** ` ```html ` code block (so the copy button grabs
   all of it).
2. Give a tappable link that opens GitHub's "create new file" page with the path
   already filled in:
   `https://github.com/ken-muturi/bible-teacher/new/main?filename=<folder>/<slug>.html`
3. Say exactly this, short: **"Tap *Copy* above, open that link (sign in if asked),
   *paste* into the box, and tap *Commit changes*. Done."**

The person must be a **collaborator** on the repo (the maintainer adds them once). If
branch protection is on, step C's commit screen will offer "create a new branch and
start a pull request" — tell them to use that and tap the green button.

---

## Rules

- Keep it to the fewest steps; don't explain git.
- One guide per file; keep the HTML fully self-contained (inline CSS).
- Never put passwords, keys, or personal data into a guide.
- You'll be credited automatically (the build stamps a "Contributed by …" byline from
  your GitHub commit) — so submit from **your own** account.
