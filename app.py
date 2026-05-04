import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Math Game 🎮", page_icon="🧠")

# Title
st.title("🧠 Math Challenge Game")
st.write("Test your math skills and beat your score!")

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = 0

# Difficulty level
level = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

# Function to generate question
def generate_question(level):
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif level == "Medium":
        a, b = random.randint(10, 50), random.randint(1, 20)
        op = random.choice(["+", "-", "*"])
    else:
        a, b = random.randint(20, 100), random.randint(1, 50)
        op = random.choice(["+", "-", "*", "/"])

    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, round(answer, 2)

# Generate question button
if st.button("Generate Question"):
    q, ans = generate_question(level)
    st.session_state.question = q
    st.session_state.answer = ans

# Display question
if st.session_state.question:
    st.subheader(f"Question: {st.session_state.question}")

    user_answer = st.text_input("Your Answer:")

    if st.button("Submit Answer"):
        try:
            if float(user_answer) == st.session_state.answer:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct answer: {st.session_state.answer}")
        except:
            st.warning("⚠️ Please enter a valid number!")

# Score display
st.write(f"🏆 Score: {st.session_state.score}")

# Reset game
if st.button("Reset Game"):
    st.session_state.score = 0
    st.session_state.question = ""
    st.session_state.answer = 0
    st.success("Game Reset!")
