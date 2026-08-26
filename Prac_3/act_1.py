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

def displayStack(stack):
    """Return the stack contents (bottom -> top)"""
    if stack.isEmpty():
        return "(empty)"
    text = ""
    for i in range(stack.count):
        text = text + str(stack.data[i]) + " "
    return text.strip() + "  <- top"


def displayQueue(queue):
    """Return the queue contents (front -> rear)"""
    if queue.isEmpty():
        return "(empty)"
    text = ""
    for i in range(queue.count):
        text = text + str(queue.data[i]) + " "
    return "front -> " + text.strip() + " <- rear"


def readInt(prompt, low, high):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("That is not a whole number. Please try again.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


def readValue(prompt):
    """Read a non-empty value. Numbers are stored as numbers, the rest as text."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("The value cannot be empty. Please try again.")
            continue
        try:
            return int(text)
        except ValueError:
            pass
        try:
            return float(text)
        except ValueError:
            pass
        return text


def stackMenu():
    """Interactive menu for the stack."""
    capacity = readInt("Stack capacity (1-100): ", 1, 100)
    stack = DSAStack(capacity)

    while True:
        print("\nDSAStack (LIFO)")
        print(f"Contents: {displayStack(stack)}")
        print(f"Size    : {stack.count}/{capacity}")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty / isFull")
        print("0. Back to the main menu")
        choice = readInt("Choose an option: ", 0, 4)

        if choice == 0:
            break

        try:
            if choice == 1:
                value = readValue("Value to push: ")
                stack.push(value)
                print(f"  Pushed {value}.")
            elif choice == 2:
                print(f"  Popped {stack.pop()}.")
            elif choice == 3:
                print(f"  Top of the stack is {stack.peek()}.")
            elif choice == 4:
                print(f"  isEmpty = {stack.isEmpty()}, isFull = {stack.isFull()}")
        except Exception as e:
            print(f"  Error: {e}")


def queueMenu():
    """Interactive menu for the queue."""
    capacity = readInt("Queue capacity (1-100): ", 1, 100)
    queue = DSAQueue(capacity)

    while True:
        print("\nDSAQueue (FIFO)")
        print(f"Contents: {displayQueue(queue)}")
        print(f"Size    : {queue.count}/{capacity}")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. isEmpty / isFull")
        print("0. Back to the main menu")
        choice = readInt("Choose an option: ", 0, 4)

        if choice == 0:
            break

        try:
            if choice == 1:
                value = readValue("Value to enqueue: ")
                queue.enqueue(value)
                print(f"  Enqueued {value}.")
            elif choice == 2:
                print(f"  Dequeued {queue.dequeue()}.")
            elif choice == 3:
                print(f"  Front of the queue is {queue.peek()}.")
            elif choice == 4:
                print(f"  isEmpty = {queue.isEmpty()}, isFull = {queue.isFull()}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    print("Activity 1: Stack and Queue")

    while True:
        print("\nMain menu")
        print("1. Stack  (Last In First Out)")
        print("2. Queue  (First In First Out)")
        print("0. Quit")
        option = readInt("Choose an option: ", 0, 2)

        if option == 1:
            stackMenu()
        elif option == 2:
            queueMenu()
        else:
            print("Bye!")
            break
