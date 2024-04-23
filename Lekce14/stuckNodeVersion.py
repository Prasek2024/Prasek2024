class Stack:
    def __init__(self):
        self.first = None
        self.size = 0

    def push(self, i):
        n = self.Node(i)
        curr_first = self.first
        self.first = n
        n.next = curr_first
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("Stack is empty, cannot pop element")
        value = self.first.value
        self.first = self.first.next
        self.size -= 1
        return value

    def top(self):
        if self.size == 0:
            raise ValueError("Stack is empty, cannot return")
        return self.first.value

    def get_size(self):
        return self.size

    def __str__(self):
        builder = []
        curr = self.first
        for i in range(self.size):
            builder.append(str(curr.value))
            curr = curr.next
        return ' '.join(builder)

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

# Example usage:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack)  # Output: 2 1
# print(stack.pop())  # Output: 2
# print(stack.top())  # Output: 1
# print(stack.get_size())  # Output: 1
