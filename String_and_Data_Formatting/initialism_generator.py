# FILE: initialism_generator.py
# CONCEPT: String Splitting and Loop Iteration
# DEMONSTRATES: Using the 'split()' method to break a phrase into words and iterating through the resulting 
#               list to extract and combine the first letter of each word.

def make_initialism():
    phrase = input("Enter a phrase: ")
    words = phrase.split()
    initials = ""
    for word in words:
        if word: # Ensure word is not empty
            initials += word[0].upper()
    print(initials)
