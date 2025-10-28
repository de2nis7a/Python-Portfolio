# FILE: iteration_insertion_sort.py
# CONCEPT: Data Structures - Iteration and Sorting (Insertion Sort)
# DEMONSTRATES: Initializing a random array, performing insertion sort,
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

    def insertion_sort(self):
        for i in range(1, len(self.data)):
            current = self.data[i]
            j = i
            while j > 0 and current < self.data[j - 1]:
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = current
        return self.data


def main():
    arr = Iteration()
    arr.initialise()
    arr.print_all()
    print(f"After the insertion sort, the array is: {arr.insertion_sort()}")


if __name__ == "__main__":
    main()
