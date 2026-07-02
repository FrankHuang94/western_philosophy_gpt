#!/usr/bin/env python3
"""Validate structured data and explicit markdown references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"

REF_RE = re.compile(r"\[\[(philosopher|school|work|concept):([^\]]+)\]\]")
ALLOWED_CRITIQUE_TYPES = {
    "本体论",
    "认识论",
    "伦理学",
    "政治哲学",
    "美学",
    "方法论",
    "宗教哲学",
    "社会哲学",
    "语言哲学",
    "科学哲学",
    "综合",
}


def load_json(name: str) -> dict:
    path = DATA_DIR / name
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def names_from_items(items: list[dict]) -> set[str]:
    names: set[str] = set()
    for item in items:
        name = item.get("name")
        if isinstance(name, str) and name.strip():
            names.add(name.strip())
        aliases = item.get("aliases", [])
        if isinstance(aliases, list):
            names.update(a.strip() for a in aliases if isinstance(a, str) and a.strip())
    return names


def validate_schema(errors: list[str]) -> tuple[set[str], set[str]]:
    philosophers = load_json("philosophers.json")
    schools = load_json("schools.json")
    critiques = load_json("critiques.json")
    timeline = load_json("timeline.json")

    for key, data, list_key in [
        ("philosophers.json", philosophers, "philosophers"),
        ("schools.json", schools, "schools"),
        ("critiques.json", critiques, "critiques"),
        ("timeline.json", timeline, "events"),
    ]:
        if list_key not in data or not isinstance(data[list_key], list):
            errors.append(f"{key}: missing list field '{list_key}'")

    philosopher_names = names_from_items(philosophers.get("philosophers", []))
    school_names = names_from_items(schools.get("schools", []))
    known_nodes = philosopher_names | school_names

    allowed = set(critiques.get("allowed_critique_types", [])) or ALLOWED_CRITIQUE_TYPES
    for i, item in enumerate(critiques.get("critiques", []), start=1):
        for field in ["source", "target", "critique_type", "summary", "key_text"]:
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"critiques[{i}]: missing non-empty field '{field}'")
        if item.get("critique_type") not in allowed:
            errors.append(f"critiques[{i}]: invalid critique_type '{item.get('critique_type')}'")
        for endpoint in ["source", "target"]:
            value = item.get(endpoint)
            if known_nodes and isinstance(value, str) and value not in known_nodes:
                errors.append(f"critiques[{i}]: {endpoint} '{value}' not found in philosophers or schools")

    return philosopher_names, school_names


def validate_markdown_refs(philosophers: set[str], schools: set[str], errors: list[str]) -> None:
    for path in DOCS_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for kind, value in REF_RE.findall(text):
            value = value.strip()
            rel = path.relative_to(ROOT)
            if kind == "philosopher" and philosophers and value not in philosophers:
                errors.append(f"{rel}: philosopher ref '{value}' not found in philosophers.json")
            if kind == "school" and schools and value not in schools:
                errors.append(f"{rel}: school ref '{value}' not found in schools.json")


def main() -> int:
    errors: list[str] = []
    try:
        philosophers, schools = validate_schema(errors)
        validate_markdown_refs(philosophers, schools, errors)
    except json.JSONDecodeError as exc:
        errors.append(f"JSON parse error: {exc}")
    except FileNotFoundError as exc:
        errors.append(f"Missing file: {exc.filename}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

