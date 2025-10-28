# FILE: stack_remove_adjacent.py
# CONCEPT: Data Structures - Stack Usage
# DEMONSTRATES: Using a stack to remove adjacent duplicate letters from a string,
#               and performing standard stack operations (push, pop, peek, reverse)

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
        print(f"Stack size: {self.length()}, top element: {self.peek()}")

    def print_all(self):
        while not self.is_empty():
            print(self.pop())

    def reverse(self):
        temp_stack = []
        while not self.is_empty():
            temp_stack.append(self.pop())
        while temp_stack:
            self.push(temp_stack.pop())

    def remove_adjacent(self, input_str):
        print(f"\nInput string: {input_str}")
        result = ""
        for character in input_str:
            if not self.is_empty() and self.peek() == character:
                self.pop()
            else:
                self.push(character)
        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())
        while not temp_stack.is_empty():
            result += temp_stack.pop()
        print(f"String after removing adjacent duplicates: {result}")
        return result


def main():
    s = Stack()
    s.remove_adjacent("dsallasg")


if __name__ == "__main__":
    main()
