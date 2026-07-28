# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(matrix_name):
    print("\nEnter details for " + matrix_name)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []  

    for i in range(rows):
        
        row_text = input("Enter row " + str(i + 1) + ": ")

        
        row_values = row_text.split()

       
        row = []
        for value in row_values:
            row.append(int(value))

        matrix.append(row)

    return matrix



def print_matrix(matrix, title):
    print("\n" + title + ":")
    for row in matrix:
        line = ""
        for value in row:
            
            line = line + str(value).rjust(4)
        print(line)



def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    
    result = []
    for i in range(num_cols):
        new_row = []
        for j in range(num_rows):
            new_row.append(0)
        result.append(new_row)

   
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][i] = matrix[i][j]

    return result



def add_matrices(matrix_a, matrix_b):
    num_rows = len(matrix_a)
    num_cols = len(matrix_a[0])

   
    result = []
    for i in range(num_rows):
        new_row = []
        for j in range(num_cols):
            new_row.append(0)
        result.append(new_row)

    
    for i in range(num_rows):
        for j in range(num_cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result



def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)        
    n = len(matrix_a[0])      

    
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            new_row.append(0)
        result.append(new_row)

    
    for i in range(m):          
        for j in range(p):      
            total = 0
            for k in range(n):  
                total = total + matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result



def same_size(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b):
        return False
    if len(matrix_a[0]) != len(matrix_b[0]):
        return False
    return True



def can_multiply(matrix_a, matrix_b):
    cols_in_a = len(matrix_a[0])
    rows_in_b = len(matrix_b)
    return cols_in_a == rows_in_b


def main():
  
    print("      MATRIX OPERATIONS MENU")
   

    while True:
        print("\nWhat would you like to do?")
        print("A - Transpose a matrix")
        print("B - Add two matrices")
        print("C - Multiply two matrices")
        print("Q - Quit the program")

        choice = input("Enter your choice: ").upper()

        if choice == "A":
            matrix = read_matrix("Matrix")
            print_matrix(matrix, "Original Matrix")

            result = transpose_matrix(matrix)
            print_matrix(result, "Transposed Matrix")

        elif choice == "B":
            print("\nNote: Both matrices must be the same size.")
            matrix_a = read_matrix("Matrix A")
            matrix_b = read_matrix("Matrix B")

            if same_size(matrix_a, matrix_b) == False:
                print("Error! Matrix A and Matrix B must be the same size.")
            else:
                print_matrix(matrix_a, "Matrix A")
                print_matrix(matrix_b, "Matrix B")

                result = add_matrices(matrix_a, matrix_b)
                print_matrix(result, "Result (A + B)")

        elif choice == "C":
            print("\nNote: Columns in Matrix A must equal rows in Matrix B.")
            matrix_a = read_matrix("Matrix A")
            matrix_b = read_matrix("Matrix B")

            if can_multiply(matrix_a, matrix_b) == False:
                print("Error! Columns of A must match rows of B.")
            else:
                print_matrix(matrix_a, "Matrix A")
                print_matrix(matrix_b, "Matrix B")

                result = multiply_matrices(matrix_a, matrix_b)
                print_matrix(result, "Result (A x B)")

        elif choice == "Q":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please type A, B, C, or Q.")



main()