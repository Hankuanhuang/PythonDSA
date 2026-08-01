class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def push(data):
    global head

    newNode = Node(data)
    newNode.next = head
    head = newNode

def pop():
    global head

    if head is None:
        return
    head = head.next


push(10)
push(20)
push(30)

current = head

while current is not None:
    print(current.data)
    current = current.next