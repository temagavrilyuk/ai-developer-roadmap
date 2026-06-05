from langchain_core.prompts import PromptTemplate


kiberlab_prompt = PromptTemplate.from_template("""
Ответь на вопрос пользователя, используя только контекст ниже.

Контекст:
{context}

Вопрос:
{question}

Если ответа нет в контексте, скажи:
"В контексте нет информации для ответа на этот вопрос."
""")