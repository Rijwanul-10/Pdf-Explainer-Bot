from langgraph.graph import StateGraph
from state.rag_state import RAGState

from rag.loaders.load_pdf import load_pdf
from rag.chunk_pdf import chunk_pdf
from rag.indexing.embed_store import embed_store
from rag.indexing.bm25_index import build_bm25
from rag.retrieval.vector_retrieve import vector_retrieve
from rag.retrieval.keyword_retrieve import keyword_retrieve
from rag.retrieval.hybrid_merge import hybrid_merge
from rag.llm_answer import llm_answer

def build_graph():
    graph = StateGraph(RAGState)

    graph.add_node("load_pdf", load_pdf)
    graph.add_node("chunk_pdf", chunk_pdf)
    graph.add_node("embed_store", embed_store)
    graph.add_node("bm25", build_bm25)
    graph.add_node("vector", vector_retrieve)
    graph.add_node("keyword", keyword_retrieve)
    graph.add_node("merge", hybrid_merge)
    graph.add_node("answer", llm_answer)

    graph.set_entry_point("load_pdf")
    graph.add_edge("load_pdf", "chunk_pdf")
    graph.add_edge("chunk_pdf", "embed_store")
    graph.add_edge("embed_store", "bm25")
    graph.add_edge("bm25", "vector")
    graph.add_edge("vector", "keyword")
    graph.add_edge("keyword", "merge")
    graph.add_edge("merge", "answer")

    return graph.compile()
