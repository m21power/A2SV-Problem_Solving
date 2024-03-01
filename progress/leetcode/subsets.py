class Solution:
    def cal(self,nums,subset,index,res):
        res.append(subset[:])
        for i in range(index,len(nums)):
            subset.append(nums[i])
            self.cal(nums,subset,i+1,res)
            subset.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        index=0
        res=[]
        self.cal(nums,subset,index,res)
        return res
        