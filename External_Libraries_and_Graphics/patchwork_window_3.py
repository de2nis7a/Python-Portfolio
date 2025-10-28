# FILE: patchwork_window_3.py
# CONCEPT: Graphics and Loop with Shrinking Shapes
# DEMONSTRATES: Creating a target-like effect using a loop that draws and shrinks rectangles 
# from the corners inwards, alternating colors.

from graphix import Window, Point, Rectangle

def draw_patch_window3():
    """Draws a patch with shrinking, concentric rectangles."""
    win = Window("Patch 3", 200, 200)
    point_one = Point(0, 0)
    point_two = Point(100, 100)
    for i in range(10):
        rectangle = Rectangle(point_one, point_two)
        if i % 2 == 0:
            rectangle.fill_colour = "red"
        else:
            rectangle.fill_colour = "white"
        rectangle.draw(win)
        # Shrink the rectangle by moving corners inwards
        point_one.move(5, 5)
        point_two.move(-5, -5)
        
    win.get_mouse()
    win.close()
