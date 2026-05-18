# Install Skill — Install one skill or all skills from a URL

## Trigger
Any message matching:
- `install skills from <url>`
- `install all skills: <url>`
- `install skill <url>`
- `install: <url>`
- `update skills` — updates all already-installed skills to their latest versions
- `update skills from <url>` — updates from a specific repo
- User pastes any GitHub URL (repo root, blob, or raw) and says "install" or "update"

---

## Step 0 — Resolve the URL

Before doing anything, normalise the URL:

| What the user pastes | Resolve to |
|---|---|
| `https://github.com/<user>/<repo>` | `https://raw.githubusercontent.com/<user>/<repo>/main/skills.json` |
| `https://github.com/<user>/<repo>/blob/<branch>/<path>` | `https://raw.githubusercontent.com/<user>/<repo>/<branch>/<path>` |
| `https://raw.githubusercontent.com/...` | Use as-is |
| Any URL ending in `skills.json` | Batch install mode |
| Any URL ending in `SKILL.md` | Single install mode |

When the URL is a **repo root** (no path after the repo name), always append `/main/skills.json` on the raw host.

---

## Mode A — Batch install from `skills.json`

Triggered when the resolved URL ends in `skills.json`.

Determine the **mode flag** from the user's message:
- "install" → **install mode**: skip skills that already exist
- "update" → **update mode**: overwrite all skills with the latest version

1. **Fetch** the JSON manifest.
2. **Parse** the `skills` array. Each item has:
   - `id` — directory name
   - `name` — human label
   - `url` — raw URL to the SKILL.md
3. **For each skill**, in order:
   - Special case: if `id` is `"foundation"`, the path is `foundation/teacher-foundation/SKILL.md`
   - Otherwise the path is `<id>/SKILL.md`
   - **Install mode**: if the file already exists → skip, mark as "already installed"
   - **Update mode**: always fetch and overwrite, mark as "updated" or "already up to date" (if content unchanged)
   - Write fetched content verbatim to the path
4. **Output a confirmation table**:

```
✓ Installed all skills from <repo>         ← install mode
✓ Updated all skills from <repo>           ← update mode

  ✓ install-skill             install-skill/SKILL.md          [installed / updated / skipped]
  ✓ foundation                foundation/teacher-foundation/SKILL.md
  ✓ book-overview-infographic book-overview-infographic/SKILL.md
  ✓ passage-study             passage-study/SKILL.md
  ✓ discussion-guide          discussion-guide/SKILL.md
  ✓ bible-timeline            bible-timeline/SKILL.md

Ready. Try:
  passage-study Romans 8:1–11
  book-overview Hosea
  bible-timeline full
```

### If the user just says `update skills` with no URL
Look for a `skills.json` manifest in the current project (check if any `*/SKILL.md` files exist and find their source repo from the `url` field inside the file, or default to `https://github.com/ken-muturi/bible-teacher`). Then run update mode against that URL.

---

## Mode B — Single install from `SKILL.md`

Triggered when the resolved URL ends in `SKILL.md`.

1. **Fetch** the content at the URL.
2. **Determine the skill directory name**
   - Read the first `# Heading`. Lowercase, replace spaces with hyphens, strip subtitles after `—`.
   - Fallback: last path segment before `/SKILL.md`.
3. **Check for existing install** — if `<skill-name>/SKILL.md` exists, ask to confirm overwrite.
4. **Write** content verbatim to `<skill-name>/SKILL.md`.
5. **Confirm**:

```
✓ Installed: <skill-name>
  Location: <skill-name>/SKILL.md

Try: <trigger from SKILL.md>
```

---

## Edge cases
- **Unreachable URL**: report the error, skip that skill, complete all others, list failures at the end.
- **No `skills.json` at repo root**: tell the user the repo doesn't have a skills manifest at `/main/skills.json` and ask them to provide the direct URL.
- **Partial failure**: install everything that succeeds, report failures clearly.
- Never modify fetched content — write verbatim.
- Installs into the **current project** (where `.claude/` lives).
