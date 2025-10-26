# FILE: string_input_validation.py
# CONCEPT: Input Validation with While Loops
# DEMONSTRATES: Two methods for ensuring a user enters a non-empty string: 
# pre-initializing a variable (get_string1) and using a 'while True' loop with 'break' (get_string2).

def get_string1():
    """Validates input by checking an empty variable twice."""
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg

def get_string2():
    """Validates input using a while True loop and break statement."""
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg
