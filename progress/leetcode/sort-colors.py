class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        while i<len(nums):
            j=i
            while nums[j]<nums[j-1] and j>=1:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                
                j-=1
            i+=1

