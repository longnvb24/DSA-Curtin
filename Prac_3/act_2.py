import numpy as np

class DSAQueue:
    def __init__(self, capacity=100):
        self.data = np.empty(capacity, dtype=object)
        self.capacity = capacity
        self.count = 0
        self.front = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


class ShufflingQueue(DSAQueue):
    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        self.data[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        frontVal = self.data[0]
        for i in range(1, self.count):
            self.data[i - 1] = self.data[i]
        self.count -= 1
        self.data[self.count] = None
        return frontVal

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[0]


class CircularQueue(DSAQueue):
    def __init__(self, capacity=100):
        super().__init__(capacity)
        self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        frontVal = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return frontVal

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[self.front]

def display(queue):
    text = ""
    for i in range(queue.capacity):
        if queue.data[i] is not None:
            text = text + str(queue.data[i]) + " "
    return text

def displayArray(queue):
    """The raw slots, to show how the two queues differ."""
    text = ""
    for i in range(queue.capacity):
        text = text + f"[{i}]{queue.data[i]} "
    return text

def menu(queue):
    choice = -1
    while choice != 0:
        print(f"\nContents: {display(queue)} ({queue.count}/{queue.capacity})")
        print("1. Enqueue   2. Dequeue   3. Peek   4. isEmpty / isFull   5. Raw array   0. Back")
        choice = int(input("Option: "))
        try:
            if choice == 1:
                queue.enqueue(input("Value: "))
            elif choice == 2:
                print(f"  Dequeued {queue.dequeue()}")
            elif choice == 3:
                print(f"  Front is {queue.peek()}")
            elif choice == 4:
                print(f"  isEmpty = {queue.isEmpty()}, isFull = {queue.isFull()}")
            elif choice == 5:
                print(f"  {displayArray(queue)}")
        except Exception as e:
            print(f"  Error: {e}")

if __name__ == "__main__":
    option = -1
    while option != 0:
        print("\n1. ShufflingQueue   2. CircularQueue   0. Quit")
        option = int(input("Option: "))

        if option == 1:
            menu(ShufflingQueue(int(input("Capacity: "))))
        elif option == 2:
            menu(CircularQueue(int(input("Capacity: "))))
