# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = defaultdict(int)
        def dfs(n):
            if n == 1: return 1
            if n in memo: return memo[n]
            prod = 0
            for i in range(1,n):
                prod = max(prod, i*max(dfs(n-i),(n-i)))
            memo[n] = prod
            return memo[n]
        return dfs(n)
        