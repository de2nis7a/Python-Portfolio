# FILE: selection_sort.py
# CONCEPT: Algorithms - Sorting
# DEMONSTRATES: Implementation of Selection Sort algorithm on a randomly generated array

from random import sample

class Iteration:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)

    def print_all(self):
        print("The size of the random array:", len(self.data))
        print("Before sorting, the array is:", self.data)

    def selection_sort(self):
        for i in range(len(self.data) - 1):
            ind_min = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[ind_min]:
                    ind_min = j
            self.data[ind_min], self.data[i] = self.data[i], self.data[ind_min]
        return self.data


def main():
    arr = Iteration()
    arr.initialise()
    arr.print_all()
    print("After the selection sort, the array is:", arr.selection_sort())


if __name__ == "__main__":
    main()
