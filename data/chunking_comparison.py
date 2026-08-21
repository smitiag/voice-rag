from statistics import mean

from data.chunker import fixed_size_chunks, sentence_based_chunks
from data.document import Document


def compare_chunking_strategies(
    document: Document,
    fixed_chunk_size: int = 100,
    fixed_overlap: int = 20,
    sentence_max_chars: int = 100,
) -> dict:
    """
    Compare fixed-size and sentence-based chunking
    using simple measurable characteristics.
    """

    fixed_chunks = fixed_size_chunks(
        document,
        chunk_size=fixed_chunk_size,
        overlap=fixed_overlap,
    )

    sentence_chunks = sentence_based_chunks(
        document,
        max_chars=sentence_max_chars,
    )

    def lengths(chunks):
        return [len(chunk.text) for chunk in chunks]

    fixed_lengths = lengths(fixed_chunks)
    sentence_lengths = lengths(sentence_chunks)

    return {
        "fixed_size": {
            "chunk_count": len(fixed_chunks),
            "average_length": (
                mean(fixed_lengths) if fixed_lengths else 0
            ),
            "min_length": min(fixed_lengths) if fixed_lengths else 0,
            "max_length": max(fixed_lengths) if fixed_lengths else 0,
            "metadata_preserved": all(
                chunk.metadata.get("parent_id") == document.id
                for chunk in fixed_chunks
            ),
        },
        "sentence_based": {
            "chunk_count": len(sentence_chunks),
            "average_length": (
                mean(sentence_lengths) if sentence_lengths else 0
            ),
            "min_length": min(sentence_lengths)
            if sentence_lengths
            else 0,
            "max_length": max(sentence_lengths)
            if sentence_lengths
            else 0,
            "metadata_preserved": all(
                chunk.metadata.get("parent_id") == document.id
                for chunk in sentence_chunks
            ),
        },
    }