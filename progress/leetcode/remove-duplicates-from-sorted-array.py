class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=set(nums)
        for n in a:
            c=nums.count(n)
            if c>=2:
                for i in range(c-1):
                    nums.remove(n)
            else:
                continue
        return len(nums)
        