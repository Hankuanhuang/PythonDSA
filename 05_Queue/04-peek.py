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
    if head is None: # Queue is not empty
        head = newNode
        tail = newNode
        return
    tail.next = newNode # queue have value in there
    tail = newNode

def dequeue():
    global head
    global tail

    if head is None:
        return
    head = head.next
    if head is None:
        tail = None

def peek():
    global head
    ##global tail ## don't need this at all

    if head is None:
        return 
    return head.data
    
    
    



enqueue(100)
enqueue(200)
enqueue(300)

current = head

while current is not None:
    print(current.data)
    current = current.next