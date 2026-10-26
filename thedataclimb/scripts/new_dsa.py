"""Create a DSA practice file with a standard header.
Usage: python scripts/new_dsa.py <pattern> <leetcode_number> "<title>"
"""

import datetime
import pathlib
import re
import sys

pattern, num, title = sys.argv[1], int(sys.argv[2]), sys.argv[3]
slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
ext = "sql" if pattern == "sql" else "py"
path = pathlib.Path("dsa") / pattern / f"{num:04d}_{slug}.{ext}"
if path.exists():
    sys.exit(f"exists: {path}")
today = datetime.date.today()
c = "--" if ext == "sql" else "#"
header = "\n".join(
    f"{c} {line}"
    for line in [
        f"LeetCode {num}: {title}",
        f"Pattern: {pattern} | Difficulty: ? | Solved: {today}",
        "Time: O(?) | Space: O(?) | Took: __ min | Peeked: no",
        "Re-solve: +3d [ ]  +7d [ ]  +30d [ ]",
        "Key insight (1 line):",
    ]
)
body = "\n\n" if ext == "sql" else "\n\n\nclass Solution:\n    pass\n"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(header + body, encoding="utf-8")
print(path)
