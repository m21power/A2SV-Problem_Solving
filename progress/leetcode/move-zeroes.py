class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=num.count(0)
        for i in range(n):
            num.remove(0)
        for i in range(n):
            num.append(0)
        print(num)
Solution().moveZeroes([0,1,0,3,12])
            