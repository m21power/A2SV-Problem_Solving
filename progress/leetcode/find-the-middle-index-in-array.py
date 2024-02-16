class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref=[nums[0]]*len(nums)
        i=1
        while i<len(nums):
            pref[i]=pref[i-1]+nums[i]
            i+=1
        mid=0
        l=len(pref)
        i=0
        while i<l:
            if i!=0 and i!=l-1:
                if pref[i-1]==pref[l-1]-pref[i]:
                    return i
            elif i==0:
                if pref[l-1]-pref[i]==0:
                    return i
                
            else:
                if pref[i-1]==0:
                    return i
            i+=1
        return -1
            
        
