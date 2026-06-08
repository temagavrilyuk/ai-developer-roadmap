from fastapi import APIRouter

from app.models.rag import RagRequest
from app.prompts.kiberlab_prompt import kiberlab_prompt
from app.services.rag_service import load_kiberlab_context
from app.services.llm_service import ask_llm

router = APIRouter()


@router.post("/rag")
def rag(request: RagRequest):

    context = load_kiberlab_context()

    prompt = kiberlab_prompt.format(
        context=context,
        question=request.question
    )

    response = ask_llm(prompt)

    return response