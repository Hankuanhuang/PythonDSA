# ============================================
# Python DSA - Array For Loop Cheat Sheet
# ============================================

# 1. 印出每個元素 (Read Only)
# for num in numbers:
#     print(num)

# # 用途：
# # 只看資料，不需要知道 Index。
# # 例如：印出全部、找總和。


# # --------------------------------------------

# # 2. 用 Index 走訪 (Most Common in DSA)
# for i in range(len(numbers)):
#     print(numbers[i])

# # 用途：
# # 需要知道 Index。
# # LeetCode 最常用。


# # --------------------------------------------

# # 3. 修改每個元素
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# # 用途：
# # 修改 Array 內容。


# # --------------------------------------------

# # 4. 累加 (Accumulator)
# total = 0

# for i in range(len(numbers)):
#     total += numbers[i]

# print(total)

# # 用途：
# # Sum
# # Average
# # Count


# # --------------------------------------------

# # 5. 找最大值 / 最小值
# largest = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i]

# print(largest)

# # 用途：
# # Max
# # Min


# # ============================================
# # 口訣
# # ============================================

# # 只讀資料
# for num in numbers

# # 要 Index
# for i in range(len(numbers))

# # 修改資料
# numbers[i] = ...

# # 累加
# total += numbers[i]

# # 找最大
# if numbers[i] > largest:
#     largest = numbers[i]



# Index:   0   1   2   3
# Value:  10  20  30  40
#  Array = 用 Index 存取資料，速度非常快（O(1)）。


# numbers = [10, 20, 30, 40]

# print(numbers[0])
# print(numbers[3])

#modify ------------------------------------
# numbers[1] = 99
# print(numbers[1])


# #lenght of the array ------------------------------------
# print(len(numbers))

# #Traversal ------------------------------------
# for num in numbers:
#     print(num)

#Using Index to Traveral ------------------------------------
# for i in range(len(numbers)):
#     print(i, numbers[i])

# #Question 1--------------------------
# number = [11, 22, 33, 44, 55]

# print(list[0])
# print(list[4])

# #Question 2--------------------------
# num = [10, 20, 30, 40, 50]

# num[2] = 99

# for i in range(len(num)):
#     print(num[i])

# ##wrong
# for i in range(num):
#     print(num[i])
#     num[i] += 1


#Question 3-------------------------
# number = [5, 10, 15, 20, 25]
# total = 0
# for i in range(len(number)):
#     total = total + number[i]

# print(total)


# #Question 4-------------------------
# number = [3, 6, 9, 12]
# largest = number[0]

# for i in range(len(number)):
#     if  number[i] > largest:
#         largest = number[i]
# print(largest)   

#Question 5-------------------------
number = [2, 4, 6, 8, 10]

for i in range(len(number)):
    number[i] = number[i] * 2

print(number)
