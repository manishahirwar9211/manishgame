import streamlit as st

# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

# UI
st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.write("Perform basic mathematical operations")

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Button
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
