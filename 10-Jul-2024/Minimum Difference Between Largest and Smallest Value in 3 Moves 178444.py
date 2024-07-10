# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        ans = float('inf')
        for i in range(4):
            left = i
            right = len(nums) -((3 - i) + 1 )
            ans = min(ans,(nums[right] - nums[left]))
        return ans

        