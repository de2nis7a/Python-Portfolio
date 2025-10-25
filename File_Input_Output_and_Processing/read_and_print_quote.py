# FILE: read_and_print_quote.py
# CONCEPT: File Input/Output (I/O) - Reading Entire File
# DEMONSTRATES: Using the 'os' library to handle file paths, opening a file in read mode ('r'), 
#               and using the 'read()' method to get all content as a single string.

import os

def read_quote():
    # NOTE: This code assumes there is a subdirectory named 'text_files'
    # and a file named 'quotation.txt' inside it for the demonstration.
    
    # Temporarily change directory to access the file
    try:
        os.chdir("text_files")
        print("Current directory:\t" + os.getcwd())
    except FileNotFoundError:
        print("Error: 'text_files' directory not found.")
        return

    try:
        with open("quotation.txt", "r") as input_file:
            # Reads the entire file content into a single string
            content = input_file.read()
            print("\n--- Quotation Content ---\n")
            print(content)
    except FileNotFoundError:
        print("Error: quotation.txt not found in text_files.")
        
    # Change back to parent directory (optional, but good practice)
    os.chdir("..")
