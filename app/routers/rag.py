from fastapi import APIRouter

from app.models.rag import RagRequest
from app.prompts.kiberlab_prompt import kiberlab_prompt
from app.services.rag_service import load_kiberlab_context
from app.services.llm_service import ask_llm
from app.services.chunk_service import split_text
from app.services.search_service import find_relevant_chunk

router = APIRouter()


@router.post("/rag")
def rag(request: RagRequest):

    full_text = load_kiberlab_context()

    chunks = split_text(full_text, chunk_size=500)

    context = find_relevant_chunk(
        request.question,
        chunks
    )

    prompt = kiberlab_prompt.format(
        context=context,
        question=request.question
    )

    response = ask_llm(prompt)

    return response