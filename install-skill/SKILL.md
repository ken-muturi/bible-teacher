# Install Skill — Install one skill or all skills from a URL

## Trigger
Any message matching:
- `install skills from <url>`
- `install all skills: <url>`
- `install skill <url>`
- `install: <url>`
- User pastes any GitHub URL (repo root, blob, or raw) and says "install"

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

1. **Fetch** the JSON manifest.
2. **Parse** the `skills` array. Each item has:
   - `id` — directory name
   - `name` — human label
   - `url` — raw URL to the SKILL.md
3. **For each skill**, in order:
   - If `<id>/SKILL.md` already exists → skip, mark as "already installed"
   - Otherwise fetch `url` and write to `<id>/SKILL.md`
   - Special case: if `id` is `"foundation"`, write to `foundation/teacher-foundation/SKILL.md`
4. **Output a confirmation table**:

```
✓ Installed all skills from <repo>

  ✓ install-skill             install-skill/SKILL.md
  ✓ foundation                foundation/teacher-foundation/SKILL.md
  ✓ book-overview-infographic book-overview-infographic/SKILL.md
  ✓ passage-study             passage-study/SKILL.md
  ✓ discussion-guide          discussion-guide/SKILL.md

Ready. Try:
  passage-study Romans 8:1–11
  book-overview Amos
  discussion-guide Judges
```

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
