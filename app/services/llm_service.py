import os
import requests


def ask_llm(prompt: str):

    api_key = os.getenv("OPENROUTER_API_KEY")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-oss-20b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        proxies={
            "http": None,
            "https": None,
        }
    )

    data = response.json()

    if "choices" not in data:
        return {
            "error": True,
            "message": "LLM provider error",
            "details": data
        }

    return {
        "result": data["choices"][0]["message"]["content"]
    }