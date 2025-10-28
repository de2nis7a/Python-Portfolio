# FILE: geometric_square.py
# CONCEPT: Object-Oriented Programming (OOP) - Composition and Property Calculation
# DEMONSTRATES: Using one custom class (MyPoint) as an attribute inside another class (Composition). 
#               Calculates derived properties (Perimeter, Area, Centre).

from geometric_point import MyPoint # Requires MyPoint class from geometric_point.py

class Square:

    def __init__(self, p1, side):
        self.p1 = p1 # Bottom-left point
        self.side = side
        # p2 is defined based on p1 and side (assuming axis-aligned square)
        self.p2 = MyPoint(p1.x + side, p1.y + side) # Top-right point 
        self.outline_colour = "black"
        self.fill_colour = "white"
        
    def move(self, dx, dy):
        # Moves both component points
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
        
    def get_perimeter(self):
        return f"Perimeter is {self.side * 4}"
        
    def get_centre(self):
        # Calculates centre point
        centre_x = (self.p1.x + self.p2.x) / 2
        centre_y = (self.p1.y + self.p2.y) / 2
        
        centre = MyPoint(centre_x, centre_y)
        return f"Square's centre is {centre}"
    
    def get_area(self, side):
        return f"Area is {side * side}"
        
    def __str__(self):
        return f"Square({self.p1}, {self.p2})"
    
def test_square():
    p = MyPoint(100, 50)
    square = Square(p, 50)

    print("square's side length is", square.side)  # 50
    print("square's p1 is", square.p1)  # MyPoint(100, 50)
    print("square's p2 is", square.p2)  # MyPoint(150, 100)

    square.side = 100
    # Re-initialize the square with the new side length
    square = Square(p, square.side) 
    print("After changing square's side length to 100 ...")
    print("square's side length is", square.side)  # 100
    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.side)  # 100
    print("square's p1 is", square.p1)  # MyPoint(110, 30)
    print("square's p2 is", square.p2)  # MyPoint(160, 80)
    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))
    
    print("square's fill colour is", square.fill_colour)
    print("square's outline colour is", square.outline_colour)
    
    # NOTE: The following lines only print the new colour names, they don't change the object state.
    print("Changing square's fill colour to purple")
    print("square's fill colour is purple")
    print("Changing square's outline colour to blue")
    print("square's outline colour is blue")
    
    print(square.get_perimeter())
    # Calling get_area with the side length as argument
    print(square.get_area(square.side)) 
    
    print(square.get_centre())

if __name__ == "__main__":
    test_square()
