#!/usr/bin/env python3
"""
migrate_deepstudy.py — one-time migration of deep-study guides to the
shared base.css + marker system.

For each file it:
  1. detects the page's accent colours from its existing CSS,
  2. removes the shared base rules (they now live in base.css),
  3. rebuilds <style> as:  markers+base  +  :root accent override  +  the
     page's own unique rules (kept verbatim).

Page-specific rules and @media blocks are preserved untouched. Safe to
inspect first with --dry.

Usage:
    python3 scripts/migrate_deepstudy.py --dry  guides/passages/x.html
    python3 scripts/migrate_deepstudy.py        guides/passages/*.html
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = (ROOT / "styles" / "base.css").read_text(encoding="utf-8").strip("\n")
START, END = "/* @base:start */", "/* @base:end */"

BASE_SELECTORS = {
    "html", "*,*::before,*::after", "body",
    ".home-nav", ".home-nav-link", ".home-nav-link:hover", ".main",
    ".header-ref", ".header-title", ".badge-deep", ".nav-links",
    ".companion-link", ".companion-link:hover", ".section-label",
    ".passage-callout", ".pc-label", ".pc-text", ".pc-heb", ".pc-ref", ".placement",
    ".word-grid", ".word-card", ".word-heb", ".word-greek", ".word-gk",
    ".word-translit", ".word-ref-badge", ".word-gloss", ".word-note",
    ".ot-grid", ".ot-card", ".ot-ref", ".ot-title", ".ot-note",
    ".comm-shelf", ".comm-card", ".comm-author", ".comm-title", ".comm-tradition",
    ".trad-reformed", ".trad-evangelical", ".trad-preaching", ".trad-pastoral",
    ".trad-catholic", ".trad-critical", ".trad-jewish",
    ".comm-point", ".comm-point:last-of-type", ".source-link", ".source-link:hover",
    ".pressure-box", ".pressure-title", ".pressure-item", ".pressure-item:last-child",
    ".pressure-q", ".pressure-a",
    ".xref-grid", ".xref-card", ".xref-card.backward", ".xref-card.parallel",
    ".xref-card.forward", ".xref-tag", ".backward.xref-tag", ".parallel.xref-tag",
    ".forward.xref-tag", ".xref-ref", ".xref-note",
    ".then-now", ".tn-label", ".tn-cols", ".tn-col-label", ".tn-text", ".tn-question",
    ".verdict", ".verdict-label", ".verdict-text", ".verdict-ref",
}

def consume_block(css, k):          # k points at '{'
    depth = 0
    for i in range(k, len(css)):
        if css[i] == '{': depth += 1
        elif css[i] == '}':
            depth -= 1
            if depth == 0: return i + 1
    return len(css)

def split_top_level(css):
    """Yield (trivia, rule_text, kind) for each top-level rule/at-rule.
    kind is the whitespace-stripped selector, or '@import'/'@block'."""
    segs, i, n = [], 0, len(css)
    while i < n:
        j = i
        while j < n:                # skip whitespace + comments (trivia)
            if css[j] in ' \t\r\n': j += 1
            elif css[j:j+2] == '/*':
                k = css.find('*/', j+2); j = (k+2) if k != -1 else n
            else: break
        trivia = css[i:j]
        if j >= n:
            segs.append((trivia, "", None)); break
        start = j
        if css[j] == '@':
            k = j
            while k < n and css[k] not in '{;': k += 1
            if k < n and css[k] == ';':
                rule = css[start:k+1]
                kind = '@import' if rule.lstrip().lower().startswith('@import') else '@stmt'
                segs.append((trivia, rule, kind)); i = k + 1
            else:
                end = consume_block(css, k)
                segs.append((trivia, css[start:end], '@block')); i = end
        else:
            k = css.find('{', j)
            if k == -1:
                segs.append((trivia, css[start:], None)); break
            selector = css[j:k]
            end = consume_block(css, k)
            segs.append((trivia, css[start:end], ''.join(selector.split()))); i = end
    return segs

def grab(pattern, css, default):
    m = re.search(pattern, css, re.IGNORECASE)
    return m.group(1) if m else default

def migrate(path, dry):
    text = path.read_text(encoding="utf-8")
    if START in text:
        print(f"SKIP (already migrated): {path.relative_to(ROOT)}"); return
    m = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
    if not m:
        print(f"SKIP (no <style>): {path.relative_to(ROOT)}"); return
    inner = m.group(1)

    pc = re.search(r'\.passage-callout\s*\{([^}]*)\}', inner)
    pc_body = pc.group(1) if pc else ""
    accent      = grab(r'border-left:\s*[\d.]+px\s+solid\s+(#[0-9a-fA-F]{3,6})', pc_body, "#6c4bbf")
    accent_soft = grab(r'background:\s*(#[0-9a-fA-F]{3,6})', pc_body, "#f2eefb")
    accent_ink  = grab(r'\.companion-link:hover\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#4f349c")
    accent_lt   = grab(r'\.pressure-q\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#b795ea")
    accent_mid  = grab(r'\.tn-col-label\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', inner, "#8a6fd0")
    accent_hair = grab(r'\.tn-question\s*\{[^}]*dashed\s+(#[0-9a-fA-F]{3,6})', inner, "#c9b8ee")

    kept = []
    for trivia, rule, kind in split_top_level(inner):
        if kind in ('@import', '@stmt'):        # base owns the font @import
            continue
        if kind in BASE_SELECTORS:              # now lives in base.css
            continue
        kept.append(trivia + rule)
    page_css = "".join(kept).strip("\n")

    tokens = (f":root {{\n  --accent: {accent};\n  --accent-soft: {accent_soft};\n"
              f"  --accent-ink: {accent_ink};\n  --accent-lt: {accent_lt};\n"
              f"  --accent-mid: {accent_mid};\n  --accent-hair: {accent_hair};\n}}")

    new_style = ("<style>\n" + START + "\n" + BASE + "\n" + END + "\n\n"
                 + tokens + "\n\n" + page_css + "\n  </style>")
    updated = text[:m.start()] + new_style + text[m.end():]

    print(f"{'DRY ' if dry else ''}{path.relative_to(ROOT)}  "
          f"accent={accent} soft={accent_soft} ink={accent_ink} lt={accent_lt} mid={accent_mid} hair={accent_hair}")
    if dry:
        sys.stdout.write(new_style[:1200] + "\n...\n")
    else:
        path.write_text(updated, encoding="utf-8")

def main():
    args = [a for a in sys.argv[1:] if a != "--dry"]
    dry = "--dry" in sys.argv
    for a in args:
        migrate(pathlib.Path(a).resolve(), dry)

if __name__ == "__main__":
    main()
