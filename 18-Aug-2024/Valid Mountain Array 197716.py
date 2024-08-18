# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left = 1
        right = len(arr) - 1

        while left < len(arr) - 1:
            if arr[left] <= arr[left - 1]:
                break

            left += 1

        left = left - 1

        if left == 0:
            return False

        while right >= 0:
            if right < left:
                return False

            if arr[right] >= arr[right - 1]:
                break

            right -= 1

        return left == right