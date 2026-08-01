class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
tail = None


def enqueue(data):
    global head
    global tail

    newNode = Node(data)
    if head is None: # if the queue is empty 
        head = newNode
        tail = newNode
        return
    tail.next = newNode # queue have value in there
    tail = newNode
