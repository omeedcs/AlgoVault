class Heap:
    def __init__(self):
        self.heap = [0] # do this so values are 1-indexed.

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        
        # perform percolation.
        while self.heap[i] < self.heap[i] // 2:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2] # remember i // 2 gets parent.
            self.heap[i // 2] = temp
            i = i // 2
        