# FILE: patchwork_window_1.py
# CONCEPT: Graphics and Nested Loops
# DEMONSTRATES: Using nested loops to draw repeating patterns of lines (grid) and text (hi!) 
# within a defined area.

from graphix import Window, Point, Line, Text

def draw_patch_window1():
    """Draws a patch with a red grid and repeating 'hi!' text."""
    win = Window("Patch 1", 200, 200)
    
    # Draw horizontal lines
    point_one = Point(0, 20)
    point_two = Point(100, 20)
    for i in range(4):
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        point_one.move(0, 20)
        point_two.move(0, 20)
        
    # Draw vertical lines
    point_one = Point(20, 0)
    point_two = Point(20, 100)
    for i in range(4):
        line = Line(point_one, point_two)
        line.fill_colour = "red"
        line.draw(win)
        point_one.move(20, 0)
        point_two.move(20, 0)
        
    # Draw repeating text pattern
    for i in range(10, 100, 20):
        for j in range(10, 100, 20):
            point = Point(i, j)
            message = Text(point, "hi!")
            message.size = 10
            message.fill_colour = "red"
            message.draw(win)
            
    win.get_mouse()
    win.close()
