# FILE: name_to_ascii_sum.py
# CONCEPT: Character Ordinal Conversion
# DEMONSTRATES: Using the built-in Python function 'ord()' to get the ASCII/Unicode value of a character 
#                and performing a numerical conversion (e.g., A=1, B=2, etc.)

def name_to_number():
    name = input("Your name is: ")
    name = name.lower()
    total_sum = 0
    # 96 is the ASCII value of 'a' minus 1, so 'a' becomes 1.
    for ch in name:
        if 'a' <= ch <= 'z':
            total_sum = total_sum + ord(ch) - 96
    print(total_sum)
