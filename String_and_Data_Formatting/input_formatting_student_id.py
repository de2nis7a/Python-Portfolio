# FILE: input_formatting_student_id.py
# CONCEPT: String Slicing and Output Formatting
# DEMONSTRATES: Accepting user input (ID), slicing the string to remove the first two characters,
#               and controlling line breaks in the output.

def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    # Slicing from index 2 to end to remove the first two characters (e.g., 'up')
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])
