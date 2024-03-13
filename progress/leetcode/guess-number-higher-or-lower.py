# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n==1:
            return 1
        def result(start,end):
            while start<=end:
                mid=(start+end)//2
                res=guess(mid)
                if res==-1:
                    end = mid-1
                elif res==1:
                    start = mid+1
                else:
                    return mid
            
        return result(1,n)
        