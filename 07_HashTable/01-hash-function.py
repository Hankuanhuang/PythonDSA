def hash(key):
    total = 0

    for char in key:
        total += ord(char)

    return total % 10


print(hash("cat"))
print(hash("dog"))
print(hash("apple"))

# ord() 作用：把一個字元（character）變成 ASCII / Unicode 數字。


