# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = defaultdict(int)
        def dfs(i,j):
            if i + 1 == j: return 0
            ans = float('inf')
            if (i,j) in memo: return memo[(i,j)]
            for k in range(i+1,j):
                ans = min(ans,values[i]*values[j]*values[k] + dfs(i,k) + dfs(k,j))
            memo[(i,j)] = ans
            return memo[(i,j)]
        return dfs(0,len(values)-1)