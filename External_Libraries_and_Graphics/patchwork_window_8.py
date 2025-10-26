# FILE: patchwork_window_8.py
# CONCEPT: Graphics and Nested Loops (Checkerboard Pattern)
# DEMONSTRATES: Using nested loops with a conditional (modulo arithmetic) to draw 
# a checkerboard pattern of circles with alternating colors.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Circle

def draw_patch_window8():
    """Draws a patch with a checkerboard pattern of circles."""
    win = Window("Patch 8", 200, 200)
    radius = 10
    pas = 0
    for y in range(10, 100, 20):
         for x in range(10, 100, 20):
             centre = Point(x, y)
             circle = Circle(centre, radius)
             
             # Conditional coloring based on row index (pas)
             if pas % 2 == 0:
                 circle.fill_colour = "red"
                 circle.outline_colour = "red"
             else:
                 circle.outline_colour = "red"
                 
             circle.draw(win)
         pas += 1
         
    win.get_mouse()
    win.close()
