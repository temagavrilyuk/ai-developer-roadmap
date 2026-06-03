from fastapi import APIRouter

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

Для каждого слайда укажи:
1. Заголовок
2. Основную мысль

Ответ дай на русском языке.
"""

    return ask_llm(prompt)