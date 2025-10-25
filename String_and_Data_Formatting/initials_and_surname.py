# FILE: initials_and_surname.py
# CONCEPT: String Slicing and Indexing
# DEMONSTRATES: Extracting the first character of a string (initial) using indexing (`[0]`).

def formal_name():
    given_name = str(input("Your given name is:"))
    family_name = str(input("Your family name is:"))
    print(given_name[0] + ". " + family_name)
