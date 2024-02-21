class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        i=0
        j=len(nums)-1
        while i<j:
            sum=nums[i]+nums[j]
            if sum==target:
                l.append(i+1)
                l.append(j+1)
                break
            elif sum>target:
                j-=1
            else:
                i+=1
        return l
        