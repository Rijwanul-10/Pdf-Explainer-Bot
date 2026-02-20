from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pdf(state):
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = state.documents or []

    if docs and isinstance(docs[0], dict):
        # List of dicts from load_pdf_with_metadata: preserve page/chapter per chunk
        chunks = []
        for d in docs:
            text = d.get("text", "")
            page = d.get("page")
            chapter = d.get("chapter")
            for part in splitter.split_text(text):
                chunks.append({"text": part, "page": page, "chapter": chapter})
        state.documents = chunks
    else:
        # List of strings (legacy): join, split, emit dicts with no metadata
        text = "\n".join(docs) if docs else ""
        state.documents = [
            {"text": part, "page": None, "chapter": None}
            for part in splitter.split_text(text)
        ]
    return state
