# the idea of anything with water flow is to see okay,
# how can my water even flow on this grid? 
# whenever you see a problem where there might be constraints,
# and things need to meet in the middle, then maybe a good approach
# would be to either do a BFS or DFS starting from nodes that 
# are permissable, and go to the edge of their constraint based 
# on what is going on in the grid.

# DFS -> pacificAtlantic
def pacificAtlantic(self, heights):
    # heights is basically the grid
    pacific = set()
    atlantic = set()
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    def dfs(row, col, oceanSet, prevHeight):
        # really, the most complex part here was the base case. 
        # and the intuition of using sets. 
        # in the base case, we just literally want to see if the current
        # node that we're traversing is less than the previous height, which 
        # means that the direction that we just moved in is at a lower 
        # altitude than the direction that we were previously at, which means
        # in an IRL scenario, water can naturally flow.
        if (row, col) in oceanSet or row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]) or heights[row][col] < prevHeight:
            return
    
        oceanSet.add((row, col))
        for dx, dy in DIRECTIONS:
            self.dfs(row + dx, col + dy, oceanSet, heights[row][col])
    
    # we're setting up our search from different nodes.
    # different start points increase our odds of hitting everything
    # since there are different heights for flow.
    for col in range(len(heights[0])):
        # this part is a bit weird, because we are trying to make
        # our starting points based on the borders.
        
        # TOP ROW / TOP BORDER IS 0 IDX for ROW, WITH ITERATIVE COLUMN.
        self.dfs(0, col, pacific, heights[0][col])
        # BOTTOM ROW / BOTTOM BORDER IS LAST IDX OF ROW, WITH ITERATE COLUMN.
        self.dfs(len(heights) - 1, col, heights[len(heights) - 1][col])
    
    # 
    for row in range(len(heights)):
        self.dfs(row, 0, atlantic, heights[row][0])
        self.dfs(row, len(heights[0]) - 1, atlantic, heights[row][len(heights[0]) - 1]) 
    
    # now after you have two sets, finding the intersection between them is pretty trivial.
    # in set theory, an intersection means finding the common elements between the sets.
    # that means we know that water successfully flowed into both cells.
    return list(pacific.intersection(atlantic))


