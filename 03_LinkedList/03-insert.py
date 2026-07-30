#Big O = O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Create Linked list
first = Node(10)
second = Node(20)
third = Node(30)
newNode = Node(40)

#Linke the Node together
first.next = second
second.next = third


current = first

while current.next is not None: 
    current = current.next
    
current.next = newNode