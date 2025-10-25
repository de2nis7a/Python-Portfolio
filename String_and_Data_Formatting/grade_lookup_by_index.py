# FILE: grade_lookup_by_index.py
# CONCEPT: String Indexing as a Lookup Table
# DEMONSTRATES: Using a fixed string where index position corresponds to a mark, and the character at that 
#               index provides the corresponding grade.

def grade_test():
    # Index 0=F, 6=C, 10=A
    grades = "FFFFCCBBAAA"
    mark = int(input("Enter a mark (between 0 and 10): "))
    
    # Added validation to prevent IndexError
    if 0 <= mark < len(grades):
        grade = grades[mark]
        print(f"A mark of {mark} gives a grade of {grade}")
    else:
        print("Error: Mark must be between 0 and 10.")
