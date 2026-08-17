import pytest

from backend.rag.embeddings.embedder import Embedder


def test_embedder_returns_embedding():
    embedder = Embedder()

    result = embedder.embed("This is a test sentence.")

    assert isinstance(result, list)
    assert len(result) == 384
    assert all(isinstance(value, float) for value in result)


def test_embedder_rejects_empty_text():
    embedder = Embedder()

    with pytest.raises(ValueError):
        embedder.embed("")


def test_embedder_rejects_whitespace_text():
    embedder = Embedder()

    with pytest.raises(ValueError):
        embedder.embed("   ")