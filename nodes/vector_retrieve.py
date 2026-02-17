def vector_retrieve(state):
    state.vector_results = [
        doc.page_content for doc in state.vector_store.similarity_search(state.question, k=3)
    ]
    return state
