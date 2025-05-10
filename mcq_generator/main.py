import streamlit as st
from llm_interface import generate_questions
from prompt_builder import build_prompt

st.set_page_config(page_title="MCQ Generator", page_icon="🔤", layout="centered", initial_sidebar_state="collapsed")

st.title("MCQ Generator")
st.write("This micro-app allows you to generate multiple-choice questions quickly and consistently. It works with GPT-3.5 Turbo, GPT-4, or GPT-4o.")

with st.form("mcq_form"):
    topic_content = st.text_area("Enter the content for question generation:", height=200)
    original_content_only = st.checkbox("Focus only on the provided text")
    learning_objective = st.text_area("Specify a learning objective (optional):")
    questions_num = st.selectbox("Number of questions:", [1, 2, 3, 4, 5])
    correct_ans_num = st.selectbox("Correct answers per question:", [1, 2, 3, 4])
    question_level = st.selectbox("Question difficulty level:", ['Grade School', 'High School', 'University', 'Other'], index=2)
    distractors_num = st.selectbox("Number of distractors:", [1, 2, 3, 4, 5], index=2)
    distractors_difficulty = st.selectbox("Distractors difficulty", ['Normal', 'Obvious', 'Challenging'])
    learner_feedback = st.checkbox("Include Learner Feedback?")
    hints = st.checkbox("Include hints?")
    output_format = st.selectbox("Output Format:", ['Plain Text', 'OLX'])

    submitted = st.form_submit_button("Generate Questions")

if submitted:
    inputs = {
        "topic_content": topic_content,
        "original_content_only": original_content_only,
        "learning_objective": learning_objective.strip(),
        "questions_num": questions_num,
        "correct_ans_num": correct_ans_num,
        "question_level": question_level,
        "distractors_num": distractors_num,
        "distractors_difficulty": distractors_difficulty,
        "learner_feedback": learner_feedback,
        "hints": hints,
        "output_format": output_format
    }

    prompt = build_prompt(inputs)
    model = "gpt-4o"
    with st.spinner("Generating..."):
        result = generate_questions(model=model, prompt=prompt)
    st.text_area("Generated MCQs", result, height=400)
