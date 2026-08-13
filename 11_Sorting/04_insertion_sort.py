def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key

    return arr

numbers = [5, 2, 8, 1]

print(insertion_sort(numbers))

# i → 現在處理哪個位置
# key → 手上拿著、準備插入的數字
# j → 往左找位置

# Insertion Sort = O(n²)（一般 / worst case）。