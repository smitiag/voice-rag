from __future__ import annotations

from backend.rag.embeddings.embedder import BaseEmbedder
from backend.rag.retrieval.retriever import Retriever
from backend.rag.retrieval.vector_store import VectorStore
from data.document import Document


def build_retrieval_pipeline(
    documents: list[Document],
    embedder: BaseEmbedder,
) -> Retriever:
    """
    Build complete retrieval pipeline.
    """

    if not documents:
        store = VectorStore(dimension=384)
        return Retriever(store)

    texts = [doc.text for doc in documents]
    vectors = embedder.embed_batch(texts)

    dimension = len(vectors[0])

    store = VectorStore(dimension=dimension)
    store.add(documents, vectors)

    return Retriever(store)