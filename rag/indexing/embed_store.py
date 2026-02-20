from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    texts = [c["text"] for c in text_chunks]
    metadatas = [{"page": c["page"], "chapter": c["chapter"]} for c in text_chunks]
    return FAISS.from_texts(texts, embeddings, metadatas=metadatas)