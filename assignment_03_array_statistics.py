# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def calculate_sum(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_max(numbers):
    return max(numbers)


def calculate_min(numbers):
    return min(numbers)


def statistics():
    # Try to get a valid whole number for "how many numbers"
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return None

    if n <= 0:
        print("Error: N must be a positive integer.")
        return None

    numbers = []
    for i in range(n):
        # Try to get a valid number for each entry
        try:
            value = float(input(f"Enter number {i + 1}: "))
            numbers.append(value)
        except ValueError:
            print(f"Error: Input {i + 1} was not a valid number. Stopping.")
            return None

    return numbers


def fmt(x):
    """Show whole numbers without a trailing .0"""
    return int(x) if x == int(x) else x


def main():
    numbers = statistics()

    if numbers is None:
        return

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)

    print("\nResults:")
    print(f"Sum:     {fmt(total)}")
    print(f"Average: {round(average, 2)}")
    print(f"Maximum: {fmt(maximum)}")
    print(f"Minimum: {fmt(minimum)}")


if __name__ == "__main__":
    main()