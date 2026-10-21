import os
import sys

from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    sys.exit("Defina GEMINI_API_KEY antes de rodar (veja o .env.example).")

client = genai.Client(api_key=api_key)

generation_config = {
    "max_output_tokens": 645,
    "thinking_level": "medium",
}

prompt = " ".join(sys.argv[1:]) or "hello"

resposta = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=prompt,
    generation_config=generation_config,
)

print(resposta.text)
