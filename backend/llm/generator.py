from backend.llm.prompts import build_prompt


def generate_answer(query: str, contexts: list[str]) -> str:
    """
    Guardrail-based answer generator.
    Currently returns grounded responses only.
    """

    if not contexts:
        return "I don't have enough information in the provided documents."

    # Prompt is prepared for future LLM integration
    _ = build_prompt(query, contexts)

    # For now, answer using retrieved context only
    return contexts[0]