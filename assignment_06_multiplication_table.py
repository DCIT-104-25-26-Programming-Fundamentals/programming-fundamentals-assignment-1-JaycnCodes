# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(num):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1,13):
        product = num * i
        print(f"{num:2d}  x  {i:2d}  =  {product:3d}")

def print_tables_up_to_n(n):
    for i in range(1, n + 1):
        print_single_table(i)
        if i < n:
            print("-" * 27)

def main():
    print("Part A: Single Multiplication Table")
    try:
        num=int(input("Enter a number: ")) 
        if num<=0:
            print("Error: Please enter a positive integer.")
            return  
        print_single_table(num)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    print("\n" + "=" *35 + "\n")

    print("Part B: Multiplication Tables from 1 to N")
    try:
        n=int(input("Enter a number N: ")) 
        if n<=0:
            print("Error: Please enter a positive integer.")
            return  
        print_tables_up_to_n(n)
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()           