import numpy as np

from app.services.embedding_service import get_embedding


def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)


def find_relevant_chunk_by_embedding(question: str, chunks: list[str]):
    question_embedding = get_embedding(question)

    best_chunk = ""
    best_score = -1

    for chunk in chunks:
        chunk_embedding = get_embedding(chunk)

        score = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk