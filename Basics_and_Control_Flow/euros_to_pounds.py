# FILE: euros_to_pounds.py
# CONCEPT: Input/Output and Float Conversion
# DEMONSTRATES: Basic currency conversion logic and handling floating-point numbers.

def euros_to_pounds():
    euros = float(input("Enter a value in euros: "))
    pounds = euros * 0.87
    print("The value in pounds is", pounds)