# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(num):
            res = []
            if len(num) == 1: return [num[::]]
            for _ in range(len(num)):
                n = num.pop(0)
                perms = backtrack(num)
                for perm in perms:
                    perm.append(n)
                res += perms
                num.append(n)
            return res
        return backtrack(nums)

                
