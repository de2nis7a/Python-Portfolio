# FILE: patchwork_window_6.py
# CONCEPT: Graphics and Cross-Hatching Lines
# DEMONSTRATES: Creating a complex hatch pattern by drawing multiple sets of lines 
# where endpoints move symmetrically in opposite directions.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Line

def draw_patch_window6():
    """Draws a patch using two intersecting sets of parallel lines."""
    win = Window("Patch 6", 200, 200)
    
    # Set 1: Lines moving up and down on the vertical axis
    point_one = Point(0, 0)
    point_two = Point(100, 100)
    for i in range(11):
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        point_one.move(0, 10) # Move bottom point up
        point_two.move(0, -10) # Move top point down
        
    # Set 2: Lines moving left and right on the horizontal axis
    point_one = Point(10, 0)
    point_two = Point(90, 100)
    for i in range(9):
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        point_one.move(10, 0) # Move left point right
        point_two.move(-10, 0) # Move right point left
        
    win.get_mouse()
    win.close()
