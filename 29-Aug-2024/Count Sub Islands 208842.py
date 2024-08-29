# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row,col = len(grid1),len(grid1[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited =set()
        def dfs(r,c):
            if r == row or c == col or min(r,c) < 0 or (r,c) in visited:
                return True
            if grid2[r][c] == 0:
                return True
            if grid1[r][c] == 0:
                return False
            visited.add((r,c))
            result = True
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                result &= dfs(nr,nc)
            return result
        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    if dfs(r,c):
                        cnt += 1
        return cnt

        