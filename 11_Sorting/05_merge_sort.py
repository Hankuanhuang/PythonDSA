def merge_sort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Cut in half
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # Recursion
    left = merge_sort(left)
    right = merge_sort(right)

    # Index
    i = 0  # left
    j = 0  # right
    k = 0  # arr

    # Compare left and right
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Left has remaining values
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Right has remaining values
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


numbers = [7, 3, 6, 2]

print(merge_sort(numbers))

# 切半 → recursion → 左右比較 → 小的放回去 → 剩下的全部放回去
# 而且 Merge Sort 的時間複雜度是 O(n log n)，比前面三個 O(n²) 更有效率。✅