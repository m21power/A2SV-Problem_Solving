class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        while True and i>=0:
            if i**2==x:
                return i
            elif i**2>x:
                return i-1
            i+=1
print(Solution().mySqrt(10))
        