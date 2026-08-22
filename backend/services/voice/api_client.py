import httpx

API_URL = "http://127.0.0.1:8000/query"


def ask_rag(query: str) -> dict:
    """
    Sends transcript to the RAG API and returns JSON response.
    """

    response = httpx.post(
        API_URL,
        json={"query": query},
        timeout=30.0,
    )

    response.raise_for_status()
    return response.json()