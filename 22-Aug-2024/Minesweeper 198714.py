# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [[1,0],[0,1],[-1,0],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]]
        row, col = len(board),len(board[0])
        r,c = click[0],click[1]
        visited = set()
        
        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        def dfs(r,c):
            count = 0
            visited.add((r,c))
            for dr,dc in direction:
                nr, nc = dr + r, dc + c
                if 0 <= nr < row and 0 <= nc < col:
                    if board[nr][nc] == "M":
                        count += 1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for dr,dc in direction:
                    nr,nc = dr + r, dc + c
                    if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visited and board[nr][nc] == "E":
                        dfs(nr,nc)
            return 

        dfs(r,c)
        return board

                