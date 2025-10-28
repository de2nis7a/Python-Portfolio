# FILE: queue_reverse_with_stack.py
# CONCEPT: Data Structures - Queue and Stack Usage
# DEMONSTRATES: Reversing a queue using a stack, as well as standard queue operations (enqueue, dequeue, peek)

class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.max_size = 10

    def push(self, new_data):
        if self.top == self.max_size - 1:
            raise OverflowError("Cannot insert into a full stack.")
        self.top += 1
        self.data.insert(self.top, new_data)

    def pop(self):
        if self.top == -1:
            raise IndexError("Cannot delete from an empty stack.")
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek from an empty stack.")
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1

    def length(self):
        return self.top + 1


class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 15

    def enqueue(self, new_data):
        if self.tail == self.max_size - 1:
            raise OverflowError("Cannot insert into a full queue.")
        self.tail += 1
        self.data.insert(self.tail, new_data)

    def dequeue(self):
        if self.tail == -1:
            raise IndexError("Cannot delete from an empty queue.")
        removed = self.data[self.head]
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
        return self.data[self.head]

    def length(self):
        return self.tail
