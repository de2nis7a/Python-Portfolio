# FILE: hello_countdown_while.py
# CONCEPT: Basic While Loops and Control
# DEMONSTRATES: The fundamental structure of a 'while' loop using incrementing (hello_while), 
# decrementing (countdown), and multiplying (mystery_loop) steps.

def hello_while():
    """Prints a message 10 times using a standard incremental while loop."""
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1

def countdown():
    """Prints a countdown from 10 to 1 using a decremental while loop."""
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")

def mystery_loop():
    """Demonstrates an exponential growth loop until a limit is reached."""
    i = 1
    # Note: The original loop will terminate when i reaches 1000
    while i < 1000:
        print(i)
        i = i * 2
