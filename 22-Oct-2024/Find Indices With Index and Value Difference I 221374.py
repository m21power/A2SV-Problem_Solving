# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDiff: int, valueDiff: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + indexDiff,len(nums)):
                if abs(nums[i] - nums[j]) >= valueDiff:
                    return [i,j]
        return [-1,-1]
        