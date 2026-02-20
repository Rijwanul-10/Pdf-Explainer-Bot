from prompts.explanation_prompt import build_prompt
from config.llm_config import llm

def generate_explanation(question, correct_answer, retrieved_chunks):
    prompt = build_prompt(
        question=question,
        answer=correct_answer,
        context=retrieved_chunks
    )
    return llm.invoke(prompt).content