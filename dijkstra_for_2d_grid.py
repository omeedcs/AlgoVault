import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid)
        start = (0, 0)
        end_goal = (rows - 1, cols - 1)
        minHeap = []
        visited = set()
        # < cost, (x, y) >
        minHeap.append((grid[0][0], (0, 0)))
        while minHeap:
            cost, (row, col) = heapq.heappop(minHeap)

            # min heap maintains minimum cost.
            if (row, col) == end_goal:
                return cost
            
            for direction in DIRECTIONS:
                x, y = direction
                new_r = row + x
                new_c = col + y
                # wraparound? nope don't need to accomodate.
                if (new_r, new_c) in visited or new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]):
                    continue
                else: 
                    # the new cost is either the current cost, or the amount it takes 
                    # for us to get to the new position in the grid
                    new_cost = max(cost, grid[new_r][new_c])
                    heapq.heappush(minHeap, (new_cost, (new_r, new_c)))
                    visited.add((new_r, new_c))
        
