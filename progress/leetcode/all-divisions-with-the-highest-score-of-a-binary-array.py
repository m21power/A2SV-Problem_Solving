class Solution:
    def maxScoreIndices(self, nums):
        left,right=0,nums.count(1)
        n=len(nums)
        ans=[0]
        comp=right
        for i in range(n):
            if nums[i]==0:
                left+=1
            else:
                right-=1
            sum=left+right
            if sum==comp:
                ans.append(i+1)
            elif sum>comp:
                ans=[]
                ans.append(i+1)
                comp=sum
        return ans