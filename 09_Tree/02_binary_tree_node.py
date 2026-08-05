# Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
#print the example
print(root.data)
print(root.left)
print(root.right)

#create a left Node
leftNode = Node(5)
# connect the root and left Node
root.left = leftNode
print("left root is", root.left.data)



# connect the root and right Node
rightNode = Node(20)
root.right = rightNode
print("right root is", root.right.data)

# possible paths in Tree
root.left.left
root.left.right
root.right.left
root.right.right
