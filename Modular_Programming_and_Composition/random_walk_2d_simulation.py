# FILE: random_walk_2d_simulation.py
# CONCEPT: Advanced Modular Simulation and Statistics
# DEMONSTRATES: Simulating multiple random walks, aggregating results, 
# and calculating the average distance from the starting point (expected distance).

from random import random

def get_inputs():
    """Gets the number of walks and steps from the user."""
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps


def take_a_walk(num_steps):
    """Simulates a single random walk and returns the final distance from start."""
    steps_forward_of_start = 0
    for step in range(num_steps):
        # 50% chance to step forward (+1) or backward (-1)
        if random() < 0.5:
            steps_forward_of_start = steps_forward_of_start - 1
        else:
            steps_forward_of_start = steps_forward_of_start + 1
    # Return absolute distance
    return abs(steps_forward_of_start)


def take_walks(num_walks, num_steps):
    """Simulates multiple walks and returns the average final distance."""
    total_steps = 0
    for walk in range(num_walks):
        steps_away = take_a_walk(num_steps)
        total_steps = total_steps + steps_away
    # Calculate and return the average distance
    return total_steps / num_walks


def print_expected_distance(average_steps):
    """Prints the final calculated expected distance."""
    print("The expected number of steps away from the", end=" ")
    print("start point is", average_steps)


def main():
    """Main function to execute the random walk simulation."""
    num_walks, num_steps = get_inputs()
    average_steps = take_walks(num_walks, num_steps)
    print_expected_distance(average_steps)


if __name__ == "__main__":
    main()
