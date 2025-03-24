
# NOTE: 
# you could technically say that this is a 
# CONNECTED COMPONENTS problem.

def numIslands(self, grid):
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def dfs(grid, row, col):
        # base case.
        # this is simply a bound check.
        if row < 0 and col < 0 and row >= len(grid) and col >= len(grid[0]):
            return

        # are we still on land?
        if grid[row][col] != 1:
            return
        
        # mark as visited. we are flooding the islands we visit.
        grid[row][col] = "0"

        # run a DFS in all 4 directions
        for d in DIRECTIONS:
            x, y = d
            self.dfs(grid, row + x, col + y)
        
        # once we mark visited., we dont care about coming back
        # there is no backtracking here.


    if not grid:
        return 0

    numIslands = 0
    for row in range(len(grid)): 
        for col in range(len(grid[0])): 
            if grid[row][col] == "1":
                # we hit an instance of an island.
                # if we're trying to find the entire island,
                # the best algorithm here is an dfs.
                dfs(grid, row, col)
                numIslands += 1
    return numIslands

   