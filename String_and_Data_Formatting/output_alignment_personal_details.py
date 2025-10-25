# FILE: output_alignment_personal_details.py
# CONCEPT: Output Formatting and Alignment
# DEMONSTRATES: Using f-string formatting (`f"..."`) with alignment specifiers (`:>` for right-alignment) 
#               and precision control (`.2f`).

def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # Right-aligns all values, ensures height is shown with two decimal places.
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")
