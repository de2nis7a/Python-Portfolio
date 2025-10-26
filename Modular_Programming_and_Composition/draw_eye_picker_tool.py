# FILE: draw_eye_picker_tool.py
# CONCEPT: Modular Programming, Graphics, and Input Validation
# DEMONSTRATES: Using a modular helper function (draw_coloured_eye) and implementing 
# robust input validation (coordinates and color list check) before drawing.
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Circle, Point
import random

def draw_coloured_eye(win, centre, radius, colour):
    """Draws a complete eye (sclera, iris, pupil) with specified color."""
    circle_one = Circle(centre, radius)
    circle_two = Circle(centre, radius // 2)
    circle_three = Circle(centre, radius //3)
    
    circle_one.fill_colour = "white"
    circle_two.fill_colour = colour
    circle_three.fill_colour = "black"
    
    circle_one.draw(win)
    circle_two.draw(win)
    circle_three.draw(win)
   

def eye_picker():
    """Gets user input for eye properties and draws the eye if inputs are valid."""
    win = Window("Eye Picker", 500, 500)
    colours_list = ["blue", "grey", "green", "brown"]
    
    # Input
    x_eye = int(input("Enter the x coordinate: "))
    y_eye = int(input("Enter the y coordinate: "))
    radius_eye = int(input("The radius of the eye is: "))
    colour = input("The colour of the eye is: ")
    
    # Validation check
    if (x_eye >= radius_eye and x_eye <= 500 - radius_eye and 
        y_eye >= radius_eye and y_eye <= 500 - radius_eye and 
        colour in colours_list):
        
        centre = Point(x_eye, y_eye)
        draw_coloured_eye(win, centre, radius_eye, colour)
        win.get_mouse()
    else:
       print("Invalid input: Eye center not safely in window or color not valid.")
       
    win.close()
    
# eye_picker()
