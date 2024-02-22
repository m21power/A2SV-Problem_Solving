class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        i=0
        lon=1
        if len(s)==0:
            return 0
        while i<len(s):
            j=i+1
            l.append(s[i])
            while j<len(s):
                if s[j] not in l:
                    l.append(s[j])
                    if len(l)>=lon:
                        lon=len(l)
                    else:
                        pass
                else:
                    l.clear()
                    break
                j+=1
            i+=1
        return lon