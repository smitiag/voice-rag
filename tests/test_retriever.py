import pytest

from backend.rag.retrieval.retriever import Retriever


def test_retriever_returns_relevant_documents():
    retriever = Retriever()

    retriever.add_documents(
        [
            "Python is a programming language.",
            "The sun is a star.",
            "RAG retrieves relevant information.",
        ]
    )

    results = retriever.retrieve("What is RAG?", top_k=1)

    assert len(results) == 1
    assert "RAG" in results[0]


def test_retriever_rejects_empty_query():
    retriever = Retriever()

    with pytest.raises(ValueError):
        retriever.retrieve("")


def test_retriever_rejects_invalid_top_k():
    retriever = Retriever()

    with pytest.raises(ValueError):
        retriever.retrieve("What is RAG?", top_k=0)