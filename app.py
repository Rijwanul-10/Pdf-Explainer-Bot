import streamlit as st
from graph.rag_graph import build_graph
from state.rag_state import RAGState

st.title(" PDF Explaining Chatbot") 

pdf = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Ask a question")

if pdf and question:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    graph = build_graph()

    state = RAGState(
        pdf_path="temp.pdf",
        question=question
    )

    result = graph.invoke(state)
    st.write("### Answer")
    st.write(result["final_answer"])

