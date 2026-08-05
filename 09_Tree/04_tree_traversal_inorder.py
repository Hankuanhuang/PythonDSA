def inorder(node):

    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

inorder(root)

# Print a BST in sorted order
    # use Inorder Traversal