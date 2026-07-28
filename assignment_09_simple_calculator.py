# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def perform_addition(a, b):
    return a + b


def perform_subtraction(a, b):
    return a - b


def perform_multiplication(a, b):
    return a * b


def perform_division(a, b):
    
    if b == 0:
        return None

    sign = -1 if (a < 0) != (b < 0) else 1
    a, b = abs(a), abs(b)

    whole, remainder = divmod(a * 100, b)

   
    if remainder * 2 >= b:
        whole += 1

    whole *= sign
    return whole  


def perform_modulus(a, b):
    if b == 0:
        return None
    return a % b


def perform_exponentiation(a, b):
    return a ** b


def format_division_result(scaled_value):
    sign = "-" if scaled_value < 0 else ""
    scaled_value = abs(scaled_value)
    whole_part = scaled_value // 100
    fraction_part = scaled_value % 100
    return f"{sign}{whole_part}.{fraction_part:02d}"


def read_operands():
    first = int(input("Enter first number : "))
    second = int(input("Enter second number: "))
    return first, second


def show_menu():
    print("     SIMPLE CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    operations = {
        "1": ("+", perform_addition),
        "2": ("-", perform_subtraction),
        "3": ("*", perform_multiplication),
        "4": ("/", perform_division),
        "5": ("%", perform_modulus),
        "6": ("**", perform_exponentiation),
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a number between 1 and 7.")
            continue

        symbol, operation = operations[choice]

        try:
            first, second = read_operands()
        except ValueError:
            print("Invalid input. Please enter whole numbers.")
            continue

        if choice in ("4", "5") and second == 0:
            if choice == "4":
                print("Error: Cannot divide by zero.")
            else:
                print("Error: Cannot perform modulus by zero.")
            continue

        result = operation(first, second)

        if choice == "4":
            result_str = format_division_result(result)
        else:
            result_str = str(result)

        print(f"Result: {first} {symbol} {second} = {result_str}")


if __name__ == "__main__":
    main()