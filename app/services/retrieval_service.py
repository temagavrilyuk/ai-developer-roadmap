from app.services.vector_store_service import search_kiberlab_context


def retrieve_context(question: str, text: str) -> str:
    return search_kiberlab_context(question)