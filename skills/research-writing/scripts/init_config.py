#!/usr/bin/env python3
"""Create a safe, editable research-writing configuration template."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = '''# Select one after filling its model below.
# default_provider = "deepseek"

default_instruction = "轻度润色这份学术草稿；保留论点、引文、术语和不确定性表达。"

[providers.openai]
model = ""
keychain_service = "research-writing-openai"

[providers.deepseek]
model = ""
keychain_service = "research-writing-deepseek"

[providers.doubao]
model = ""
keychain_service = "research-writing-doubao"
# base_url = "https://ark.cn-beijing.volces.com/api/v3"

[providers.qwen]
model = ""
keychain_service = "research-writing-qwen"
# Set the compatible-mode base for your workspace and region.
base_url = ""
'''


def main() -> int:
    parser = argparse.ArgumentParser(description="Create research-writing config.toml")
    parser.add_argument(
        "--path",
        default="~/.config/research-writing/config.toml",
        help="Destination; defaults to ~/.config/research-writing/config.toml",
    )
    args = parser.parse_args()
    destination = Path(args.path).expanduser()
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing config: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(TEMPLATE, encoding="utf-8")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
