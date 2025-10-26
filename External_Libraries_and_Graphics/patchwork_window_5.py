# FILE: patchwork_window_5.py
# CONCEPT: Graphics and Complex Rectangle Movement V2
# DEMONSTRATES: Drawing a series of rectangles where both corners move diagonally 
# and identically, creating a repeating diagonal element.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Rectangle

def draw_patch_window5():
    """Draws a patch with repeating diagonal rectangles."""
    win = Window("Patch 5", 200, 200)
    point_one = Point(0, 90)
    point_two = Point(10, 100)
    for i in range(10):
        rectangle = Rectangle(point_one, point_two)
        rectangle.fill_colour = "red"
        rectangle.draw(win)
        
        # Both points move diagonally downwards and right
        point_one.move(10, -10)
        point_two.move(10, -10)
        
    win.get_mouse()
    win.close()
