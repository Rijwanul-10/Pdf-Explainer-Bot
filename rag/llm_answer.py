from config.llm_config import llm
from prompts.rag_prompt import SYSTEM_PROMPT, USER_PROMPT

def llm_answer(state):
    prompt = SYSTEM_PROMPT + USER_PROMPT.format(
        context="\n".join(state.merged_context),
        question=state.question
    )
    response = llm.invoke(prompt)
    state.final_answer = response.content
    return state
