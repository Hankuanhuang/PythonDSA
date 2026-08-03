table = [None] * 10


def hash(key):
    total = 0

    for char in key:
        total += ord(char)

    return total % 10


def insert(key, value):
    index = hash(key)
    table[index] = (key, value)

insert("cat", 100)
insert("dog", 80)

print(table)