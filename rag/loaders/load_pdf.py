from langchain_community.document_loaders import PyPDFLoader

def load_pdf_with_metadata(pdf_path, chapter):
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