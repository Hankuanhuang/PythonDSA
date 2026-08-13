def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [5, 2, 8, 1]

print(selection_sort(numbers))


# i → 要放最小值的位置
# j → 往後找更小的
# min_index → 記住目前最小值的 index

# 而且 Selection Sort = O(n²)，跟 Bubble Sort 一樣。✅