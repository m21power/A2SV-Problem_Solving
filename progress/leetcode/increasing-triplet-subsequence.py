class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=mid=float('inf')
        for n in nums:
            if n<=first:
                first=n
            elif n<=mid:
                mid=n
            else:
                return True
                

        """if len(nums)<3:
            return False
        first =None
        mid=None
        last=None
        i=0
        while i<len(nums):
            if first is None:
                first=nums[i]
                i+=1
                continue
            if nums[i]<first:
                first=nums[i]
                mid=None
                i+=1
                continue
            if nums[i]>first and mid is None:
                mid=nums[i]
                i+=1
                continue
            if mid and mid<nums[i]:
                return True
            else:
                i+=1
        return False
            
            
            

            """