from langchain_community.document_loaders import PyPDFLoader

def load_pdf(state):
    loader = PyPDFLoader(state.pdf_path)
    docs = loader.load()
    state.documents = [d.page_content for d in docs]
    return state
