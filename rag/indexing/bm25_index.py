from rank_bm25 import BM25Okapi

def _doc_text(doc):
    return doc["text"] if isinstance(doc, dict) else doc

def build_bm25(state):
    tokenized = [_doc_text(doc).split() for doc in (state.documents or [])]
    state.bm25_index = BM25Okapi(tokenized)
    return state
