# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        temp = sum(nums)
        if temp % k != 0: return False
        nums.sort(reverse = True)
        target = temp//k
        used = [False] * len(nums)
        memo = {}
        def backtrack(i,k,total):
            if k == 0: return True
            if total == target:
                return backtrack(0,k-1,0)
            if i == len(nums): return False
            if not used[i] and (i,k,total) in memo: return memo[(i,k,total)]
            for j in range(i,len(nums)):
                if used[j] or total + nums[j] > target:
                    continue
                used[j] = True
                memo[(i,k,total)] =  backtrack(j+1,k,total + nums[j])
                if memo[(i,k,total)]: return True
                used[j] = False
            return False
        return backtrack(0,k,0)