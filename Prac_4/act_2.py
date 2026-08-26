from act_1 import DSALinkedList

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

    def top(self):
        return self.list.peekFirst()

q = DSAQueue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
assert q.dequeue() == "A"
assert q.dequeue() == "B"
assert q.dequeue() == "C"
assert q.isEmpty() == True
print("PASS: DSAQueue is FIFO")

s = DSAStack()
s.push("A")
s.push("B")
assert s.pop() == "B"
assert s.pop() == "A"
assert s.isEmpty() == True
print("PASS: DSAStack is LIFO")