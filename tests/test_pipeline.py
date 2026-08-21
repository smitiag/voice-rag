from backend.rag.pipeline import build_embedding_pipeline
from backend.rag.embeddings.embedder import BaseEmbedder
from data.document import Document


class DummyEmbedder(BaseEmbedder):
    def embed_text(self, text: str) -> list[float]:
        return [1.0, 2.0, 3.0]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [[1.0, 2.0, 3.0] for _ in texts]


def test_embedding_pipeline():
    docs = [
        Document(
            id="1",
            text="Hello",
            metadata={"source": "test"},
        )
    ]

    result = build_embedding_pipeline(
        docs,
        DummyEmbedder(),
    )

    assert len(result) == 1
    assert result[0]["id"] == "1"
    assert result[0]["text"] == "Hello"
    assert result[0]["embedding"] == [1.0, 2.0, 3.0]
    assert result[0]["metadata"]["source"] == "test"


def test_pipeline_empty_input():
    result = build_embedding_pipeline(
        [],
        DummyEmbedder(),
    )

    assert result == []