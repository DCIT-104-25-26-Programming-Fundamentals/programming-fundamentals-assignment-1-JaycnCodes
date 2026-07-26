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
def read_matrix(rows, cols, matrix_name=""):
    if matrix_name:
        print(f"\nEnter {matrix_name} ({rows} x {cols}):")
    else:
        print(f"\nEnter matrix ({rows} x {cols}):")

    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input=input(f"Enter row {i + 1}: ").split()
                if len(row_input) != cols:
                    print(f"Error: Expected {cols} numbers, but got {len(row_input)}. Please try again.")
                    continue
                row = [float(val) for val in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
    return matrix

def display_matrix(matrix):
    for row in matrix:
        formatted_row=[]
        for val in row:
            val_str=f"{int(val)}" if val == int(val) else f"{val:.2f}"
            formatted_row.append(f"{val_str:>4}")
        print(" ".join(formatted_row))

def transpose_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    transposed=[]
    for c in range(cols):
        new_row=[]
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix_a, matrix_b):
    rows=len(matrix_a)
    cols=len(matrix_a[0])

    result=[]
    for r in range(rows):
        row=[]
        for c in range(cols):
            row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a=len(matrix_a)
    cols_a=len(matrix_a[0])
    cols_b=len(matrix_b[0])

    result=[]
    for r in range(rows_a):
        row=[]
        for j in range(cols_b):
            dot_product=0
            for k in range(cols_a):
                dot_product +=matrix_a[r][k]* matrix_b[k][j]
            row.append(dot_product)
        result.append(row)
    return result

def main():
    try:
        print("Part A: Transpose Matrix")
        m=int(input("Enter number of rows(M): "))
        n=int(input("Enter number of columns(N): "))
        if m<=0 or n<=0:
            print("Dimensions must be positive integers. ")
            return

        mat_a=read_matrix(m,n,"Matrix")
        print("\nOriginal Matrix:")
        display_matrix(mat_a)

        transposed=transpose_matrix(mat_a)
        print("\nTransposed Matrix:")
        display_matrix(transposed)

        print("\n" + "="*40)
        print("Part B: Add Two Matrices")
        print(f"Reading two {m}*{n} matrices")

        mat_b1=read_matrix(m,n,"Matrix 1")
        mat_b2=read_matrix(m,n,"Matrix 2")
        sum_matrix=add_matrices(mat_b1, mat_b2)
        print("\nSum of Matrices:")
        display_matrix(sum_matrix)

        print("\n" + "="*40)
        print("Part C: Multiply Two Matrices")
        print("For A x B: Columns of A must equal Rows of B")
        m_a=int(input("Enter number of rows for Matrix A (M): "))
        n_a=int(input("Enter columns for Matrix A/ rows for Matrix B (N): "))
        p_b=int(input("Enter columns for Matrix B (P): "))

        if m_a<=0 or n_a<=0 or p_b<=0:
            print("Dimensions must be positive integers. ")
            return

        mat_c1=read_matrix(m_a, n_a,"Matrix A")
        mat_c2=read_matrix(n_a, p_b,"Matrix B")

        product_matrix=multiply_matrices(mat_c1, mat_c2)
        print("\nProduct of Matrices (A x B):")
        display_matrix(product_matrix)

    except ValueError:
        print("Error: Invalid numeric input entered.")

if __name__=="__main__":
    main()
