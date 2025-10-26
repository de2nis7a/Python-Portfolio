# FILE: input_loop_vote_check_v2.py
# CONCEPT: Input Validation Loop (Simple)
# DEMONSTRATES: Two methods for continuously prompting the user until a minimum age condition is met.

def can_vote1():
    """Uses a while loop checked against a condition."""
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))

def can_vote2():
    """Uses a while True loop with a break statement."""
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")
