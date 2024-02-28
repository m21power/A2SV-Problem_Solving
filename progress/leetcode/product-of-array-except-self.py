class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preP=[nums[0]]*len(nums)
        suffP=[nums[len(nums)-1]]*len(nums)
        output=[0]*len(nums)
        i=1
        while i<len(nums):
            preP[i]=(preP[i-1]*nums[i])
            i+=1
        l=len(nums)-2
        while l>=0:
            suffP[l]=suffP[l+1]*nums[l]
            l-=1
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                output[i]=preP[i-1]
                i+=1
                continue
            if i==0:
                output[i]=suffP[i+1]
                i+=1
                continue
            output[i]=preP[i-1]*suffP[i+1]
            i+=1
        return output