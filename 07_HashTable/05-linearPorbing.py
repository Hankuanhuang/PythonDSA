table = [None] * 10

def hash(key):
    return 2

def insert(key, value):
    index = hash(key)

    if table[index] is None:
        table[index] = (key, value)
    else:
        while table[index] is not None:
            index += 1

        table[index] = (key, value)

insert("cat", 100)
insert("dog", 80)
insert("apple", 60)

print(table)