import streamlit as st
from utils.auth_mock import get_role
from rag.explanation.explain_from_pdf import explain_from_pdf

# ================== SESSION STATE INIT ==================

if "documents" not in st.session_state:
    st.session_state.documents = []

if "quizzes" not in st.session_state:
    st.session_state.quizzes = []

if "student_answers" not in st.session_state:
    st.session_state.student_answers = []

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "option_count" not in st.session_state:
    st.session_state.option_count = 4

# ================== ROLE SELECTION ==================

role = get_role()

# ======================================================
# ==================== TEACHER PANEL ===================
# ======================================================

if role == "Teacher":
    st.header("👩‍🏫 Teacher Panel")

    # -------- PHASE 1: PDF UPLOAD --------
    st.subheader("Phase 1: Upload Reference PDF")

    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    chapter_name = st.text_input("Chapter Name")

    if uploaded_pdf and st.button("Process PDF"):
        with open("teacher_doc.pdf", "wb") as f:
            f.write(uploaded_pdf.read())

        st.session_state.documents = [{
            "pdf_path": "teacher_doc.pdf",
            "chapter": chapter_name
        }]

        st.success("PDF uploaded and stored successfully!")

    # -------- PHASE 2: QUIZ CREATION --------
    st.subheader("Phase 2: Create Quiz")

    question = st.text_input("Question")

    st.subheader("Options")
    options = []

    for i in range(st.session_state.option_count):
        opt = st.text_input(f"Option {i + 1}", key=f"opt_{i}")
        if opt:
            options.append(opt)

    if st.button("Add Another Option"):
        st.session_state.option_count += 1
        st.rerun()

    if options:
        correct_answer = st.selectbox("Select Correct Answer", options)
    else:
        correct_answer = None

    if st.button("Add Question"):
        if not question or not options or not correct_answer:
            st.error("Please fill question, options, and correct answer.")
        else:
            quiz_question = {
                "question": question,
                "options": options,
                "correct_answer": correct_answer
            }
            st.session_state.quizzes.append(quiz_question)
            st.success("Question added successfully!")

    if st.checkbox("Show Current Quiz Data"):
        st.write(st.session_state.quizzes)

# ======================================================
# ==================== STUDENT PANEL ===================
# ======================================================

elif role == "Student":
    st.header("🎓 Student Panel")

    if not st.session_state.quizzes:
        st.warning("No quizzes available yet.")
        st.stop()

    # -------- PHASE 3: ATTEMPT QUIZ --------
    st.subheader("Phase 3: Attempt Quiz")

    answers = []

    for idx, q in enumerate(st.session_state.quizzes):
        st.subheader(f"Q{idx + 1}: {q['question']}")
        ans = st.radio(
            "Choose an option:",
            q["options"],
            key=f"student_q_{idx}"
        )
        answers.append(ans)

    # -------- PHASE 4: SUBMIT QUIZ --------
    if st.button("Submit Quiz"):
        st.session_state.student_answers = answers
        st.session_state.submitted = True
        st.success("Quiz submitted successfully!")

    # -------- PHASE 5 & 6: EVALUATION + EXPLANATION --------
    if st.session_state.submitted:
        st.subheader("Evaluation & Explanation")

        for idx, q in enumerate(st.session_state.quizzes):
            selected = st.session_state.student_answers[idx]
            correct = q["correct_answer"]

            if selected == correct:
                st.success(f"Q{idx + 1}: Correct")
            else:
                st.error(f"Q{idx + 1}: Wrong")
                st.write(f"Correct Answer: {correct}")

                if st.button(f"Explain Q{idx + 1}", key=f"explain_{idx}"):

                    pdf_path = st.session_state.documents[0]["pdf_path"]

                    explanation = explain_from_pdf(
                        pdf_path=pdf_path,
                        question=q["question"],
                        correct_answer=correct
                    )

                    st.markdown("### 📘 Detailed Explanation")
                    st.write(explanation)
