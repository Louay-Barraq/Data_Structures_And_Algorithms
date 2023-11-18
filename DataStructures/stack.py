class Stack:
    def __init__(self):
        self.elements = []
        self.min_stack = []
        self.max_stack = []

    def push(self, value):
        self.elements.append(value)
        if not self.max_stack or value > self.max_stack[-1]:
            self.max_stack.append(value)
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)

    def push_values(self, values):
        for value in values:
            self.push(value=value)

    def pop(self):
        popped = self.elements.pop()
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        if self.elements:
            return self.elements[-1]

    def size(self):
        if self.elements:
            return len(self.elements)

    def isEmpty(self):
        return True if len(self.elements) == 0 else False

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]

    def print(self):
        stack_elements_string = ""
        for idx in range(len(self.elements) - 1, -1, -1):
            if idx != 0:
                stack_elements_string += str(self.elements[idx]) + " - "
            else:
                stack_elements_string += str(self.elements[idx])

        print(f"The Stack has: {stack_elements_string}")