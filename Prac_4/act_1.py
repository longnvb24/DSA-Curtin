class DSAListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            newNd.next = self.head
            self.head.prev = newNd
            self.head = newNd

    def insertLast(self,value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            newNd.prev = self.tail
            self.tail.next = newNd
            self.tail = newNd

    def insertBefore(self,target, value):
        currNd = self.tail
        while currNd is not None and currNd.data != target:
            currNd = currNd.prev
        if currNd is None:
            raise ValueError("Target is not found")

        if currNd is self.head:
            self.insertFirst(value)
            return

        newNd = DSAListNode(value)
        newNd.next = currNd
        newNd.prev = currNd.prev
        currNd.prev.next = newNd
        currNd.prev = newNd

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        nodeValue = self.head.data
        if self.head.next is None: # List has only 1 element
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return nodeValue

    def removeLast(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        nodeValue = self.tail.data
        if self.tail.prev is None: # list only have 1 element
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return nodeValue

    def removeValue(self,value):
        currNd = self.head
        while currNd is not None and currNd.data != value:
            currNd = currNd.next
        if currNd is None:
            raise ValueError("Value is not found")

        if currNd is self.head:
            return self.removeFirst()
        if currNd is self.tail:
            return self.removeLast()

        currNd.prev.next = currNd.next
        currNd.next.prev = currNd.prev
        return currNd.data

    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        else:
            return self.head.data

    def peekLast(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        else:
            return self.tail.data
        
    def find(self, value):
        currNd = self.head
        while currNd is not None:
            if currNd.data == value:
                return True
            currNd = currNd.next
        return False
