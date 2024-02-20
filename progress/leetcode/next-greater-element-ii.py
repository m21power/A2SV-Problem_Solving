class Solution:
    def nextGreaterElements(self, nums):
        output=[-1]*len(nums)
        stack=[]
        for i,n in enumerate(nums):
            while stack and nums[stack[-1]]<n:
                output[stack[-1]]=n
                stack.pop()
            stack.append(i)
        for n in stack:
            i=0
            while i<n:
                if nums[i]>nums[n]:
                    output[n]=nums[i]
                    break
                i+=1
            
        return output