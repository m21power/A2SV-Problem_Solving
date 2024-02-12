class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m=s.copy()
        i=len(s)-1
        j=0
        while i>=0 and j<len(s):
            s[j]=m[i]
            i-=1
            j+=1
        



        