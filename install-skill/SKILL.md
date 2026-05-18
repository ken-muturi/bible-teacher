# Install Skill — Fetch and install one skill or all skills from a URL

## Trigger
Any message matching:
- `install skill <url>`
- `install: <url>`
- `install this skill: <url>`
- `install all skills: <url>`
- `install all skills from <url>`
- User pastes a raw GitHub URL ending in `SKILL.md` or `skills.json` and says "install"

---

## Mode A — Install all skills from a manifest

Triggered when the URL ends in `.json` or the message says "all skills".

### Steps

1. **Fetch** the JSON manifest from the URL.

2. **Parse** the `skills` array. Each item has:
   - `id` — the directory name to create
   - `name` — human-readable name
   - `url` — raw URL to the SKILL.md

3. **For each skill in the array**, in order:
   - Check if `<id>/SKILL.md` already exists
   - If it does, skip it (note it as "already installed")
   - If not, fetch the URL and write to `<id>/SKILL.md`

4. **Output a single confirmation table**:

```
✓ Installed all Bible Teacher skills

  ✓ install-skill        → install-skill/SKILL.md
  ✓ foundation           → foundation/teacher-foundation/SKILL.md
  ✓ book-overview-infographic → book-overview-infographic/SKILL.md
  ✓ passage-study        → passage-study/SKILL.md
  ✓ discussion-guide     → discussion-guide/SKILL.md

Ready. Try:
  passage-study Romans 8:1–11
  book-overview Amos
  discussion-guide Judges
```

---

## Mode B — Install a single skill from a SKILL.md URL

Triggered when the URL ends in `SKILL.md`.

### Steps

1. **Fetch** the content at the URL.

2. **Determine the skill directory name**  
   Read the first `# Heading`. Lowercase it, replace spaces with hyphens, strip subtitles after `—`.  
   Fallback: use the path segment before `/SKILL.md` in the URL.

3. **Check for existing install**  
   If `<skill-name>/SKILL.md` already exists, ask:  
   "Skill `<name>` is already installed. Overwrite? (yes / no)"  
   Wait for confirmation before writing.

4. **Write** the fetched content verbatim to `<skill-name>/SKILL.md`.

5. **Confirm**:

```
✓ Installed: <skill-name>
  Source: <url>
  Location: <skill-name>/SKILL.md

Try: <example-trigger>
```

---

## Special case — foundation skill

The foundation skill writes to `foundation/teacher-foundation/SKILL.md` (not `foundation/SKILL.md`).  
If the manifest `id` is `"foundation"`, write to `foundation/teacher-foundation/SKILL.md` and create the nested directory if needed.

---

## Edge cases

- **Unreachable URL**: report the error and skip that skill. Complete all others first, then list failures at the end.
- **Invalid content**: if fetched content has no `#` heading, warn but still write it if the user confirms.
- **Partial manifest failure**: install everything that succeeds, report failures clearly.

---

## Notes
- Never modify fetched content — write verbatim.
- Installs into the **current project** (where `.claude/` lives).
- The manifest URL is: `https://raw.githubusercontent.com/ken-muturi/bible-teacher/main/skills.json`
