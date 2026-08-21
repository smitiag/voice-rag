from backend.rag.embeddings.local_embedder import LocalEmbedder


def test_single_embedding_dimension():
    embedder = LocalEmbedder()

    vector = embedder.embed_text("What is AI?")

    assert isinstance(vector, list)
    assert len(vector) == 384


def test_batch_embeddings():
    embedder = LocalEmbedder()

    vectors = embedder.embed_batch([
        "hello",
        "world",
    ])

    assert len(vectors) == 2
    assert len(vectors[0]) == 384
    assert len(vectors[1]) == 384