from tools.base import Tool

class CalculatorTool(Tool):

    name = "calculator"
    description = "Performs calculations"

    def execute(self, a, b, operator):

        if operator == "+":
            return a + b

        elif operator == "-":
            return a - b

        elif operator == "*":
            return a * b

        elif operator == "/":
            if b == 0:
                return "Cannot divide by zero"
            return a / b

calc = CalculatorTool()

print(calc.execute(5, "+", 7))