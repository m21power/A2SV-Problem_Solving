class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        b=0
        e=0
        c=0
        sum=nums[0]
        mi=0
        while b<len(nums) and e<len(nums):
            if sum<target:
                e+=1
                if e<len(nums):
                    sum+=nums[e]
            elif sum>=target:
                if c==0:
                    mi=e-b+1
                else:
                    if mi>e-b+1:
                        mi=e-b+1
                c+=1
                sum-=nums[b]
                b+=1
        return mi
