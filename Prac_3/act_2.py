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


def displayQueue(queue):
    """Return the queue contents as text (front -> rear)"""
    if queue.isEmpty():
        return "(empty)"
    start = getattr(queue, "front", 0)
    text = ""
    for i in range(queue.count):
        text = text + str(queue.data[(start + i) % queue.capacity]) + " "
    return "front -> " + text.strip() + " <- rear"


def displayArray(queue):
    """Return the raw array slots"""
    text = ""
    for i in range(queue.capacity):
        text = text + f"[{i}]{queue.data[i]} "
    return text.strip()


def readInt(prompt, low, high):
    value = None
    while value is None:
        text = input(prompt).strip()
        try:
            number = int(text)
            if low <= number <= high:
                value = number
            else:
                print(f"  Please enter a number between {low} and {high}.")
        except ValueError:
            print("  That is not a whole number. Please try again.")
    return value


def readValue(prompt):
    value = None
    while value is None:
        text = input(prompt).strip()
        if text == "":
            print("  The value cannot be empty. Please try again.")
        else:
            try:
                value = int(text)
            except ValueError:
                try:
                    value = float(text)
                except ValueError:
                    value = text
    return value


def queueMenu(queueClass):
    """Interactive menu for one kind of queue."""
    capacity = readInt("Queue capacity (1-100): ", 1, 100)
    queue = queueClass(capacity)

    choice = -1
    while choice != 0:
        print(f"\n{queueClass.__name__}")
        print(f"Contents: {displayQueue(queue)}")
        print(f"Size    : {queue.count}/{capacity}")
        if isinstance(queue, CircularQueue):
            print(f"Indexes : front = {queue.front}, rear = {queue.rear}")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. isEmpty / isFull")
        print("5. Show the raw array")
        print("0. Back to the main menu")
        choice = readInt("Choose an option: ", 0, 5)

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
            elif choice == 5:
                print(f"  {displayArray(queue)}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    print("Shuffling and Circular Queue")

    option = -1
    while option != 0:
        print("\nMain menu")
        print("1. ShufflingQueue")
        print("2. CircularQueue")
        print("0. Quit")
        option = readInt("Choose an option: ", 0, 2)

        if option == 1:
            queueMenu(ShufflingQueue)
        elif option == 2:
            queueMenu(CircularQueue)
        else:
            print("Bye!")
