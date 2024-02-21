class Solution:
    """def sorter(self,nums):
        return nums.sort(reverse=True)
    def check(self,nums):
        if nums.count(nums[0])==len(nums):
            return True"""
    def reductionOperations(self, nums: List[int]) -> int:
        """self.sorter(nums)
        count=0
        m=0
        i=1
        while self.check !=True and i<len(nums):
            m=nums[0]
            if nums[i]!=m:
                count+=1
                nums[0]=nums[i]
                self.sorter(nums)
                a=self.check(nums)
                if a:
                    return count
            else:
                i+=1
        return 0
        """
        nums.sort()
        count=0
        ans=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count+=1
            ans+=count
        return ans