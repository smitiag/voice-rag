from backend.rag.retrieval.retriever import Retriever
from backend.rag.retrieval.vector_store import VectorStore
from data.document import Document


def build_store():
    store = VectorStore(dimension=3)

    docs = [
        Document(id="doc1", text="Apple", metadata={"source": "A"}),
        Document(id="doc2", text="Banana", metadata={"source": "B"}),
        Document(id="doc3", text="Cherry", metadata={"source": "C"}),
    ]

    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]

    store.add(docs, vectors)
    return store


def test_top_k_retrieval():
    retriever = Retriever(build_store())

    results = retriever.retrieve([1.0, 0.0, 0.0], top_k=2)

    assert len(results) == 2
    assert results[0]["document"].id == "doc1"
    assert results[0]["document"].text == "Apple"


def test_empty_retrieval():
    retriever = Retriever(VectorStore(dimension=3))

    results = retriever.retrieve([1.0, 0.0, 0.0])

    assert results == []


def test_metadata_preserved():
    retriever = Retriever(build_store())

    result = retriever.retrieve([0.0, 1.0, 0.0], top_k=1)[0]

    assert result["document"].metadata["source"] == "B"


def test_similarity_score_range():
    retriever = Retriever(build_store())

    result = retriever.retrieve([1.0, 0.0, 0.0], top_k=1)[0]

    assert 0.0 <= result["score"] <= 1.0
    assert isinstance(result["distance"], float)