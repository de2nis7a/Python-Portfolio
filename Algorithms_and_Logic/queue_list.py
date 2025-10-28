# FILE: queue_list.py
# CONCEPT: Data Structures - Queue Implementation
# DEMONSTRATES: Implementing a queue using a list, performing enqueue, dequeue, peek operations,
#               reversing the queue, and printing queue contents

class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 15

    def enqueue(self, new_data):
        if self.tail == self.max_size - 1:
            raise OverflowError("Cannot insert into a full queue.")
        print(f"Enqueue the data {new_data}")
        self.tail += 1
        self.data.insert(self.tail, new_data)
        print(f"Now the tail index is {self.tail}")

    def dequeue(self):
        if self.tail == -1:
            raise IndexError("Cannot delete from an empty queue.")
        removed = self.data[self.head]
        print(f"Dequeue the data {removed}")
        temp = self.head
        while temp < self.tail:
            temp += 1
            self.data[temp - 1] = self.data[temp]
        del self.data[temp]
        self.tail -= 1
        return removed

    def peek(self):
        if self.tail == -1:
            raise IndexError("Cannot peek from an empty queue.")
        print("Peek the head")
        return self.data[self.head]

    def length(self):
        return self.tail - self.head + 1

    def print_message(self):
        print(f"Queue size: {self.length()}, first element: {self.peek()}")

    def print_all(self):
        while self.tail != -1:
            print(self.dequeue())

    def reverse(self):
        print("\nBefore reverse, the queue is ", self.data)
        temp_stack = []
        while self.length() > 0:
            temp_stack.append(self.dequeue())
        while temp_stack:
            self.enqueue(temp_stack.pop())
        print("\nThe reversed queue is ", self.data)


def main():
    q = Queue()
    for j in range(10, 20):
        q.enqueue(50 - j)
    q.print_message()
    for i in range(10, 16):
        q.dequeue()
    q.print_message()
    q.print_all()


if __name__ == "__main__":
    main()
