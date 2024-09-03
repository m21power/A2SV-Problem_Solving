# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        i = 0
        ans = []
        for _ in range(m):
            pack = []
            for j in range(n):
                pack.append(original[i+j])
            i += j+1
            ans.append(pack)
        return ans

