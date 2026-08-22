from __future__ import annotations

from backend.rag.retrieval.vector_store import VectorStore
from data.document import Document


class Retriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve(
        self,
        query_vector: list[float],
        top_k: int = 3,
    ) -> list[dict]:
        """
        Returns ranked retrieval results with metadata.
        """

        scores, ids = self.vector_store.search(query_vector, top_k)

        results = []

        for doc_id, distance in zip(ids, scores):
            doc = self.vector_store.documents[doc_id]

            similarity = 1 / (1 + float(distance))

            results.append(
                {
                    "document": doc,
                    "score": similarity,
                    "distance": float(distance),
                }
            )

        return results