# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl, ans = SortedList(), 0
        for num1, num2 in zip(nums1, nums2):
            ans += sl.bisect_right(num1 - num2 + diff)
            sl.add(num1 - num2)
        return ans