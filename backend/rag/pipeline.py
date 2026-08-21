from backend.rag.embeddings.generator import generate_embeddings
from backend.rag.embeddings.embedder import BaseEmbedder
from data.document import Document


def build_embedding_pipeline(
    documents: list[Document],
    embedder: BaseEmbedder,
) -> list[dict]:
    """
    Complete embedding pipeline.
    Takes documents and returns documents + embeddings.
    """

    return generate_embeddings(documents, embedder)