from rank_bm25 import BM25Okapi

def build_bm25(state):
    tokenized = [doc.split() for doc in state.documents]
    state.bm25_index = BM25Okapi(tokenized)
    return state
