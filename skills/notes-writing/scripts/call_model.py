#!/usr/bin/env python3
"""Send one scoped revision request to an OpenAI-compatible provider."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path


PROVIDERS = {
    "openai": {
        "key_env": "OPENAI_API_KEY",
        "base_env": "OPENAI_BASE_URL",
        "default_base": "https://api.openai.com/v1",
    },
    "deepseek": {
        "key_env": "DEEPSEEK_API_KEY",
        "base_env": "DEEPSEEK_BASE_URL",
        "default_base": "https://api.deepseek.com",
    },
    "doubao": {
        "key_env": "ARK_API_KEY",
        "base_env": "ARK_BASE_URL",
        "default_base": "https://ark.cn-beijing.volces.com/api/v3",
    },
    "qwen": {
        "key_env": "DASHSCOPE_API_KEY",
        "base_env": "QWEN_BASE_URL",
        "default_base": None,
    },
}

SYSTEM_PROMPT = """You are revising researcher-authored academic notes or an early draft.
Preserve the author's claims, conceptual distinctions, voice, citations, quotations,
examples, and degree of uncertainty. Do not invent sources, evidence, findings, or
theoretical agreement. Make only the intervention requested. Unless the instruction
asks for commentary, return the revised text only."""

DEFAULT_INSTRUCTION = (
    "Lightly polish this draft while preserving its argument, citations, and uncertainty."
)
DEFAULT_CONFIG = Path("~/.config/notes-writing/config.toml").expanduser()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Call OpenAI, DeepSeek, Doubao/Ark, or Qwen for one revision request."
    )
    parser.add_argument("--provider", choices=sorted(PROVIDERS), help="Overrides default_provider")
    parser.add_argument("--model", help="Overrides the configured model or endpoint ID")
    parser.add_argument("--input", default="-", help="UTF-8 input file; '-' reads stdin")
    parser.add_argument("--instruction", help="Overrides default_instruction")
    parser.add_argument("--base-url", help="Override the provider API base URL")
    parser.add_argument(
        "--config",
        default=os.environ.get("NOTES_WRITING_CONFIG", str(DEFAULT_CONFIG)),
        help="TOML config path (default: ~/.config/notes-writing/config.toml)",
    )
    parser.add_argument("--output", help="Write output to a new UTF-8 file")
    parser.add_argument("--temperature", type=float, help="Optional sampling temperature")
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--dry-run", action="store_true", help="Validate settings without sending text")
    return parser.parse_args()


def load_config(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        with path.open("rb") as handle:
            data = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise SystemExit(f"Could not read config {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Config root must be a TOML table: {path}")
    return data


def provider_settings(config: dict[str, object], provider: str) -> dict[str, object]:
    providers = config.get("providers", {})
    if not isinstance(providers, dict):
        raise SystemExit("Config field 'providers' must be a TOML table.")
    settings = providers.get(provider, {})
    if not isinstance(settings, dict):
        raise SystemExit(f"Config field 'providers.{provider}' must be a TOML table.")
    if "api_key" in settings:
        raise SystemExit(
            f"Remove plaintext providers.{provider}.api_key from the config. "
            "Use an environment variable or macOS Keychain instead."
        )
    return settings


def optional_string(value: object) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def keychain_secret(settings: dict[str, object]) -> str | None:
    service = optional_string(settings.get("keychain_service"))
    if not service:
        return None
    command = ["security", "find-generic-password", "-s", service]
    account = optional_string(settings.get("keychain_account"))
    if account:
        command.extend(["-a", account])
    command.append("-w")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise SystemExit("macOS Keychain command 'security' is unavailable.") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            f"Could not read API key from Keychain service '{service}'."
        ) from exc
    return result.stdout.rstrip("\n")


def read_text(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    return Path(source).read_text(encoding="utf-8")


def endpoint_for(base_url: str) -> str:
    clean = base_url.rstrip("/")
    if clean.endswith("/chat/completions"):
        return clean
    return clean + "/chat/completions"


def extract_content(response: object) -> str:
    try:
        content = response["choices"][0]["message"]["content"]  # type: ignore[index]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("Response did not contain choices[0].message.content") from exc
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [item.get("text", "") for item in content if isinstance(item, dict)]
        joined = "".join(parts)
        if joined:
            return joined
    raise ValueError("Response content was not text")


def main() -> int:
    args = parse_args()
    config_path = Path(args.config).expanduser()
    user_config = load_config(config_path)
    provider = args.provider or optional_string(user_config.get("default_provider"))
    if not provider:
        raise SystemExit(
            f"No provider selected. Set default_provider in {config_path} or use --provider."
        )
    if provider not in PROVIDERS:
        raise SystemExit(f"Unsupported provider in config: {provider}")
    settings = provider_settings(user_config, provider)
    config = PROVIDERS[provider]

    model = args.model or optional_string(settings.get("model"))
    if not model:
        raise SystemExit(
            f"No model configured for {provider}. Set providers.{provider}.model "
            "in the config or use --model."
        )
    instruction = (
        args.instruction
        or optional_string(user_config.get("default_instruction"))
        or DEFAULT_INSTRUCTION
    )
    text = read_text(args.input)
    if not text.strip():
        raise SystemExit("Input text is empty.")

    base_url = (
        args.base_url
        or optional_string(settings.get("base_url"))
        or os.environ.get(config["base_env"])
        or config["default_base"]
    )
    if not base_url:
        raise SystemExit(
            f"No base URL configured for {provider}. Set providers.{provider}.base_url, "
            f"use --base-url, or set {config['base_env']}."
        )
    endpoint = endpoint_for(base_url)

    if args.output and Path(args.output).exists():
        raise SystemExit(f"Refusing to overwrite existing output file: {args.output}")

    if args.dry_run:
        summary = {
            "config": str(config_path),
            "provider": provider,
            "model": model,
            "endpoint": endpoint,
            "input_characters": len(text),
            "credential_variable": config["key_env"],
            "transmitted": False,
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    api_key = os.environ.get(config["key_env"]) or keychain_secret(settings)
    if not api_key:
        raise SystemExit(
            f"No credential available for {provider}. Set {config['key_env']} or configure "
            f"providers.{provider}.keychain_service."
        )

    payload: dict[str, object] = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Editing instruction:\n{instruction}\n\nDraft:\n{text}",
            },
        ],
    }
    if args.temperature is not None:
        payload["temperature"] = args.temperature

    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        raise SystemExit(f"Provider returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach provider: {exc.reason}") from exc

    try:
        result = extract_content(json.loads(body))
    except (json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"Could not parse provider response: {exc}") from exc

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Wrote revision to {args.output}", file=sys.stderr)
    else:
        print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
