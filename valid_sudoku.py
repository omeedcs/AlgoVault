from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.isValidUnit(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValidUnit(column):
                return False
        
        # Check 3x3 sub-boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                sub_box = []
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        value = board[row][col]
                        sub_box.append(value)
                
                if not self.isValidUnit(sub_box):
                    return False
        
        return True
    
    def isValidUnit(self, unit: List[str]) -> bool:
        seen = set()
        for num in unit:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

temp_board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

result = isValidSudoku(temp_board)

print(result)