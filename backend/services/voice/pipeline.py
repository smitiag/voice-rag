from backend.services.voice.api_client import ask_rag


def process_voice_query(transcript: str) -> dict:
    """
    Takes speech transcript, sends it to the RAG API,
    and returns the grounded response.
    """

    result = ask_rag(transcript)

    return {
        "transcript": transcript,
        "answer": result["answer"],
        "citations": result["citations"],
    }