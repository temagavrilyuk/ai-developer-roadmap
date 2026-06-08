from app.services.chunk_service import split_text
from app.services.search_service import find_relevant_chunk


def retrieve_context(question: str, text: str) -> str:
    chunks = split_text(text, chunk_size=500)

    context = find_relevant_chunk(
        question,
        chunks
    )

    return context