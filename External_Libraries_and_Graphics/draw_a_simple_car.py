# FILE: draw_a_simple_car.py
# CONCEPT: Composition of Basic Shapes
# DEMONSTRATES: Using multiple graphical objects (Rectangles for the body/roof, Circles for the wheels)
# to compose a complex object (a car) and applying different fill colors.
from graphix import Window, Rectangle, Circle, Point

def draw_car():
    win = Window("Simple Car", 400, 300)
    
    # Main car body
    car_body = Rectangle(Point(100, 150), Point(300, 200))
    car_body.fill_colour = 'blue'
    car_body.draw(win)
    
    # Car roof/cabin
    car_top = Rectangle(Point(140, 120), Point(260, 150))
    car_top.fill_colour = 'lightblue'
    car_top.draw(win)
    
    # Front wheel
    wheel1 = Circle(Point(130, 210), 20)  
    wheel1.fill_colour = 'black'
    wheel1.draw(win)
    
    # Rear wheel
    wheel2 = Circle(Point(270, 210), 20) 
    wheel2.fill_colour = 'black'
    wheel2.draw(win)
    
    win.get_mouse() 
    win.close()
