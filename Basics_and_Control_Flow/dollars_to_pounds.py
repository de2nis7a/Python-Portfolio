# FILE: dollars_to_pounds.py
# CONCEPT: Input/Output and Float Conversion
# DEMONSTRATES: Basic currency conversion logic based on user input.

def dollars_to_pounds():
    dollars=float(input("Enter an amount in dollars:"))
    pounds=dollars/1.35
    print("The amount in pounds is:", pounds)