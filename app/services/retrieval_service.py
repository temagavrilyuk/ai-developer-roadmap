from app.services.chunk_service import split_text
from app.services.semantic_search_service import find_relevant_chunk_by_embedding


def retrieve_context(question: str, text: str) -> str:
    chunks = split_text(text, chunk_size=500)

    context = find_relevant_chunk_by_embedding(question, chunks)

    return context