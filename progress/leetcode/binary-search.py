class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<=1 and nums[0]==target:
            return 0
        elif len(nums)<=1 and nums[0]!=target :
            return -1
            
        def result(start,end):
            mid=(start+end)//2
            if start<=end:
                if nums[mid] > target:
                    end = mid-1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    return mid
            else:
                return -1
            return result(start,end)
        return result(0,len(nums)-1)

        