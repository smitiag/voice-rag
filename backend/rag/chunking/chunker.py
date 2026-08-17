from __future__ import annotations

import re
from typing import List


def fixed_size_chunks(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> List[str]:
    """Split text into fixed-size chunks with overlap."""

    if not text.strip():
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")

    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + chunk_size])

        if chunk:
            chunks.append(chunk)

        if start + chunk_size >= len(words):
            break

    return chunks


def sentence_chunks(
    text: str,
    sentences_per_chunk: int = 5,
) -> List[str]:
    """Split text into chunks containing multiple complete sentences."""

    if not text.strip():
        return []

    if sentences_per_chunk <= 0:
        raise ValueError("sentences_per_chunk must be greater than 0")

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return [
        " ".join(sentences[i : i + sentences_per_chunk])
        for i in range(0, len(sentences), sentences_per_chunk)
    ]