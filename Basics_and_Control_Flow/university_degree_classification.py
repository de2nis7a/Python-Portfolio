# FILE: university_degree_classification.py
# CONCEPT: Conditional Logic (if/elif/else)
# DEMONSTRATES: Multi-branch conditional logic to assign a classification based on a score.

def get_degree_class(mark):
    """Returns the university degree classification based on the mark."""
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"
