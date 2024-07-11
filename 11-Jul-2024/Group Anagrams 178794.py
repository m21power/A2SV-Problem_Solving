# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
           key = ''.join(sorted(st))
           dic[key].append(st)
        ans = []
        for key,items in dic.items():
            ans.append(items)
        return ans
            

        