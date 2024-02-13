class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        i=0
        c=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    if (i*j)%k==0:
                        c+=1
                    else:
                        pass
                else:
                    pass
                j+=1
            i+=1
        return c

        