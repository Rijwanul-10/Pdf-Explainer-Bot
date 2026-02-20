def evaluate_answers(attempts):
    results = []
    for item in attempts:
        is_correct = item["selected"] == item["correct"]
        results.append({
            **item,
            "is_correct": is_correct
        })
    return results