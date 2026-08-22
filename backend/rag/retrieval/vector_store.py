from __future__ import annotations

import faiss
import numpy as np

from data.document import Document


class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents: dict[str, Document] = {}

    def add(
        self,
        documents: list[Document],
        vectors: list[list[float]],
    ) -> None:
        """Add documents and their embeddings to the vector store."""

        if len(documents) != len(vectors):
            raise ValueError("documents and vectors must have same length")

        if not documents:
            return

        array = np.asarray(vectors, dtype="float32")
        self.index.add(array)

        for doc in documents:
            self.documents[doc.id] = doc

    def size(self) -> int:
        """Return number of indexed vectors."""
        return self.index.ntotal

    def search(
        self,
        query_vector: list[float],
        top_k: int = 3,
    ) -> tuple[list[float], list[str]]:
        """Return top-k most similar document IDs and scores."""

        if self.size() == 0:
            return [], []

        query = np.asarray([query_vector], dtype="float32")

        scores, indices = self.index.search(
            query,
            min(top_k, self.size()),
        )

        result_scores = scores[0].tolist()

        doc_ids = list(self.documents.keys())
        result_ids = [doc_ids[i] for i in indices[0]]

        return result_scores, result_ids