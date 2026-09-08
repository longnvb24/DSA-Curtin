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

    def insert(self, key, value):
        self.root = self.insertRec(key, value, self.root)

    def insertRec(self, key, value, cur):
        updateNode = cur

        if cur == None: # base case: found insertion point
            newNode = DSATreeNode(key, value)
            updateNode = newNode

        elif key == cur.getKey(): # key already in the tree -> abort
            raise ValueError(f"Key {key} already exists")

        elif key < cur.getKey(): # recurse left
            cur.setLeft(self.insertRec(key, value, cur.getLeft()))

        else:                    # recurse right
            cur.setRight(self.insertRec(key, value, cur.getRight()))

        return updateNode

    def min(self):
        if self.root == None:
            raise ValueError("Tree is empty")
        return self.minRec(self.root)

    def minRec(self, cur):
        if cur.getLeft() != None:          # not base case
            minKey = self.minRec(cur.getLeft())   # recursive call
        else:
            minKey = cur.getKey()
        return minKey

    def max(self):
        if self.root == None:
            raise ValueError("Tree is empty")
        return self.maxRec(self.root)

    def maxRec(self, cur):
        if cur.getRight() != None:         # not base case
            maxKey = self.maxRec(cur.getRight())  # recursive call
        else:
            maxKey = cur.getKey()
        return maxKey

    def height(self):
        return self.heightRec(self.root)

    def heightRec(self, cur):
        if cur == None:                    # base case - no more along this branch
            htSoFar = -1
        else:
            leftHt = self.heightRec(cur.getLeft())    # calc left height
            rightHt = self.heightRec(cur.getRight())  # calc right height

            if leftHt > rightHt:           # get highest of left vs right branches
                htSoFar = leftHt + 1
            else:
                htSoFar = rightHt + 1
        return htSoFar

if __name__ == "__main__":
    bst = DSABinarySearchTree()
    bst.insert(10, "Ten")
    bst.insert(5, "Five")
    bst.insert(15, "Fifteen")

    print(bst.find(10))  # Output: Ten
    print(bst.find(5))   # Output: Five
    print(bst.find(15))  # Output: Fifteen

    print(bst.min())  # Output: 5
    print(bst.max())  # Output: 15
    print(bst.height())  # Output: 1
    try:
        print(bst.find(20))  # This will raise an exception
    except ValueError as e:
        print(e)  # Output: Key 20 not found