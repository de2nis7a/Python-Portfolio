# FILE: add_dashes_to_word.py
# CONCEPT: String Manipulation and Looping
# DEMONSTRATES: Iterating through a string (word) and building a new string by concatenating 
# each character with a separator (dash).

def add_dash():
    word = input("Enter a word: ")
    result = ""
    for ch in word:
        result += ch + "-"
        
    # Remove the trailing dash for a cleaner output
    print(result.rstrip('-')) 

# add_dash()
