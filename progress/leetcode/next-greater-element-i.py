class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        for n in nums1:
            i=0
            while i<len(nums2):
                if n==nums2[i]:
                    j=i
                    m=nums2[j]
                    n=m
                    while j<len(nums2)-1:
                        
                        if nums2[j+1]>nums2[i]:
                            m=nums2[j+1]
                            break
                        else:
                            pass
                        j+=1
                    if m==n:
                        stack.append(-1)
                    else:
                        stack.append(m)
                i+=1
        return stack
"""class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        for n in nums1:
            i=0
            while i<len(nums2):
                if n==nums2[i]:
                    if i+1<len(nums2):
                        if nums2[i+1]>n:
                            stack.append(nums2[i+1])
                        else:
                            stack.append(-1)
                    else:
                        stack.append(-1)
                i+=1
        return stack"""