# FILE: grade_calculator_by_mark.py
# CONCEPT: Multi-Branch Conditional Logic
# DEMONSTRATES: A practical grading system using sequential checks.

def calculate_grade(mark):
    """Calculates a grade (A, B, C, F, X) based on an integer mark."""
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
