import numpy as np

class DSAStack:
    """Last In First Out."""

    def __init__(self, capacity=100):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.data = np.empty(capacity, dtype=object)
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.data)

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is full")
        self.data[self.count] = value
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        top_val = self.data[self.count - 1]
        self.data[self.count - 1] = None
        self.count -= 1
        return top_val

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.data[self.count - 1]


class DSAQueue:
    """First In First Out (shuffling queue)."""

    def __init__(self, capacity=100):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.data = np.empty(capacity, dtype=object)
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.data)

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        self.data[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        front_val = self.data[0]
        for i in range(1, self.count):
            self.data[i - 1] = self.data[i]
        self.count -= 1
        self.data[self.count] = None
        return front_val

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[0]
