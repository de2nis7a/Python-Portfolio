# FILE: construct_vision_chart.py
# CONCEPT: Modular Programming and Data Formatting
# DEMONSTRATES: Using a helper function to format data (text spacing) and a main function 
# to control the flow and visualization (decreasing font size for a vision chart).

from graphix import Window, Point, Text

def display_text_with_spaces(string, size, p, win):
    """Formats text by adding spaces between letters and displays it on the window."""
    string = string.upper()
    string_two = ""
    for word in string:
        string_two = string_two + word + " "
    
    message = Text(p , string_two)
    message.size = size
    message.draw(win)
    
    
def construct_vision_chart():
    """Creates a basic eye vision chart by prompting for input and decreasing font size iteratively."""
    win = Window("Vision Chart", 800, 800)
    size = 30
    
    for i in range(6):
      string = input(f"String {i+1}: ")
      p = Point(400, 100 + 100 * i)
      display_text_with_spaces(string, size, p, win)
      size = size-5
      
    win.get_mouse()
    win.close()
    
# construct_vision_chart()
