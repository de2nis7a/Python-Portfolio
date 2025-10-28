# FILE: circular_queue.py
# CONCEPT: Data Structures - Circular Queue Implementation
# DEMONSTRATES: Implementing a circular queue using a list, performing enqueue, dequeue, peek operations, 
#               and tracking head/tail indices with modular arithmetic

class CircularQueue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
        self.max_size = 5

    def enqueue(self, new_data):
        if self.tail - self.head == self.max_size:
            raise OverflowError("Cannot insert into a full circular queue.")
        print("Enqueue the data " + str(new_data))
        ind_tail = self.tail % self.max_size
        self.tail += 1
        if ind_tail >= len(self.data):
            self.data.append(new_data)
        else:
            self.data[ind_tail] = new_data
        print(f"New tail: {self.tail}, index used for tail: {ind_tail}")

    def dequeue(self):
        if self.tail == self.head:
            self.data = []
            self.head = 0
            self.tail = 0
            raise IndexError("Cannot delete from an empty circular queue.")
        ind_head = self.head % self.max_size
        self.head += 1
        removed = self.data[ind_head]
        print(f"Dequeue the data {removed}, new head: {self.head}, index used for head: {ind_head}")
        return removed

    def peek(self):
        if self.tail == self.head:
            raise IndexError("Can't peek from an empty queue")
        ind_head = self.head % self.max_size
        print("Peek the head")
        return self.data[ind_head]

    def length(self):
        return self.tail - self.head

    def print_message(self):
        print(f"Circular queue size: {self.length()}, first element: {self.peek()}, head index: {self.head}, tail index: {self.tail}")

    def print_all(self):
        while self.tail != self.head:
            print(self.dequeue())


def main():
    cq = CircularQueue()
    for k in range(1, 6):
        cq.enqueue(k)
    cq.print_message()
    for i in range(1, 3):
        cq.dequeue()
    cq.print_message()
    cq.print_all()


if __name__ == "__main__":
    main()
