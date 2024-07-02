# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(pack):
            if len(pack) == len(nums):
                ans.append(pack[::])
                return
            for n in nums:
                if n not in pack:
                    pack.append(n)
                    backtrack(pack)
                    pack.pop()
            return
        backtrack([])
        return ans
