class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        for i,n in enumerate(nums):
            l,r=i+1,len(nums)-1
            while l<r:
                sum=n+nums[l]+nums[r]
                if abs(sum-target)<abs(diff):# keeping track of minimum distance 
                    diff=target-sum # sum=target - diff
                if sum<target:
                    l+=1
                else:
                    r-=1
            if diff==0:
                break
        return target-diff # the reason we didn't return sum is that since in the loop sum is varying continiously
                            # except taret and diff which only changes if the distance is minimized than before

        