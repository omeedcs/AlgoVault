def exist(self, board, word):
    if not board or not board[0] or not word:
        return False
    
    rows = len(board)
    cols = len(board[0])

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(row, col, index):
        # base case.
        if index == len(word): 
            return True

        # alternative base case 
        if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"
         

        for dx, dy in directions: 
            new_r = row + dx 
            new_c = col + dy
            if dfs(new_r, new_c, index + 1): 
                return True

        board[row][col] = temp
        return False
    
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0] and dfs(row, col, 0):
                return True
    
    return False