# FILE: generate_student_email.py
# CONCEPT: String Manipulation and Formatting
# DEMONSTRATES: Combining multiple string manipulation techniques: slicing, conversion to lowercase, 
#               and arithmetic (modulus `%`) for year truncation.

def generate_email():
    surname = str(input("Enter your surname:"))
    forename = str(input("Enter your forename:"))
    year = int(input("Enter the start year:"))
    
    # Logic for email generation
    year_two_digits = year % 100
    surname = surname.lower()
    forename = forename.lower()
    year_str = str(year_two_digits)
    
    # Format: first 4 chars of surname + dot + first char of forename + dot + 2-digit year
    print(surname[:4] + "." + forename[0] + "." + year_str + "@myport.ac.uk")
