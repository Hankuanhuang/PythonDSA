def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
          for j in range(n-1):
               if arr[j] < arr[j+1]:
                     arr[j+1], arr[j] = arr[j], arr[j+1] 
    return arr      


numbers = [5, 2, 8, 1]

print(bubble_sort(numbers))

# 你現在抓住這三個就夠：

# i → 控制跑幾輪
# j → 比較相鄰兩個
# 左 > 右 → swap

# so bubble sort means the biggest number will bubble up to the last, for example is acending