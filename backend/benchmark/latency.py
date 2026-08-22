import time
import statistics

from backend.rag.embeddings.local_embedder import LocalEmbedder
from backend.rag.pipeline import build_retrieval_pipeline
from backend.llm.generator import generate_answer
from data.sample_dataset import load_sample_documents

# Initialize once
documents = load_sample_documents()
embedder = LocalEmbedder()
retriever = build_retrieval_pipeline(documents, embedder)

queries = [
    "What is FAISS?",
    "Explain vector databases.",
    "What is MSMARCO-XI?",
    "What are embeddings?",
    "How does similarity search work?",
    "What is chunking?",
    "Define retrieval.",
    "Explain multilingual datasets.",
    "What is semantic search?",
    "What is document indexing?"
]

latencies = []

print("Running benchmark...\n")

for q in queries:
    start = time.perf_counter()

    vector = embedder.embed_batch([q])[0]
    chunks = retriever.retrieve(vector, top_k=3)
    contexts = [c["document"].text for c in chunks if c["score"] >= 0.45]
    _ = generate_answer(q, contexts)

    elapsed = (time.perf_counter() - start) * 1000
    latencies.append(elapsed)

    print(f"{q:35} {elapsed:.2f} ms")

latencies.sort()

def percentile(data, p):
    idx = int(round((len(data)-1) * p))
    return data[idx]

print("\n------ RESULTS ------")
print(f"P50 : {percentile(latencies,0.50):.2f} ms")
print(f"P70 : {percentile(latencies,0.70):.2f} ms")
print(f"P100: {max(latencies):.2f} ms")
print(f"AVG : {statistics.mean(latencies):.2f} ms")