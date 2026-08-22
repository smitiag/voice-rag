import re


def clean_text(text: str) -> str:
    """
    Clean and normalize text without changing its meaning.
    """

    if not isinstance(text, str):
        return ""

    # Normalize line breaks and tabs
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")

    # Collapse repeated whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def preprocess_record(record: dict) -> dict | None:
    """
    Convert a raw dataset record into a clean RAG-ready record.
    """

    query = clean_text(record.get("query", ""))
    answer = clean_text(record.get("Answer", ""))

    # Ignore records without usable text
    if not query and not answer:
        return None

    return {
        "query_id": record.get("query_id"),
        "query": query,
        "answer": answer,
    }