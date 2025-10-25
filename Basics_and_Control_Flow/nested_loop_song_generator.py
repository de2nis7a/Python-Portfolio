# FILE: nested_loop_song_generator.py
# CONCEPT: Control Flow - Nested Loops
# DEMONSTRATES: Using a 'for' loop inside another 'for' loop (nested loops) to control both 
#               the number of lines and the repetition within each line.

def sing_a_song():
    word = input("Song's word is: ")
    lines = int(input("Song's lines: "))
    times_on_line = int(input("How many times the word should be repeated on each line? "))
    
    for i in range(lines):
        # Inner loop prints the word 'n' times on the same line
        for j in range(times_on_line):
            print(word, end=" ")
        # Outer print adds a newline character
        print()
