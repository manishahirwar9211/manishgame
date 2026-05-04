import streamlit as st
import random

st.title("🧮 सिंपल मैथ क्विज़")

# गेम को रीसेट करने के लिए बटन
if st.button('नया सवाल लाओ'):
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.ans = st.session_state.num1 + st.session_state.num2

# पहली बार चलाने के लिए वैल्यू सेट करना
if 'num1' not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.ans = st.session_state.num1 + st.session_state.num2

# सवाल दिखाएं
st.subheader(f"बताओ: {st.session_state.num1} + {st.session_state.num2} = ?")

# जवाब इनपुट
user_input = st.number_input("अपना जवाब यहाँ लिखें:", step=1)

if st.button("Check Answer"):
    if user_input == st.session_state.ans:
        st.success("सही जवाब! 🎯")
        st.balloons()
    else:
        st.error(f"गलत! सही जवाब {st.session_state.ans} था।")
