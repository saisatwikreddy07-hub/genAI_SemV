
import os
from pathlib import Path
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

# Load Gemini API key
load_dotenv(Path(__file__).with_name(".env"))

print("\n===== WEEK 2 LLM CLIENT =====")
print("1. Gemini AI (Online)")
print("2. Qwen2.5-Coder 14B (Local)")

choice = input("\nChoose provider (1/2): ").strip()

if choice == "1":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found!")

    provider = GeminiProvider(api_key)
    print("\nUsing Gemini AI")

elif choice == "2":
    provider = OllamaProvider("qwen2.5-coder:14b")
    print("\nUsing Qwen2.5-Coder 14B")

else:
    raise ValueError("Invalid provider selected!")

# Common LLM interface
client = LLMClient(provider)

prompt = input("\nEnter your question: ")

answer = client.generate(prompt)

print("\n===== AI RESPONSE =====")
print(answer)
