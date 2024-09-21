import collections

def findTreasure(self, matrix):
    queue = collections.deque()
    while queue:
        for i in range(len(queue)):
            row, col = queue.popleft()
            # distance from treasure.
            grid[row][col] = dist 


