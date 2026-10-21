# Gemini AI Repo

Cliente mínimo da API Gemini via SDK [`google-genai`](https://pypi.org/project/google-genai/).

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt        # ou requirements.lock.txt p/ versões fixas
export GEMINI_API_KEY="..."            # https://aistudio.google.com/apikey
```

## Uso

```bash
python aiPython.py                     # prompt padrão: "hello"
python aiPython.py "explique recursão"
```

Sem `GEMINI_API_KEY` → exit 1.

## Stack

| Item     | Valor                    |
| -------- | ------------------------ |
| Python   | 3.10+                    |
| SDK      | `google-genai` >= 2.32.0 |
| Modelo   | `gemini-3.1-flash-lite`  |
| Endpoint | `client.interactions.create` |

## `generation_config`

```python
{"max_output_tokens": 645, "thinking_level": "medium"}
```

Também aceita `temperature`, `top_p`, `seed`, `stop_sequences`, `thinking_summaries`,
`tool_choice`. Kwargs de `create`: `model`, `input`, `generation_config`,
`system_instruction`, `tools`, `stream`.

## Arquivos

```
aiPython.py              entrypoint
requirements.txt         dependência direta
requirements.lock.txt    pip freeze
.env.example             modelo de config
```
