# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(s): 
                return 0
            if i in memo: return memo[i]
            ans = float('inf')
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:  
                    ans = min(ans,1 + backtrack(j+1))
            memo[i] = ans
            return memo[i]
        return backtrack(0)-1