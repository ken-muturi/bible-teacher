#!/usr/bin/env python3
"""
build_guides.py — inline the shared base stylesheet into every guide.

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

Usage:
    python3 scripts/build_guides.py            # inject into all guides
    python3 scripts/build_guides.py --check     # report only, write nothing
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = (ROOT / "styles" / "base.css").read_text(encoding="utf-8").strip("\n")
START, END = "/* @base:start */", "/* @base:end */"
PATTERN = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)

def main():
    check = "--check" in sys.argv
    injected, skipped = 0, 0
    for html in sorted((ROOT / "guides").rglob("*.html")):
        text = html.read_text(encoding="utf-8")
        if START not in text or END not in text:
            skipped += 1
            continue
        new_block = f"{START}\n{BASE}\n{END}"
        updated = PATTERN.sub(lambda m: new_block, text, count=1)
        if updated != text:
            injected += 1
            if not check:
                html.write_text(updated, encoding="utf-8")
            print(("would update " if check else "updated ") + str(html.relative_to(ROOT)))
    print(f"\n{injected} guide(s) {'would change' if check else 'updated'}; "
          f"{skipped} without base markers (self-contained / not migrated).")

if __name__ == "__main__":
    main()
