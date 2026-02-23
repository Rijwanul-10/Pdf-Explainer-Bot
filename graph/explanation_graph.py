from langgraph.graph import StateGraph
from state.rag_state import RAGState
from rag.retrieval.vector_retrieve import vector_search
from rag.retrieval.keyword_retrieve import keyword_search
from rag.retrieval.hybrid_merge import hybrid_merge
from rag.explanation.explain_answer import generate_explanation

def build_explanation_graph():
    graph = StateGraph(RAGState)

    graph.add_node("vector", vector_search)
    graph.add_node("keyword", keyword_search)
    graph.add_node("merge", hybrid_merge)
    graph.add_node("explain", generate_explanation)

    graph.set_entry_point("vector")
    graph.add_edge("vector", "keyword")
    graph.add_edge("keyword", "merge")
    graph.add_edge("merge", "explain")

    return graph.compile()