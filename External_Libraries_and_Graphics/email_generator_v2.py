# FILE: email_generator_v2.py
# CONCEPT: String Manipulation and Formatting (v2)
# DEMONSTRATES: Combining string slicing, the 'lower()' method, and concatenation to form a university email address.

def generate_email ():
    surname = input("Surname: ")
    forename = input("Forename: ")
    year = input("Year: ")
    string = "@myport.ac.uk"
    
    # Logic: first 4 chars of forename + dot + lowercase surname + dot + 2-digit year
    email = forename[:4] + "." + surname.lower() + "." + year[2:] + string  
    print(email)
