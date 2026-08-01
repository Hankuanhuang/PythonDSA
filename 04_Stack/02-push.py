## linked list push

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def push(data):
    global head

    newNode = Node(data) # newNode -> 40 -> none 生一個（建立）
    newNode.next = head # 接舊頭（next=head）
    head = newNode # 換新頭（head=newNode）

push(10)
push(20)
push(30)
push(40)

current = head

while current is not None:
    print(current.data)
    current = current.next
