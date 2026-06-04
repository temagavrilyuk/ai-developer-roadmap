from fastapi import APIRouter
import json

from app.models.requests import (
    GenerateRequest,
    PresentationRequest
)

from app.services.llm_service import ask_llm


router = APIRouter()


@router.post("/generate")
def generate(request: GenerateRequest):
    return ask_llm(request.prompt)


@router.post("/presentation")
def presentation(request: PresentationRequest):

    prompt = f"""
Создай структуру презентации.

Тема: {request.topic}

Целевая аудитория: {request.audience}

Количество слайдов: {request.slides}

Верни только чистый JSON без markdown-разметки, без ```json, без пояснений и без текста до или после JSON.

Пример:

{{
    "slides": [
        {{
            "title": "Название слайда",
            "description": "Описание"
        }}
    ]
}}

Никакого текста вне JSON.
Ответ должен начинаться с {{ и заканчиваться }}.
"""

    response = ask_llm(prompt)


    if response.get("error"):
        return response

    slides_json = json.loads(response["result"])

    return slides_json