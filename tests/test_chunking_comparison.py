from data.chunking_comparison import compare_chunking_strategies
from data.document import Document


def test_compare_chunking_strategies():
    document = Document(
        id="comparison_doc",
        text=(
            "This is the first sentence. "
            "This is the second sentence. "
            "This is the third sentence. "
            "This is the fourth sentence."
        ),
        metadata={"source": "test"},
    )

    result = compare_chunking_strategies(
        document,
        fixed_chunk_size=50,
        fixed_overlap=10,
        sentence_max_chars=50,
    )

    assert "fixed_size" in result
    assert "sentence_based" in result

    assert result["fixed_size"]["chunk_count"] > 0
    assert result["sentence_based"]["chunk_count"] > 0


def test_comparison_metrics_are_valid():
    document = Document(
        id="comparison_doc",
        text=(
            "First sentence. "
            "Second sentence. "
            "Third sentence."
        ),
        metadata={"source": "test"},
    )

    result = compare_chunking_strategies(document)

    for strategy in ("fixed_size", "sentence_based"):
        metrics = result[strategy]

        assert metrics["chunk_count"] > 0
        assert metrics["average_length"] > 0
        assert metrics["min_length"] > 0
        assert metrics["max_length"] >= metrics["min_length"]
        assert metrics["metadata_preserved"] is True


def test_empty_document_comparison():
    document = Document(
        id="empty",
        text="",
        metadata={},
    )

    result = compare_chunking_strategies(document)

    assert result["fixed_size"]["chunk_count"] == 0
    assert result["sentence_based"]["chunk_count"] == 0
    assert result["fixed_size"]["average_length"] == 0
    assert result["sentence_based"]["average_length"] == 0