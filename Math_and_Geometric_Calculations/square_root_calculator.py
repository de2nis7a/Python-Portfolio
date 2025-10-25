# FILE: square_root_calculator.py
# CONCEPT: Math Functions and Input Validation
# DEMONSTRATES: Using the 'math.sqrt' function and implementing conditional logic (if/else) 
#               to handle invalid negative input.

import math

def square_root_calculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrt_value = math.sqrt(num)
        print("Square root:", round(sqrt_value, 2))
