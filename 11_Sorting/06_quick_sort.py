def quick_sort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Last value as pivot
    pivot = arr[-1]

    left = []
    right = []

    # Don't include pivot
    for value in arr[:-1]:

        if value < pivot:
            left.append(value)
        else:
            right.append(value)

    # Recursion
    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [7, 3, 9, 2, 5]

print(quick_sort(numbers))


# Quick Sort = Pivot → 小的 left → 大的 right → Recursion

# 平均時間複雜度：O(n log n)
# Worst case：O(n²)