from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def embed_store(state):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    state.vector_store = FAISS.from_texts(state.documents, embeddings)
    return state
