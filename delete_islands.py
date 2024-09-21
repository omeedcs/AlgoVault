def deleteIslandInteriors(grid):
    if not grid or not grid[0]:
        return grid

    rows, cols = len(grid), len(grid[0])

    def is_border(r, c):
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return True
        return any(grid[r+dr][c+dc] == 0 for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)])

    # First pass: Mark interior lands with 2
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not is_border(r, c):
                grid[r][c] = 2

    # Second pass: Convert marked interiors to water
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                grid[r][c] = 0

    return grid

# Test the function
x = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

result = deleteIslandInteriors(x)
correct = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

if result == correct:
    print("Correct")
else:
    print("Incorrect")
    print("Result:")
    for row in result:
        print(row)
    print("Expected:")
    for row in correct:
        print(row)