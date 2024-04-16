class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
            return True
        return False

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack.clear()

    def count(self):
        return len(self.stack)