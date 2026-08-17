from sentence_transformers import SentenceTransformer


class Embedder:
    """Generate vector embeddings for text."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        """Generate an embedding for a single text."""
        if not text.strip():
            raise ValueError("text must not be empty")

        embedding = self.model.encode(text)
        return embedding.tolist()