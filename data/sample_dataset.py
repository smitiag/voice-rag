from data.document import Document


def load_sample_documents():
    return [
        Document(
            id="doc1",
            text="Retrieval-Augmented Generation combines document retrieval with large language models.",
            metadata={},
        ),
        Document(
            id="doc2",
            text="FAISS is a vector database library used for efficient similarity search.",
            metadata={},
        ),
        Document(
            id="doc3",
            text="Sentence Transformers convert text into dense embeddings for semantic search.",
            metadata={},
        ),
        Document(
            id="doc4",
            text="MSMARCO-XI is a multilingual question answering dataset including Hindi.",
            metadata={},
        ),
        Document(
            id="doc5",
            text="Chunking breaks large documents into smaller passages before embedding.",
            metadata={},
        ),
    ]