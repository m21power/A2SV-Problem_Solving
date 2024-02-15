class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """off=False
        for num in nums:
            if num>=0:
                off=True
                break
       
        sum=0
        i=0
        if off:
            while i<len(nums):
                j=i
                
                while j<len(nums):
                    n=i
                    a=sum
                    sum=0
                    while n<=j:
                        sum+=nums[n]
                        n+=1
                    if a>sum:
                        sum=a
                    else:
                        sum=sum
                    j+=1
                i+=1
        else:
            sum=max(nums)

        return sum
                """
        sum=0
        ans=nums[0]
        for i in nums:
            if sum<0:
                sum=0
            sum+=i
            ans= max(ans,sum)
        return ans

