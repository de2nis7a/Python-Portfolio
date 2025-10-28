# FILE: interactive_text_input_demo.py
# CONCEPT: Graphical User Input (Entry)
# DEMONSTRATES: Using the 'Entry' object to capture text input from the user directly 
# within the graphics window, and then displaying the result using a 'Text' object.
from graphix import Window, Point, Text, Entry

def text_input_interaction():
    win = Window("User Input", 400, 200)
    
    # Create an input box centered on the screen
    input_box = Entry(Point(200, 100), 20)
    input_box.draw(win)  
    
    # Display instruction message
    message = Text(Point(200, 50), "Enter your name:")  
    message.draw(win)
    
    # Wait for the user to click to submit input
    win.get_mouse()                         
    
    # Retrieve the text from the input box
    user_input = input_box.text              
    
    # Update the message to greet the user
    message.text = "Hello, " + user_input 
    
    # Wait for a final click before closing
    win.get_mouse()                          
    win.close()
