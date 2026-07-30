#Array 用 Index 找下一個元素；Linked List 用 next 找下一個 Node。
#Big O = O(n)

#Create Class
class Node:
    def __init__(self, data): #constructor
        self.data = data # store value
        self.next = None # next Node(default is None)


#create objects
first = Node(10)
second = Node(20)
third = Node(30)

#Link the Nodes together
first.next = second
second.next = third

#current from the first one
current = first

#while Node still avaliable and keep going
while current is not None:
    print(current.data)
    current = current.next #move to next Node