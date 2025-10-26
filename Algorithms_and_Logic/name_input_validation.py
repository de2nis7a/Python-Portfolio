# FILE: name_input_validation.py
# CONCEPT: Advanced String Validation
# DEMONSTRATES: Using a while True loop with string methods (isalpha, isupper) to enforce 
# a rule: input must be alphabetic and start with a capital letter.

def get_name():
    """Prompts for a name until a valid name (alphabetic, starts uppercase) is entered."""
    while True:
        name = input("Enter a name: ")
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Enter a valid name: ")
