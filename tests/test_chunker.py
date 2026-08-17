from backend.rag.chunking.chunker import (
    fixed_size_chunks,
    sentence_chunks,
)


def test_fixed_size_chunks():
    text = "one two three four five six seven eight"

    chunks = fixed_size_chunks(
        text,
        chunk_size=4,
        overlap=1,
    )

    assert chunks == [
        "one two three four",
        "four five six seven",
        "seven eight",
    ]


def test_sentence_chunks():
    text = (
        "Sentence one. "
        "Sentence two. "
        "Sentence three. "
        "Sentence four."
    )

    chunks = sentence_chunks(
        text,
        sentences_per_chunk=2,
    )

    assert chunks == [
        "Sentence one. Sentence two.",
        "Sentence three. Sentence four.",
    ]


def test_empty_text():
    assert fixed_size_chunks("") == []
    assert sentence_chunks("") == []


def test_invalid_fixed_size_parameters():
    try:
        fixed_size_chunks("hello world", chunk_size=0)
        assert False
    except ValueError:
        assert True


def test_invalid_sentence_parameters():
    try:
        sentence_chunks("Hello.", sentences_per_chunk=0)
        assert False
    except ValueError:
        assert True