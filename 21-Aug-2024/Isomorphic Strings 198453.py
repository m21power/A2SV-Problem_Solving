# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic = defaultdict()
        taken = set()
        for i in range(len(s)):
            if s[i] in dic:
                if not (dic[s[i]] == t[i]):
                    return False
            else:
                if t[i] not in taken:
                    dic[s[i]] = t[i]
                else:
                    return False
                taken.add(t[i])
                
        return True

        