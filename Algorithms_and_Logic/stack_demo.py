# FILE: stack_demo.py
# CONCEPT: Data Structures - Stack
# DEMONSTRATES: Implementation of a stack with push, pop, peek, reverse, and print operations

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

    def print_message(self):
        print("Stack size:", self.length(), "Top element:", self.peek())

    def print_all(self):
        while not self.is_empty():
            print(self.pop())

    def reverse(self):
        temp_stack = []
        while not self.is_empty():
            temp_stack.append(self.pop())
        while temp_stack:
            self.push(temp_stack.pop())


def main():
    s = Stack()
    for i in range(1, 9):
        s.push(i)
    s.print_message()
    for _ in range(4):
        s.pop()
    s.print_message()
    s.print_all()


if __name__ == "__main__":
    main()
