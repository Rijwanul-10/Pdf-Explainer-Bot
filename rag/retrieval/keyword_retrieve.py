def _to_text(doc):
    return doc["text"] if isinstance(doc, dict) else doc

def keyword_retrieve(state):
    scores = state.bm25_index.get_top_n(
        state.question.split(), state.documents, n=3
    )
    state.keyword_results = [_to_text(d) for d in scores]
    return state
