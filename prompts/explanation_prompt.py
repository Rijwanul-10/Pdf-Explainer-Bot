def build_prompt(question, answer, context):
    return f"""
You are an educational assistant.
Explain why the correct answer is "{answer}".
Use only the provided textbook context.

Context:
{context}

Question:
{question}
"""