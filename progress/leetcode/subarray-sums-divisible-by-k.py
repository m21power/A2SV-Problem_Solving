class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}
        prefsum=0
        res=0
        for i in nums:
            prefsum+=i
            a=prefsum%k
            if a in dic:
                res+=dic[a]
                dic[a]+=1
            else:
                dic[a]=1
        return res

        