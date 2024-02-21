class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum=0
        i=len(piles)-2
        for _ in range(int(len(piles)/3)):
            sum+=piles[i]
            i-=2
        return sum
        