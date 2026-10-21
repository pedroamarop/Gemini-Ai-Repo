import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

generation_config = {
    'max_output_tokens': 645,
    'thinking_level': 'medium',
}

resposta = client.interactions.create(model="gemini-3.1-flash-lite", input="hello")

print(resposta.text)


