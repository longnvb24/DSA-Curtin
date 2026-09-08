class DSATreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return ("Key: " + str(self.key) + " Value: "+ str(self.value))
    
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
# class DSABinarySearchTree:

if __name__ == "__main__":
    print("Testing node creation")
    myNode = DSATreeNode(1, "one")
    print(myNode)