import numpy as np

class DSAQueue:
    '''
    First in first out
    '''
    def __init__(self, capacity = 100):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.data = np.empty(capacity, dtype=object)
        self.count = 0
        self.capacity = capacity

    def isEmpty(self):
        return self.count == 0
        
    def isFull(self):
        return self.count == len(self.data)

class ShufflingQueue(DSAQueue):
    def enqueue(self,value):
        if self.isFull():
            raise Exception('The array is full')
        self.data[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('The array is empty')
        front_val = self.data[0]
        for i in range(1, self.count):
            self.data[i-1] = self.data[i]
        self.count -= 1
        return front_val

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[0]

class CircularQueue(DSAQueue):
    def __init__(self, capacity=100):
        super().__init__(capacity)
        self.front = 0
        self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            raise Exception('The array is full')
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('The array is empty')
        front_val = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return front_val

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[self.front]
