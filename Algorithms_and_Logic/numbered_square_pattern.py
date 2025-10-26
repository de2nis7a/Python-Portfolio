# FILE: numbered_square_pattern.py
# CONCEPT: Nested Loops and Pattern Generation
# DEMONSTRATES: Using nested loops with complex initialization (num -= 1) to create 
# a sequence-based square pattern.

def numbered_square(n):
    """Prints a square pattern where numbers change diagonally."""
    num = n
    for i in range(n):
        for j in range(num, num+n):
            print(j, end = " ")
        num -= 1
        print()
