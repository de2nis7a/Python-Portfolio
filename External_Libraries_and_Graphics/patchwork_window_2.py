# FILE: patchwork_window_2.py
# CONCEPT: Graphics and Nested Loops (Complex Lines)
# DEMONSTRATES: Generating a complex, interwoven line pattern by carefully moving 
# start and end points in opposing directions within a loop.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Line

def draw_patch_window2():
    """Draws a complex patch with diagonal, interwoven lines."""
    win = Window("Patch 2", 200, 200)
    
    # Draw lines from top-left to center-right area (pattern 1)
    p_one = Point(0, 0)
    p_two = Point(100, 100)
    for i in range(5):
        line = Line(p_one, p_two)
        line.fill_colour = "red"
        line.draw(win)
        p_one.move(20, 0)
        p_two.move(0, -20)
        
    # Continue pattern 1
    point_one = Point(0, 0)
    point_two = Point(100, 100)
    for i in range(4):
        point_one.move(0, 20)
        point_two.move(-20, 0)
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        
    # Draw lines from top-right to center-left area (pattern 2)
    p_one = Point(100, 0)
    p_two = Point(0, 100)
    for i in range(5):
        line = Line(p_one, p_two)
        line.fill_colour = "red"
        line.draw(win)
        p_one.move(-20, 0)
        p_two.move(0, -20)
        
    # Continue pattern 2
    point_one = Point(100, 0)
    point_two = Point(0, 100)
    for i in range(4):
        point_one.move(0, 20)
        point_two.move(20, 0)
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        
    win.get_mouse()
    win.close()
