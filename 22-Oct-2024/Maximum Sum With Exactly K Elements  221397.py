# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        end = m + k - 1
        start = m - 1
        return int(((end/2) * (end + 1)) - ((start/2) * (start + 1)))