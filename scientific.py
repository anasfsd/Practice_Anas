import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Set up the calculator title
st.title("Scientific Graphical Calculator")

# Options for scientific functions
options = ["Addition", "Subtraction", "Multiplication", "Division", "Sin", "Cos", "Tan", "Exponential", "Logarithm", "Square Root"]

# Choose a function
function = st.selectbox("Choose a function", options)

# Take inputs based on the function selected
if function in ["Addition", "Subtraction", "Multiplication", "Division"]:
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")
elif function in ["Sin", "Cos", "Tan"]:
    angle = st.number_input("Enter the angle in degrees")
elif function == "Exponential":
    base = st.number_input("Enter the base number")
    exp = st.number_input("Enter the exponent")
elif function == "Logarithm":
    num = st.number_input("Enter the number")
elif function == "Square Root":
    num = st.number_input("Enter the number")

# Calculate and display result
if st.button("Calculate"):
    if function == "Addition":
        result = num1 + num2
    elif function == "Subtraction":
        result = num1 - num2
    elif function == "Multiplication":
        result = num1 * num2
    elif function == "Division":
        result = num1 / num2 if num2 != 0 else "Error (division by zero)"
    elif function == "Sin":
        result = math.sin(math.radians(angle))
    elif function == "Cos":
        result = math.cos(math.radians(angle))
    elif function == "Tan":
        result = math.tan(math.radians(angle))
    elif function == "Exponential":
        result = base ** exp
    elif function == "Logarithm":
        result = math.log(num) if num > 0 else "Error (log of non-positive number)"
    elif function == "Square Root":
        result = math.sqrt(num) if num >= 0 else "Error (square root of negative number)"
    st.write("Result:", result)

# Graph plotting feature
st.header("Graphing Tool")
function_to_graph = st.text_input("Enter a mathematical function to graph (use 'x' as variable, e.g., sin(x) or x**2)")
x_min = st.number_input("X-axis min", value=-10)
x_max = st.number_input("X-axis max", value=10)

if st.button("Plot Graph"):
    x = np.linspace(x_min, x_max, 1000)
    try:
        y = eval(function_to_graph)  # Evaluate the function
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(f"Graph of {function_to_graph}")
        st.pyplot(fig)
    except Exception as e:
        st.write("Error in function input. Please enter a valid mathematical function.")
