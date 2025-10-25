# FILE: geometric_point.py
# CONCEPT: Object-Oriented Programming (OOP) - Base Class
# DEMONSTRATES: Simple class structure, attribute initialization, mutation methods (move), and custom string representation (__str__).

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"
    
def test_my_point():
    my_point = MyPoint(100, 50)
    print("my_point's x coordinate is", my_point.x)  # 100
    print("my_point's y coordinate is", my_point.y)  # 50
    my_point.move(10, -20)
    print("my_point's x coordinate is", my_point.x)  # 110
    print("my_point's y coordinate is", my_point.y)  # 30

if __name__ == "__main__":
    test_my_point()
