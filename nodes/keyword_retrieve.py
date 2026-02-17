def keyword_retrieve(state):
    scores = state.bm25_index.get_top_n(
        state.question.split(), state.documents, n=3
    )
    state.keyword_results = scores
    return state
