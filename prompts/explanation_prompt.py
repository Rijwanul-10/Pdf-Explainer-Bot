EXPLANATION_PROMPT = """
Context:
{context}

Question: {question}
Correct answer: {answer}

Explain why this answer is correct based on the context above.
"""

def build_prompt(question, answer, context):
    if isinstance(context, list):
        context = "\n\n".join(str(c) for c in context)
    return EXPLANATION_PROMPT.format(
        question=question,
        answer=answer,
        context=context
    )
