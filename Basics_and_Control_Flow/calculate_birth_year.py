# FILE: calculate_birth_year.py
# CONCEPT: Basic Input/Output and Arithmetic
# DEMONSTRATES: Taking user input (age) and performing a simple calculation 
# (birth year, years since opening) based on fixed constants (1995, 2024).

def calculate_birth_year():
    print("Welcome to The Media Hub!")
    print("We have been serving entertainment enthusiasts since 1995.")
    age = int(input("Please enter your age: "))
    # Assuming current year is 2024 for context
    birth_year = 2024 - age
    print("You were born in", birth_year, ",", birth_year - 1995, "years after our opening!")
