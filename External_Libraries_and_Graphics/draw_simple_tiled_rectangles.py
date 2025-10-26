# FILE: draw_simple_tiled_rectangles.py
# CONCEPT: Nested Loops for Grid Drawing
# DEMONSTRATES: Using two nested 'for' loops to iterate over rows and columns, 
# calculating the coordinates (p1 and p2) for each cell in a 5x5 grid.
from graphix import Window, Rectangle, Point

# Constants (Assumed based on previous code)
WIN_SIZE = 500
WIDTH = 100
HEIGHT = 100

def draw_tiled_rectangles1():
    win = Window("Tiled Rectangles", WIN_SIZE, WIN_SIZE)
    for row in range(5):
        for col in range(5):
            p1 = Point(col * WIDTH, row * HEIGHT)
            p2 = Point((col + 1) * WIDTH, (row + 1) * HEIGHT)
            rect = Rectangle(p1, p2)
            rect.draw(win)
    win.get_mouse()  
    win.close()
