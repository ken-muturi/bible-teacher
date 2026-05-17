#!/usr/bin/env python3
"""
Convert HTML teaching guides and visual panels to PDF.

Usage:
    python3 scripts/to-pdf.py guides/discussions/judges-discussion-guide.html
    python3 scripts/to-pdf.py guides/visuals/judges-panel.html
    python3 scripts/to-pdf.py guides/discussions/*.html
    python3 scripts/to-pdf.py --all
"""

import sys
import argparse
from pathlib import Path
from weasyprint import HTML, CSS


DISCUSSION_PRINT_CSS = CSS(string="""
    @page { size: A4; margin: 1.5cm; }
    body { font-size: 10pt; }
""")

PANEL_PRINT_CSS = CSS(string="""
    @page { size: A3 landscape; margin: 1cm; }
    body { font-size: 9pt; }
""")


def to_pdf(html_path: Path) -> Path:
    pdf_path = html_path.with_suffix(".pdf")

    if "discussion" in html_path.name:
        css = DISCUSSION_PRINT_CSS
    else:
        css = PANEL_PRINT_CSS

    HTML(filename=str(html_path.resolve())).write_pdf(
        str(pdf_path),
        stylesheets=[css],
        presentational_hints=True,
    )
    return pdf_path


def main():
    parser = argparse.ArgumentParser(description="Convert HTML guides to PDF")
    parser.add_argument("files", nargs="*", help="HTML file(s) to convert")
    parser.add_argument("--all", action="store_true", help="Convert all HTML guides")
    args = parser.parse_args()

    base = Path(__file__).parent.parent / "guides"

    if args.all:
        targets = list(base.rglob("*.html"))
        targets = [p for p in targets if "screenshots" not in str(p)]
    elif args.files:
        targets = [Path(f) for f in args.files]
    else:
        parser.print_help()
        sys.exit(1)

    if not targets:
        print("No HTML files found.")
        sys.exit(1)

    for html_path in targets:
        if not html_path.exists():
            print(f"  not found: {html_path}")
            continue
        try:
            pdf_path = to_pdf(html_path)
            print(f"  saved: {pdf_path}")
        except Exception as e:
            print(f"  error: {html_path} — {e}")


if __name__ == "__main__":
    main()
