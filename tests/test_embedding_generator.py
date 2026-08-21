from backend.rag.embeddings.embedder import BaseEmbedder
from backend.rag.embeddings.generator import generate_embeddings
from data.document import Document


class DummyEmbedder(BaseEmbedder):
    def embed_text(self, text: str) -> list[float]:
        return [0.1, 0.2, 0.3]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [[0.1, 0.2, 0.3] for _ in texts]


def test_generate_embeddings():
    docs = [
        Document("1", "Hello", {"source": "test"}),
        Document("2", "World", {"source": "test"}),
    ]

    results = generate_embeddings(docs, DummyEmbedder())

    assert len(results) == 2
    assert results[0]["id"] == "1"
    assert results[1]["id"] == "2"
    assert len(results[0]["embedding"]) == 3
    assert results[0]["metadata"]["source"] == "test"


def test_empty_documents():
    results = generate_embeddings([], DummyEmbedder())
    assert results == []