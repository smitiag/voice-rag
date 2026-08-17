import chromadb

from backend.rag.embeddings.embedder import Embedder


class Retriever:
    """Store text embeddings and retrieve relevant documents."""

    def __init__(self):
        self.client = chromadb.EphemeralClient()
        self.collection = self.client.get_or_create_collection(
            name="voice_rag"
        )
        self.embedder = Embedder()

    def add_documents(self, documents: list[str]) -> None:
        """Add documents to the vector store."""
        if not documents:
            return

        embeddings = [
            self.embedder.embed(document)
            for document in documents
        ]

        existing_count = self.collection.count()
        ids = [
            f"doc_{existing_count + i}"
            for i in range(len(documents))
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
        )

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        """Retrieve the most relevant documents for a query."""
        if not query.strip():
            raise ValueError("query must not be empty")

        if top_k <= 0:
            raise ValueError("top_k must be greater than 0")

        query_embedding = self.embedder.embed(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results["documents"][0]