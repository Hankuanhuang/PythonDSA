# Collision
#
# Two different keys produce the same index.
#
# Problem:
# The second value overwrites the first value.
#
# Solution:
# 1. Separate Chaining
# 2. Linear Probing


table = [None] * 10


def hash(key):
    total = 0

    for char in key:
        total += ord(char)

    return total % 10


def insert(key, value):
    index = hash(key)

    print(f"{key} -> index {index}")

    table[index] = (key, value)


insert("cat", 100)
insert("tac", 200)      # 可以換一個碰撞的字串

print(table)