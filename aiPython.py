import os
import sys
from dotenv import load_dotenv
from google import genai
import getpass
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

documento = TextLoader("documents/01_manual_colaborador_nebula.txt").load()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    api_key = getpass.getpass("GEMINI_API_KEY: ")

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