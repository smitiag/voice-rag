from backend.rag.chunking.chunker import sentence_chunks
from backend.rag.retrieval.retriever import Retriever


class RAGPipeline:
    """Coordinate chunking and retrieval for RAG."""

    def __init__(
        self,
        chunk_size: int = 3,
        sentences_per_chunk: int = 2,
    ):
        self.chunk_size = chunk_size
        self.sentences_per_chunk = sentences_per_chunk
        self.retriever = Retriever()

    def add_text(self, text: str) -> None:
        """Chunk text and add the chunks to the retriever."""
        if not text.strip():
            raise ValueError("text must not be empty")

        chunks = sentence_chunks(
            text,
            sentences_per_chunk=self.sentences_per_chunk,
        )

        if chunks:
            self.retriever.add_documents(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        """Retrieve relevant chunks for a query."""
        return self.retriever.retrieve(query, top_k=top_k)