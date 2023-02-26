from calculator_art import logo
import os


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


def calculator():
    print(logo)
    resolution = 0
    still_calculating = True

    num1 = float(input("What is the first number? "))

    while still_calculating:
        for operator in operations:
            print(operator)

        symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number? "))

        for key in operations:
            if key == symbol:
                resolution = operations[key](num1, num2)

        print(f"{num1} {symbol} {num2} = {resolution}")

        game_continue = input(
            f"Type 'y' to continue calculation with {resolution} \
or type 'n' to start a new calculation: "
        ).lower()

        if game_continue == "y":
            num1 = resolution
        else:
            still_calculating = False
            os.system("cls" if os.name == "nt" else "clear")
            calculator()


calculator()
