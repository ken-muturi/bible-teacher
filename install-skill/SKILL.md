# Install Skill — Fetch and install a skill from a URL

## Trigger
Any message matching:
- `install skill <url>`
- `install: <url>`
- `install this skill: <url>`
- User pastes a raw GitHub URL ending in `SKILL.md` and says "install"

## What this skill does
Fetches a remote SKILL.md file, determines the correct local directory name,
writes it into the current project, and confirms installation.

---

## Steps

### 1 — Fetch the SKILL.md
Use WebFetch (or curl via Bash) to retrieve the content at the URL.

If the URL is a GitHub repo page (not raw), convert it to the raw URL:
- `github.com/<user>/<repo>/blob/<branch>/<path>` →
  `raw.githubusercontent.com/<user>/<repo>/<branch>/<path>`

### 2 — Determine the skill directory name
Read the first `# Heading` in the fetched SKILL.md.
Extract the skill name from it — lowercase, hyphens for spaces, strip "—" and subtitles.

Examples:
- `# Passage Study — Verse and Chapter Deep Dive` → `passage-study`
- `# Book Overview Infographic` → `book-overview-infographic`
- `# Discussion Guide` → `discussion-guide`

If you cannot determine the name from the heading, derive it from the last path segment
of the URL before `/SKILL.md`.

### 3 — Write the file
Create the directory if it doesn't exist:
```
<project-root>/<skill-name>/SKILL.md
```

Write the fetched content verbatim.

### 4 — Confirm
Output exactly:

```
✓ Installed: **<skill-name>**
  Source: <url>
  Location: <skill-name>/SKILL.md

You can now use it — try: `<example-trigger>`
```

Extract the example trigger from the SKILL.md's **Trigger** or **Usage** section.
If none found, use the skill directory name as the trigger.

---

## Edge cases

- **Already installed**: If `<skill-name>/SKILL.md` already exists, ask:
  "Skill `<name>` is already installed. Overwrite? (yes / no)"
  Wait for confirmation before writing.

- **Unreachable URL**: If the fetch fails, report the error clearly and stop.
  Do not write a partial file.

- **Wrong file type**: If the fetched content does not look like a SKILL.md
  (no `#` heading, no trigger section), warn:
  "This doesn't look like a valid SKILL.md. Install anyway? (yes / no)"

---

## Notes
- Never modify the fetched content — write it exactly as received.
- This skill installs into the **current project directory** (where `.claude/` lives).
- To install into a different project, the user must run the command from that project.
