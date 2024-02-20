class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return Solution().fib(n-1)+Solution().fib(n-2)
print(Solution().fib(2))
        