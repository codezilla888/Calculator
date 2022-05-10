import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    should_continue = True
    number1 = float(input("What's the first number?:\n"))
    for operation in operations:
        print(operation)
    while should_continue:
        operation_symbol = input("Pick an operation from the line above:\n")
        number2 = float(input("What's the next number?:\n"))
        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        decision = input(f"Type 'yes' to continue calculating with {answer}, or 'new' to start a new calculation, or 'stop' if you want to quit the calculator: ").lower()
        if decision == "yes":
            number1 = answer
        elif decision == "new":
            should_continue = False
            calculator()
        else:
            should_continue = False


print(art.logo)
calculator()