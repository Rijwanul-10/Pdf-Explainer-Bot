def hybrid_merge(state):
    merged = list(dict.fromkeys(state.vector_results + state.keyword_results))
    state.merged_context = merged[:5]
    return state
