class Solution:
    def isValid(self,num,res):
        if num in res:
            return False
        else:
            return True
    def finalRes(self,res):
        for i in res:
            i.sort()
        for i in res:
            n=res.count(i)
            if n>1:
                for _ in range(n-1):
                    res.remove(i)
            else:
                pass
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        res=[]
        idx=0
        def cal(nums,subset,idx,res):
            if self.isValid(subset[:],res):
                res.append(subset[:])
            else:
                pass
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                cal(nums,subset,i+1,res)
                subset.pop()
        cal(nums,subset,idx,res)
        return self.finalRes(res)

        