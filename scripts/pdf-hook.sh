#!/bin/bash
# PostToolUse hook — auto-generates PDF when an HTML guide is written.
# Reads tool result JSON from stdin.

input=$(cat)
file_path=$(echo "$input" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" 2>/dev/null)

if [[ "$file_path" == *"/guides/"*".html" ]]; then
  cd "$(dirname "$0")/.." || exit 0
  python3 scripts/to-pdf.py "$file_path" 2>/dev/null && echo "PDF saved: ${file_path%.html}.pdf"
fi
