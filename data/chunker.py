from data.document import Document


def fixed_size_chunks(
    document: Document,
    chunk_size: int = 100,
    overlap: int = 20,
) -> list[Document]:
    """
    Split a document into fixed-size character chunks.

    chunk_size: maximum characters per chunk.
    overlap: number of characters shared between consecutive chunks.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = document.text

    if not text:
        return []

    chunks = []
    start = 0
    chunk_index = 0
    step = chunk_size - overlap

    while start < len(text):
        chunk_text = text[start:start + chunk_size]

        chunks.append(
            Document(
                id=f"{document.id}_chunk_{chunk_index}",
                text=chunk_text,
                metadata={
                    **document.metadata,
                    "parent_id": document.id,
                    "chunk_index": chunk_index,
                },
            )
        )

        chunk_index += 1
        start += step

    return chunks

import re


def sentence_based_chunks(
    document: Document,
    max_chars: int = 300,
) -> list[Document]:
    """
    Split a document into chunks while keeping sentences together.
    """

    if max_chars <= 0:
        raise ValueError("max_chars must be greater than 0")

    if not document.text:
        return []

    sentences = re.split(
        r"(?<=[.!?।])\s+",
        document.text.strip(),
    )

    chunks = []
    current_sentences = []
    current_length = 0
    chunk_index = 0

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        additional_length = (
            len(sentence)
            if not current_sentences
            else len(sentence) + 1
        )

        if (
            current_sentences
            and current_length + additional_length > max_chars
        ):
            chunks.append(
                Document(
                    id=f"{document.id}_chunk_{chunk_index}",
                    text=" ".join(current_sentences),
                    metadata={
                        **document.metadata,
                        "parent_id": document.id,
                        "chunk_index": chunk_index,
                    },
                )
            )

            chunk_index += 1
            current_sentences = [sentence]
            current_length = len(sentence)

        else:
            current_sentences.append(sentence)
            current_length += additional_length

    if current_sentences:
        chunks.append(
            Document(
                id=f"{document.id}_chunk_{chunk_index}",
                text=" ".join(current_sentences),
                metadata={
                    **document.metadata,
                    "parent_id": document.id,
                    "chunk_index": chunk_index,
                },
            )
        )

    return chunks
