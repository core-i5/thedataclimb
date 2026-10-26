"""Count solved problems per pattern and write the table into dsa/README.md."""

import pathlib
import re

root = pathlib.Path("dsa")
rows, total = [], 0
for d in sorted(p for p in root.iterdir() if p.is_dir()):
    n = len([f for f in d.iterdir() if f.suffix in (".py", ".sql")])
    total += n
    rows.append(f"| {d.name} | {n} |")
table = "| Pattern | Solved |\n|---|---|\n" + "\n".join(rows) + f"\n| **Total** | **{total}** |"
readme = root / "README.md"
text = readme.read_text(encoding="utf-8")
text = re.sub(
    r"<!-- progress:start -->.*<!-- progress:end -->",
    f"<!-- progress:start -->\n{table}\n<!-- progress:end -->",
    text,
    flags=re.S,
)
readme.write_text(text, encoding="utf-8")
print(f"{total} problems solved")
