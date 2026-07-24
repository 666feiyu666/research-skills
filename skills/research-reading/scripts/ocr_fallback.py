#!/usr/bin/env python3
"""OCR a PDF or image only as an explicit fallback, retaining page mapping."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


INSTALL_HINT = (
    "OCR requires pymupdf, pillow, pytesseract, Tesseract, and requested language packs. "
    "See the repository README; dependencies are never installed automatically."
)


def require_ocr_dependencies():
    try:
        import fitz
        import pytesseract
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError(INSTALL_HINT) from exc
    return fitz, pytesseract, Image


def verify_languages(pytesseract, languages: str) -> None:
    requested = set(languages.split("+"))
    installed = set(pytesseract.get_languages(config=""))
    missing = sorted(requested - installed)
    if missing:
        raise RuntimeError(f"missing Tesseract language packs: {', '.join(missing)}. {INSTALL_HINT}")


def ocr_pdf(path: Path, languages: str, dpi: int) -> list[dict]:
    fitz, pytesseract, Image = require_ocr_dependencies()
    verify_languages(pytesseract, languages)
    pages = []
    with fitz.open(path) as document:
        scale = dpi / 72
        for page_number, page in enumerate(document, 1):
            pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
            image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
            text = pytesseract.image_to_string(image, lang=languages)
            pages.append({"page": page_number, "text": text, "source": "ocr", "ocr_verified": False})
    return pages


def ocr_image(path: Path, languages: str) -> list[dict]:
    _, pytesseract, Image = require_ocr_dependencies()
    verify_languages(pytesseract, languages)
    with Image.open(path) as image:
        text = pytesseract.image_to_string(image, lang=languages)
    return [{"page": 1, "text": text, "source": "ocr", "ocr_verified": False}]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--languages", default="chi_sim+chi_tra+eng")
    parser.add_argument("--dpi", type=int, default=300)
    args = parser.parse_args()
    try:
        if not args.input.is_file():
            raise OSError(f"file not found: {args.input}")
        if args.dpi < 150 or args.dpi > 600:
            raise ValueError("dpi must be between 150 and 600")
        pages = (
            ocr_pdf(args.input, args.languages, args.dpi)
            if args.input.suffix.lower() == ".pdf"
            else ocr_image(args.input, args.languages)
        )
        result = {
            "file": str(args.input),
            "pages": pages,
            "page_numbering": "1-based source sequence; printed page numbers may differ",
            "ocr": {
                "languages": args.languages,
                "dpi": args.dpi,
                "warning": "机器识别文本可能有误；任何引用、专名、数字、脚注和页码均须对照原页核验。",
            },
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ocr_fallback: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

