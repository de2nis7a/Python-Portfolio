# FILE: draw_archery_target.py
# CONCEPT: External Library Usage - Layering and Coloring
# DEMONSTRATES: Drawing multiple overlapping shapes (circles) with different colors and sizes 
#               to create a visual target, showing drawing order (largest to smallest).

from graphix import Window, Circle, Point

def draw_archery_target():
    win=Window()
    radius_1 = 50
    radius_2 = 100
    radius_3 = 150
    centre = Point(200,200)
    
    # Draw order matters for layering
    circle_3= Circle(centre,radius_3)
    circle_3.fill_colour = "blue"
    
    circle_2= Circle(centre,radius_2)
    circle_2.fill_colour = "red"
    
    circle_1= Circle(centre,radius_1)
    circle_1.fill_colour = "yellow"
    
    circle_3.draw(win)
    circle_2.draw(win)
    circle_1.draw(win)
