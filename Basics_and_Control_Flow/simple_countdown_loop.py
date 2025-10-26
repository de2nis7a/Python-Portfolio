# FILE: simple_countdown_loop.py
# CONCEPT: Control Flow (Loop with Step)
# DEMONSTRATES: Using the 'range' function with a negative step to count down.

def count_down():
    """Prints a countdown from 10 to 1."""
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")

grade_calculator_by_mark.py