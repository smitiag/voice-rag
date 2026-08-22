SYSTEM_PROMPT = """
You are a helpful RAG assistant.

Rules:
1. Answer ONLY from the retrieved context.
2. Do not invent facts.
3. If the context is insufficient, reply:
   "I don't have enough information in the provided documents."
4. Keep answers concise and grounded.
"""


def build_prompt(query: str, contexts: list[str]) -> str:
    context_block = "\n\n".join(
        [f"Context {i+1}: {text}" for i, text in enumerate(contexts)]
    )

    return f"""
{SYSTEM_PROMPT}

Retrieved Context:
{context_block}

User Question:
{query}

Answer:
"""