class Queue:
    def __init__(self):
        self.elements = []
        self.max_queue = []
        self.min_queue = []

    def push(self, value):
        self.elements.append(value)
        if not self.max_queue or value > self.max_queue[0]:
            self.max_queue.insert(0, value)
        if not self.min_queue or value < self.min_queue[0]:
            self.min_queue.insert(0, value)

    def push_values(self, values):
        for value in values:
            self.push(value)

    def pop(self):
        popped = self.elements.pop(0)
        if popped == self.min_queue[0]:
            del self.min_queue[0]
        if popped == self.max_queue[0]:
            del self.max_queue[0]

    def top(self):
        if self.elements:
            return self.elements[0]

    def size(self):
        if self.elements:
            return len(self.elements)

    def isEmpty(self):
        return True if len(self.elements) == 0 else False

    def max(self):
        if self.max_queue:
            return self.max_queue[0]

    def min(self):
        if self.min_queue:
            return self.min_queue[0]

    def print(self):
        queue_elements_string = ""
        size = self.size()
        for idx in range(size):
            if idx != size - 1:
                queue_elements_string += str(self.elements[idx]) + ' - '
            else:
                queue_elements_string += str(self.elements[idx])

        print(f"The Queue Has: {queue_elements_string}")
