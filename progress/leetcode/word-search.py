class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board),len(board[0])
        visited = set()
        def backtracking(r,c,idx):
            if idx == len(word): 
                return True
            if (r >= row or c >= col or
                r < 0 or c < 0 or 
                (r,c) in visited or
                board[r][c] != word[idx]):
                return False

            visited.add((r,c))

            res = (backtracking(r+1,c,idx + 1) or
                    backtracking(r,c+1,idx + 1) or
                    backtracking(r-1,c,idx + 1) or
                    backtracking(r,c-1,idx + 1))
            visited.remove((r,c))
            return res
        for i in range(row):
            for j in range(col):
                if backtracking(i,j,0): return True
        return False