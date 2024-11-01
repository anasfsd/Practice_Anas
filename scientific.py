# Install Streamlit if you haven't already
# !pip install streamlit

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define basic operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

# Define scientific functions
def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))

def tan(x):
    return np.tan(np.radians(x))

def log(x, base=10):
    return np.log(x) / np.log(base)

def sqrt(x):
    return np.sqrt(x)

# Streamlit app layout
st.title("Scientific Graphical Calculator")

# Choose operation type: Basic or Scientific
operation_type = st.selectbox("Select Operation Type", ["Basic Operations", "Scientific Functions", "Plot Functions"])

if operation_type == "Basic Operations":
    # Basic operations
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)
    operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

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

elif operation_type == "Scientific Functions":
    # Scientific functions
    num = st.number_input("Enter the number:", value=0.0)
    function = st.selectbox("Choose function:", ["Sine", "Cosine", "Tangent", "Logarithm", "Square Root"])

    if st.button("Calculate"):
        if function == "Sine":
            result = sin(num)
        elif function == "Cosine":
            result = cos(num)
        elif function == "Tangent":
            result = tan(num)
        elif function == "Logarithm":
            base = st.number_input("Enter the logarithm base:", value=10.0)
            result = log(num, base)
        elif function == "Square Root":
            result = sqrt(num)
        st.write(f"The result is: {result}")

elif operation_type == "Plot Functions":
    # Graphing functionality
    st.write("Select a function to plot:")
    func_choice = st.selectbox("Function", ["sin(x)", "cos(x)", "tan(x)", "log(x)", "sqrt(x)"])

    # Define x values for plotting
    x = np.linspace(-10, 10, 400)

    # Set up function mappings
    if func_choice == "sin(x)":
        y = np.sin(x)
        func_name = "y = sin(x)"
    elif func_choice == "cos(x)":
        y = np.cos(x)
        func_name = "y = cos(x)"
    elif func_choice == "tan(x)":
        y = np.tan(x)
        func_name = "y = tan(x)"
    elif func_choice == "log(x)":
        y = np.log(x)
        func_name = "y = log(x)"
    elif func_choice == "sqrt(x)":
        y = np.sqrt(np.clip(x, 0, None))
        func_name = "y = sqrt(x)"

    # Plot the selected function
    fig, ax = plt.subplots()
    ax.plot(x, y, label=func_name)
    ax.set_title(f"Graph of {func_name}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)
