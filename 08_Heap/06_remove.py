def remove(self):
    if len(self.heap) == 0:
        return None
    removed = self.heap[0]   
    self.heap[0] = self.heap[-1]
    self.heap.pop()

    if len(self.heap) == 0:
        return removed
    index = 0

    while True:
        left = 2 * index + 1
        right = 2 * index + 2


        if left >= len(self.heap):
            break
        largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[left]:
            largest = right

         # Parent 已經比最大的 Child 大
        if self.heap[index] >= self.heap[largest]:
            break

        # Swap
        self.heap[index], self.heap[largest] = \
            self.heap[largest], self.heap[index]

        # 繼續往下
        index = largest

    return removed