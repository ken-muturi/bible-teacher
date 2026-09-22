# Bible Teacher on Your Phone (or Desktop App / Browser) — 5-Minute Setup

This is for people using **Claude in the normal way** — the **phone/tablet app**, the
**Claude desktop app** (Mac/Windows), or **claude.ai in a browser**. No terminal, no downloads,
no code. You copy one block of text in once, and then you can type simple commands like
`passage-study John 3` any time.

Because a Project is tied to your Claude account, **you only set this up once** — do it on
whichever device is easiest, and it's automatically there on your phone, the desktop app, and
the browser.

> The plugin / "install skills" instructions elsewhere are **only for Claude Code** (the
> developer tool — the terminal, or the "Code" tab inside the desktop app). They do **not**
> work in the normal phone/desktop/browser chat. Use these steps instead.

---

## The easiest way — a Project (recommended)

*A "Project" is a Claude workspace that remembers instructions across chats. Projects need a
paid plan (Claude Pro). If you're on the free plan, skip to "No Project? Do this instead" below.*

### Step 1 — Copy the skills text
1. Open this link in your phone's browser:
   **https://raw.githubusercontent.com/ken-muturi/bible-teacher/main/mobile/bible-teacher-project.md**
2. Tap and hold the text → **Select All** → **Copy**. (It's long — that's fine, copy all of it.)

### Step 2 — Make a Project in the Claude app
1. Open the **Claude** app.
2. Tap the menu (☰) → **Projects** → **＋ New Project**.
3. Name it **Bible Teacher**.

### Step 3 — Paste the skills into the Project
1. Open your new **Bible Teacher** project.
2. Find **Project knowledge** (sometimes "Add content" / "＋"), choose **Add text**.
3. **Paste** the text you copied. Give it a title like "Skills" and save.

### Step 4 — Add one line of instructions
1. In the same project, open **Instructions** (or "Set custom instructions").
2. Paste this one line:
   > *You are my Bible teaching assistant. Follow the skills in this project's knowledge. When I type a command like `passage-study`, `book-overview`, `discussion-guide`, or `bible-timeline`, follow the matching skill and show the result as a viewable HTML panel plus a short summary.*
3. Save.

### Step 5 — Use it
Start a new chat **inside the Bible Teacher project** and type, for example:
- `passage-study John 3:16`
- `passage-study Romans 8:1-11 --deep`
- `book-overview Jonah`
- `discussion-guide James`
- `bible-timeline Moses`

Claude will make a teaching panel you can view and copy. The very first time, it may ask you a
few questions to set your profile (translation, tradition, audience) — answer once and it
remembers them in the project.

---

## No Project? (free plan) — Do this instead

Projects need Claude Pro. Without one, you can still use everything — you just paste the skills
at the **start of each new chat**:

1. Open the link from Step 1 above and **copy all** the text.
2. In the Claude app, start a **new chat** and **paste** it as your first message. Send it.
3. Then type your command, e.g. `passage-study Psalm 23`.

That's it — the only difference is you re-paste the block whenever you begin a brand-new chat.

---

## Good to know

- **What you get back:** a nicely formatted HTML teaching panel shown in the chat, plus a short
  written summary. On a phone you can read it, screenshot it, or copy it. (The "save to a file"
  and "Save as PDF" features only exist in the desktop developer version.)
- **Set your profile once:** the first skill in the bundle is your *Teacher Foundation* —
  your Bible translation, tradition, audience, and tone. Tell Claude these once and every panel
  will match your church and style.
- **You don't need to memorize commands.** You can also just ask in plain words, e.g.
  "make me a small-group discussion guide on Philippians 2."
- **Updating:** if the skills are improved later, just repeat Step 1 and Step 3 (paste the newer
  text over the old project knowledge).

---

## Which version am I? (quick guide)

| You use… | Follow… |
|---|---|
| **Claude phone/tablet app** | **This page** (Project or paste-in) |
| **Claude desktop app** — the normal chat / Projects | **This page** (Project or paste-in) |
| **claude.ai** in a web browser | **This page** (Project or paste-in) |
| **Claude Code** — the terminal, or the **"Code" tab** inside the desktop app | The plugin install in the main README — two commands and done |

> Note: the Claude **desktop app** contains *both* worlds — a normal chat/Projects side (use
> this page) and a developer **"Code" tab** (use the plugin install). Pick based on which one
> you actually open.
