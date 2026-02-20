def attempt_quiz(quiz, student_answers):
    attempts = []
    for q, a in zip(quiz["questions"], student_answers):
        attempts.append({
            "question": q["question"],
            "selected": a,
            "correct": q.get("correct_answer")
        })
    return attempts