import pytest

from data.chunker import fixed_size_chunks, sentence_based_chunks
from data.document import Document

def test_sentence_based_chunks():
    document = Document(
        id="doc2",
        text=(
            "This is the first sentence. "
            "This is the second sentence. "
            "This is the third sentence."
        ),
        metadata={"source": "test"},
    )

    chunks = sentence_based_chunks(
        document,
        max_chars=50,
    )

    assert len(chunks) == 3

    assert chunks[0].text == "This is the first sentence."
    assert chunks[1].text == "This is the second sentence."
    assert chunks[2].text == "This is the third sentence."


def test_sentence_chunk_metadata():
    document = Document(
        id="doc2",
        text="First sentence. Second sentence.",
        metadata={"source": "test"},
    )

    chunks = sentence_based_chunks(
        document,
        max_chars=100,
    )

    assert len(chunks) == 1
    assert chunks[0].metadata["parent_id"] == "doc2"
    assert chunks[0].metadata["chunk_index"] == 0
    assert chunks[0].metadata["source"] == "test"


def test_invalid_sentence_chunk_size():
    document = Document(
        id="doc2",
        text="Some sentence.",
        metadata={},
    )

    with pytest.raises(ValueError):
        sentence_based_chunks(document, max_chars=0)

def test_fixed_size_chunks():
    document = Document(
        id="doc1",
        text="abcdefghijklmnopqrstuvwxyz",
        metadata={"source": "test"},
    )

    chunks = fixed_size_chunks(
        document,
        chunk_size=10,
        overlap=2,
    )

    assert len(chunks) == 4

    assert chunks[0].text == "abcdefghij"
    assert chunks[1].text == "ijklmnopqr"
    assert chunks[2].text == "qrstuvwxyz"
    assert chunks[3].text == "yz"

def test_chunk_metadata():
    document = Document(
        id="doc1",
        text="abcdefghijklmnopqrstuvwxyz",
        metadata={"source": "test"},
    )

    chunks = fixed_size_chunks(
        document,
        chunk_size=10,
        overlap=2,
    )

    assert chunks[0].id == "doc1_chunk_0"
    assert chunks[0].metadata["parent_id"] == "doc1"
    assert chunks[0].metadata["chunk_index"] == 0
    assert chunks[0].metadata["source"] == "test"


def test_invalid_chunk_size():
    document = Document(
        id="doc1",
        text="hello world",
        metadata={},
    )

    with pytest.raises(ValueError):
        fixed_size_chunks(document, chunk_size=0)


def test_invalid_overlap():
    document = Document(
        id="doc1",
        text="hello world",
        metadata={},
    )

    with pytest.raises(ValueError):
        fixed_size_chunks(document, chunk_size=10, overlap=10)


def test_empty_document():
    document = Document(
        id="doc1",
        text="",
        metadata={},
    )

    assert fixed_size_chunks(document) == []