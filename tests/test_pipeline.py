import pytest

from backend.rag.pipeline import RAGPipeline


def test_pipeline_adds_and_retrieves_text():
    pipeline = RAGPipeline()

    pipeline.add_text(
        "Python is a programming language. "
        "RAG retrieves relevant information from documents. "
        "Embeddings represent text as vectors."
    )

    results = pipeline.retrieve(
        "What does RAG retrieve?",
        top_k=2,
    )

    assert len(results) == 2
    assert any("RAG" in result for result in results)


def test_pipeline_rejects_empty_text():
    pipeline = RAGPipeline()

    with pytest.raises(ValueError):
        pipeline.add_text("")


def test_pipeline_rejects_empty_query():
    pipeline = RAGPipeline()

    with pytest.raises(ValueError):
        pipeline.retrieve("")


def test_pipeline_handles_multiple_documents():
    pipeline = RAGPipeline()

    pipeline.add_text(
        "Python is used for software development. "
        "FastAPI is a Python web framework."
    )

    pipeline.add_text(
        "The solar system contains planets. "
        "Earth is the third planet from the Sun."
    )

    results = pipeline.retrieve(
        "Which planet is Earth?",
        top_k=2,
    )

    assert len(results) == 2
    assert any("Earth" in result for result in results)