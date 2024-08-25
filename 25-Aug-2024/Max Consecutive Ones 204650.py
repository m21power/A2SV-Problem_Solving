# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left = None
        for i in range(len(nums)):
            if nums[i] == 1 and left is None:
                left = i
            elif nums[i]==0 and left is not None:
                res = max(res,abs(i-left))
                left = None
            if i==len(nums)-1 and nums[i]==1:
                res = max(res,abs(i-left)+1)
        return res




        