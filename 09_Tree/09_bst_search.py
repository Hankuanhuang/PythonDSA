class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search(self,data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False
                
