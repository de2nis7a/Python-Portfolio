# FILE: geometric_circle.py
# CONCEPT: Object-Oriented Programming (OOP) - Composition
# DEMONSTRATES: Using an instance of another class (MyPoint) as the 'centre' attribute 
#               and defining basic geometric properties.

from geometric_point import MyPoint 

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre # centre is an instance of MyPoint
        self.radius = radius
        self.fill_colour = "red"
        self.outline_colour = "blue"
    
    def get_radius(self):
        return f"{self.radius}"
    
    def __str__(self):
        return f"Circle({self.centre.x}, {self.centre.y}), {self.radius})"
    
def test_circle():
    p = MyPoint(50, 150)
    radius = 50
    circle = Circle(p, radius)
    print(circle)
    print("circle's centre's x coordinate is", p.x) #50
    print("circle's centre's y coordinate is", p.y) #150
    print("circles's radius is", circle.get_radius())
    print("circles's fill colour is", circle.fill_colour)
    print("circles's outline colour is", circle.outline_colour)
        
if __name__ == "__main__":
    test_circle()
