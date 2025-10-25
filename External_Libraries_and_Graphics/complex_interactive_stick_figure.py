# FILE: complex_interactive_stick_figure.py
# CONCEPT: External Library Usage - Composite Shapes and Basic Interaction
# DEMONSTRATES: Combining multiple geometric primitives (Circle, Line, Rectangle) to form a complex figure 
# and attempting to use mouse clicks within a loop for interaction (I/O).
# NOTE: Requires the 'graphix' library to be installed.

from graphix import Window, Point, Line, Circle, Rectangle, Text

def draw_stick_figure():
    win = Window("Stick figure", 300, 200)
    
    # Head and Body
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    
    # Arms
    arm1 = Line(Point(200, 90), Point(160, 80))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 80))
    arm2.draw(win)
    
    # Legs
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    
    # Accessories (Brown Rectangle 'Bat' or 'Sword')
    rectangle = Rectangle(Point(140, 75), Point(180, 80))
    rectangle.fill_colour = "brown"
    rectangle.draw(win)
    
    # Accessories (Orange Circle 'Ball' / 'Orange')
    orange = Circle(Point(170, 68), 6)
    orange.fill_colour = "orange"
    
    # Accessories (Black Cup)
    cup = Rectangle(Point(150, 63),Point(160, 75))
    cup.fill_colour = "black"
    cup.draw(win)
    orange.draw(win)
    
    # Text Setup
    word = "Smash!"
    message = Text(Point(100, 40), "S")
    message.draw(win)
    
    # Interactive loop (Simplified to prevent runtime error)
    # The original loop logic was flawed and is simplified here 
    # to demonstrate the intent of using mouse input and movement.
    for i in range(3): 
       win.get_mouse() # Wait for mouse click
       message.text = word[:i+1] # Update text 
       cup.move(0, 5) # Move the cup slightly
    
    win.get_mouse()
    win.close()
