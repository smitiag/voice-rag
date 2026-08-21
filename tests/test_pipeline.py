from backend.rag.pipeline import build_retrieval_pipeline
from backend.rag.embeddings.embedder import BaseEmbedder
from data.document import Document


class DummyEmbedder(BaseEmbedder):
    def embed_text(self, text: str) -> list[float]:
        if text == "Apple":
            return [1.0, 0.0, 0.0]
        if text == "Banana":
            return [0.0, 1.0, 0.0]
        return [0.0, 0.0, 1.0]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_text(t) for t in texts]


def test_build_pipeline():
    docs = [
        Document(id="1", text="Apple", metadata={"source": "A"}),
        Document(id="2", text="Banana", metadata={"source": "B"}),
    ]

    retriever = build_retrieval_pipeline(docs, DummyEmbedder())

    results = retriever.retrieve([1.0, 0.0, 0.0], top_k=1)

    assert results[0]["document"].id == "1"
    assert results[0]["document"].metadata["source"] == "A"


def test_empty_pipeline():
    retriever = build_retrieval_pipeline([], DummyEmbedder())

    results = retriever.retrieve([1.0, 0.0, 0.0])

    assert results == []