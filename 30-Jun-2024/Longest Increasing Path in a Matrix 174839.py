# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        row, col = len(matrix),len(matrix[0])
        memo = defaultdict(int)
        def dfs(prev,r,c):
            if (r == row or c == col or min(r,c) < 0 or prev >= matrix[r][c] ) :
                return 0
            if (r,c) in memo: return memo[(r,c)]
            temp = 0
            for dr,dc in direction:
                nr,nc = dr + r, dc + c
                temp = 1 + dfs(matrix[r][c],nr,nc)
                memo[(r,c)] = max(temp,memo[(r,c)])
            return memo[(r,c)]
        for r in range(row):
            for c in range(col):
                dfs(-1,r,c)
        res = 0
        for key,d in memo.items():
            res = max(res,d)
        return res
            

        