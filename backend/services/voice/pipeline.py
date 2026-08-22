from data.sample_dataset import load_sample_documents
from backend.rag.embeddings.local_embedder import LocalEmbedder
from backend.rag.pipeline import build_retrieval_pipeline
from backend.llm.generator import generate_answer
from backend.services.voice.tts import text_to_speech

# Initialize once
documents = load_sample_documents()
embedder = LocalEmbedder()
retriever = build_retrieval_pipeline(documents, embedder)


def process_voice_query(transcript: str) -> dict:
    # Embed query
    query_vector = embedder.embed_batch([transcript])[0]

    # Retrieve chunks
    chunks = retriever.retrieve(query_vector, top_k=3)

    # Extract text only
    contexts = [item["document"].text for item in chunks]

    # Generate answer (returns STRING)
    answer = generate_answer(transcript, contexts)

    # Text → Speech
    audio_file = text_to_speech(answer)

    return {
        "transcript": transcript,
        "answer": answer,
        "citations": [1] if contexts else [],
        "audio_file": audio_file,
    }