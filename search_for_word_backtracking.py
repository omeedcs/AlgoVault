def wordSearch(self, board, word) -> bool:
    if not board or not word:
        return False
    for row in range(len(board)):
        for col in range(len(board[0])):
            val = board[row][col]
            # looking for the first letter of the word.
            if val == word[0]:
                # perform a dfs.
    
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            # we are out of bounds
            return
        
        # perform the dfs, and look for target. 
        

