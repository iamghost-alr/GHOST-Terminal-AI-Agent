import math

def calculator(a, b, operator):
    """
    Args:
    a (int): First number
    b (int): Second number
    operator (str): +, -, *, /, **
    
    """

    try:
        if operator == "+" or operator == "add":
            return a + b

        elif operator == "-" or operator == "sub":
            return a - b

        elif operator == "*" or operator == "mul":
            return a * b

        elif operator == "/" or operator == "div":
            if b == 0:
                return "Cannot divide by zero"
            return a / b

        elif operator == "**" or operator == "pow":
            return a ** b

        else:
            return "Invalid operator"

    except Exception as e:
        return f"Error: {e}"
