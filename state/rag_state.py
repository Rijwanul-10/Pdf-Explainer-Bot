from typing import List, Any
from dataclasses import dataclass

@dataclass
class RAGState:
    pdf_path: str = ""
    documents: List[str] = None
    vector_store: Any = None
    bm25_index: Any = None
    question: str = ""
    vector_results: List[str] = None
    keyword_results: List[str] = None
    merged_context: List[str] = None
    final_answer: str = ""
