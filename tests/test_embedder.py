import pytest

from backend.rag.embeddings.embedder import BaseEmbedder


class DummyEmbedder(BaseEmbedder):
    def embed_text(self, text: str) -> list[float]:
        if not text.strip():
            return []
        return [0.1, 0.2, 0.3]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_text(t) for t in texts]


def test_single_embedding():
    embedder = DummyEmbedder()

    vector = embedder.embed_text("hello world")

    assert isinstance(vector, list)
    assert len(vector) == 3


def test_batch_embedding():
    embedder = DummyEmbedder()

    vectors = embedder.embed_batch(["hello", "world"])

    assert len(vectors) == 2
    assert vectors[0] == [0.1, 0.2, 0.3]


def test_empty_text():
    embedder = DummyEmbedder()

    assert embedder.embed_text("") == []