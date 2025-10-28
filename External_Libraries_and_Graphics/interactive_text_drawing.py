# FILE: interactive_text_drawing.py
# CONCEPT: External Library Usage - Interactive Graphics and Text
# DEMONSTRATES: Drawing text interactively based on mouse clicks, requiring the user to type a word and 
#               then click to place each letter on the screen.

from graphix import Window, Point, Text

def graphic_letters():
    win = Window()
    word = str(input("Your word is:" ))
    
    print("Click on the window to place each letter...")
    
    for i in word:
        p = win.get_mouse() # Waits for the user to click
        message = Text(p, i)
        message.size = 30
        message.draw(win)
        # Undraw the previous letter for a flicker effect (or wait for the next click)
        
    win.get_mouse() # Final click to close
    win.close()
