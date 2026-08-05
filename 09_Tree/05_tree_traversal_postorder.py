def postorder(node):

    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)
    
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

postorder(root)