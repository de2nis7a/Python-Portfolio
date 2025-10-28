# FILE: iteration_bubble_binary.py
# CONCEPT: Data Structures - Iteration, Sorting (Bubble Sort), and Search (Binary Search)
# DEMONSTRATES: Initializing a random array, performing an optimized bubble sort, 
#               and executing iterative binary search on sorted data

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
            for j in range(n - 1 - i):  # reduce comparisons each pass
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    swapped = True
            if not swapped:  # if no swaps, array is sorted
                break
        return self.data

    def binary_iter_search(self, item):
        start = 0
        end = len(self.data) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.data[mid] < item:
                start = mid + 1
            elif self.data[mid] > item:
                end = mid - 1
            else:
                return mid
        print("Not found")
        return -1
    
def main():
    arr = Iteration()
    arr.initialise()
    arr.print_all()
    print(f"After the bubble sort, the array is: {arr.bubble_sort()}")
    ind = arr.binary_iter_search(5)
    print(ind)

if __name__ == "__main__":
    main()
