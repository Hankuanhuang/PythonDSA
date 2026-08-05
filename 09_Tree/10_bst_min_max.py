
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def finMin(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def finMax(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data