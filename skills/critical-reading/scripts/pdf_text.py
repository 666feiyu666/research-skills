#!/usr/bin/env python3
"""Inspect or extract a PDF text layer while retaining 1-based page mapping."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


class PDFDependencyError(RuntimeError):
    pass


def extract_pages(path: Path) -> list[dict]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise PDFDependencyError(
            "pypdf is required for PDF text extraction; install with `python -m pip install pypdf`"
        ) from exc
    reader = PdfReader(str(path))
    pages: list[dict] = []
    for page_number, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
            error = None
        except Exception as exc:  # malformed individual pages should remain mapped
            text = ""
            error = f"{type(exc).__name__}: {exc}"
        pages.append(
            {
                "page": page_number,
                "text": text,
                "source": "text_layer",
                "extraction_error": error,
            }
        )
    return pages


def assess_pages(pages: list[dict], min_total_chars: int = 40) -> dict:
    texts = [str(page.get("text", "")) for page in pages]
    compact = [re.sub(r"\s+", "", text) for text in texts]
    total_chars = sum(map(len, compact))
    nonempty = sum(bool(text) for text in compact)
    replacement = sum(text.count("\ufffd") for text in texts)
    control = sum(1 for text in texts for char in text if ord(char) < 32 and char not in "\n\r\t")
    page_count = len(pages)
    nonempty_ratio = nonempty / page_count if page_count else 0.0
    noise_ratio = (replacement + control) / max(total_chars, 1)
    errors = [page["page"] for page in pages if page.get("extraction_error")]
    usable = total_chars >= min_total_chars and nonempty_ratio >= 0.5 and noise_ratio < 0.02
    warnings: list[str] = []
    if total_chars < min_total_chars:
        warnings.append("extracted text is too short")
    if page_count and nonempty_ratio < 0.5:
        warnings.append("more than half of pages have no usable text")
    if noise_ratio >= 0.02:
        warnings.append("replacement/control character ratio suggests garbled text")
    if errors:
        warnings.append(f"page extraction failed on pages: {errors}")
    return {
        "page_count": page_count,
        "extracted_characters": total_chars,
        "nonempty_page_ratio": round(nonempty_ratio, 4),
        "noise_ratio": round(noise_ratio, 6),
        "has_usable_text_layer": usable,
        "pages_with_errors": errors,
        "warnings": warnings,
    }


def build_result(path: Path, include_text: bool) -> dict:
    pages = extract_pages(path)
    result = {
        "file": str(path),
        "assessment": assess_pages(pages),
        "page_numbering": "1-based PDF page sequence; printed page numbers may differ",
    }
    if include_text:
        result["pages"] = pages
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("inspect", "extract"):
        sub = subparsers.add_parser(command)
        sub.add_argument("pdf", type=Path)
        sub.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    try:
        if not args.pdf.is_file():
            raise OSError(f"file not found: {args.pdf}")
        result = build_result(args.pdf, include_text=args.command == "extract")
        payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(payload, encoding="utf-8")
        else:
            sys.stdout.write(payload)
        return 0
    except (OSError, PDFDependencyError, ValueError) as exc:
        print(f"pdf_text: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

