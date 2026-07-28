# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms(n):
    
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    
    second = 1

   
    sequence = []

    for i in range(n):
        sequence.append(first)

        
        next_term = first + second

        
        first = second
        second = next_term

    
    print("Fibonacci sequence:", end=" ")
    for number in sequence:
        print(number, end=" ")
    print()  



def is_fibonacci_number(number):
    
    if number < 0:
        return False

    
    first = 0
    second = 1

    
    while first <= number:
        if first == number:
            return True
        next_term = first + second
        first = second
        second = next_term

    
    return False



def main():
   
    print("      FIBONACCI SEQUENCE MENU")

    while True:
        print("\nWhat would you like to do?")
        print("A - Print the first N Fibonacci terms")
        print("B - Check if a number is a Fibonacci number")
        print("Q - Quit the program")

        choice = input("Enter your choice: ").upper()

        if choice == "A":
            n = int(input("How many terms? "))
            print_fibonacci_terms(n)

        elif choice == "B":
            number = int(input("Enter a number to check: "))

            if is_fibonacci_number(number) == True:
                print(number, "is a Fibonacci number.")
            else:
                print(number, "is NOT a Fibonacci number.")

        elif choice == "Q":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please type A, B, or Q.")



main()