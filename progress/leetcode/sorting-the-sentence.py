class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(s.split())
        i=1
        while i<len(s):
            j=i
            while j>0 and s[j][-1]<s[j-1][-1]:
                s[j],s[j-1]=s[j-1],s[j]
                j-=1
            i+=1
        i=0
        for word in s:
            while i<len(s):
                s[i]=s[i][:-1]
                i+=1
        return ' '.join(s)