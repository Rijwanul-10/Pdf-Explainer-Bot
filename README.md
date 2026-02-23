## Pdf-Explainer-Bot

An interactive Streamlit app that turns your PDF textbooks into explainable multiple‑choice quizzes.

Teachers upload a reference PDF, create quiz questions and options, and students can then attempt the quiz. When a student gets a question wrong, the app retrieves relevant passages from the PDF (using a RAG pipeline with FAISS + BM25) and asks an LLM to generate a focused explanation grounded in the textbook.

---

## Features

- **Teacher workflow**
  - Upload a PDF chapter and store it as the authoritative source.
  - Create multiple‑choice questions with any number of options.
  - Mark the correct answer for each question.
  - Inspect the current quiz configuration.

- **Student workflow**
  - Select the **Teacher** or **Student** role via a sidebar toggle (`utils.auth_mock.get_role`).
  - Attempt quizzes created by the teacher.
  - See per‑question correctness feedback after submission.
  - Request a **detailed explanation** for incorrect answers that is generated from the PDF content.

- **RAG & explanation**
  - PDF loading via `PyPDFLoader`.
  - Text chunking with `RecursiveCharacterTextSplitter`.
  - Semantic search using **HuggingFace** embeddings + **FAISS**.
  - Keyword search using **BM25**.
  - Hybrid merge of vector and keyword results.
  - Explanation generation via a Groq‑hosted LLM (`config.llm_config.llm`) using only retrieved context.

---

## Tech Stack

- **Python** (3.11 recommended)
- **Streamlit** – UI for teacher/student flows (`app.py`)
- **LangChain** + **langchain-community**
- **LangGraph** – graph‑based RAG pipeline (`graph/rag_graph.py`, `graph/explanation_graph.py`)
- **FAISS** – vector store
- **rank-bm25** – keyword retrieval
- **sentence-transformers / HuggingFaceEmbeddings**
- **Groq LLM** via `langchain-groq`
- **python-dotenv** – environment variable loading

See `requirements.txt` for the full dependency list.

---

## Project Structure

```text
app.py                         # Streamlit app (Teacher/Student panels)
config/
  llm_config.py                # ChatGroq LLM configuration (uses GROQ_API_KEY)
graph/
  rag_graph.py                 # Core RAG pipeline graph (PDF QA)
  explanation_graph.py         # Explanation-only graph
prompts/
  rag_prompt.py                # Base RAG prompt
  explanation_prompt.py        # Explanation-specific prompt builder
rag/
  loaders/load_pdf.py          # PDF loading with chapter metadata
  chunk_pdf.py                 # Text chunking
  indexing/
    bm25_index.py              # BM25 index builder
    embed_store.py             # FAISS vector store creation
  retrieval/
    vector_retrieve.py         # Vector search nodes
    keyword_retrieve.py        # Keyword/BM25 search nodes
    hybrid_merge.py            # Hybrid merge of results
  explanation/
    explain_answer.py          # Graph node to explain answers
    explain_from_pdf.py        # Standalone PDF-based explanation function
  find_correct_answer.py       # Utility to infer correct option from PDF
quiz/
  create_quiz.py               # Quiz creation helpers
  attempt_quiz.py              # (Simple) quiz attempt model
  evaluate_quiz.py             # Quiz evaluation logic
state/
  rag_state.py                 # Shared RAG state dataclass
utils/
  auth_mock.py                 # Mock role selector (Teacher/Student)
```

---

## Setup

1. **Clone the repo**

   ```bash
   git clone <your-repo-url>
   cd Pdf-Explainer-Bot
   ```

2. **Create & activate a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   # or cmd
   .venv\Scripts\activate.bat
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

   > **Security note:** Do **not** commit real API keys to git. Use placeholders locally and keep the real key in your private `.env`.

---

## Running the App

From the project root:

```bash
streamlit run app.py
```

Then open the URL printed in the terminal (typically `http://localhost:8501`).

- Use the sidebar role picker to switch between **Teacher** and **Student**.
- As a **Teacher**, upload a PDF and create quiz questions.
- As a **Student**, answer the quiz and, for incorrect answers, click the **Explain** button to see a PDF‑grounded explanation.

---

## Notes & Limitations

- The authentication layer is a simple mock (`utils.auth_mock`) for local/testing use only.
- Explanations are constrained to the retrieved PDF chunks; if the answer is not clearly in the document, explanations may be vague.
- Retrieval quality depends on the embedding model (`all-MiniLM-L6-v2`) and BM25 configuration; adjust chunking and models for your data if needed.
