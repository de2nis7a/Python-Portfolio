# FILE: write_to_file.py
# CONCEPT: File Input/Output (I/O) - Writing to File
# DEMONSTRATES: Opening a file in write mode ('w'), and writing content using the 'print(..., file=...)' 
#               syntax for easy output redirection.

import os

def write_quote():
    # NOTE: This code assumes there is a subdirectory named 'text_files'.
    try:
        os.chdir("text_files")
    except FileNotFoundError:
        print("Error: 'text_files' directory not found.")
        return

    try:
        with open("my_quotation.txt", "w") as output_file:
            # The 'print' function redirects output to the specified file handle
            print("I love Python!", file=output_file)
            print("(Matthew Poole)", file=output_file)
        print("Successfully wrote content to text_files/my_quotation.txt")
        
    except Exception as e:
        print(f"An error occurred during writing: {e}")
        
    os.chdir("..")
