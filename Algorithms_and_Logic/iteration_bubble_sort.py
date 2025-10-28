# FILE: iteration_bubble_sort.py
# CONCEPT: Data Structures - Iteration and Sorting (Bubble Sort)
# DEMONSTRATES: Initializing a random array, performing bubble sort, 
#               and displaying the sorted array

from random import sample

class Iteration:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)

    def print_all(self):
        print(f"The size of the random array: {len(self.data)}")
        print(f"Before sorting, the array is: {self.data}")

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            if not swapped:
                break
        return self.data


def main():
    arr = Iteration()
    arr.initialise()
    arr.print_all()
    print(f"After the bubble sort, the array is: {arr.bubble_sort()}")


if __name__ == "__main__":
    main()
