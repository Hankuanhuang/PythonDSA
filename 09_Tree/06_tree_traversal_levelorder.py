from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):

    queue = deque()

    queue.append(root)

    while queue:

        print("--------------------")
        print("Queue Before:", [node.data for node in queue])

        node = queue.popleft()

        print("Current Node:", node.data)

        if node.left:
            print("Append Left :", node.left.data)
            queue.append(node.left)

        if node.right:
            print("Append Right:", node.right.data)
            queue.append(node.right)

        print("Queue After :", [node.data for node in queue])


root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

level_order(root)


"--------------------------------------------"

# Queue = 等待工作的 Node。
# node = 從 Queue 拿出來，目前正在工作的 Node。