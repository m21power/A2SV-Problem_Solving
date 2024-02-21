class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c=0
        for i,n in enumerate(nums):
            j=i+1
            while j<len(nums):
                if n+nums[j]<target:
                    c+=1
                else:
                    break
                j+=1
        return c

        