# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        memo = {}
        def dfs(prev,ans):
            if ans == n:
                return 1
            if ans > n:
                return float('inf')
            if (prev,ans) in memo: return memo[(prev,ans)]
            res = float('inf')
            if  prev != ans:
                res = min(res,1 + dfs(ans,ans))
            res =min(res,1 + dfs(prev ,ans + prev))
            memo[(prev,ans)] = res
            return res
        return dfs(1,1)

            
        