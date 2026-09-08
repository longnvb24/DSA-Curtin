class DSATreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return f"Key: {self.key} Value: {self.value}"

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.leftChild

    def setLeft(self, newLeft):
        self.leftChild = newLeft

    def getRight(self):
        return self.rightChild

    def setRight(self, newRight):
        self.rightChild = newRight

class DSABinarySearchTree:
    def __init__(self):
        self.root = None

    # wrapper methods, will call recursive implementations

    def find(self, key):
        return self.findRec(key, self.root)

    def findRec(self, key, cur):
        value = None

        if cur == None: # Base case: not found
            raise ValueError(f"Key {key} not found")
        
        elif key == cur.key: # Base case: found
            value = cur.value

        elif key < cur.key: # Go left (recursive)
            value = self.findRec(key, cur.leftChild)

        else: # Go right(recursive)
            value = self.findRec(key, cur.rightChild)
        return value