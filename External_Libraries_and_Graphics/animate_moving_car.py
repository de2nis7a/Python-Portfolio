# FILE: animate_moving_car.py
# CONCEPT: Basic Animation and Composition
# DEMONSTRATES: Combining multiple geometric shapes (Rectangles, Circles) into a list 
# and using a loop (time.sleep) to incrementally move all parts simultaneously, 
# simulating animation.
from graphix import Window, Rectangle, Circle, Point
import time

def move_car():
    win = Window("Moving Car Animation", 600, 300)
    
    # 1. Define all car parts
    car_body = Rectangle(Point(100, 150), Point(300, 200))
    car_body.fill_colour = 'blue'
    car_top = Rectangle(Point(140, 120), Point(260, 150))
    car_top.fill_colour = 'lightblue'
    wheel1 = Circle(Point(130, 210), 20) 
    wheel1.fill_colour = 'black'
    wheel2 = Circle(Point(270, 210), 20)  
    wheel2.fill_colour = 'black'
    
    # 2. Draw them once
    car_body.draw(win)
    car_top.draw(win)
    wheel1.draw(win)
    wheel2.draw(win)
    
    # 3. Store parts in a list for easy iteration
    car_objects = [car_body, car_top, wheel1, wheel2]
    
    # 4. Animation loop
    for _ in range(100): 
        time.sleep(0.05)  
        for part in car_objects:
            part.move(2, 0) # Move 2 units to the right
    
    win.get_mouse() 
    win.close()
