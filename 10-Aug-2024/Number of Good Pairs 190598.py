# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for i,n in enumerate(nums):
            j=i+1
            while j<len(nums):
                if nums[j]==n:
                    c+=1
                else:
                    pass
                j+=1
        return c
            

        