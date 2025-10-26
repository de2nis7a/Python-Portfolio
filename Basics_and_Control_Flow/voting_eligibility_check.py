# FILE: voting_eligibility_check.py
# CONCEPT: Conditional Logic (if/else)
# DEMONSTRATES: Checking an integer input against a condition to determine eligibility.

def can_you_vote(age):
    """Checks if the user's age meets the voting requirement."""
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")
