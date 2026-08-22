from fastapi import APIRouter
from backend.api.schemas import QueryRequest, QueryResponse
from backend.rag.pipeline import build_retrieval_pipeline
from backend.rag.embeddings.local_embedder import LocalEmbedder
from data.sample_dataset import load_sample_documents

router = APIRouter()

# Build retriever once
documents = load_sample_documents()
embedder = LocalEmbedder()
retriever = build_retrieval_pipeline(documents, embedder)


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    query_vector = embedder.embed_batch([request.query])[0]
    chunks = retriever.retrieve(query_vector, top_k=3)

    return QueryResponse(
        answer="Retrieval completed successfully.",
        retrieved_chunks=[item["document"].text for item in chunks]
    )