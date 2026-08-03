class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):

        self.heap.append(value)

        print("Append:", self.heap)

        index = len(self.heap) - 1

        while index > 0:

            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:

                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

                print("Swap :", self.heap)

                index = parent
            else:
                break

heap = MaxHeap()

numbers = [100, 90, 80, 70, 60, 50, 95, 120]

for num in numbers:
    heap.insert(num)
    print(heap.heap)