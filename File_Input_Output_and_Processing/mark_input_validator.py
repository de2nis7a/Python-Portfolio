# FILE: mark_input_validator.py
# CONCEPT: Input Validation and Modular Function Call
# DEMONSTRATES: Using a while loop to ensure the mark is in a valid range (0-20) 
# before calling a helper function to determine the grade.

# Define helper function inline for file independence (assumed to be available)
def calculate_grade(mark):
    """Calculates a grade based on a 20-point mark scale."""
    if mark >= 16:
         return "A"
    elif mark >= 12:
         return "B"
    elif mark >= 8:
         return"C"
    elif mark > 0:
         return "F"
    else:
        return "X"

def grade_coursework():
    """Continuously prompts the user until a valid mark (1-20) is entered and prints the grade."""
    while True:
        try:
            mark = int(input("The mark is: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if 0 < mark and mark <= 20:
            c = calculate_grade(mark)
            print(f"The grade is: {c}")
            break
        else:
            print("Enter a valid mark (1-20): ")

# grade_coursework()
