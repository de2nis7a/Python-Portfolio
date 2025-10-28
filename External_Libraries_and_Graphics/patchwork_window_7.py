# FILE: patchwork_window_7.py
# CONCEPT: Graphics and Shrinking Circles
# DEMONSTRATES: Creating a 3D tunnel effect by drawing concentric circles that shrink 
# in radius and shift their center simultaneously within a loop.

from graphix import Window, Point, Circle

def draw_patch_window7():
    """Draws a patch of shrinking, off-center circles."""
    win = Window("Patch 7", 200, 200)
    centre = Point(50,50)
    radius = 50
    for i in range(10):
        circle = Circle(centre, radius)
        circle.outline_colour = "red"
        circle.draw(win)
        radius -= 5      # Shrink radius
        centre.move(0, 5) # Move center down
            
    win.get_mouse()
    win.close()
