# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapper(num):
            num = str(num)
            res = 0
            for i in num:
                res *= 10
                res += mapping[int(i)]
            return res
       
        
        result = []

        for idx, num in enumerate(nums):
            result.append([mapper(num), idx])
        
        result.sort(key = lambda x: (x[0], x[1]))

        ans = []

        for num, idx in result:
            ans.append(nums[idx])

        return ans