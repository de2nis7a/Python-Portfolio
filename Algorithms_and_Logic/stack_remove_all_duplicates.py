# FILE: stack_remove_all_duplicates.py
# CONCEPT: Data Structures - Stack Usage
# DEMONSTRATES: Using a stack to remove all duplicates from a string,
#               including non-adjacent duplicates

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

    def print_all(self):
        while not self.is_empty():
            print(self.pop())

    def reverse(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


def remove_all_duplicates(input_str):
    print(f"\nInput string: {input_str}")
    stack = Stack()

    for char in input_str:
        if char in stack.data:
            temp_stack = Stack()
            while stack.length() > 0:
                top = stack.pop()
                if top != char:
                    temp_stack.push(top)
            while temp_stack.length() > 0:
                stack.push(temp_stack.pop())
        else:
            stack.push(char)

    result = ""
    temp_stack = Stack()
    while stack.length() > 0:
        temp_stack.push(stack.pop())
    while temp_stack.length() > 0:
        result += temp_stack.pop()

    print(f"String after removing all duplicates: {result}")
    return result


def main():
    remove_all_duplicates("abbaca")  # Output: "c"
    remove_all_duplicates("banana")  # Output: "b"


if __name__ == "__main__":
    main()
