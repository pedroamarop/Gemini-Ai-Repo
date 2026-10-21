# Gemini AI Repo

Script mínimo em Python para conversar com a API da Gemini usando o SDK oficial
[`google-genai`](https://pypi.org/project/google-genai/).

## Requisitos

- Python 3.10+
- Uma chave da API Gemini — gere em [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## Instalação

```bash
git clone https://github.com/pedroamarop/Gemini-Ai-Repo.git
cd Gemini-Ai-Repo

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Para reproduzir exatamente as versões já testadas, use o lockfile:

```bash
pip install -r requirements.lock.txt
```

## Configuração

A chave é lida da variável de ambiente `GEMINI_API_KEY`:

```bash
cp .env.example .env     # preencha a chave no .env
export GEMINI_API_KEY="sua-chave-aqui"
```

O `.env` está no `.gitignore` — a chave nunca vai pro repositório.

## Uso

```bash
python aiPython.py                           # usa o prompt padrão ("hello")
python aiPython.py "explique recursão"       # prompt pela linha de comando
```

## Estrutura

```
.
├── aiPython.py              # script principal
├── requirements.txt         # dependência direta
├── requirements.lock.txt    # versões fixas (pip freeze)
├── .env.example             # modelo de configuração
└── .gitignore
```

## Parâmetros de geração

Ajustáveis no dicionário `generation_config` do script:

| Parâmetro           | Valor atual | O que faz                                     |
| ------------------- | ----------- | --------------------------------------------- |
| `max_output_tokens` | `645`       | Limite de tokens na resposta                  |
| `thinking_level`    | `medium`    | Quanto o modelo "pensa" antes de responder    |

Outros campos aceitos: `temperature`, `top_p`, `seed`, `stop_sequences`.
O modelo usado é `gemini-3.1-flash-lite`.
