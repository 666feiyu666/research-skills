# Provider configuration

Check these official pages before the first external call in a task. Model IDs, regional hosts, compatibility behavior, pricing, data handling, and account requirements can change.

| Skill name | Service actually called | Credential variable | Default API base | Configuration note |
|---|---|---|---|---|
| `openai` | OpenAI API | `OPENAI_API_KEY` | `https://api.openai.com/v1` | A ChatGPT subscription is not an API credential. Pass an API model ID explicitly. |
| `deepseek` | DeepSeek API | `DEEPSEEK_API_KEY` | `https://api.deepseek.com` | Pass a current model ID explicitly. |
| `doubao` | Volcengine Ark / 豆包模型 | `ARK_API_KEY` | `https://ark.cn-beijing.volces.com/api/v3` | The model argument may be a model or endpoint ID, depending on the Ark setup. Check region and account configuration. |
| `qwen` | Alibaba Cloud Model Studio / 通义千问 | `DASHSCOPE_API_KEY` | none | Set `QWEN_BASE_URL` or `--base-url` to the compatible-mode base for the account's workspace and region. |

The script appends `/chat/completions` to the configured base unless it is already present. It uses the common `Authorization: Bearer ...` convention and an OpenAI-compatible `messages` payload.

## Persistent configuration

The default file is `~/.config/notes-writing/config.toml`; override it with `--config` or `NOTES_WRITING_CONFIG`. Copy `config.example.toml` or run `scripts/init_config.py`, then fill the settings once. Resolution order is command-line argument, TOML setting, environment setting, and built-in provider default.

Do not add an `api_key` field. The client rejects plaintext keys in TOML. It first reads the provider's credential environment variable, then an optional macOS Keychain item named by `keychain_service` (and, if supplied, `keychain_account`).

## Official documentation

- OpenAI: [Models](https://developers.openai.com/api/docs/models) and [Chat Completions API reference](https://platform.openai.com/docs/api-reference/chat)
- DeepSeek: [API documentation](https://api-docs.deepseek.com/) and [Create Chat Completion](https://api-docs.deepseek.com/api/create-chat-completion)
- Volcengine Ark: [API call overview](https://www.volcengine.com/docs/82379/1795150)
- Alibaba Cloud Model Studio: [First API call to Qwen](https://help.aliyun.com/en/model-studio/first-api-call-to-qwen)

## Data and credential safety

- Obtain explicit user authorization for the named provider before transmission.
- Minimize the passage sent. Remove identifying or confidential information when it is not needed for revision.
- Never put credentials in prompts, command-line arguments, Markdown, source files, or saved outputs.
- Do not interpret `--dry-run` as a provider privacy guarantee; it only confirms that this script makes no request in that invocation.
- Consult the provider's current data-use, retention, and regional terms for sensitive or unpublished research.

## Example configuration

After setting the default provider and model in the config, a routine call only needs the changing input and output paths:

```bash
python3 scripts/call_model.py \
  --input note.md \
  --output note.openai.md
```

For Qwen:

```bash
python3 scripts/call_model.py \
  --provider qwen \
  --base-url "YOUR_WORKSPACE_AND_REGION_COMPATIBLE_MODE_BASE" \
  --model MODEL_ID \
  --input note.md \
  --dry-run
```
