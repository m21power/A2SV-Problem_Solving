# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        bBefore = [0]*len(s)
        aAfter = [0] * len(s)

        for i in range(1,len(s)):
            if s[i-1] == 'b':
                bBefore[i] += bBefore[i - 1] + 1
            else:
                bBefore[i] += bBefore[i - 1]
        for i in range(len(s) - 2,-1,-1):
            if s[i+1] == 'a':
                aAfter[i] += aAfter[i+1] + 1
            else:
                aAfter[i] += aAfter[i+1]
        ans = float('inf')
        for i in range(len(s)):
            ans = min(ans,aAfter[i] + bBefore[i])
        return ans

        