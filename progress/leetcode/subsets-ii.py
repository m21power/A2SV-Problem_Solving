class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(sets,i):
            if sets in ans:
                pass
            else:
                ans.append(sets[:])
            for j in range(i,len(nums)):
                sets.append(nums[j])
                backtrack(sets,j+1)
                sets.pop()
        backtrack([],0)
        return ans

        