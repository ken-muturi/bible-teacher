#!/usr/bin/env python3
"""
build_guides.py — inline the shared base stylesheet into every guide, and
stamp a contributor byline on guides submitted by other people.

The single source of truth is styles/base.css. Each guide keeps a
self-contained <style> with a marked region:

    <style>
    /* @base:start */
    ...(base.css is auto-injected here)...
    /* @base:end */

    :root { --accent: #....; ... }   /* per-page tokens */
    ...page-specific rules...
    </style>

Running this script re-injects the current base.css between the markers
of every guides/**/*.html that has them, so one edit to base.css
propagates everywhere while each file stays a single portable HTML file.

Contributor byline
------------------
It also stamps a small "Contributed by <name> · <date>" line at the foot of
each guide, read from git history (the author of the commit that first added
the file). This credits people who submit guides from their phone without any
effort on their part. Guides authored by the maintainer (see MAINTAINERS) get
no byline — credit is shown for outside contributors only. The byline lives
between <!-- @credit:start --> / <!-- @credit:end --> markers and is
refreshed (or removed) on every run, so it is safe to re-run anytime.

Usage:
    python3 scripts/build_guides.py            # inject + stamp into all guides
    python3 scripts/build_guides.py --check     # report only, write nothing
"""
import re, sys, subprocess, pathlib
import html as htmllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = (ROOT / "styles" / "base.css").read_text(encoding="utf-8").strip("\n")
START, END = "/* @base:start */", "/* @base:end */"
PATTERN = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)

CSTART, CEND = "<!-- @credit:start -->", "<!-- @credit:end -->"
CREDIT_PATTERN = re.compile(re.escape(CSTART) + r".*?" + re.escape(CEND), re.DOTALL)

# Commit-author names treated as the maintainer: guides they authored get NO
# visible byline (credit is for outside contributors only). Compared
# case-insensitively. Add aliases here if you ever commit under another name.
MAINTAINERS = {"kenneth muturi", "muturiken", "ken muturi", "ken-muturi", "ken"}


def first_author(relpath):
    """(name, YYYY-MM-DD) of the commit that first added the file, or None."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--diff-filter=A",
             "--format=%an%x09%ad", "--date=short", "--", relpath],
            capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return None
    if not out:
        return None
    name, _, date = out.splitlines()[-1].partition("\t")  # earliest "add" commit
    name, date = name.strip(), date.strip()
    return (name, date) if name else None


def credit_block(name, date):
    who = htmllib.escape(name)
    return (
        f"{CSTART}\n"
        f'<div class="contributor-credit" style="max-width:900px;margin:0 auto;'
        f"padding:12px 24px 34px;font-family:\'Gentium Book Plus\',serif;"
        f"font-size:0.78rem;color:#b9b2a6;text-align:center;letter-spacing:0.02em;\">"
        f"Contributed by {who} &middot; {date}</div>\n{CEND}"
    )


def apply_credit(text, relpath):
    """Upsert the byline for outside contributors; strip it otherwise."""
    info = first_author(relpath)
    show = bool(info) and info[0].strip().lower() not in MAINTAINERS
    has_block = CSTART in text and CEND in text

    if show:
        block = credit_block(*info)
        if has_block:
            return CREDIT_PATTERN.sub(lambda m: block, text, count=1)
        idx = text.rfind("</body>")
        if idx == -1:
            return text  # malformed; leave alone
        return text[:idx] + block + "\n" + text[idx:]

    # maintainer-authored or author unknown: ensure no stale byline remains
    if has_block:
        cleaned = CREDIT_PATTERN.sub("", text, count=1)
        return re.sub(r"\n{3,}", "\n\n", cleaned)
    return text


def main():
    check = "--check" in sys.argv
    changed = base_injected = credited = no_markers = 0
    for html in sorted((ROOT / "guides").rglob("*.html")):
        original = html.read_text(encoding="utf-8")
        text = original

        if START in text and END in text:
            text = PATTERN.sub(lambda m: f"{START}\n{BASE}\n{END}", text, count=1)
            if text != original:
                base_injected += 1
        else:
            no_markers += 1

        before_credit = text
        text = apply_credit(text, str(html.relative_to(ROOT)))
        if text != before_credit:
            credited += 1

        if text != original:
            changed += 1
            if not check:
                html.write_text(text, encoding="utf-8")
            print(("would update " if check else "updated ") + str(html.relative_to(ROOT)))

    verb = "would change" if check else "updated"
    print(f"\n{changed} guide(s) {verb} "
          f"(base: {base_injected}, byline: {credited}); "
          f"{no_markers} without base markers (self-contained / not migrated).")


if __name__ == "__main__":
    main()
