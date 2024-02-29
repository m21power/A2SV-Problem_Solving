class Solution:
    def longestPalindrome(self, s: str) -> int:
        lis=set()
        count=0
        for let in s:
            if let not in lis:
                lis.add(let)
            else:
                count+=2
                lis.remove(let)
        return count if count==len(s) else count+1
