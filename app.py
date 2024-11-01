# Install Streamlit if you haven't already
# !pip install streamlit

# Import Streamlit
import streamlit as st

# Define the functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit app layout
st.title("Simple Calculator")
st.write("Select an operation and enter numbers to perform a calculation.")

# Operation selection
operation = st.selectbox("Choose operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Number inputs
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Perform calculation based on selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"The result is: {result}")
