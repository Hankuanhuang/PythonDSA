# 目標：當條件成立時，一直重複。

count = 1

while count <= 5:
    print(count)
    count += 1

password = ""
while password != "1234":
    password = input("Enter password: ")

    print("Access Granted")

count = 5
while count > 0:
    print(count)
    count -= 1
print("Go")


count = 10
while count > 0:
    print(count)
    count -= 1



correct = ""

while correct != "0":
    correct = input("Enter password: ")

print("Finished")

