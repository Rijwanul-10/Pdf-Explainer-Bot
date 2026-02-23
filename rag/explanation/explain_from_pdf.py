from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from rank_bm25 import BM25Okapi
from config.llm_config import llm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def explain_from_pdf(pdf_path, question, correct_answer):
    # 1️⃣ Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    texts = [d.page_content for d in docs]

    # 2️⃣ Chunk text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text("\n".join(texts))

    # 3️⃣ Vector store (FAISS)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_texts(chunks, embeddings)

    # 4️⃣ Vector search
    vector_results = vector_store.similarity_search(question, k=3)
    vector_texts = [doc.page_content for doc in vector_results]

    # 5️⃣ BM25 keyword search
    tokenized_chunks = [c.split() for c in chunks]
    bm25 = BM25Okapi(tokenized_chunks)
    keyword_results = bm25.get_top_n(
        question.split(), chunks, n=3
    )

    # 6️⃣ Hybrid merge
    context_chunks = list(dict.fromkeys(
        vector_texts + keyword_results
    ))[:5]

    # 7️⃣ Build prompt
    prompt = f"""
You are an educational assistant.

Explain in detail (5–6 sentences) why the correct answer is:
"{correct_answer}"

Your explanation MUST include:
- Concept explanation
- Chapter name
- Topic name (if identifiable)
- Page number reference (if available)

Use ONLY the textbook content below.
Do NOT add outside knowledge.

Textbook Content:
{chr(10).join(context_chunks)}

Question:
{question}
"""

    # 8️⃣ LLM call
    response = llm.invoke(prompt)

    return response.content