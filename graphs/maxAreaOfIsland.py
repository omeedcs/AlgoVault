def maxAreaOfIsland(self, grid):
    maximum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1: # reached land.
                area = self.dfs(grid, row, col)
                maximum = max(maximum, area)
    return maximum


def dfs(self, grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
        return 0
    
    # first, flood the current position on the island.
    grid[row][col] = 0
    # keep track of a count, accounting for the current
    # square that we are on.

    # set count to 1. increment count consisently with the 
    # recursive calls until we hit the base case.
    count = 1 
    for d in DIRECTIONS: 
        x, y = d
        count += self.dfs(grid, row + x, col + y)
    return count




