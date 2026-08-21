import pytest

from backend.rag.retrieval.vector_store import VectorStore
from data.document import Document


def test_add_vectors():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Hello", metadata={}),
        Document(id="doc2", text="World", metadata={}),
    ]

    vectors = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]

    store.add(docs, vectors)

    assert store.size() == 2


def test_empty_store():
    store = VectorStore(dimension=3)

    scores, ids = store.search([0.1, 0.2, 0.3])

    assert scores == []
    assert ids == []


def test_id_vector_mismatch():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Hello", metadata={}),
    ]

    vectors = [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]

    with pytest.raises(ValueError):
        store.add(docs, vectors)


def test_add_documents():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Hello", metadata={}),
        Document(id="doc2", text="World", metadata={}),
    ]

    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    store.add(docs, vectors)

    assert store.size() == 2
    assert "doc1" in store.documents
    assert "doc2" in store.documents


def test_document_vector_mismatch():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Hello", metadata={}),
    ]

    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    with pytest.raises(ValueError):
        store.add(docs, vectors)


def test_search_returns_top_k():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Apple", metadata={}),
        Document(id="doc2", text="Banana", metadata={}),
        Document(id="doc3", text="Cherry", metadata={}),
    ]

    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]

    store.add(docs, vectors)

    scores, ids = store.search([1.0, 0.0, 0.0], top_k=2)

    assert len(scores) == 2
    assert len(ids) == 2
    assert ids[0] == "doc1"


def test_search_empty_store():
    store = VectorStore(dimension=3)

    scores, ids = store.search([1.0, 0.0, 0.0])

    assert scores == []
    assert ids == []


def test_top_k_larger_than_store():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Hello", metadata={}),
        Document(id="doc2", text="World", metadata={}),
    ]

    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    store.add(docs, vectors)

    scores, ids = store.search([1.0, 0.0, 0.0], top_k=10)

    assert len(ids) == 2
    assert store.size() == 2