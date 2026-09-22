#!/usr/bin/env python3
"""
migrate_categories.py — migrate discussion guides and simple teachings to
the master base.css (their whole shared template now lives in base, scoped
under body.discuss / body.simple).

  discuss : remove all inline <style> blocks, add one markers block in
            <head>, tag <body class="discuss">. (No per-page CSS — the
            template is identical across guides.)
  simple  : replace the head <style> with markers + per-page accent tokens
            (detected from the page's own colours), tag <body class="simple">.

Run scripts/build_guides.py afterwards to inject base.css into the markers.

Usage:
  python3 scripts/migrate_categories.py discuss guides/discussions/*.html
  python3 scripts/migrate_categories.py simple  guides/passages/*simple*.html
"""
import re, sys, pathlib

MARKERS = "  <style>\n/* @base:start */\n/* @base:end */\n  </style>"

def grab(pat, s, default):
    m = re.search(pat, s, re.IGNORECASE|re.DOTALL)
    return m.group(1) if m else default

def migrate_discuss(text):
    text = re.sub(r'[ \t]*<style>.*?</style>\n?', '', text, flags=re.DOTALL)   # drop all inline styles
    text = text.replace("</head>", MARKERS + "\n</head>", 1)                    # one markers block
    text = re.sub(r'<body[^>]*>', '<body class="discuss">', text, count=1)
    return text

def migrate_simple(text):
    style = re.search(r'<style>(.*?)</style>', text, re.DOTALL).group(1)
    kv = re.search(r'\.key-verse\s*\{([^}]*)\}', style)
    kvb = kv.group(1) if kv else ""
    accent      = grab(r'border:\s*[\d.]+px\s+solid\s+(#[0-9a-fA-F]{3,6})', kvb, "#c0392b")
    accent_soft = grab(r'background:\s*(#[0-9a-fA-F]{3,6})', kvb, "#fdf2f2")
    accent_ink  = grab(r'\.plain strong\s*\{[^}]*color:\s*(#[0-9a-fA-F]{3,6})', style, "#a5302a")
    tokens = (f":root {{ --accent:{accent}; --accent-soft:{accent_soft}; "
              f"--accent-ink:{accent_ink}; }}")
    new_style = "<style>\n/* @base:start */\n/* @base:end */\n\n  " + tokens + "\n  </style>"
    text = re.sub(r'<style>.*?</style>', lambda m: new_style, text, count=1, flags=re.DOTALL)
    text = re.sub(r'<body[^>]*>', '<body class="simple">', text, count=1)
    print(f"    accent={accent} soft={accent_soft} ink={accent_ink}")
    return text

def main():
    mode = sys.argv[1]
    fn = {"discuss": migrate_discuss, "simple": migrate_simple}[mode]
    for a in sys.argv[2:]:
        p = pathlib.Path(a)
        t = p.read_text(encoding="utf-8")
        if "/* @base:start */" in t:
            print(f"SKIP (migrated): {p.name}"); continue
        print(f"{mode}: {p.name}")
        p.write_text(fn(t), encoding="utf-8")

if __name__ == "__main__":
    main()
