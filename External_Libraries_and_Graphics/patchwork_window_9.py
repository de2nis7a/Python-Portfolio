# FILE: patchwork_window_9.py
# CONCEPT: Graphics and Shrinking Rectangles V2
# DEMONSTRATES: Drawing a shrinking rectangle pattern with one corner fixed and the 
# other moving diagonally, while alternating colors.

from graphix import Window, Point, Rectangle

def draw_patch_window9():
     """Draws a patch with shrinking rectangles moving diagonally, alternating colors."""
     win = Window("Patch 9", 200, 200)
     point_one = Point(90, 10)
     point_two = Point(0, 100)
     for i in range(9):
         rectangle = Rectangle(point_one, point_two)
         
         # Conditional coloring
         if i % 2 == 0:
           rectangle.fill_colour = "red"
           rectangle.outline_colour = "red"
         else:
             rectangle.fill_colour = "white"
             rectangle.outline_colour = "white"
             
         rectangle.draw(win)
         # Shrink and shift top-right point
         point_one.move(-10, 10)
         
     win.get_mouse()
     win.close()
