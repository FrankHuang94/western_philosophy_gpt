#!/usr/bin/env python3
"""Generate markdown index and Mermaid critique graph from data/*.json."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OVERVIEW_DIR = ROOT / "docs" / "00-overview"


def load_json(name: str) -> dict:
    with (DATA_DIR / name).open("r", encoding="utf-8") as f:
        return json.load(f)


def node_id(value: str) -> str:
    base = re.sub(r"\W+", "_", value, flags=re.UNICODE).strip("_")
    return base or "node"


def write_index(philosophers: list[dict], schools: list[dict], events: list[dict]) -> None:
    lines = [
        "# 自动生成索引",
        "",
        "> 本文件由 `scripts/build_index.py` 生成。正文稳定后可复制到附录并人工修订。",
        "",
        "## 人物",
        "",
    ]
    if philosophers:
        for item in sorted(philosophers, key=lambda x: x.get("name", "")):
            lines.append(f"- {item.get('name', '[未命名]')}")
    else:
        lines.append("- 暂无人物数据")

    lines.extend(["", "## 流派", ""])
    if schools:
        for item in sorted(schools, key=lambda x: x.get("name", "")):
            lines.append(f"- {item.get('name', '[未命名]')}")
    else:
        lines.append("- 暂无流派数据")

    lines.extend(["", "## 时间线事件", ""])
    if events:
        for item in events:
            year = item.get("year", "[年份待定]")
            title = item.get("title", "[事件待定]")
            lines.append(f"- {year}: {title}")
    else:
        lines.append("- 暂无时间线数据")

    (OVERVIEW_DIR / "generated-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_mermaid(critiques: list[dict]) -> None:
    lines = [
        "# 自动生成批判关系图",
        "",
        "```mermaid",
        "graph LR",
    ]
    if critiques:
        for item in critiques:
            source = item.get("source", "source")
            target = item.get("target", "target")
            label = item.get("critique_type", "批判")
            lines.append(f'  {node_id(source)}["{source}"] -- "{label}" --> {node_id(target)}["{target}"]')
    else:
        lines.append('  empty["暂无批判关系数据"]')
    lines.extend(["```", ""])
    (OVERVIEW_DIR / "generated-critique-graph.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    philosophers = load_json("philosophers.json").get("philosophers", [])
    schools = load_json("schools.json").get("schools", [])
    critiques = load_json("critiques.json").get("critiques", [])
    events = load_json("timeline.json").get("events", [])

    OVERVIEW_DIR.mkdir(parents=True, exist_ok=True)
    write_index(philosophers, schools, events)
    write_mermaid(critiques)
    print("Generated docs/00-overview/generated-index.md")
    print("Generated docs/00-overview/generated-critique-graph.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

