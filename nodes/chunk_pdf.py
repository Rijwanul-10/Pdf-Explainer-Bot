from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pdf(state):
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    state.documents = splitter.split_text("\n".join(state.documents))
    return state
