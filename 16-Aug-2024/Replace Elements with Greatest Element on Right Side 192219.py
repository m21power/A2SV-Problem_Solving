# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0
        for i in range(len(arr)-1,-1,-1):
            if m == 0:
                m = arr[i]
                arr[i] = -1
            else:
                temp = m
                m = max(arr[i],m)
                arr[i] = temp
        return arr

