#!/usr/bin/env python3
"""
migrate_panels.py — migrate STANDARD book-overview panels to base.css.

Only panels that use the standard panel template (header-wrap + .main at
1020px + the shared word/comm/hard/then-now/verdict components) should be
passed in. Bespoke panels (timelines, comparisons, 3-column and one-off
layouts) are intentionally left self-contained.

Strips the now-shared base rules, keeps each panel's unique parts (acts /
units / chap-map / signature strips), and rewraps with markers +
:root{ --main-max:1020px; accent tokens }. Run build_guides.py after.

Usage:
  python3 scripts/migrate_panels.py [--dry] guides/visuals/esther-panel.html ...
"""
import re, sys, pathlib
from migrate_deepstudy import split_top_level, grab, START, BASE   # reuse helpers

PANEL_BASE = {
    "html", "*,*::before,*::after", "body",
    ".home-nav", ".home-nav-link", ".home-nav-link:hover", ".main", ".section-label",
    ".passage-callout", ".pc-label", ".pc-text", ".pc-heb", ".pc-ref",
    ".word-grid", ".word-card", ".word-heb", ".word-greek", ".word-gk",
    ".word-translit", ".word-count", ".word-gloss", ".word-note",
    ".comm-grid", ".comm-card", ".comm-author", ".comm-title", ".comm-tradition",
    ".trad-reformed", ".trad-evangelical", ".trad-preaching", ".trad-pastoral",
    ".trad-critical", ".trad-catholic", ".trad-jewish",
    ".comm-point", ".comm-point:last-of-type", ".source-link", ".source-link:hover",
    ".hard-box", ".hard-title", ".hard-item", ".hard-item:last-child", ".hard-q", ".hard-a",
    ".then-now", ".tn-label", ".tn-cols", ".tn-col-label", ".tn-text", ".tn-question",
    ".verdict", ".verdict-label", ".verdict-text", ".verdict-ref",
    ".header-wrap", ".header-top", ".header-book", ".header-sub", ".header-meta",
    ".meta-row", ".meta-rowstrong", ".header-char",
}
ROOT = pathlib.Path(__file__).resolve().parent.parent

def migrate(path, dry):
    text = path.read_text(encoding="utf-8")
    if START in text:
        print(f"SKIP (migrated): {path.name}"); return
    m = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
    if not m:
        print(f"SKIP (no <style>): {path.name}"); return
    inner = m.group(1)

    accent      = grab(r'\.header-char\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#3b6fd4")
    pc = re.search(r'\.passage-callout\s*\{([^}]*)\}', inner)
    pcb = pc.group(1) if pc else ""
    accent_soft = grab(r'background:\s*(#[0-9a-fA-F]{3,6})', pcb, "#eef2fb")
    accent_lt   = grab(r'\.hard-q\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#7eb8f7")
    accent_mid  = grab(r'\.tn-col-label\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#6f9ae0")
    accent_hair = grab(r'\.tn-question\s*\{[^}]*dashed\s+(#[0-9a-fA-F]{3,6})', inner, "#b8ccef")
    accent_ink  = grab(r'\.companion-link:hover\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, accent)

    kept = []
    for trivia, rule, kind in split_top_level(inner):
        if kind in ('@import', '@stmt'):
            continue
        if kind in PANEL_BASE:
            continue
        kept.append(trivia + rule)
    page_css = "".join(kept).strip("\n")

    tokens = (f":root {{\n  --main-max: 1020px;\n  --accent: {accent};\n"
              f"  --accent-soft: {accent_soft};\n  --accent-ink: {accent_ink};\n"
              f"  --accent-lt: {accent_lt};\n  --accent-mid: {accent_mid};\n"
              f"  --accent-hair: {accent_hair};\n}}")
    new_style = ("<style>\n" + START + "\n/* @base:end */\n\n" + tokens + "\n\n"
                 + page_css + "\n  </style>")
    updated = text[:m.start()] + new_style + text[m.end():]
    print(f"{'DRY ' if dry else ''}{path.name}  accent={accent} soft={accent_soft} lt={accent_lt}")
    if not dry:
        path.write_text(updated, encoding="utf-8")

def main():
    dry = "--dry" in sys.argv
    for a in [x for x in sys.argv[1:] if x != "--dry"]:
        migrate(pathlib.Path(a).resolve(), dry)

if __name__ == "__main__":
    main()
