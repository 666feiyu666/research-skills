#!/usr/bin/env python3
"""Conservatively clean page-mapped JSON produced by pdf_text or OCR."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


def edge_lines(text: str) -> tuple[str, str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return (lines[0], lines[-1]) if lines else ("", "")


def repeated_edges(pages: list[dict]) -> set[str]:
    counts: Counter[str] = Counter()
    for page in pages:
        for line in set(edge_lines(str(page.get("text", "")))):
            if 2 <= len(line) <= 120:
                counts[line] += 1
    threshold = max(3, int(len(pages) * 0.6 + 0.5))
    return {line for line, count in counts.items() if count >= threshold}


def clean_page(text: str, removable_edges: set[str]) -> str:
    text = text.replace("\u00ad", "")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    lines = [line for line in lines if line and line not in removable_edges]
    output: list[str] = []
    for line in lines:
        if output and output[-1].endswith("-") and re.match(r"^[a-z]", line):
            output[-1] = output[-1][:-1] + line
        else:
            output.append(line)
    return "\n".join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        pages = data.get("pages")
        if not isinstance(pages, list):
            raise ValueError("input JSON must contain a pages array")
        repeated = repeated_edges(pages)
        for page in pages:
            page["text"] = clean_page(str(page.get("text", "")), repeated)
        data["cleaning"] = {
            "removed_repeated_edge_lines": sorted(repeated),
            "warning": "Conservative mechanical cleanup; verify reading order, tables, footnotes, and OCR against source pages.",
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"clean_text: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

