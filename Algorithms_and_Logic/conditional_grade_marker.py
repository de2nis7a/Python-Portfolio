# FILE: conditional_grade_marker.py
# CONCEPT: Input Validation and Modular Function Call
# DEMONSTRATES: Using a while loop to ensure the mark is in a valid range (0-20) 


def grade_coursework():

    def calculate_grade(mark):
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
            
    while True:
        mark = int(input("The mark is: "))
        if 0 < mark and mark <= 20:
            c = calculate_grade(mark)
            print(c)
            break
        else:
            print("Enter a valid mark: ")
