import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

# Title for the app
st.title("Scientific Graphical Calculator")

# Options for different operations
operations = ["Addition", "Subtraction", "Multiplication", "Division", 
              "Sin", "Cos", "Tan", "Exponential", "Logarithm", "Square Root"]

# Dropdown to select an operation
operation = st.selectbox("Select an Operation", operations)

# Input fields based on the operation selected
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")
elif operation in ["Sin", "Cos", "Tan"]:
    angle = st.number_input("Enter angle (in degrees)")
elif operation == "Exponential":
    base = st.number_input("Enter base")
    exp = st.number_input("Enter exponent")
elif operation == "Logarithm":
    num = st.number_input("Enter number (must be positive)")
elif operation == "Square Root":
    num = st.number_input("Enter number (must be non-negative)")

# Calculation and output
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif operation == "Sin":
            result = math.sin(math.radians(angle))
        elif operation == "Cos":
            result = math.cos(math.radians(angle))
        elif operation == "Tan":
            result = math.tan(math.radians(angle))
        elif operation == "Exponential":
            result = base ** exp
        elif operation == "Logarithm":
            result = math.log(num) if num > 0 else "Error: Logarithm of non-positive number"
        elif operation == "Square Root":
            result = math.sqrt(num) if num >= 0 else "Error: Square root of negative number"
        st.write("Result:", result)
    except Exception as e:
        st.write(f"Error: {e}")

# Graph plotting with Plotly
st.header("Graphing Tool")
function_to_graph = st.text_input("Enter a function to graph (use 'x' as variable, e.g., sin(x), x**2)")
x_min = st.number_input("X-axis minimum", value=-10)
x_max = st.number_input("X-axis maximum", value=10)

if st.button("Plot Graph"):
    x = np.linspace(x_min, x_max, 1000)
    try:
        y = eval(function_to_graph)  # Evaluate the function for the plot
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        fig.update_layout(title=f"Graph of {function_to_graph}", xaxis_title="x", yaxis_title="y")
        st.plotly_chart(fig)
    except Exception as e:
        st.write("Invalid function input. Please enter a valid mathematical function.")
