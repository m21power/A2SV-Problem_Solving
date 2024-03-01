class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start, comb, target):
            if target == 0:
                res.append(comb[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                comb.append(candidates[i])
                backtrack(i, comb, target - candidates[i])
                comb.pop()
        
        backtrack(0, [], target)
        return res