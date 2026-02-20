from langchain_community.document_loaders import PyPDFLoader

def load_pdf_with_metadata(pdf_path, chapter=""):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    enriched_docs = []
    for d in docs:
        enriched_docs.append({
            "text": d.page_content,
            "page": d.metadata.get("page"),
            "chapter": chapter
        })

    return enriched_docs

def load_pdf(state):
    chapter = getattr(state, "chapter", "") or ""
    state.documents = load_pdf_with_metadata(state.pdf_path, chapter)
    return state