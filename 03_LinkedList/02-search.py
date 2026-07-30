#Big O = O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Create Linked list
first = Node(10)
second = Node(20)
third = Node(30)

#Linke the Node together
first.next = second
second.next = third

#create target
target = 20

found = False
current = first

while current is not None:
    if current.data == target:
         found = True
         print("Found")
         break
    current = current.next

if not found:
        print("Not found")
    