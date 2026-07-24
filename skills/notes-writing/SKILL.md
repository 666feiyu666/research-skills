---
name: notes-writing
description: Revise and polish researcher-authored notes, reading responses, idea fragments, and early drafts after source reading. Use when Codex needs to clarify, lightly restructure, compress, expand cautiously, compare versions, or improve Chinese or English academic prose while preserving the researcher's claims, voice, citations, and uncertainty. Supports optional, explicit calls to OpenAI, DeepSeek, Doubao through Volcengine Ark, and Qwen through Alibaba Cloud Model Studio. Do not use for close reading, literature-note consolidation, project-level diagnosis, or drafting a paper from sources the researcher has not yet interpreted.
---

# Notes Writing

## Overview

Help the researcher turn already-understood material into clearer prose without replacing their thinking. Treat editing as a traceable collaboration: preserve the argument and evidentiary limits, make the smallest useful intervention, and distinguish wording changes from substantive suggestions.

## Place in the research workflow

- Use `critical-reading` before this skill when the source itself still needs to be understood.
- Use `research-notes` when multiple sources or claims need to be consolidated and traced.
- Use this skill for researcher-authored notes, reflections, paragraphs, and early drafts.
- Use `paper-writing` when the task becomes paper-level outlining, drafting, or argument and citation auditing.
- Use `research-editor` for project-level diagnosis across the question, theory, method, evidence, literature, and writing.

## Editing workflow

1. Identify the text's purpose, intended reader, language, and requested degree of intervention. Infer these when safe; ask only when the choice would materially change the result.
2. Identify the non-negotiable content: central claim, conceptual distinctions, citations, quotations, examples, uncertainty markers, and deliberate stylistic features.
3. Choose the lightest fitting mode:
   - **Polish**: grammar, diction, rhythm, transitions, and academic register.
   - **Clarify**: expose the claim, subject, causal relation, or conceptual distinction.
   - **Compress**: remove repetition while retaining qualifications and evidence.
   - **Light restructure**: reorder sentences or paragraphs without redesigning the argument.
   - **Develop**: suggest questions, missing links, or possible elaborations; do not silently add them as established claims.
   - **Compare**: provide alternatives or compare the original with one or more revisions.
4. Revise. Never invent sources, quotations, findings, empirical detail, or theoretical agreement.
5. Return the revised text first unless the user asks for another format. Add a short change memo only when changes are substantive or potentially contestable.

## Preserve authorship

- Keep the researcher's theoretical commitments and argumentative force unless asked to challenge them.
- Retain citations and page numbers exactly unless correcting an obvious formatting issue. Flag questionable attribution instead of repairing it from memory.
- Preserve uncertainty such as “可能”“似乎”“初步而言” when the evidence remains provisional.
- Do not convert exploratory notes into false certainty or prematurely formalize them as a paper-ready research question.
- Mark proposed conceptual additions as suggestions, not as if they were present in the original.
- When a passage has more than one plausible meaning, explain the ambiguity briefly rather than choosing silently.

## Optional external model calls

The default is to revise within the current Codex session. Call an external provider only when the user explicitly selects that provider or explicitly requests a cross-model comparison. A provider choice authorizes only the text in scope for that request.

Before sending text externally:

1. State which provider will receive the text.
2. Warn when the draft may contain unpublished, personal, confidential, or sensitive material; obtain confirmation if the user has not already clearly authorized transmission.
3. Use environment variables for credentials. Never request that a key be pasted into chat, write it into a file, or expose it in command output.
4. Require a configured or explicit model identifier because provider model catalogs change.
5. Do not overwrite the source file. Save model output separately or return it in the conversation.

Use `scripts/call_model.py` for a single OpenAI-compatible chat-completions request. It reads `~/.config/notes-writing/config.toml` by default; command-line arguments override the file. Create the file once with `scripts/init_config.py`, then set `default_provider`, the chosen model, and any regional base URL. Keep API keys out of TOML: use the named environment variable or a configured macOS Keychain service. Read `references/providers.md` before the first call in a task because endpoints, regions, and model identifiers can change.

```bash
python3 scripts/call_model.py \
  --input draft.md \
  --output draft.deepseek.md
```

For Qwen, supply the workspace- and region-specific compatible-mode base URL with `--base-url` or `QWEN_BASE_URL`. For any provider, `--dry-run` verifies configuration without transmitting text.

## Cross-model comparison

Only send the same scoped passage to multiple providers when the user asks for comparison. Keep prompts and parameters materially equivalent. Compare outputs by:

- fidelity to the original claim and uncertainty;
- clarity and economy;
- preservation of citations and terminology;
- unsupported additions or loss of nuance;
- fit with the researcher's voice.

Do not choose a winner solely for fluency. Prefer the version that best preserves scholarly responsibility.

## Resources

- `scripts/call_model.py`: dependency-free client for configured or explicit provider calls.
- `scripts/init_config.py`: safely create the one-time user configuration template.
- `references/config.example.toml`: configuration schema and provider examples.
- `references/providers.md`: credential names, endpoint configuration, privacy notes, and official documentation links.
