def solveNQueens(n):
    cols = set()
    posDiag = set()
    negDiag = set()
    result = []
    board = [["."] * n for i in range(n)]
    def backtrack(row):
        if row == n:
            # we made it to the end.
            # base case.
            result.append(row)
        
        for col in range(n):
            if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                continue

            cols.add(col)
            # the reason we can do this, is when you add 
            # these values or subtract these values, it
            # stays consistent across the entire diagonal.
            # if you draw out a matrix with these combos,
            # the value will be consistent across the diagonal.
            posDiag.add(row + col) 
            negDiag.add(row - col)
            board[row][col] = "Q"

            backtrack(row + 1) # move onto the next row

            # reverse
            cols.remove(col) 
            posDiag.remove(row + col)
            negDiag.remove(row - col)
            board[row][col] = "."
    backtrack(0)
    return result