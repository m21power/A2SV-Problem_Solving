# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        def binarySearch(nums, target, i):
            left, right = i, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for left in range(len(nums)-2):
            for mid in range(left + 1, len(nums)-1):
                if nums[left] == 0:
                    break
                target = nums[left] + nums[mid]
                temp = binarySearch(nums,target,mid)
                cnt += max(0,(temp - mid - 1))
        return cnt
        