class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pref=[nums[0]]*len(nums)
        i=1
        while i<len(nums):
            pref[i]=pref[i-1]+nums[i]
            i+=1
        maxi=pref[k-1]/k
        i=0
        while i<len(nums)-k:
            j=i+k
            maxi=max(maxi,(pref[j]-pref[i])/k)
            i+=1
        return maxi


        