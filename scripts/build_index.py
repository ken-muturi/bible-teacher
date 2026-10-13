#!/usr/bin/env python3
"""
build_index.py — make sure every guide has a card on the home page.

Scans guides/**/*.html and, for any guide that is not yet linked from
index.html, inserts a gallery card into the matching section. It is
idempotent: a guide that already has a card (by href) is left alone, so
this is safe to run on every push / pull request.

Card text is derived from the guide itself (its <title> and subtitle) and
its contributor is read from git history (the author who first added the
file), so community submissions show up on the home page automatically,
credited, with no hand-editing.

Usage:
    python3 scripts/build_index.py            # add any missing cards
    python3 scripts/build_index.py --check     # report only, write nothing
"""
import re, sys, subprocess, pathlib
import html as H

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

# Commit-author names treated as the maintainer (no "contributed by" note).
MAINTAINERS = {"kenneth muturi", "muturiken", "ken muturi", "ken-muturi", "ken"}


def classify(rel):
    """rel like 'guides/sermons/x.html' -> (section_label, <a> attrs, book-style, badge)."""
    name = rel.rsplit("/", 1)[-1]
    if rel.startswith("guides/sermons/"):
        return ("Sermon Outlines", 'class="guide-card card-green"', "",
                '<span class="card-badge badge-preach">Preaching</span>')
    if rel.startswith("guides/discussions/"):
        return ("Discussion Guides", 'class="guide-card card-orange"', "", "")
    if rel.startswith("guides/visuals/"):
        if name.endswith("-infographics.html"):
            return ("Message Infographics", 'class="guide-card card-gold"', "",
                    '<span class="card-badge badge-video">Video slides</span>')
        if "comparison" in name:
            return ("Book &amp; Passage Comparisons",
                    'class="guide-card" style="border-color:#2e8a4a; background:#eaf4ee;"',
                    ' style="color:#2c2c2c;"', "")
        return ("Book Overview Panels", 'class="guide-card card-blue"', "", "")
    if rel.startswith("guides/passages/"):
        badge = '<span class="card-badge badge-deep">Deep</span>' if "deep" in name else ""
        return ("Passage Studies", 'class="guide-card card-purple"', "", badge)
    return (None, None, None, None)


def title_of(text, stem):
    m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    title = (m.group(1) if m else stem).strip()
    # Drop the "— Deep Study" / "(Simple Teaching)" style suffixes.
    title = re.split(r"\s*[—\-–]\s*(?:deep study|passage study|sermon outline|"
                     r"simple teaching|message infographics?|comparison|"
                     r"correlation|discussion guide|panel)\b",
                     title, flags=re.I)[0]
    title = re.sub(r"\s*\((?:deep study|simple teaching|deep)\)\s*$", "", title, flags=re.I)
    return re.sub(r"\s+", " ", title).strip() or stem


def subtitle_of(text):
    for cls in ("header-title", "head-sub", "subtitle", "title", "head-kicker"):
        m = re.search(r'class="' + cls + r'"[^>]*>(.*?)</div>', text, re.S | re.I)
        if m:
            s = re.sub(r"<[^>]+>", "", m.group(1))
            s = re.sub(r"\s+", " ", s).strip()
            if s:
                return s
    return ""


def contributor(rel):
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--diff-filter=A",
             "--format=%an", "--", rel],
            capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return None
    if not out:
        return None
    name = out.splitlines()[-1].strip()
    return None if name.lower() in MAINTAINERS else name


def insert_card(index_text, section_label, card_html):
    """Insert card as the first item of the section's .guide-list."""
    pos = index_text.find(f">{section_label}</div>")
    if pos == -1:
        return index_text, False
    gl = index_text.find('<div class="guide-list">', pos)
    if gl == -1:
        return index_text, False
    at = gl + len('<div class="guide-list">')
    return index_text[:at] + "\n" + card_html + index_text[at:], True


def main():
    check = "--check" in sys.argv
    text = INDEX.read_text(encoding="utf-8")
    linked = set(re.findall(r'href="(guides/[^"]+\.html)"', text))
    added, unplaced = 0, []

    for path in sorted((ROOT / "guides").rglob("*.html")):
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if rel in linked:
            continue
        section, attrs, book_style, badge = classify(rel)
        if not section:
            continue
        gtext = path.read_text(encoding="utf-8")
        title = title_of(gtext, path.stem)
        desc = subtitle_of(gtext)
        who = contributor(rel)
        if who:
            desc = (desc + " · " if desc else "") + f"contributed by {H.escape(who)}"
        badge_line = ("          " + badge + "\n") if badge else ""
        card = (f'        <a {attrs} href="{rel}">\n'
                f'          <div class="card-book"{book_style}>{H.escape(title)}</div>\n'
                f'          <div class="card-type">{desc or "Community contribution"}</div>\n'
                f'{badge_line}'
                f'        </a>')
        new_text, ok = insert_card(text, section, card)
        if ok:
            text = new_text
            added += 1
            print(f"{'would add' if check else 'added'} card: {rel}  →  {section}")
        else:
            unplaced.append(rel)

    if added and not check:
        INDEX.write_text(text, encoding="utf-8")
    for u in unplaced:
        print(f"!! could not place (section missing): {u}")
    print(f"\n{added} card(s) {'would be added' if check else 'added'}; "
          f"{len(unplaced)} unplaced.")


if __name__ == "__main__":
    main()
