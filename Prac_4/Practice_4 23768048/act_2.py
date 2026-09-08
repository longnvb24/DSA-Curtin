# reference: Practical_3/act_1.py
from Prac_5.act_1 import DSALinkedList

class DSAStack:
    """Last In First Out."""

    def __init__(self):
        self.list = DSALinkedList()

    def isEmpty(self):
        return self.list.isEmpty()

    def push(self, value):
        return self.list.insertLast(value)

    def pop(self):
        return self.list.removeLast()

    def top(self):
        return self.list.peekLast()


class DSAQueue:
    """First In First Out (shuffling queue)."""

    def __init__(self):
        self.list = DSALinkedList()

    def isEmpty(self):
        return self.list.isEmpty()

    def enqueue(self, value):
        return self.list.insertLast(value)

    def dequeue(self):
        return self.list.removeFirst()

    def peek(self):
        return self.list.peekFirst()

def display(adt):
    """Walk the linked list from head to tail."""
    text = ""
    currNd = adt.list.head
    while currNd is not None:
        text = text + str(currNd.data) + " "
        currNd = currNd.next
    return text


def getMenuChoice():
    """Keep asking until the choice is a number between 0 and 4."""
    choice = -1
    valid = False
    while not valid:
        try:
            choice = int(input("Option: "))
            if 0 <= choice <= 4:
                valid = True
            else:
                print("  Choice must be between 0 and 4.")
        except ValueError:
            print("  Please enter a number.")
    return choice


def stackMenu():
    stack = DSAStack()
    choice = -1
    while choice != 0:
        print(f"\nDSAStack: {display(stack)} <- top")
        print("1. Push   2. Pop   3. Top   4. isEmpty   0. Back")
        choice = getMenuChoice()
        try:
            if choice == 1:
                stack.push(input("Value: "))
            elif choice == 2:
                print(f"  Popped {stack.pop()}")
            elif choice == 3:
                print(f"  Top is {stack.top()}")
            elif choice == 4:
                print(f"  isEmpty = {stack.isEmpty()}")
        except Exception as e:
            print(f"  Error: {e}")


def queueMenu():
    queue = DSAQueue()
    choice = -1
    while choice != 0:
        print(f"\nDSAQueue: front -> {display(queue)}<- rear")
        print("1. Enqueue   2. Dequeue   3. Peek   4. isEmpty   0. Back")
        choice = getMenuChoice()
        try:
            if choice == 1:
                queue.enqueue(input("Value: "))
            elif choice == 2:
                print(f"  Dequeued {queue.dequeue()}")
            elif choice == 3:
                print(f"  Front is {queue.peek()}")
            elif choice == 4:
                print(f"  isEmpty = {queue.isEmpty()}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    option = -1
    while option != 0:
        print("\n1. DSAStack   2. DSAQueue   0. Quit")
        option = getMenuChoice()

        if option == 1:
            stackMenu()
        elif option == 2:
            queueMenu()
