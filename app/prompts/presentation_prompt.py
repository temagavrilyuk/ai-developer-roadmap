from langchain_core.prompts import PromptTemplate


presentation_prompt = PromptTemplate.from_template("""
Создай структуру презентации.

Тема: {topic}

Целевая аудитория: {audience}

Количество слайдов: {slides}

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

Ответ должен начинаться с {{ и заканчиваться }}.
""")