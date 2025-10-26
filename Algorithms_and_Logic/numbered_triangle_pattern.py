# FILE: numbered_triangle_pattern.py
# CONCEPT: Nested Loops and Pattern Generation
# DEMONSTRATES: Using an inner loop to control columns and an outer loop to control rows 
# to generate a specific numeric pattern.

def numbered_triangle(n):
    """Prints a numbered triangle pattern up to n rows."""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
