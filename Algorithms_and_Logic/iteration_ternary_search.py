# FILE: iteration_ternary_search.py
# CONCEPT: Advanced Algorithms - Bubble Sort & Ternary Search
# DEMONSTRATES: Sorting an array using bubble sort and searching using recursive ternary search

from random import sample

class Iteration:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)

    def print_all(self):
        print("Array size:", len(self.data))
        print("Array contents:", self.data)

    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    def ternary_search(self, item):
        return self._ternary_search(self.data, 0, len(self.data) - 1, item)

    def _ternary_search(self, arr, start, end, item):
        if start <= end:
            third1 = (end - start) // 3 + start
            if arr[third1] == item:
                return third1
            elif arr[third1] > item:
                return self._ternary_search(arr, start, third1 - 1, item)
            else:
                third2 = (end - start) // 3 + third1
                if arr[third2] == item:
                    return third2
                elif arr[third2] > item:
                    return self._ternary_search(arr, third1 + 1, third2 - 1, item)
                else:
                    return self._ternary_search(arr, third2 + 1, end, item)
        print("Not found")
        return -1


def main():
    arr = Iteration()
    arr.initialise()
    arr.print_all()
    print("After bubble sort:", arr.bubble_sort())
    index = arr.ternary_search(5)
    print("Index of 5:", index)


if __name__ == "__main__":
    main()
