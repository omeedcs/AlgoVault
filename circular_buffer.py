class CircularBufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push_front(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.front = (self.front - 1) % self.capacity
        self.buffer[self.front] = item
        self.size += 1

    def push_back(self, item):
        if self.is_full():
            raise IndexError("Deque is full")
        self.buffer[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        item = self.buffer[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        self.rear = (self.rear - 1) % self.capacity
        item = self.buffer[self.rear]
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.buffer[self.front]

    def peek_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.buffer[(self.rear - 1) % self.capacity]

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "[]"
        items = []
        index = self.front
        for _ in range(self.size):
            items.append(str(self.buffer[index]))
            index = (index + 1) % self.capacity
        return "[" + ", ".join(items) + "]"