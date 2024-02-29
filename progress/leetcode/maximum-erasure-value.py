class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited=set()
        i=sum=res=0
        for n in nums:
            while n in visited:
                visited.remove(nums[i])
                sum-=nums[i]
                i+=1
            sum+=n
            visited.add(n)
            res=max(res,sum)
        return res
            

