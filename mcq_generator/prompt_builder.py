def build_prompt(inputs):
    prompt_parts = []

    prompt_parts.append(f"Please write {inputs['questions_num']} {inputs['question_level']} level multiple-choice question(s), each with {inputs['correct_ans_num']} correct answer(s) and {inputs['distractors_num']} distractors, based on text that I will provide.")

    if inputs.get("original_content_only"):
        prompt_parts.append("Please create questions based solely on the provided text.")
    else:
        prompt_parts.append("Please create questions that incorporate both the provided text as well as your knowledge of the topic.")

    if inputs["distractors_difficulty"] == "Obvious":
        prompt_parts.append("Distractors should be obviously incorrect options.")
    elif inputs["distractors_difficulty"] == "Challenging":
        prompt_parts.append("Distractors should sound like they could be plausible, but are ultimately incorrect.")

    if inputs.get("learning_objective"):
        prompt_parts.append(f"Focus on meeting the following learning objective(s): {inputs['learning_objective']}")

    if inputs.get("learner_feedback"):
        prompt_parts.append("Please provide a feedback section for each question that says why the correct answer is the best answer and the other options are incorrect.")

    if inputs.get("hints"):
        prompt_parts.append("Also, include a hint for each question.")

    if inputs.get("output_format") == "OLX":
        prompt_parts.append("Please write your MCQs in Open edX OLX format")
    else:
        prompt_parts.append("""Format each question like the following:
Question: [Question Text]
A) [Answer A]
B) [Answer B]
....
N) [Answer N]

Solution: [Answer A, B...N]
""")

    prompt_parts.append(f"Here is the content/topic:\n================\n{inputs['topic_content']}")
    return "\n\n".join(prompt_parts)
