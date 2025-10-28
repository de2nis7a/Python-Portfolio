# FILE: iteration_bubble_binary_recursive.py
# CONCEPT: Data Structures - Iteration, Sorting (Bubble Sort), and Recursive Search (Binary Search)
# DEMONSTRATES: Initializing a random array, performing bubble sort, 
#               and executing recursive binary search on sorted data

from random import sample

class Iteration:
        
    def __init__(self):
        self.data = []
        self.max_size = 100
        
    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)
        
    def prin_all(self):
        print("The size of the random array " + str(len(self.data)))
        print("Before sorting, the array is " + str(self.data))

    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                #for j in range(len(self.data) - 1 - i):
                if (self.data[j] > self.data[j + 1]):
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data
    
    def binary_recur_search(self, item):
        return self._binaryRecurSearch(self.data, 0, len(self.data) - 1, item)
    
    def _binary_recur_search(self, arr, start, end, item):
        if (start <= end):
            mid = (start + end) // 2
            if (arr[mid] < item):
                return self._binaryRecurSearch(arr, mid + 1, end, item)
            elif (arr[mid] > item):
                return self._binaryRecurSearch(arr, start, mid - 1, item)
            else:
                return mid
        print("Not found")
        return -1
    
def main():
    arr = Iteration()
    arr.initialise()
    arr.printAll()
    print("After the bubble sort, the array is " + str(arr.bubbleSort()))
    ind = arr.binaryRecurSearch(5)
    print(ind)

if __name__ == "__main__":
    main()