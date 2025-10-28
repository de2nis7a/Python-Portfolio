# FILE: stack_bracket_validation.py
# CONCEPT: Data Structures - Stack Implementation and Bracket Validation
# DEMONSTRATES: Implementing a custom stack class, performing standard stack operations 
#               (push, pop, peek, is_empty), reversing stack contents, and validating 
#               bracket sequences in strings using stack logic

# FILE: stack_bracket_validation.py
# CONCEPT: Data Structures - Stack Implementation and Bracket Validation
# DEMONSTRATES: Implementing a custom stack class, performing standard stack operations 
#               (push, pop, peek, is_empty), reversing stack contents, and validating 
#               bracket sequences in strings using stack logic

class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.max_size = 10

    def push(self, new_data):
        print("Push the data " + str(new_data))
        if self.top == self.max_size - 1:
            raise OverflowError("Cannot insert into a full stack.")
        self.top += 1
        self.data.insert(self.top, new_data)
        print("Now the top index is " + str(self.top))

    def pop(self):
        if self.top == -1:
            raise IndexError("Cannot delete from an empty stack.")
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        print("Pop the data " + str(removed))
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek from an empty stack.")
        print("Peek the top")
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1

    def length(self):
        return self.top + 1

    def print_message(self):
        print(f"The stack size is {self.length()} The top element is {self.peek()}")

    def print_all(self):
        while not self.is_empty():
            print(self.pop())

    def reverse(self):
        temp_stack = []
        print("\nBefore reverse, the stack is ", self.data)
        while not self.is_empty():
            temp_stack.append(self.pop())
        while temp_stack:
            self.data.append(temp_stack.pop())
        print("\nThe reversed stack is ", self.data)

    def bracket_check(self, input_str):
        print("\nThe input string is: ", input_str)
        pairs = {')': '(', '}': '{', ']': '['}
        for character in input_str:
            if character in pairs.values():
                self.push(character)
            elif character in pairs:
                if self.is_empty() or self.peek() != pairs[character]:
                    return False
                self.pop()
        return self.is_empty()


def main():
    s3 = Stack()
    print("(abc) is valid? ", s3.bracket_check("(abc)"))
    s4 = Stack()
    print("d[sa]l(g) is valid? ", s4.bracket_check("d[sa]l(g)"))
    s5 = Stack()
    print("[a{b]c} is valid? ", s5.bracket_check("[a{b]c}"))


if __name__ == "__main__":
    main()
