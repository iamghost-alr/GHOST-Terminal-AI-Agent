from tools.base import Tool


# Words / symbols the user may type -> canonical operator.
operator_map = {
    "plus": "add",
    "add": "add",
    "+": "add",
    "minus": "sub",
    "subtract": "sub",
    "sub": "sub",
    "-": "sub",
    "multiply": "mul",
    "times": "mul",
    "mul": "mul",
    "*": "mul",
    "divide": "div",
    "div": "div",
    "/": "div",
    "power": "pow",
    "pow": "pow",
    "^": "pow",
    "**": "pow",
}


def calculator(a, b, operator):
    """Run a single binary calculation.

    Accepts both symbols (+, -, *, /) and words
    (plus, minus, multiply, divide, power, ...).
    """
    try:

        if operator in operator_map:
            operator = operator_map[operator]

        if operator == "add":
            return a + b

        elif operator == "sub":
            return a - b

        elif operator == "mul":
            return a * b

        elif operator == "div":
            if b == 0:
                return "Cannot divide by zero"
            return a / b

        elif operator == "pow":
            return a ** b

        return "Invalid operator"

    except Exception as e:
        return f"Error: {e}"


class CalculatorTool(Tool):

    name = "calculator"
    description = "Performs calculations"

    def execute(self, a, b, operator):
        return calculator(a, b, operator)
