class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [row for row in board]
        cols = list(zip(*board))
        subs = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subs.append([board[r][c] for r in range(i, i+3) for c in range(j, j+3)])
        
        def is_valid(arr):
            nums = [x for x in arr if x.isdigit()]
            return len(nums) == len(set(nums))
        
        return all([
            all(map(is_valid, rows)),
            all(map(is_valid, cols)),
            all(map(is_valid, subs))
        ])
            
        
        