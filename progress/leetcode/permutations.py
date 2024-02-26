import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=list(itertools.permutations(nums))
        for i,t in enumerate(a):
            a[i]=list(t)
        return a
        