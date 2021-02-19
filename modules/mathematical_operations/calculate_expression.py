from advanced.modules.mathematical_operations.math_operations import multiply, divide, add, subtract, power


def calculate_expression(expression):
    x, operator, y = expression.split()
    x = float(x)
    y = int(y)

    if operator == "*":
        result = multiply(x, y)
    elif operator == "/":
        result = divide(x, y)
    elif operator == "+":
        result = add(x, y)
    elif operator == "-":
        result = subtract(x, y)
    elif operator == "^":
        result = power(x, y)
    else:
        raise Exception(f"Invalid operator {operator}")
    return f"{result:.2f}"


