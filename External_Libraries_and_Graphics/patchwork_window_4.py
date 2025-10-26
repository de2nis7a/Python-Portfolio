# FILE: patchwork_window_4.py
# CONCEPT: Graphics and Complex Rectangle Movement
# DEMONSTRATES: Drawing a stack of rectangles where one corner moves diagonally 
# while the other moves only vertically, creating a stepped pattern.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Rectangle

def draw_patch_window4():
    """Draws a patch with stacked, stepped rectangles."""
    win = Window("Patch 4", 200, 200)
    
    # Start near top left
    point_one = Point(0, 90)
    point_two = Point(100, 100)
    
    for i in range(10):
        rectangle = Rectangle(point_one, point_two)
        rectangle.fill_colour = "red"
        rectangle.outline_colour = "red"
        rectangle.draw(win)
        
        # Move top-left point diagonally (down-right)
        point_one.move(10, -10)
        # Move bottom-right point only vertically (up)
        point_two.move(0, -10)
        
    win.get_mouse()
    win.close()
