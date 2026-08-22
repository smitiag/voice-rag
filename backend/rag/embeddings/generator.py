from backend.rag.embeddings.embedder import BaseEmbedder
from data.document import Document


def generate_embeddings(
    documents: list[Document],
    embedder: BaseEmbedder,
) -> list[dict]:
    """
    Generate embeddings for a list of Documents.
    """

    if not documents:
        return []

    texts = [doc.text for doc in documents]
    vectors = embedder.embed_batch(texts)

    results = []

    for doc, vector in zip(documents, vectors):
        results.append({
            "id": doc.id,
            "text": doc.text,
            "embedding": vector,
            "metadata": doc.metadata,
        })

    return results