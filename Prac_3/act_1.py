import numpy as np

class DSAStack:
    """Last In First Out."""

    def __init__(self, capacity=100):
        self.data = np.empty(capacity, dtype=object)
        self.capacity = capacity
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is full")
        self.data[self.count] = value
        self.count += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        self.count -= 1
        return self.data[self.count]

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.data[self.count - 1]


class DSAQueue:
    """First In First Out (shuffling)."""

    def __init__(self, capacity=100):
        self.data = np.empty(capacity, dtype=object)
        self.capacity = capacity
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        self.data[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        frontVal = self.data[0]
        for i in range(1, self.count):        # shuffle the rest down
            self.data[i - 1] = self.data[i]
        self.count -= 1
        return frontVal

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.data[0]


def display(adt):
    text = ""
    for i in range(adt.count):
        text = text + str(adt.data[i]) + " "
    return text


def menu(adt, addName, removeName, add, remove):
    choice = -1
    while choice != 0:
        print(f"\nContents: {display(adt)} ({adt.count}/{adt.capacity})")
        print(f"1. {addName}   2. {removeName}   3. Peek   4. isEmpty / isFull   0. Back")
        choice = int(input("Option: "))
        try:
            if choice == 1:
                add(input("Value: "))
            elif choice == 2:
                print(f"  Removed {remove()}")
            elif choice == 3:
                print(f"  Front/top is {adt.peek()}")
            elif choice == 4:
                print(f"  isEmpty = {adt.isEmpty()}, isFull = {adt.isFull()}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    option = -1
    while option != 0:
        print("\n1. DSAStack   2. DSAQueue   0. Quit")
        option = int(input("Option: "))

        if option == 1:
            stack = DSAStack(int(input("Capacity: ")))
            menu(stack, "Push", "Pop", stack.push, stack.pop)
        elif option == 2:
            queue = DSAQueue(int(input("Capacity: ")))
            menu(queue, "Enqueue", "Dequeue", queue.enqueue, queue.dequeue)
