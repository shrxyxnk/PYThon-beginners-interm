#Here's a simple example of how you can implement a stack in Python:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.stack)

print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after pop:", stack.stack)
print("Is stack empty?", stack.is_empty())
