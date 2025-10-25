# FILE: read_file_to_uppercase.py
# CONCEPT: File I/O and String Methods
# DEMONSTRATES: Reading lines from a file and transforming each line to uppercase using the 'upper()' method.

def file_in_caps():
    # NOTE: Assumes 'quotation.txt' is available in the run directory.
    try:
        with open("quotation.txt", "r") as input_file:
            lines = input_file.readlines()
            for line in lines:
                # 'end=" "' prevents an extra newline and adds a space between lines.
                print(line.upper(), end=" ") 
            print() # Final newline
            
    except FileNotFoundError:
        print("Error: quotation.txt not found.")
