#!/usr/bin/env python3
"""Normalize and exactly deduplicate tagged research notes from JSON.

Input is a JSON array of objects with kind, text, and optional source/topics,
method, case, and function fields. The script never asks a model to infer kind.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

LABELS = {
    "literature": "[文献观点]",
    "user": "[用户判断]",
    "assistant": "[模型建议]",
    "question": "[未解决问题]",
}


def normalize_for_match(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def merge_notes(notes: list[dict]) -> tuple[list[dict], list[str]]:
    merged: OrderedDict[tuple[str, str], dict] = OrderedDict()
    warnings: list[str] = []
    for index, raw in enumerate(notes, 1):
        kind = str(raw.get("kind", "")).strip()
        text = str(raw.get("text", "")).strip()
        if kind not in LABELS:
            raise ValueError(f"note {index}: kind must be one of {sorted(LABELS)}")
        if not text:
            raise ValueError(f"note {index}: text is empty")
        sources = raw.get("sources", raw.get("source", []))
        if isinstance(sources, str):
            sources = [sources]
        sources = [str(item).strip() for item in sources if str(item).strip()]
        if kind == "literature" and not sources:
            warnings.append(f"note {index}: literature claim has no source")
        key = (kind, normalize_for_match(text))
        if key not in merged:
            merged[key] = {
                "kind": kind,
                "text": text,
                "sources": [],
                "topics": [],
                "method": str(raw.get("method", "")).strip(),
                "case": str(raw.get("case", "")).strip(),
                "function": str(raw.get("function", "")).strip(),
            }
        item = merged[key]
        for source in sources:
            if source not in item["sources"]:
                item["sources"].append(source)
        topics = raw.get("topics", [])
        if isinstance(topics, str):
            topics = [topics]
        for topic in topics:
            topic = str(topic).strip()
            if topic and topic not in item["topics"]:
                item["topics"].append(topic)
    return list(merged.values()), warnings


def as_markdown(notes: list[dict], warnings: list[str]) -> str:
    rows = [
        "# 笔记整理候选",
        "",
        "| 标签 | 内容 | 主题 | 方法/案例 | 论证功能 | 来源 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for note in notes:
        escape = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        method_case = " / ".join(filter(None, [note["method"], note["case"]]))
        rows.append(
            "| {label} | {text} | {topics} | {method_case} | {function} | {sources} |".format(
                label=LABELS[note["kind"]],
                text=escape(note["text"]),
                topics=escape("; ".join(note["topics"])),
                method_case=escape(method_case),
                function=escape(note["function"]),
                sources=escape("; ".join(note["sources"])),
            )
        )
    if warnings:
        rows.extend(["", "## 待核查", ""] + [f"- {item}" for item in warnings])
    return "\n".join(rows) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON array of tagged notes")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError("input root must be a JSON array")
        notes, warnings = merge_notes(data)
        result = as_markdown(notes, warnings)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(result, encoding="utf-8")
        else:
            sys.stdout.write(result)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"organize_notes: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

