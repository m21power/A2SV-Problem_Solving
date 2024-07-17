# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = defaultdict(int)
        left = res = 0
        for i,let in enumerate(s):

            if let in dic and dic[let] >= left:
                left = dic[let]+1
                dic[let] = i
            else:
                dic[let] = i

            res = max(res,i-left+1)
            
        return res