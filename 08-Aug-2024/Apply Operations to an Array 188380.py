# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        ans = []
        for n in nums:
            if n:
                ans.append(n)
        zero = [0] * (len(nums) - len(ans))
        return ans + zero