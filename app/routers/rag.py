from fastapi import APIRouter

from app.models.rag import RagRequest
from app.prompts.kiberlab_prompt import kiberlab_prompt
from app.services.rag_service import load_kiberlab_context
from app.services.llm_service import ask_llm
from app.services.chunk_service import split_text
from app.services.search_service import find_relevant_chunk
from app.services.retrieval_service import retrieve_context
from app.services.vector_store_service import build_kiberlab_vector_store

router = APIRouter()


@router.post("/rag")
def rag(request: RagRequest):

    full_text = load_kiberlab_context()

    context = retrieve_context(
        request.question,
        full_text
    )

    prompt = kiberlab_prompt.format(
        context=context,
        question=request.question
    )

    response = ask_llm(prompt)

    return response

@router.post("/rag/index")
def index_kiberlab():
    full_text = load_kiberlab_context()

    result = build_kiberlab_vector_store(full_text)

    return result