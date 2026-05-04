import streamlit as st
import random

# Initialize session state for game variables
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.question_count = 0
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)
    st.session_state.op = random.choice(['+', '-', '*'])
    st.session_state.game_over = False

def next_question():
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)
    st.session_state.op = random.choice(['+', '-', '*'])
    st.session_state.question_count += 1

def reset_game():
    st.session_state.score = 0
    st.session_state.question_count = 0
    st.session_state.game_over = False
    next_question()

# --- UI Layout ---
st.title("🧮 AI Math Quiz")
st.write(f"Score: **{st.session_state.score}** | Question: **{st.session_state.question_count + 1}/5**")

if not st.session_state.game_over:
    # Display the problem
    q_text = f"What is {st.session_state.num1} {st.session_state.op} {st.session_state.num2}?"
    st.subheader(q_text)

    # User Input
    user_ans = st.number_input("Enter your answer:", step=1, key="answer_input")

    if st.button("Submit Answer"):
        # Logic to check answer
        correct_ans = eval(f"{st.session_state.num1} {st.session_state.op} {st.session_state.num2}")
        
        if user_ans == correct_ans:
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! The answer was {correct_ans}.")

        # Check if game should continue
        if st.session_state.question_count < 4:
            next_question()
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    st.balloons()
    st.header("Game Over!")
    st.subheader(f"Your final score: {st.session_state.score} / 5")
    if st.button("Play Again"):
        reset_game()
        st.rerun()
