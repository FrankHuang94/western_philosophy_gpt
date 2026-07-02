#!/usr/bin/env python3
"""Count Chinese characters in docs and compare against target chapter sizes."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"

TARGETS = {
    "00-overview": 3000,
    "01-ancient": 12000,
    "02-medieval": 8000,
    "03-early-modern": 15000,
    "04-enlightenment": 25000,
    "05-german-idealism": 15000,
    "06-post-kantian": 12000,
    "07-19th-century": 12000,
    "08-phenomenology": 15000,
    "09-analytic": 15000,
    "10-pragmatism": 6000,
    "11-critical-theory": 8000,
    "12-structuralism": 8000,
    "13-postmodern": 6000,
    "14-political-phil": 8000,
    "15-cross-cutting": 6000,
    "appendix": 4000,
}

CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def count_cjk(path: Path) -> int:
    total = 0
    for md in path.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        total += len(CJK_RE.findall(text))
    return total


def main() -> int:
    grand_total = 0
    print("| 目录 | 当前中文字数 | 目标字数 | 完成率 |")
    print("| --- | ---: | ---: | ---: |")
    for dirname, target in TARGETS.items():
        path = DOCS_DIR / dirname
        count = count_cjk(path) if path.exists() else 0
        grand_total += count
        ratio = count / target if target else 0
        print(f"| {dirname} | {count} | {target} | {ratio:.1%} |")
    print(f"\nTotal Chinese characters: {grand_total}")
    print("Minimum target: 150000")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

