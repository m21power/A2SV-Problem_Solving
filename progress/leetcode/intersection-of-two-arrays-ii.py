class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1=len(nums1)
        l2=len(nums2)
        lis=[]
        if l1<l2:
            for i in nums1:
                if i in nums2:
                    lis.append(i)
                    nums2.remove(i)
                else:
                    pass
        else:
            for i in nums2:
                if i in nums1:
                    lis.append(i)
                    nums1.remove(i)
                else:
                    pass
        return lis

        