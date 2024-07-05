# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        lis = [0,1]
        for i in range(2,n+1):
            lis[0],lis[1] = lis[1],lis[0] + lis[1]
        return lis[1]

        