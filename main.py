import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()


class GenerateRequest(BaseModel):
    prompt: str

class PresentationRequest(BaseModel):
    topic: str
    audience: str
    slides: int

@app.get("/")
def root():
    return {
        "message": "AI Developer Roadmap"
    }

@app.post("/generate")
def generate(request: GenerateRequest):
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": request.prompt
                }
            ]
        }
    )

    data = response.json()
    print(data)

    if "choices" not in data:
        return {
            "error": data
        }

    return {
        "result": data["choices"][0]["message"]["content"]
    }

@app.post("/presentation")
def create_presentation(request: PresentationRequest):
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")
    prompt = f"""
Создай структуру презентации.

Тема: {request.topic}

Целевая аудитория: {request.audience}

Количество слайдов: {request.slides}

Для каждого слайда укажи:
1. Заголовок
2. Основную мысль

Ответ дай на русском языке.
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()
    print(data)

    if "choices" not in data:
        return {
            "error": data
        }

    return {
        "result": data["choices"][0]["message"]["content"]
    }