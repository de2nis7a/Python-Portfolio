# FILE: patchwork_window_10.py
# CONCEPT: Graphics and Line Hatching (Opposite Corners)
# DEMONSTRATES: Drawing a line pattern where two sets of lines are drawn using 
# opposing point movements, creating a complex V-shaped texture.

from graphix import Window, Point, Line

def draw_patch_window10():
        """Draws a patch using two opposing sets of lines."""
        win = Window("Patch 10", 200, 200)
        
        # Set 1: Lines starting top-left, moving outwards
        point_one = Point(0, 0)
        point_two = Point(100, 10)
        for i in range(10):
            line = Line(point_one, point_two)
            line.fill_colour = "red"
            line.draw(win)
            point_one.move(10, 0)
            point_two.move(0, 10)
            
        # Set 2: Lines starting bottom-right, moving inwards
        point_one = Point(100, 100)
        point_two = Point(0, 90)
        for i in range(10):
            line = Line(point_one, point_two)
            line.fill_colour = "red"
            line.draw(win)
            point_one.move(-10, 0)
            point_two.move(0, -10)
            
        win.get_mouse()
        win.close()
