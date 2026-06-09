import chromadb

from app.services.chunk_service import split_text


client = chromadb.PersistentClient(
    path="app/chroma_db"
)

collection = client.get_or_create_collection(
    name="kiberlab"
)


def build_kiberlab_vector_store(text: str):
    chunks = split_text(text, chunk_size=500)

    ids = []
    documents = []

    for index, chunk in enumerate(chunks):
        ids.append(f"kiberlab-{index}")
        documents.append(chunk)

    collection.add(
        ids=ids,
        documents=documents
    )

    return {
        "chunks_count": len(chunks)
    }


def search_kiberlab_context(question: str):
    results = collection.query(
        query_texts=[question],
        n_results=1
    )

    return results["documents"][0][0]