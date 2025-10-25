# FILE: file_word_line_char_counter.py
# CONCEPT: File I/O - Word Count Utility (wc)
# DEMONSTRATES: Iterating through a file to count lines, words (using split()), and total characters, 
#               simulating the Unix 'wc' command.

def wc():
    file_name = input("The name of the file is: ")
    lines = 0
    words = 0
    characters = 0
    
    try:
        with open(file_name, "r") as file:
            for line in file:
                lines += 1
                words += len(line.split())
                characters += len(line)
        
        print(f"File: {file_name}")
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {characters}")
        
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
