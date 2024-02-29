class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack=[]
        mi=nums[0]
        for n in nums[1:]:
            while stack and n>=stack[-1][0]:
                stack.pop()
            if stack and n>stack[-1][1]:
                return True
            stack.append([n,mi])
            mi=min(mi,n)
        return False
        """
        n = len(nums)
        
        minFromLeft = [nums[0]]
        for i in range(1, n):
            minFromLeft.append(min(minFromLeft[i-1], nums[i]))
        
        stack = [] 
        for j in range(n-1, -1, -1):
            if nums[j] > minFromLeft[j]:
                while stack and stack[-1] <= minFromLeft[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False
        
        """
        """
        class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [num, currentMin]
        curMin = nums[0]

        for i in range(1, len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] > stack[-1][1] and stack[-1][0]:
                return True
            stack.append((nums[i], curMin))
            if curMin > nums[i]:
                curMin = nums[i]
        return False
        """