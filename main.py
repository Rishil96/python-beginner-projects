# Calculator Application
import art


# Operation functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Calculate function to return the result as per operator
def calculate(n1, n2, operator):
    if operator == "+":
        return add(n1, n2)
    elif operator == "-":
        return subtract(n1, n2)
    elif operator == "*":
        return multiply(n1, n2)
    elif operator == "/":
        return divide(n1, n2)
    else:
        return "Invalid Operator."


is_on = True
continue_with_prev_number = False
result = 0

print(art.logo)

while is_on:
    # Get first number
    num1 = result if continue_with_prev_number else float(input("What's the first number?: "))
    # Get operation
    current_operator = input("+\n-\n*\n/\nPick an operation: ")
    # Get next number
    num2 = float(input("What's the next number?: "))

    # Calculate the result
    result = calculate(num1, num2, current_operator)
    print(f"{num1} {current_operator} {num2} = {result}")

    should_continue = input(f"Type 'y' to continue calculating with {result}, "
                            f"or type 'n' to start a new calculation, or type any other key to quit: ")

    # Ask how the user wants to continue
    if should_continue == "y":
        continue_with_prev_number = True
    elif should_continue == "n":
        continue_with_prev_number = False
        print(art.logo)
    else:
        is_on = False

print("Thanks for using the calculator app!")
