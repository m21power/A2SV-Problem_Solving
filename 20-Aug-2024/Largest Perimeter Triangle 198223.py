# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a,b,c = 0,0,0
        ans = 0
        for i in range(len(nums)-1,1,-1):
            a,b,c = nums[i],nums[i-1],nums[i-2]
            if a < b + c:
                return a + b + c
        return 0
        