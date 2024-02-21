class Solution:
    def binary(self,nums,start,end,n):
        mid=(start+end)//2
        if nums[mid]>n:
            end=mid-1
        elif nums[mid]<n:
            start=mid+1
        else:
            return mid
        return Solution().binary(nums,start,end,n)
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:     
        lis=[]
        for i in nums:
            start=0
            end=len(nums)-1
            num=sorted(nums)
            if nums.count(i)<=1:
                a= Solution().binary(num,start,end,i)
                lis.append(a)
            else:
                b=nums.count(i)
                for j in range(b-1):
                    num.remove(i)
                start=0
                end=len(num)-1
                a= Solution().binary(num,start,end,i)
                lis.append(a)
        return lis