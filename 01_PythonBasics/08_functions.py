# def say_hello():
#     print("Hello!")

# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()

#-------------------------------------
#加入參數（Parameter）
# def greet(name):
#     print("Hello", name)

# greet("Ken")
# greet("Sina")

#-------------------------------------
# # 兩個參數
# def add(a, b):
#     print(a + b)

# add(5, 9)

#-------------------------------------
#回傳值（Return）
# def add(a, b):
#     return a + b

# result = add(3, 2) #return back here.... the reuslt will received the return value
# print(result)

# print() = 給人看
# return = 給程式用

#-------------------------------------
#Challenge 1
#double number function

def double(num):
    return num *2

result = double(6)
print(result)

#-------------------------------------
#Challenge 2
def maxNum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print("they are same size")
        return ("same")

result = maxNum(8, 8)
print(result)
#-------------------------------------
#Challenge 3 

def score(num):
    if num >= 50:
        return "Pass"
    else:
        return "False"

print(score(79))
print(score(30))

#-------------------------------------
#Challenge 4

def square(num):
    return num*num

print(square(6))
#-------------------------------------
#Challenge 5

def is_positive(num):
    if num > 0:
        return True
    else:
        return False
    
print(is_positive(-10))
print(is_positive(5))