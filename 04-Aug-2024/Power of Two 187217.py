# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while n>=2**i:
            if n==2**i:
                return True
            else:
                pass
            i+=1
        return False
result=Solution()
print(result.isPowerOfTwo(4))