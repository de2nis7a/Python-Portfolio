# FILE: formal_name_v2.py
# CONCEPT: String Slicing and Concatenation
# DEMONSTRATES: Extracting the initial of the given name and concatenating it with the family name for a formal output.

def formal_name ():
    given_name= input("The given name is: ")
    family_name= input("The family name is: ")
    # Extracts the first character, adds a dot and a space, and then the family name
    name= given_name[0] + "." + " " + family_name
    print(name)
