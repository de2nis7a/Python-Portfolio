# FILE: draw_letter_a.py
# CONCEPT: Algorithmic Character Drawing (ASCII Art with Spaces)
# DEMONSTRATES: Advanced character drawing using function composition and combining
# spaces and characters to create a specific shape (the letter 'A').

def draw_blocks(width_one, width_two, width_three, width_four, height):
    """Draws a line segment using blocks of spaces and stars."""
    for i in range(height):
            print(" " * width_one, end="")
            print("*" * width_two, end="")
            print(" " * width_three, end="")
            print("*" * width_four, end="")
            print()
            

def draw_letter_a():
    """Draws the letter 'A' by calling draw_blocks multiple times."""
    # Top bar
    draw_blocks(1, 8, 1, 0, 2)
    # Sides (vertical part)
    draw_blocks(0, 2, 6, 2, 2)
    # Middle bar
    draw_blocks(0, 10, 0, 0, 2)
    # Lower sides
    draw_blocks(0, 2, 6, 2, 3)

# draw_letter_a()
