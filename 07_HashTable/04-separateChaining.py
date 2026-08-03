class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


table = [None] * 10 ## create a empty array,Hash Table 本體（Bucket Array）。

def hash(key):

    return 2
    # total = 0

    # for char in key:
    #     total += ord(char)

    # return total % 10

def insert(key, value):
    index = hash(key)

    newNode = Node(key, value)

    if table[index] is None:
        table[index] = newNode
    else:
        current = table[index]
        while current.next is not None:
            current = current.next
        current.next = newNode


insert("cat", 100)
insert("dog", 80)
insert("apple", 60)

current = table[2]

while current is not None:
    print(current.key, current.value)
    current = current.next