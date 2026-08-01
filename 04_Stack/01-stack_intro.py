class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

#Push 10
newNode = Node(10)
newNode.next = head
head = newNode

#Push 20
newNode = Node(20)
newNode.next = head
head = newNode

#Push 30
newNode = Node(30)
newNode.next = head
head = newNode

current = head

while current is not None:
    print(current.data)
    current = current.next
