# FILE: draw_patchwork_grid.py
# CONCEPT: Modular Programming and Composition (Complex Scene)
# DEMONSTRATES: Creating a main function that calls multiple modular drawing functions 
# (draw_patch_windowXv2) and uses nested loops to place them in a 2x3 grid pattern.
# NOTE: This file assumes the existence of helper functions like draw_patch_window10v2 and draw_patch_window3v2.

from graphix import Window, Point, Line, Rectangle

# --- REQUIRED HELPER FUNCTIONS (assuming they are in this module or imported) ---
# Function to draw Patch 10 style pattern at a specific location
def draw_patch_window10v2(win, x, y, colour):
        point_one = Point(x, y)
        point_two = Point(100 + x, 10 + y)
        for i in range(10):
            line = Line(point_one, point_two)
            line.fill_colour = colour
            line.draw(win)
            point_one.move(10, 0)
            point_two.move(0, 10)
        point_one = Point(100 + x, 100 + y)
        point_two = Point(0 + x, 90 + y)
        for i in range(10):
            line = Line(point_one, point_two)
            line.fill_colour = colour
            line.draw(win)
            point_one.move(-10, 0)
            point_two.move(0, -10)

# Function to draw Patch 3 style pattern at a specific location
def draw_patch_window3v2(win, x, y, colour):
    point_one = Point(x, y)
    point_two = Point(100 + x, 100 + y)
    for i in range(10):
        rectangle = Rectangle(point_one, point_two)
        if i % 2 == 0:
            rectangle.fill_colour = colour
            rectangle.outline_colour = colour
        else:
            rectangle.fill_colour = "white"
            rectangle.outline_colour = "white"
        rectangle.draw(win)
        point_one.move(5, 5)
        point_two.move(-5, -5)
# ---------------------------------------------------------------------------------


def draw_patchwork():
    """Draws a 2x3 grid of different patchwork designs."""
    win = Window("Six Patch Grid", 300, 200)
    y = 0
    
    # Outer loop for rows (2 rows)
    for j in range(2):
         x=0
         # Inner loop for columns (3 columns)
         for i in range(3):
             # Alternating calls to drawing functions
             if (i + j) % 2 == 0:
                 draw_patch_window10v2(win, x, y, "blue")
             else:
                 draw_patch_window3v2(win, x, y, "red")
             x += 100
         y += 100
         
    win.get_mouse()
    win.close()
    
# draw_patchwork()
