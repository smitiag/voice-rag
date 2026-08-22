from fastapi import APIRouter
from backend.api.schemas import QueryRequest, QueryResponse
from backend.rag.pipeline import build_retrieval_pipeline
from backend.rag.embeddings.local_embedder import LocalEmbedder
from data.sample_dataset import load_sample_documents
from backend.llm.generator import generate_answer

router = APIRouter()

documents = load_sample_documents()
embedder = LocalEmbedder()
retriever = build_retrieval_pipeline(documents, embedder)


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    query_vector = embedder.embed_batch([request.query])[0]
    results = retriever.retrieve(query_vector, top_k=3)

    # Guardrail: keep only sufficiently similar chunks
    filtered = [r for r in results if r["score"] >= 0.45]

    contexts = [r["document"].text for r in filtered]

    answer = generate_answer(request.query, contexts)

    return QueryResponse(
    answer=answer,
    retrieved_chunks=contexts,
    citations=list(range(1, len(contexts) + 1))
)