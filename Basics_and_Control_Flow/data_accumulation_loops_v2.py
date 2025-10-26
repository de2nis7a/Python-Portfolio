# FILE: data_accumulation_loops_v2.py
# CONCEPT: While Loops for Data Accumulation
# DEMONSTRATES: Four different patterns for summing numbers based on various stop conditions: 
# flag variable (y/n), sentinel value (0), empty string, and break statement.

def add_up_numbers1():
    """Sums numbers based on a flag variable ('y'/'n')."""
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)

def add_up_numbers2():
    """Sums numbers based on a sentinel value (0) for stopping."""
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)

def add_up_numbers3():
    """Sums numbers based on an empty string input for stopping."""
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)

def add_up_numbers4():
    """Sums numbers using an infinite loop with a break statement based on non-digit input."""
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)
