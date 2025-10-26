# FILE: draw_row_of_rectangles.py
# CONCEPT: Drawing with Loops, Coordinate Calculation, and Conditional Logic
# DEMONSTRATES: Generating a row of rectangles using calculated coordinates inside a loop 
# (i * WIDTH), and using an if/else conditional (ternary operator) to alternate colors.
from graphix import Window, Rectangle, Point

# Constants used for the window and the size of each rectangle
WIN_SIZE = 500
WIDTH = 100
HEIGHT = 100

def draw_row_of_rectangles3(colour1, colour2):
    win = Window("Rectangle Row", WIN_SIZE, WIN_SIZE)
    
    # Draw 5 rectangles with alternating colors
    for i in range(5):
        # Calculate P1 (top-left) and P2 (bottom-right) coordinates based on the iteration 'i'
        p1 = Point(i * WIDTH, 0)
        p2 = Point((i + 1) * WIDTH, HEIGHT)
        rect = Rectangle(p1, p2)
        
        # Conditional coloring based on index i (alternating colors)
        rect.fill_colour = colour1 if i % 2 == 0 else colour2
        rect.draw(win)
        
    win.get_mouse() 
    win.close()

# Example usage:
# draw_row_of_rectangles3("red", "black")
