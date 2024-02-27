class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefsum=0
        dic={0:1}
        res=0
        for n in nums:
            prefsum+=n
            a=prefsum-k
            if a in dic:
                res+=dic[a]
            if prefsum in dic:
                dic[prefsum]+=1
            else:
                dic[prefsum]=1
        return res
            