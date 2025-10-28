# FILE: interactive_eye_color_change.py
# CONCEPT: Modular Graphics and Iterative Drawing
# DEMONSTRATES: Reusing a complex modular function (draw_coloured_eye) within a loop 
# to show different color variants based on a predefined list.

from graphix import Window, Point

def draw_coloured_eye(win, centre, radius, colour):
    circle_one = Circle(centre, radius)
    circle_two = Circle(centre, radius // 2)
    circle_three = Circle(centre, radius //3)
    circle_one.fill_colour = "white"
    circle_two.fill_colour = colour
    circle_three.fill_colour = "black"
    circle_one.draw(win)
    circle_two.draw(win)
    circle_three.draw(win)


def eyes_all_around():
    """Draws multiple eyes with different colors based on user clicks."""
    win = Window("Eyes", 500, 500)
    
    centre = win.get_mouse() # Initial click for center
    radius = 30
    colours = ["blue", "grey", "green", "brown"]
    
    for colour in colours:
        draw_coloured_eye(win, centre, radius, colour)
        centre = win.get_mouse() # New click for next eye's center
        
    win.get_mouse()
    win.close()
    
# eyes_all_around()
