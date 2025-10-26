# FILE: draw_letter_e.py
# CONCEPT: Algorithmic Character Drawing (ASCII Art)
# DEMONSTRATES: Using function composition and iteration to construct a complex 
# shape (the letter 'E') purely from text characters.

def draw_block_of_stars(width, height):
    """Prints a solid block of stars of the specified width and height."""
    for i in range (height):
        for j in range (width):
            print('*' , end="")
        print()

def draw_letter_e():
    """Draws the letter 'E' by calling draw_block_of_stars multiple times."""
    draw_block_of_stars(8,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(5,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(8,2)
    
# draw_letter_e()
