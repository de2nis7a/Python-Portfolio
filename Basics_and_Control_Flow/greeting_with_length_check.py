# FILE: greeting_with_length_check.py
# CONCEPT: Conditional Logic (if)
# DEMONSTRATES: Basic input/output and an 'if' statement to check a string condition.

def greet(name):
    """Prints a greeting and checks if the name is unusually long."""
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")
