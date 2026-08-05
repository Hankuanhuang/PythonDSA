class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def remove(self, node, data):
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._remove(node.left, data)

        elif data > node.data:
            node.right = self._remove(node.right, data)

        else:
            if node.left is Nne and node.right is None:
                return None



        


                 